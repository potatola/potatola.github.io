Title: 为Pelican+GitHub pages搭建的静态博客 添加godaddy域名
Date: 2015-11-20 21:13:52
Tags: 
Slug: GitHub-pages-godaddy

用Pelican和Github pages搭静态博客还是很方便的, 美中不足是默认只能使用 XXX.GitHub.io 这样比较Geek的域名. Github提供了自定义域名的设置, 可以很容易地为个人博客设定自定义域名. 而要买域名就去godaddy上剁手吧.

为GitHub pages位置自定义域名主要操作包括:

1. godaddy购买域名
1. 在Pelican中指定CNAME文件
1. 在godaddy配置域名
1. 等待DNS生效

<!-- PELICAN_END_SUMMARY -->

# godaddy购买域名

- 注册 [godaddy](https://www.godaddy.com/) 用户
- 搜索想要的域名, 只要列出来的都是可以使用的, 下单付费即可.

# 在Pelican中指定CNAME文件

- 要在GitHub Pages中使用自定义域名, 需要在相关repository中添加`CNAME`文件, 文件内容为自己的域名(`gengyf.com`). 因为我们的内容使用Pelican生成的, 所以这一步需要在Pelican中配置.
- 新建`content/extra`目录, 在其中添加上述`CNAME`文件. 在Pelican的配置文件(`pelicanconf.py`)中增加如下内容:

>	STATIC_PATHS = ['images', 'extra/CNAME']
>	EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# 在godaddy配置域名

- 登录godaddy, 在`Visit My Account`页面中点击`DOMAINS`右侧的`Manage`按钮打开自己的域名列表. 点击要修改的域名右上角的设置符号, 选择`Manage DNS`.

![domains setting]({filename}/images/godaddy-domains.jpg)

- 在`DNS ZONE FILE`页面点击`Add Record`, 添加两个`A(Host)`, 其中"host" = @ and "Points to" = 192.30.252.153/154

![A host]({filename}/images/godaddy-ahost.jpg)

# 等待DNS生效

- 由于全球DNS系统的缓存更新延迟, 新的域名设置可能要等一定时间才能生效.

>	#参考内容
>
>	- [Setting up a custom domain with GitHub Pages](https://help.GitHub.com/articles/setting-up-a-custom-domain-with-GitHub-pages/) 
>	- [Configuring a Godaddy domain name with GitHub pages](http://andrewsturges.com/blog/jekyll/tutorial/2014/11/06/GitHub-and-godaddy.html)