from html.parser import HTMLParser


class SpiderHtmlParser(HTMLParser):
    re = []  # 放置结果
    flg = 0  # 标志，用以标记是否找到我们需要的标签
    dataIds = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # 目标标签
            for attr in attrs:
                if attr[0] == "data-id":
                    exists = False
                    for did in self.dataIds:
                        if did == attr[1]:
                            exists = True
                            break
                    if ~exists:
                        self.dataIds.append(attr[1])
                    break
        else:
            pass

    def handle_data(self, data):
        if self.flg == 1:
            self.re.append(data.strip())  # 如果标志为我们需要的标志，则将数据添加到列表中
            self.flg = 0  # 重置标志，进行下次迭代
        else:
            pass

    def error(self, message):
        pass

strs = '''
<h4>恐怖·悬疑</h4>
<ul class="tab-nav" id="classifySort" data-id="78|1241">
  <li class="active" data-sort="1"><span>最近流行</span></li>
  <li class="" data-sort="2"><span>最热</span></li>
  <li class="" data-sort="3"><span>最近更新</span></li>
</ul>
<div class="content-box" data-id="78|1241" data-sort="1">
  <ul class="content-list">

<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007772" data-content="main" data-title="苗疆道事"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/160/q/75!"  alt="苗疆道事"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007772" data-content="main" data-title="苗疆道事">苗疆道事</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10059451" data-content="main" data-title="文学触手">文学触手</a></p>
  <p class="item-play">978.58万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007765" data-content="main" data-title="黄河捞尸人"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;98ba543264a7203abb001acf739aa7ba.jpg?imageView2/2/w/160/q/75!"  alt="黄河捞尸人"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007765" data-content="main" data-title="黄河捞尸人">黄河捞尸人</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="1415" data-content="main" data-title="主播 空白">主播 空白</a></p>
  <p class="item-play">240.35万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007775" data-content="main" data-title="谋杀法则"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;0ae05ee17a91284f9cc8fcf911ab4d4b.jpg?imageView2/2/w/160/q/75!"  alt="谋杀法则"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007775" data-content="main" data-title="谋杀法则">谋杀法则</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10059451" data-content="main" data-title="文学触手">文学触手</a></p>
  <p class="item-play">215.91万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1006891" data-content="main" data-title="鬼吹灯之精绝古城（一）"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;2019&#47;2&#47;26&#47;403354de7ea24634bbc104dc73f3f98e.png?imageView2/2/w/160/q/75!"  alt="鬼吹灯之精绝古城（一）"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1006891" data-content="main" data-title="鬼吹灯之精绝古城（一）">鬼吹灯之精绝古城（一）</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="1666" data-content="main" data-title="周建龙">周建龙</a></p>
  <p class="item-play">199.19万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1009342" data-content="main" data-title="苗疆蛊事"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d7fb1e7fc1c87af2507894f9ab2005ae.jpg?imageView2/2/w/160/q/75!"  alt="苗疆蛊事"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1009342" data-content="main" data-title="苗疆蛊事">苗疆蛊事</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10069563" data-content="main" data-title="东方卿">东方卿</a></p>
  <p class="item-play">119.26万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|13509" data-content="main" data-title="鬼事异闻录"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_010&#47;20160826144456utyj0.jpg?imageView2/2/w/160/q/75!"  alt="鬼事异闻录"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|13509" data-content="main" data-title="鬼事异闻录">鬼事异闻录</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="216" data-content="main" data-title="箫客行">箫客行</a></p>
  <p class="item-play">132.77万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1006240" data-content="main" data-title="鬼事异闻录 第二季"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;75a475be8796219bfff85b044a486f72.png?imageView2/2/w/160/q/75!"  alt="鬼事异闻录 第二季"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1006240" data-content="main" data-title="鬼事异闻录 第二季">鬼事异闻录 第二季</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="216" data-content="main" data-title="箫客行">箫客行</a></p>
  <p class="item-play">52.89万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007874" data-content="main" data-title="民调局异闻录后传"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;080c59459e4d9e4b3d6f2e9c60720f53.jpg?imageView2/2/w/160/q/75!"  alt="民调局异闻录后传"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007874" data-content="main" data-title="民调局异闻录后传">民调局异闻录后传</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="1060" data-content="main" data-title="谷仓">谷仓</a></p>
  <p class="item-play">342.49万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|8273" data-content="main" data-title="微悬疑"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_010&#47;2016001414154572py0.jpg?imageView2/2/w/160/q/75!"  alt="微悬疑"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|8273" data-content="main" data-title="微悬疑">微悬疑</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="1883" data-content="main" data-title="喵星人">喵星人</a></p>
  <p class="item-play">112.34万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1005941" data-content="main" data-title="心跳4号列车"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;1a8046f0988823598ec6d999fa382b3e.png?imageView2/2/w/160/q/75!"  alt="心跳4号列车"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1005941" data-content="main" data-title="心跳4号列车">心跳4号列车</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="33592" data-content="main" data-title="微微一笑丿你瞅啥">微微一笑丿你瞅啥</a></p>
  <p class="item-play">23.3万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007072" data-content="main" data-title="鬼语怪谈"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;ed6e726c871ebaf48890b8a928e81021.png?imageView2/2/w/160/q/75!"  alt="鬼语怪谈"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1007072" data-content="main" data-title="鬼语怪谈">鬼语怪谈</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="32779" data-content="main" data-title="微小西">微小西</a></p>
  <p class="item-play">4.68万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1008839" data-content="main" data-title="大圣辩阴阳之越听越害怕"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d00d9d4d7084c853757a528746db17d9.png?imageView2/2/w/160/q/75!"  alt="大圣辩阴阳之越听越害怕"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1008839" data-content="main" data-title="大圣辩阴阳之越听越害怕">大圣辩阴阳之越听越害怕</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10064419" data-content="main" data-title="大师兄孟谦">大师兄孟谦</a></p>
  <p class="item-play">4.93万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|7849" data-content="main" data-title="鬼事连篇"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_010&#47;2015010241351467u3q0.jpg?imageView2/2/w/160/q/75!"  alt="鬼事连篇"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|7849" data-content="main" data-title="鬼事连篇">鬼事连篇</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="216" data-content="main" data-title="箫客行">箫客行</a></p>
  <p class="item-play">20.81万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1010378" data-content="main" data-title="鬼笑不发丘"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;12bb0396141a8ef68a1e82b0ad141d6f.png?imageView2/2/w/160/q/75!"  alt="鬼笑不发丘"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1010378" data-content="main" data-title="鬼笑不发丘">鬼笑不发丘</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10072595" data-content="main" data-title="东方视角">东方视角</a></p>
  <p class="item-play">117.65万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1009383" data-content="main" data-title="盗墓迷局"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;411fa767873c8b2a565699a7d5592ab8.JPG?imageView2/2/w/160/q/75!"  alt="盗墓迷局"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1009383" data-content="main" data-title="盗墓迷局">盗墓迷局</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10069564" data-content="main" data-title="东方语桐">东方语桐</a></p>
  <p class="item-play">129.78万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|12135" data-content="main" data-title="空前绝后"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_010&#47;201604181435486yh1.jpg?imageView2/2/w/160/q/75!"  alt="空前绝后"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|12135" data-content="main" data-title="空前绝后">空前绝后</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="216" data-content="main" data-title="箫客行">箫客行</a></p>
  <p class="item-play">2.63万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1009485" data-content="main" data-title="黄河异事录（二）"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;a5cf1a828de0bb6faf88db8d9c9848d8.jpg?imageView2/2/w/160/q/75!"  alt="黄河异事录（二）"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1009485" data-content="main" data-title="黄河异事录（二）">黄河异事录（二）</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10070489" data-content="main" data-title="东方小子">东方小子</a></p>
  <p class="item-play">101.52万</p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|11285" data-content="main" data-title="皇寺金佛失踪之谜"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_014&#47;20160214133933g20n0.jpg?imageView2/2/w/160/q/75!"  alt="皇寺金佛失踪之谜"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|11285" data-content="main" data-title="皇寺金佛失踪之谜">皇寺金佛失踪之谜</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="1666" data-content="main" data-title="周建龙">周建龙</a></p>
  <p class="item-play">1.49万</p>
</li>
<li>
  <div class="item-img">
    <span class="pay">付费</span>
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1111495" data-content="main" data-title="东北招阴人"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;2017&#47;10&#47;20&#47;3c60a0b2cee049d38f868d0f02e30756.png?imageView2/2/w/160/q/75!"  alt="东北招阴人"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1111495" data-content="main" data-title="东北招阴人">东北招阴人</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="233" data-content="main" data-title="郝志">郝志</a></p>
  <p class="item-price">
    <span class="pricing">29.9</span>
    <span class="price">29.9 听票</span>
  </p>
</li>
<li>
  <div class="item-img">
    <a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1118283" data-content="main" data-title="我当算命先生那几年"><img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;2018&#47;7&#47;27&#47;50b965b4f620451798f9bda62a484aee.png?imageView2/2/w/160/q/75!"  alt="我当算命先生那几年"></a>
  </div>
  <p class="item-name"><a href="javascript:;" data-page="album" data-interface="/pcalbum_info/get_page_list" data-id="1241|1118283" data-content="main" data-title="我当算命先生那几年">我当算命先生那几年</a></p>
  <p class="item-sub">by：<a href="javascript:;" data-page="personal" data-interface="/pcall_users/get_tab_content_template" data-id="10069563" data-content="main" data-title="东方卿">东方卿</a></p>
  <p class="item-play">86.59万</p>
</li>

  </ul>
  <div class="page-box" id="classifyPage"></div>
</div>
<script>
  $(function(){
    $('#classifyPage').html('').page({
      total: 109,
      pageSize: 20
    }).on('pageClicked', function(event, pageNumber){
      var typeId = $(this).parents('.content-box').attr('data-id');
      var sort = $(this).parents('.content-box').attr('data-sort');
      changePage(typeId, sort, 'content-list', pageNumber);
    }).on('jumpClicked', function(event, pageNumber){
      var typeId = $(this).parents('.content-box').attr('data-id');
      var sort = $(this).parents('.content-box').attr('data-sort');
      changePage(typeId, sort, 'content-list', pageNumber);
    });
  });
</script> 
'''

str1 = '''
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070520"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事001">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070520" data-content="main" data-title="苗疆道事001">苗疆道事001</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:31</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.14万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>11</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070520" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070520">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070521"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事002">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070521" data-content="main" data-title="苗疆道事002">苗疆道事002</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:56</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.13万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>3</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070521" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070521">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070522"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事003">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070522" data-content="main" data-title="苗疆道事003">苗疆道事003</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>20:09</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.51万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070522" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070522">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070523"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事004">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070523" data-content="main" data-title="苗疆道事004">苗疆道事004</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:54</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.41万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>2</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070523" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070523">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070524"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事005">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070524" data-content="main" data-title="苗疆道事005">苗疆道事005</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:33</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>9906</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>0</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070524" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070524">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070525"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事006">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070525" data-content="main" data-title="苗疆道事006">苗疆道事006</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:37</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.46万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070525" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070525">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070526"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事007">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070526" data-content="main" data-title="苗疆道事007">苗疆道事007</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:37</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.38万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070526" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070526">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070527"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事008">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070527" data-content="main" data-title="苗疆道事008">苗疆道事008</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:43</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.14万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070527" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070527">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070528"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事009">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070528" data-content="main" data-title="苗疆道事009">苗疆道事009</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>20:01</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>9746</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070528" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070528">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070529"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事010">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070529" data-content="main" data-title="苗疆道事010">苗疆道事010</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:37</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>9923</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>2</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070529" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070529">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070530"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事011">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070530" data-content="main" data-title="苗疆道事011">苗疆道事011</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:48</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.17万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070530" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070530">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070531"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事012">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070531" data-content="main" data-title="苗疆道事012">苗疆道事012</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:54</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.14万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>2</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070531" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070531">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070532"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事013">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070532" data-content="main" data-title="苗疆道事013">苗疆道事013</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:38</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.36万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>0</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070532" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070532">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070533"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事014">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070533" data-content="main" data-title="苗疆道事014">苗疆道事014</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:26</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.5万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>0</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070533" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070533">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070534"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事015">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070534" data-content="main" data-title="苗疆道事015">苗疆道事015</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:57</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.38万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070534" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070534">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070562"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事016">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070562" data-content="main" data-title="苗疆道事016">苗疆道事016</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:27</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.32万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>0</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070562" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070562">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070563"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事017">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070563" data-content="main" data-title="苗疆道事017">苗疆道事017</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>20:00</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.33万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>0</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070563" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070563">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070564"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事018">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070564" data-content="main" data-title="苗疆道事018">苗疆道事018</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:53</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.02万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>0</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070564" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070564">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070565"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事019">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070565" data-content="main" data-title="苗疆道事019">苗疆道事019</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:50</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>1.16万</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>1</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070565" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070565">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>
<li>
  <div class="icon-box">
    <span class="play-btn" data-pay="0" data-id="1007772|1070566"></span>
    <img src="https:&#47;&#47;img.aiyinsitanfm.com&#47;data&#47;img&#47;AAC&#47;AAC_008&#47;d9d36203eeab4bede9b15c984a74234e.jpg?imageView2/2/w/50/q/75!" alt="苗疆道事020">
  </div>
  <span class="sound-name">
    <a href="javascript:;" data-page="audio" data-interface="/pcaudio_info/get_page_list" data-id="1007772|1070566" data-content="main" data-title="苗疆道事020">苗疆道事020</a>
  </span>
  <div class="sound-info">
    <span class="duration"><i class="iconfont">&#xe65f;</i><em>19:43</em></span>
    <span class="play"><i class="iconfont">&#xe7c8;</i><em>9790</em></span>
    <!-- <span class="like"><i class="iconfont">&#xe684;</i><em>0</em></span> -->
    <span class="time">2017-03-31</span>
  </div>
  <div class="sound-action">
    <span class='like-btn ' data-id="1007772|1070566" data-write="favor"><i class="iconfont">&#xe684;</i></span>
    <!-- <div class="share-btn">
      <span class="share-tit"><i class="iconfont">&#xe654;</i></span>
      <div class="share-box">
        <div class="share-list" data-url="audio/1007772|1070566">
          <span class="wx"><i class="iconfont">&#xe649;</i></span>
          <span class="pyq"><i class="iconfont">&#xe6e0;</i></span>
          <span class="qq"><i class="iconfont">&#xe64b;</i></span>
          <span class="kj"><i class="iconfont">&#xe7dc;</i></span>
          <span class="wb"><i class="iconfont">&#xe64c;</i></span>
          <span class="copy"><i class="iconfont">&#xe632;</i></span>
        </div>
      </div>
    </div> -->
  </div>
</li>

'''

parser = SpiderHtmlParser()
parser.feed(str1)
print(parser.dataIds)
#
# parser = MyParser()
#
# parser.feed(strs)
#
# print(parser.dataIds)
