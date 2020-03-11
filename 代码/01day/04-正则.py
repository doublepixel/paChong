import re

# pattern = re.compile(r'\d{4}')
# result = re.match(pattern, '1234')
# print(result)
#
# result = re.match(r'\d+?','1234')
# print(result)
#
# result = re.match(r'1[345678]\d{9}','13812345678')

# result = re.search(r'\d+','abc1234dfg')
# print(result)

# result = re.findall(r'\d','abc1234dfg')
# print(result)

# result = re.finditer(r'\d','abc1234dfg')
# for i in result:
#     print(i)


name = '陈前是个大富翁陈前'

# 分割
# result = name.split('前')
# print(result)
#
# result = re.split('前', name)
# print(result)

# 替换
# result = re.sub('陈前', '小马云', name, count=1)
# print(result)

# name = name.replace('陈前', '小马云')
# print(name)


s = '''<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; chaRset=utf-8" />
<meta name="renderer" content="ie-stand">
<title>世说新语 - 内涵吧</title>
<meta name="applicable-device" content="pc">
<meta http-equiv="X-UA-Compatible" content="IE=9; IE=8; IE=7; IE=EDGE">
<meta name="keywords" content="" />
<meta name="description" content="让你了解最近网络上流行的语言都有什么，含义是什么，做一个用不out的人，就关注最新网络流行语吧，再不学习就真的out了！自造网络成语你懂吗？." />
<link rel="stylesheet" type="text/css" href="/css/wui_reset.css">
<link rel="stylesheet" type="text/css" href="/css/default.css">
<link rel="stylesheet" type="text/css" href="/css/css-shake.css">
<script src="/js/jquery-1.8.3.min.js"></script>
<script src="/js/jquery.timeago.js"></script>
<script src="/js/main.js"></script>
<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.neihan8.com/lxy//" >
<script type="text/javascript">
(function(){var ua=navigator.userAgent.toLowerCase();var bIsIpad=ua.match(/ipad/i)=="ipad";var bIsIphoneOs=ua.match(/iphone os/i)=="iphone os";var bIsAndroid=ua.match(/android/i)=="android";var bIsWM=ua.match(/windows mobile/i)=="windows mobile";if(bIsIpad||bIsIphoneOs||bIsAndroid||bIsWM){window.location.href="http://m.neihan8.com/lxy//"}})();
</script>
</head>
<body>
<div class="wrap header">
  <div class="inner">
    <h2 class="logo"> <a href="/" ><img src="/images/logo.png" alt="内涵吧" /></a> </h2>
    <ul class="top-nav"><!--
      <li><a href="#" target="_blank" class="icon-hd-originality csshake shake-rotate">原创</a></li>
      <li><a href="#" target="_blank" class="icon-hd-bzp csshake shake-opacity">暴走拍</a></li>
      <li><a href="#" target="_blank" class="icon-hd-bqg csshake shake-rotate">表情馆</a></li>
      <li><a href="#" target="_blank" class="icon-hd-gg csshake shake-little">公告</a></li>
      <li><a href="#" target="_blank" class="icon-hd-xl csshake">系列</a></li>
      <li><a href="#" target="_blank" class="icon-hd-ncdh csshake shake-slow">脑残对话</a></li>
      <li><a href="#" target="_blank" class="icon-hd-gif csshake shake-hard">GIF怪兽</a></li>
      <li><a href="#" target="_blank" class="icon-hd-lt csshake shake-crazy">论坛</a></li>-->
      <li><a href="https://www.neihan8.com/tags/" target="_blank" class="icon-hd-stc csshake shake-rotate">神吐槽</a></li>
      <li><a href="/ribao/" target="_blank" class="icon-hd-bzrb csshake shake-opacity">内涵日报</a></li>
    </ul>
  </div>
</div>
<div class="wrap nav">
  <div class="inner">
    <div class="menu">
      <ul>
        <li class="home" id="nav-home"><a href="/" rel="nofollow">主站</a></li>
        <li class="menu-top" id="nav-pic"><a href="/tupian//"><img src="/images/pic-ico.png"/> 图片 <img src="/images/nav-arrow.png" /> </a>
          <ul class="menu-sub menu-text">           
           <li><a href="/pic//" title="内涵图">内涵图</a></li><li><a href="/mm/" title="妹纸图">妹纸图</a></li><li><a href="/ps/" title="恶搞PS">恶搞PS</a></li><li><a href="/pic/xlbk/" title="笑料百科">笑料百科</a></li><li><a href="/gaoxiaomanhua/" title="搞笑漫画">搞笑漫画</a></li><li><a href="/gif/" title="GIF动态图">GIF动态图</a></li><li><a href="/pic/mjx/" title="奇葩买家秀">奇葩买家秀</a></li><li><a href="/baozou/" title="暴走漫画">暴走漫画</a></li>  
          </ul>
        </li>
        <li class="menu-top"  id="nav-video"><a href="/shipin/"><img src="/images/video-ico.png"/> 视频 <img src="/images/nav-arrow.png" /> </a>
          <ul class="menu-sub menu-video " style="z-index: 999;">            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/" target="_blank"><img src="/images/video1.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/daomeixiong/" target="_blank"><img src="/images/video2.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/smzgw/" target="_blank"><img src="/images/video3.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/yqzsf/" target="_blank"><img src="/images/video4.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="#" target="_blank"><img src="/images/video5.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/laoshi/" target="_blank"><img src="/images/video6.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/mmhh/" target="_blank"><img src="/images/video7.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>            
            <li style="width: 300px; height: 100px;"><a class="submenu" href="/video/jianbixiaohua/" target="_blank"><img src="/images/video8.jpg" style="margin-left: -10px;" width="300" height="100"></a></li>           
          </ul>
        </li>
        <li class="menu-top" id="nav-txt"><a href="/wenzi//"><img src="/images/text-ico.png"/> 段子 <img src="/images/nav-arrow.png" /> </a>
        <ul class="menu-sub menu-text">
             <li><a href="/lxy//" title="世说新语">世说新语</a></li><li><a href="/lxh//" title="冷笑话">冷笑话</a></li><li><a href="/njjzw//" title="脑筋急转弯">脑筋急转弯</a></li><li><a href="/article//" title="内涵段子">内涵段子</a></li> 
          </ul>
        </li>
        <li><a href="/s/" target="_blank"><img src="/images/pb-ico.png"/> 瀑布流看图</a></li>
        <li><a href="/zm/" target="_blank"><img src="/images/zzq-ico.png"/>内涵字幕制作器</a></li>
      </ul>
    </div>
    <div class="user" id="show_userinfo"><li class="menu-pm"><a  href="javascript:void(0);" target="_self" onclick="AjaxLog()" rel="nofollow">登录</a></li><li class="menu-pm"><a href="/e/member/register/index.php?tobind=0&groupid=1" target="_blank" class="new_top_reg" rel="nofollow">注册</a></li></div>
  </div>
</div>
 <script type="text/javascript" src="/e/member/ajaxlog/?loadjs=1"></script>
<script>$("#nav-txt").addClass("curr");</script>
<div class="crumbs wrap">
<div class="inner">
<a href="/">内涵吧</a>&nbsp;>&nbsp;<a href="/wenzi//">段子</a>&nbsp;>&nbsp;<a href="/lxy//">世说新语</a>
</div>
</div><div class="main wrap">
  <div class="inner">
    <div class="left">
      <div class="column-title box box-790"> <a href="/lxy/" class="pic"> <img src="http://imgs.isocialkey.com/p/2015-09-23/cf0f9dc133cc2844f7bdb052034f5cb6.jpg" width="145" height="145" /> </a>
        <h1><a class="title">世说新语</a><b>作者：世说新语作者</b></h1>
        <div class="desc"> 让你了解最近网络上流行的语言都有什么，含义是什么，做一个用不out的人，就关注最新网络流行语吧，再不学习就真的out了！自造网络成语你懂吗？....</div>
      </div>      
      <div class="text-column-list mt10">      
           
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/157898.html" class="title" title=""蓝瘦香菇"是什么？">"蓝瘦香菇"是什么？</a></h3>
        <div class="desc">　　“蓝瘦，香菇”是“难受，想哭”的意思。广西的壮语里面的发音没有翘舌音，没有送气音。 <br />
　　2016年10月，广西南宁一小哥失恋后录视频：“蓝瘦，香菇”，本来今颠高高兴兴，泥为什莫要</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-10-11.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >22</div>
                <div class="bad" >10</div>
                <div class="view" >1910</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/156175.html" class="title" title="我和我大表哥二表哥都笑了">我和我大表哥二表哥都笑了</a></h3>
        <div class="desc">最近，网络上流行着这样一句话：我和我大表哥二表哥都笑了。这究竟是什么意思呢？其实，这句我和我大表哥二表哥都笑了是一张搞笑图片上的文字。形式诙谐幽默。</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-09-28.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >23</div>
                <div class="bad" >7</div>
                <div class="view" >3404</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/153012.html" class="title" title="撩粉是种怎样的体验">撩粉是种怎样的体验</a></h3>
        <div class="desc"> 　　释义：指与粉丝调侃互动，懂得讨粉丝欢心。　　人间精品花式撩粉界一哥大张伟大老师撩粉界的一股清(泥石)流。把粉丝称呼为大蜜(不同地区的粉丝还有大老师钦点专属”&amp;times</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-09-09.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >19</div>
                <div class="bad" >4</div>
                <div class="view" >2350</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/153009.html" class="title" title="老翻颠">老翻颠</a></h3>
        <div class="desc"> 　　老翻颠通常用于调侃某人老糊涂了。　　老翻颠的代表形象是动漫《樱桃小丸子》中的爷爷一角。</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-09-09.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >18</div>
                <div class="bad" >5</div>
                <div class="view" >1319</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/153006.html" class="title" title="宇宙葬是什么意思">宇宙葬是什么意思</a></h3>
        <div class="desc"> 　　日本“宇宙葬”这个名词近几年已开始出现，可让一些人选择在自己死后，把骨灰送上太空。日本有公司甚至会将服务“升级”，把骨灰送到月球。　　/你们问过宇宙了吗/　　日本</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-09-09.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >19</div>
                <div class="bad" >5</div>
                <div class="view" >1378</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/152692.html" class="title" title="伦家是什么意思">伦家是什么意思</a></h3>
        <div class="desc">伦家，网络主流名词，伦家就是“人家”的意思，多见于聊天，帖子中，是女生卖萌撒娇中常用的词。多用于指代说话人自己。而非普通的“人家”指代的他人，属于网络语言。</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-09-08.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >18</div>
                <div class="bad" >7</div>
                <div class="view" >1098</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/152514.html" class="title" title="先定一个能达到的小目标，比如挣它一个亿">先定一个能达到的小目标，比如挣它一个亿</a></h3>
        <div class="desc"> 最近，朋友圈就被一个关于王健林的截图刷屏了，就是&quot;先定一个能达到的小目标，比方说我先挣它一个亿”。那么，这又是什么意思呢？在《鲁豫大咖一日行》节目中，鲁豫深入万达集团，采访了</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-09-07.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >18</div>
                <div class="bad" >8</div>
                <div class="view" >924</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/152166.html" class="title" title="当红炸子鸡是什么意思">当红炸子鸡是什么意思</a></h3>
        <div class="desc"> 比喻正走红，最近很受追捧的人或物。被人称为事物流行或潮流的指向。</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-09-05.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >20</div>
                <div class="bad" >5</div>
                <div class="view" >906</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/150853.html" class="title" title="北京瘫是什么意思">北京瘫是什么意思</a></h3>
        <div class="desc">“北京瘫”是一种坐姿，网络语，形容北京孩子没坐相儿。“北京瘫”源自大张伟在某节目中自称北京孩子没坐相儿。按照大张伟说出的北京人特性，网友找出了娱乐圈中的“京城四瘫”，分</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-30.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >18</div>
                <div class="bad" >6</div>
                <div class="view" >1172</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/150640.html" class="title" title="这是马蓉最新号码是什么梗">这是马蓉最新号码是什么梗</a></h3>
        <div class="desc">随着王宝强马蓉离婚事件的不断热搜，近来也出现了有关马蓉的网络新词，那就是这是马蓉最新号码！那么，这是马蓉最新号码是什么梗？大家请往下看。面对提出分手的女友，黄山一男子为了泄</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-29.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >11</div>
                <div class="bad" >2</div>
                <div class="view" >873</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/150639.html" class="title" title="一言不合就开车什么梗">一言不合就开车什么梗</a></h3>
        <div class="desc"> 一言不合就开车什么梗？作为网友们当下最常用的网络用语，许多网友都会讲这句话挂在嘴边，但是至于这句话的出处和意思,一起来看看吧！这个现在主要指喜欢发一些特殊资源的事情，最早</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-29.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >7</div>
                <div class="bad" >4</div>
                <div class="view" >926</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/150454.html" class="title" title="大数据是什么意思">大数据是什么意思</a></h3>
        <div class="desc"> 现在网络上流行着一个新词，就是大数据。大家知道大数据是什么意思吗？对于“大数据”(Big  data)研究机构Gartner给出了这样的定义。“大数据”是需要新处理模式才能具有更强</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-27.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >7</div>
                <div class="bad" >4</div>
                <div class="view" >612</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/149989.html" class="title" title="黑风梨是什么意思">黑风梨是什么意思</a></h3>
        <div class="desc">之前，网络上面流传一个叫做《黑凤梨》的短视频，那么大家知道黑凤梨到底是什么意思吗?下面，小编为大家解释一下。  其实，黑凤梨是粤语喜欢你的谐音，来自于邓紫棋翻唱的beyond的《</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-24.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >8</div>
                <div class="bad" >4</div>
                <div class="view" >813</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/149988.html" class="title" title="喵星人是什么意思">喵星人是什么意思</a></h3>
        <div class="desc">现在有很多人经常讲喵星人什么什么的，那么大家知道喵星人是什么意思吗？喵星人  ，是一种网络语言，假想猫咪是从遥远外太空来的，喵星人是来到地球的外星人，因为很萌的外表而获得人类</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-24.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >10</div>
                <div class="bad" >2</div>
                <div class="view" >1392</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/149605.html" class="title" title="段子手是什么意思">段子手是什么意思</a></h3>
        <div class="desc">段子手是写段子的笔者，而与作家一类进行区分的则是段子手大多以副业的形式存在而非主业，除却写段子以外仍有其他的工作。关于段子手的定义很多，个人觉着段子手不只是会说几句俏</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-22.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >6</div>
                <div class="bad" >1</div>
                <div class="view" >758</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/149388.html" class="title" title="大满贯是什么意思">大满贯是什么意思</a></h3>
        <div class="desc">相信大家在历届奥运会上的时候都会听到某某某大满贯了之类的！那么，大伙儿知道什么是大满贯吗？大满贯原本是桥牌术语，解作赢得一局中所有的叫牌，而中文译名则来自麻将术语。在中国</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-20.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >4</div>
                <div class="bad" >2</div>
                <div class="view" >262</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/149280.html" class="title" title="接盘侠是什么意思">接盘侠是什么意思</a></h3>
        <div class="desc">接盘一开始是用来形容股票的，现在多指在不知情的情况下娶了怀了别的男人孩子的女人，就叫做接盘侠，也就是喜当爹的男人，也可以用来形容那些被骗接下别人留下的烂摊子的人。</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-19.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >6</div>
                <div class="bad" >4</div>
                <div class="view" >998</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/149085.html" class="title" title="童子蛋是什么梗">童子蛋是什么梗</a></h3>
        <div class="desc">童子蛋最近在新闻上又掀起一波舆论，其做法是用童子尿来煮鸡蛋，据说还入选了非物质文化遗产。一般都是好多户人家一起煮的，大家都在自己家的鸡蛋上用碳做上记号，再用大锅煮两天一</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-17.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >7</div>
                <div class="bad" >3</div>
                <div class="view" >262</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/149084.html" class="title" title="洪荒之力是什么意思">洪荒之力是什么意思</a></h3>
        <div class="desc">洪荒之力源于此前的一部热播剧《花千骨》，大家应该都听过吧。东海无名小岛，花千骨要求单春秋交出白子画，单春秋得意洋洋称白子画已经昏迷不醒，正躺在某处自生自灭。花千骨救白子</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-17.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >4</div>
                <div class="bad" >4</div>
                <div class="view" >514</div>             
            </div>
      </div>
	     
			<div class="text-column-item box box-790">
        <h3><a href="/lxy/148998.html" class="title" title="中元节是什么节">中元节是什么节</a></h3>
        <div class="desc">中元节，俗称鬼节、施孤、七月半，佛教称为盂兰盆节。与除夕、清明节、重阳节三节是中国传统的祭祖大节，也是流行于汉字文化圈诸国的传统文化节日。中元节有放河灯、焚纸锭的习俗</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2016-08-16.0"></time><i>属于：<a href="/lxy//" class="title">世说新语</a></i></div>
                <div class="good" >7</div>
                <div class="bad" >4</div>
                <div class="view" >274</div>             
            </div>
      </div>
	
      </div>     
       <div class="pagenav"><a href="#" class="prev">上一页</a><b>1</b><a href="/lxy//index_2.html">2</a><a href="/lxy//index_3.html">3</a><a href="/lxy//index_4.html">4</a><a href="/lxy//index_5.html">5</a><a href="/lxy//index_16.html">…</a><a href="/lxy//index_2.html" class="next">下一页</a><a href="/lxy//index_16.html">尾页</a><span>316条记录 2 / 16 页</span>
</div>
    </div>
<div class="sidebar">
  <div class="side-column side box">
    <h2 class="box-title" >
      <a class="name" href="/lxy/">世说新语</a>
    </h2>
    <div class="con">
	<a href="/lxy//" title="世说新语" id="cid12">世说新语</a><a href="/lxh//" title="冷笑话" id="cid13">冷笑话</a><a href="/njjzw//" title="脑筋急转弯" id="cid14">脑筋急转弯</a><a href="/article//" title="内涵段子" id="cid11">内涵段子</a>   
    </div>
  </div>
  <script type="text/javascript">
$("#cid12").addClass("curr");
</script>
  <div class="side-rank-tab side box">
    <h2 class="box-title" id="tabs">
      <li><a name="#con1">今日排行</a></li>
      <li><a name="#con2">本月排行</a></li>
      <li><a name="#con3">年度排行</a></li>
    </h2>
    <div class="con" id="cons">
      <div class="rank-list" id="con1">
        <ul>
		           <li>
            <div class="ico no-1">1</div>
            <a href="/av/34465.html" title="大桥未久(大橋未久)出道至今的作品封面以及番号大全">大桥未久(大橋未久)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-2">2</div>
            <a href="/av/34226.html" title="麻生希(あそうのぞみ)出道至今的作品封面以及番号大全">麻生希(あそうのぞみ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-3">3</div>
            <a href="/gif/104028.html" title="真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人">真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人</a>
			</li>
                    <li>
            <div class="ico no-4">4</div>
            <a href="/av/34372.html" title="波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师">波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师</a>
			</li>
                    <li>
            <div class="ico no-5">5</div>
            <a href="/av/34300.html" title="京香Julia(julia)出道至今的作品封面以及番号大全">京香Julia(julia)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-6">6</div>
            <a href="/gif/197146.html" title="日本美女啪啪啪入室 站立背后入啪啪啪图片">日本美女啪啪啪入室 站立背后入啪啪啪图片</a>
			</li>
                    <li>
            <div class="ico no-7">7</div>
            <a href="/av/34475.html" title="濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全">濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-8">8</div>
            <a href="/av/38002.html" title="新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全">新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全</a>
			</li>
                    <li>
            <div class="ico no-9">9</div>
            <a href="/av/34477.html" title="吉泽明步出道至今封面番号作品">吉泽明步出道至今封面番号作品</a>
			</li>
                    <li>
            <div class="ico no-10">10</div>
            <a href="/baozou/62656.html" title="厕所中的成语">厕所中的成语</a>
			</li>
                  </ul>
      </div>
      <div class="rank-list" id="con2">
        <ul>
                    <li>
            <div class="ico no-1">1</div>
            <a href="/av/34465.html" title="大桥未久(大橋未久)出道至今的作品封面以及番号大全">大桥未久(大橋未久)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-2">2</div>
            <a href="/av/34226.html" title="麻生希(あそうのぞみ)出道至今的作品封面以及番号大全">麻生希(あそうのぞみ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-3">3</div>
            <a href="/gif/104028.html" title="真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人">真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人</a>
			</li>
                    <li>
            <div class="ico no-4">4</div>
            <a href="/av/34372.html" title="波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师">波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师</a>
			</li>
                    <li>
            <div class="ico no-5">5</div>
            <a href="/av/34300.html" title="京香Julia(julia)出道至今的作品封面以及番号大全">京香Julia(julia)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-6">6</div>
            <a href="/gif/197146.html" title="日本美女啪啪啪入室 站立背后入啪啪啪图片">日本美女啪啪啪入室 站立背后入啪啪啪图片</a>
			</li>
                    <li>
            <div class="ico no-7">7</div>
            <a href="/av/34475.html" title="濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全">濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-8">8</div>
            <a href="/av/38002.html" title="新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全">新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全</a>
			</li>
                    <li>
            <div class="ico no-9">9</div>
            <a href="/av/34477.html" title="吉泽明步出道至今封面番号作品">吉泽明步出道至今封面番号作品</a>
			</li>
                    <li>
            <div class="ico no-10">10</div>
            <a href="/baozou/62656.html" title="厕所中的成语">厕所中的成语</a>
			</li>
                  </ul>
      </div>
      <div class="rank-list" id="con3">
        <ul>
                    <li>
            <div class="ico no-1">1</div>
            <a href="/av/34465.html" title="大桥未久(大橋未久)出道至今的作品封面以及番号大全">大桥未久(大橋未久)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-2">2</div>
            <a href="/av/34226.html" title="麻生希(あそうのぞみ)出道至今的作品封面以及番号大全">麻生希(あそうのぞみ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-3">3</div>
            <a href="/gif/104028.html" title="真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人">真人做动态进出图片:男女配交图片100张 美国人拍的命根叉进女人</a>
			</li>
                    <li>
            <div class="ico no-4">4</div>
            <a href="/av/34372.html" title="波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师">波多野结衣作品封面图片 はたの ゆい番号大全 波多野结衣家庭教师</a>
			</li>
                    <li>
            <div class="ico no-5">5</div>
            <a href="/av/34300.html" title="京香Julia(julia)出道至今的作品封面以及番号大全">京香Julia(julia)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-6">6</div>
            <a href="/gif/197146.html" title="日本美女啪啪啪入室 站立背后入啪啪啪图片">日本美女啪啪啪入室 站立背后入啪啪啪图片</a>
			</li>
                    <li>
            <div class="ico no-7">7</div>
            <a href="/av/34475.html" title="濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全">濑亚美莉(一ノ瀬アメリ)出道至今的作品封面以及番号大全</a>
			</li>
                    <li>
            <div class="ico no-8">8</div>
            <a href="/av/38002.html" title="新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全">新宅男AV女优林由奈出道至今作品番号封面 林ゆな番号大全</a>
			</li>
                    <li>
            <div class="ico no-9">9</div>
            <a href="/av/34477.html" title="吉泽明步出道至今封面番号作品">吉泽明步出道至今封面番号作品</a>
			</li>
                    <li>
            <div class="ico no-10">10</div>
            <a href="/baozou/62656.html" title="厕所中的成语">厕所中的成语</a>
			</li>
                  </ul>
      </div>
    </div>
   <script src="/js/Tab.js"></script>
  </div>
   <div class="ad">
   </div>
  <div class="side-rank side box">
    <h2 class="box-title" >
      <a class="name" href="javascript:void(0);">世说新语好评榜</a>
      <a class="more" href="javascript:void(0);" rel="nofollow">更多+</a>
    </h2>
    <div class="con" >
      <div class="rank-list">
        <ul>
    <li>
      <div class="ico no-1">1</div>
            <a href="/lxy/68942.html" title="你咋不上天呢是个什么梗">你咋不上天呢是个什么梗</a></li>
		<li>
      <div class="ico no-2">2</div>
            <a href="/lxy/41493.html" title="sp主是什么意思">sp主是什么意思</a></li>
		<li>
      <div class="ico no-3">3</div>
            <a href="/lxy/156175.html" title="我和我大表哥二表哥都笑了">我和我大表哥二表哥都笑了</a></li>
		<li>
      <div class="ico no-4">4</div>
            <a href="/lxy/73737.html" title="床咚是什么意思">床咚是什么意思</a></li>
		<li>
      <div class="ico no-5">5</div>
            <a href="/lxy/157898.html" title=""蓝瘦香菇"是什么？">"蓝瘦香菇"是什么？</a></li>
		<li>
      <div class="ico no-6">6</div>
            <a href="/lxy/65563.html" title="B站是什么意思">B站是什么意思</a></li>
		<li>
      <div class="ico no-7">7</div>
            <a href="/lxy/67725.html" title="主要看气质是什么梗">主要看气质是什么梗</a></li>
		<li>
      <div class="ico no-8">8</div>
            <a href="/lxy/152166.html" title="当红炸子鸡是什么意思">当红炸子鸡是什么意思</a></li>
		<li>
      <div class="ico no-9">9</div>
            <a href="/lxy/65564.html" title="强推是什么意思">强推是什么意思</a></li>
		<li>
      <div class="ico no-10">10</div>
            <a href="/lxy/73741.html" title="笑哭是什么意思">笑哭是什么意思</a></li>
		        </ul>
      </div>
    </div>
  </div>
  <div class="scroll">
  <div class="side-tags side box">
    <h2 class="box-title"><a class="name" href="/tags/">热门标签</a><a class="more" href="/tags/" rel="nofollow">更多+</a></h2>
    <div class="con"> 
       <a target="_blank" href="http://www.neihan8.com/tags/hhhbl/" >很黄很暴力</a><a target="_blank" href="http://www.neihan8.com/tags/budejie/" >百思不得姐</a><a target="_blank" href="http://www.neihan8.com/tags/eblw/" >隔壁老王</a><a target="_blank" href="http://www.neihan8.com/tags/yeliangchen/" >叶良辰</a><a href="/tags/nvyou/" >女优</a><a href="/tags/meizi/" >妹纸</a><a href="/tags/laoshi/" >老师</a><a href="/tags/fuli/" >福利</a><a href="/tags/fuqi/" >夫妻</a><a href="/tags/2b/" >二逼</a><a href="/tags/nvshen/" >女神</a><a href="/tags/xiaoming/" >小明</a><a href="/tags/nvdiaosi/" >女吊丝</a><a href="/tags/mengchong/" >萌宠</a><a href="/tags/danshengou/" >单身狗</a><a href="/tags/tuhao/" >土豪</a><a href="/tags/xegif/" >邪恶动态图</a><a href="/tags/tongshi/" >同事</a><a href="/tags/xuduba/" >胥渡吧</a><a href="/tags/papapa/" >啪啪啪</a><a href="/tags/qigai/" >乞丐</a><a href="/tags/yisheng/" >医生</a><a href="/tags/tongzhuo/" >同桌</a>

     </div>
  </div>
     <div class="ad">
	 </div>
  </div>
    </div>
	</div>
</div>
   	  <script type="text/javascript" src="/js/scroll.js"></script>	
<script src='/e/public/onclick/?enews=doclass&classid=12'></script>
<div class="footer wrap">
<div class="inner">
    <div class="footer-block">
      <h4>关于我们</h4>
      <ul class="footer-ul">
        <li><a href="/about.html" target="_blank" rel="nofollow">网站简介</a></li>
        <li><a href="/duty.html" target="_blank" rel="nofollow">免责声明</a></li>
        <li><a href="/joinus.html" target="_blank" rel="nofollow">加入我们</a></li>
        <li><a href="/contact.html" target="_blank" rel="nofollow">联系我们</a></li>        
        <li><a href="/feedback.html" target="_blank" rel="nofollow">反馈意见</a></li>

      </ul>
    </div>
    <div class="footer-block">
      <h4>互动规则</h4>
      <ul class="footer-ul">
        <li><a href="#" target="_blank" rel="nofollow">投稿规则</a></li>
        <li><a href="#" target="_blank" rel="nofollow">审稿规则</a></li>
        <li><a href="#" target="_blank" rel="nofollow">升级规则</a></li>
      </ul>
    </div>    
    <div class="footer-block">
      <h4>关注我们</h4>
      <ul class="footer-ul">
        <li><a href="https://weibo.com/neihan8" target="_blank">新浪微博</a></li>
        <li><a href="https://weibo.com/neihan8" target="_blank">腾讯微博</a></li>
        <li><a href="https://tieba.baidu.com/f?kw=%E5%86%85%E6%B6%B5&ie=utf-8" target="_blank" rel="nofollow">百度贴吧</a></li>
        <li><a href="https://zhan.renren.com/neihan8com" target="_blank" rel="nofollow">人人小站</a></li>
        <li><a href="#" target="_blank" rel="nofollow">人人主页</a></li>
        <li><a href="#" target="_blank" rel="nofollow">新浪微刊</a></li>
      </ul>
    </div>
    <div class="footer-block">
<h4>内涵吧IOS版</h4>
<div class="qrcode"><img style="width: 120px; height: 120px;" src="/images/app_ios.jpg" alt="内涵吧IOS版" data-bd-imgshare-binded="1"></div>
</div>
<div class="footer-block">
<h4>内涵吧安卓版</h4>
<div class="qrcode"><img style="width: 120px; height: 120px;" src="/images/app_az.jpg" alt="内涵吧安卓版" data-bd-imgshare-binded="1"></div>
</div>
<div class="footer-sign">
    </div>
    <div class="cl">
        <p>Copyright 2005-2015 Neihan8.com <a href="/" target="_blank" title="内涵吧">内涵吧</a> 版权所有 <span style="color: #333333; font-size: 12px; line-height: 16px;">沪ICP备14040517号-1</span> <div style="display:none;"><script language="javascript" src="/js/stats.js"></script></div>
</p>
    </div>
</div>
</div>
<!--<a rel="nofollow" class="feedback">
反<br>馈</a> -->
<div class="backToTop"></div>
</body>
</html>'''

pattern = re.compile(r'.*?<div class="desc">(.*?)</div>',re.S)
result = re.findall(pattern,s)
print(result)