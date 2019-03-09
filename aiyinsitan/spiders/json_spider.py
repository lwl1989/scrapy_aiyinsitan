import scrapy
import io
import sys
from scrapy.http.headers import Headers
import json


class JsonSpider(scrapy.Spider):
    name = "json"

    isStart = True
    startUrl = 'https://www.aiyinsitanfm.com/pcalbum_audio_list/get_page_list'

    album_ids = [

    ]

    def start_requests(self):
        headers = Headers()
        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        #data = {"album_id": "1241|13509"}
        data = "album_id=1029|1010080&order_type=1&page_num=1"
        yield scrapy.Request(url=self.startUrl, callback=self.parse, method="POST", headers=headers, body=data)

    def parse(self, response):
        obj = json.loads(response.body_as_unicode())
        print(obj)

