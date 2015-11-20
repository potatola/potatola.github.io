Title: 为 github pages 添加 godaddy 域名
Date: 2015-11-20 21:13:52
Tags: 
Slug: github-pages-godaddy

用Pelican和Github pages搭静态博客还是很方便的, 美中不足是默认只能使用 XXX.github.io 这样比较Geek的域名. Github提供了自定义域名的设置, 可以很容易地为个人博客设定个性化的域名. 而要买域名就去godaddy上剁手吧.

为github pages位置自定义域名主要操作包括:

1. godaddy购买域名
1. 为github pages项目添加CNAME文件
1. 在godaddy配置域名
1. 等待DNS生效

<!-- PELICAN_END_SUMMARY -->

# godaddy购买域名

- 注册 [godaddy](https://www.godaddy.com/) 用户
- 搜索想要的域名, 只要列出来的都是可以使用的, 下单付费即可.

# 为github pages项目添加CNAME文件

- 打开自己的github pages项目, 在`master`分支中添加一个`CNAME`文件(全部大写). 内容只有一行, 就是自己的域名(例如`gengyf.com`)

# 在godaddy配置域名

- 登录godaddy, 在`Visit My Account`页面中点击`DOMAINS`右侧的`Manage`按钮打开自己的域名列表. 点击要修改的域名右上角的设置符号, 选择`Manage DNS`.
![domains setting]({filename}/images/godaddy-domains.jpg)
- 在`DNS ZONE FILE`页面点击`Add Record`, 添加两个`A(Host)`, 其中"host" = @ and "Points to" = 192.30.252.153/154
![A host]({filename}/images/godaddy-ahost.jpg)

# 等待DNS生效

- 由于全球DNS系统的缓存更新延迟, 新的域名设置可能要等一定时间才能生效.

>	#参考内容
>
>	- [Setting up a custom domain with GitHub Pages](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/) 
>	- [Configuring a Godaddy domain name with github pages](http://andrewsturges.com/blog/jekyll/tutorial/2014/11/06/github-and-godaddy.html)