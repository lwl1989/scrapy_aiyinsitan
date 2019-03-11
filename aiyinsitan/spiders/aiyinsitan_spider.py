import scrapy
import io
import sys
from scrapy.http.headers import Headers
import json
import urllib.parse
from html.parser import HTMLParser
from pymongo import MongoClient
from pymongo import InsertOne
import os


class AiyinsitanSpider(scrapy.Spider):

    name = "aiyinsitan"
    json_success_code = "00001"
    startUrl = 'https://www.aiyinsitanfm.com/classify/0%7C78.html'
    img_host = 'https://img.aiyinsitanfm.com'
    mongo_client = MongoClient('mongodb://@47.101.174.224:27017/aiyinsitan')
    # 进程名
    pro_name = ''
    # 运行标识
    run_name = ''
    # 爬取id
    sub_id = ''
    # 爬取页码，只对分类和专辑列表有效
    page = 1

    def __init__(self, run_name="", sub_id="", pro_name="", page=1, *args, **kwargs):
        super(AiyinsitanSpider, self).__init__(*args, **kwargs)
        self.sub_id = sub_id
        self.pro_name = pro_name
        self.run_name = run_name
        self.page = page

    def start_crawl(self):
        if self.pro_name == "":
            return False

        pid = os.getpid()
        if pid > 0:
            f = open("pid_%s" % self.pro_name, "w")
            f.write(str(pid))
            f.close()
            return True

        return False

    def closed(self):
        if self.pro_name != "":
            file_name = "pid_%s" % self.pro_name
            f = open(file_name, "w")
            f.write("")
            f.close()

    # 开始请求
    def start_requests(self):
        # 1113542|1371834 1241|1007772
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        # yield self.request_album("1241|1007772", "1")
        # yield self.request_all_audio("1113542|1371834")
        # yield self.request_classify("78|1241", "2")
        # aid = "1241|1007765"
        # headers = Headers()
        # headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
        # url = "https://www.aiyinsitanfm.com/album/%s.html" % aid
        # yield scrapy.Request(url=url, callback=self.parse_album_detail, method="GET",
        #                      headers=headers)
        if self.start_crawl():
            if self.run_name == "all":
                yield scrapy.Request(url=self.startUrl, callback=self.parse)
            if self.run_name == "classify":
                # 获取某个分类下所有的专辑和音频数据（页码默认1）
                yield self.request_classify(self.sub_id, self.page)
            if self.run_name == "album":
                # 获取专辑列表+音频数据
                yield self.request_album_detail(self.sub_id)
                yield self.request_album(self.sub_id, self.page)
            if self.run_name == "album_audio":
                # 获取制定专辑下的音频数据
                yield self.request_all_audio(self.sub_id)

    def request_album_detail(self, aid):
        headers = Headers()
        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
        url = "https://www.aiyinsitanfm.com/album/%s.html" % aid
        req = scrapy.Request(url=url, callback=self.parse_album_detail, method="GET",
                             headers=headers)
        return req

    # 入口页解析
    def parse(self, response):
        # print(response.request.body)
        for href in response.css(".sub-box a"):
            for did in href.css("::attr(data-id)").extract():
                yield self.request_classify(did, 1)

    # 将response转换成json obj
    def parse_response_json_obj(self, response):
        res_str = response.body_as_unicode()
        if res_str[0:1] != "{":
            return self.error_response(response)

        obj = json.loads(response.body_as_unicode())
        code = obj.get('status_code')

        if code != self.json_success_code:
            return self.error_response(response)
        return obj

    # 从json对象中获取html
    def json_get_html(self, obj, response):
        if obj == "":
            return ""
        info = obj.get('data_info')
        if info == "":
            return self.error_response(response)

        str_html = info.get('html')
        if str_html == "":
            return self.error_response(response)
        return str_html

    # 解析json
    def parse_response_json(self, response):
        obj = self.parse_response_json_obj(response)
        return self.json_get_html(obj, response)

    # 分页获取栏目
    def parse_classify(self, response):
        obj = self.parse_response_json_obj(response)
        str_html = self.json_get_html(obj, response)

        if str_html != "":
            parser = SpiderClassContentAlbumParser()
            parser.feed(str_html)

            # print(str_html)
            req_obj = urllib.parse.parse_qs(response.request.body)
            now_page = int(req_obj.get(b'page_num')[0].decode())
            tid = req_obj.get(b'type_id')[0].decode()
            max_page = int(obj.get("data_info").get("total"))/20
            # print(parser.album_ids)
            # print(parser.audio_ids)
            while True:
                if len(parser.album_ids) > 0:
                    aid = parser.album_ids.pop()
                    yield self.request_album(aid, "1")
                else:
                    if len(parser.audio_ids) > 0:
                        aid = parser.audio_ids.pop()
                        parser.audio_ids = []
                        yield self.request_all_audio(aid)
                    else:
                        break

            if max_page > now_page:
                yield self.request_classify(tid, now_page + 1)

    # 分析专辑页面
    def parse_album(self, response):
        str_html = self.parse_response_json(response)

        parser = SpiderAlbumParser()
        parser.feed(str_html)

        while True:
            if len(parser.album_ids) > 0:
                aid = parser.album_ids.pop()
                yield self.request_album(aid, "1")
            else:
                if len(parser.audio_ids) > 0:
                    aid = parser.audio_ids.pop()
                    parser.audio_ids = []
                    yield self.request_all_audio(aid)
                else:
                    return

    # 分析音频json
    def parse_audio(self, response):
        str_json = response.body_as_unicode()
        if str_json == "":
            return

        obj = self.parse_response_json_obj(response)
        if obj == "":
            return

        info = obj.get("data_info")
        if info != "":

            my_db = self.mongo_client['aiyinsitan']
            all_music = info.get("album_allMusic")
            if all_music == "":
                return

            if len(all_music) > 0:
                album_id = 'album_'+all_music[0]['db_album_id']
                my_collection = my_db[album_id]
                data = []
                for audio in all_music:
                    audio['_id'] = audio['db_id']
                    data.append(InsertOne(audio))
                    if len(data) == 1000:
                        my_collection.bulk_write(data)
                        data = []
                if len(data) > 0:
                    my_collection.bulk_write(data)

        print("success write mongodb")

    # 请求音频专辑列表
    def request_album(self, did, page):
        headers = Headers()
        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
        url = "https://www.aiyinsitanfm.com/pcalbum_info/get_page_list"
        req = scrapy.Request(url=url, callback=self.parse_album, method="POST",
                             headers=headers, body="album_id=%s&order_type=1&page_num=%s" % (did, page))
        # print("=============--------album %s---------================" % did)
        return req

    def parse_album_detail(self, response):
        names = response.xpath('//div[@class="album-content"]/p[@class="album-name"]/text()')
        authors = response.xpath('//div[@class="album-content"]/p[@class="album-user"]/'
                                 'span[@class="user-name"]/a/text()')
        album_id = response.xpath('//div[@class="album-content"]/p[@class="album-action"]/button/@data-id')
        tags = response.xpath('//div[@class="album-content"]/p[@class="album-tags"]/a')
        desc = response.xpath('//div[@class="album-content"]/div[@class="album-profile"]'
                              '/p[@class="profile-text"]/text()')

        m = {"name": "", "author": "", "album_id": "",
            "tags": "", "desc": "", "album_id_bind": ""}
        # m = {}
        m["name"] = str(names.extract_first())
        m["author"] = authors.extract_first()

        aid = album_id.extract_first()
        m["album_id_bind"] = aid
        if aid != "":
            aids = aid.split("|")
            if len(aids) == 2:
                m["album_id"] = aids[1]
        tgs = ""
        for t in tags:
            tgs += str(t.xpath("@data-title").extract_first())+","
        if tgs != "":
            tgs = tgs.rstrip(",")
        m["tags"] = tgs
        m["desc"] = desc.extract_first()

        my_db = self.mongo_client['aiyinsitan']
        my_collection = my_db["albums"]
        my_collection.insert_one(m)
        return None

    # 请求专辑分类列表
    def request_classify(self, tid, page):
        headers = Headers()
        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
        url = "https://www.aiyinsitanfm.com/pcall_types/get_page_list"
        req = scrapy.Request(url=url, callback=self.parse_classify, method="POST",
                             headers=headers, body="type_id=%s&sort_type=1&page_num=%s" % (tid, str(page)))
        # print("=============--------classify %s---------================" % tid)
        return req

    # 请求一个专辑下所有音频
    def request_all_audio(self, audio_id):
        headers = Headers()
        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
        url = "https://www.aiyinsitanfm.com/pcplayer/get_all_list"
        req = scrapy.Request(url=url, callback=self.parse_audio, method="POST",
                             headers=headers, body="audio_id=%s" % audio_id)

        print("=============--------audio %s---------================" % audio_id)
        return req

    # 错误抓取写日志
    def error_response(self, response):
        req = '{"url": %s, "body": %s}' % (response.request.url, response.request.body)
        str_json = response.body_as_unicode()
        try:
            f = open('error.log', 'a+')
            f.write(str_json)
            f.write(req)
        finally:
            f.write("\r\n")
            f.close()
        return ""


class SpiderClassContentAlbumParser(HTMLParser):
    album_ids = []
    audio_ids = []

    def append_to_ids(self, get_id, id_type):
        if get_id.find("|") == -1:
            return
        ids = []
        if id_type == "album":
            ids = self.album_ids
        if id_type == "audio":
            ids = self.audio_ids

        exists = False
        for did in ids:
            if did == get_id:
                exists = True
                break
        if ~exists:
            ids.append(get_id)

        if id_type == "audio":
            self.audio_ids = ids

        if id_type == "album":
            self.album_ids = ids

    def handle_starttag(self, tag, attrs):

        if tag == 'a':  # 目标标签
            id_type = ""
            get_id = ""
            for attr in attrs:
                if attr[0] == "data-page":
                    id_type = attr[1]

                if attr[0] == "data-id":
                    get_id = attr[1]

            if get_id != "" and id_type != "":
                self.append_to_ids(get_id, id_type)
        else:
            pass

    def handle_data(self, data):
        pass

    def error(self, message):
        pass


class SpiderAlbumParser(HTMLParser):
    album_ids = []
    audio_ids = []

    def append_to_ids(self, get_id, id_type):
        if get_id.find("|") == -1:
            return
        ids = []
        if id_type == "album":
            ids = self.album_ids
        if id_type == "audio":
            ids = self.audio_ids

        exists = False
        for did in ids:
            if did == get_id:
                exists = True
                break
        if ~exists:
            ids.append(get_id)

        if id_type == "audio":
            self.audio_ids = ids

        if id_type == "album":
            self.album_ids = ids

    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # 目标标签
            id_type = ""
            get_id = ""
            for attr in attrs:
                if attr[0] == "data-page":
                    if attr[1] == "audio":
                        id_type = attr[1]
                if attr[0] == "data-id":
                    get_id = attr[1]

            if get_id != "" and id_type != "":
                self.append_to_ids(get_id, id_type)
        else:
            pass

    def handle_data(self, data):
            pass

    def error(self, message):
        pass

# class SpiderHtmlParser(HTMLParser):
#     re = []  # 放置结果
#     flg = 0  # 标志，用以标记是否找到我们需要的标签
#     dataIds = []
#
#     def handle_starttag(self, tag, attrs):
#         if tag == 'a':  # 目标标签
#             for attr in attrs:
#                 if attr[0] == "data-id":
#                     exists = False
#                     for did in self.dataIds:
#                         if did == attr[1]:
#                             exists = True
#                             break
#                     if ~exists:
#                         self.dataIds.append(attr[1])
#                     break
#         else:
#             pass
#
#     def handle_data(self, data):
#         if self.flg == 1:
#             self.re.append(data.strip())  # 如果标志为我们需要的标志，则将数据添加到列表中
#             self.flg = 0  # 重置标志，进行下次迭代
#         else:
#             pass
#
#     def error(self, message):
#         pass
