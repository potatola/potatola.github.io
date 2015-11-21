Title: Github pages和Pelican搭建静态博客
Date: 2014-11-24 13:23:21
Tags: Blog
slug: setup-pelican-github

Octopress刚刚安装完, 我这个败家玩意就开始想换一个生成器了, 因为对Ruby实在是一无所知, 在安装过程中遇到各种Bug只能疯狂google, 照搬别人的解决方案. 另外在我安装自定义主题的时候有很多不满意的地方都不太清楚怎么修改. 如果用了别人的东西写博客却连原理是什么都不知道, 就有点怂了.

好歹还是知道点Python的, 不如干脆换一个基于Python的生成器, 一番调研最后决定用Pelican了(其实就是随便挑了一个吧喂= =)

为了体现一个计算机渣硕的专业技能, 决定不看网上各种教程, 自己对照官方文档安装(‘▽′)/  

<!-- PELICAN_END_SUMMARY -->

# 安装Pelican及相关软件(Windows 7)
为了完成目标我们需要用到一些依赖软件, 比如`python` `pip` `git` 等, 简单说下.

## 安装`python` `pip` `git`
1. 我用的python版本是2.7.8, 在[python官网](https://www.python.org/downloads/)下载安装即可.
2. 安装`pip`, 参考[pip quickstart](https://pip.pypa.io/en/latest/installing.html), windows用户需要注意在PATH系统变量中添加python安装路径下的scripts文件夹.
3. 安装`git`, 直接官网下载最新版安装
4. 安装`ghp-import`, 执行`pip install ghp-import`即可. 如果安装完在命令行中提示没有这个命令, 需要把python安装目录下的`/Lib/site-packages`目录添加到系统path中.

## 安装及初始化Pelican
参照Pelican文档中[quickstart](http://docs.getpelican.com/en/3.5.0/quickstart.html)这一章可以快速完成Pelican的安装和初始化.

### 安装Pelican
在cmd窗口中执行`pip install pelican markdown`, 自动安装一堆之后显示"Successfully installed pelican markdown jinja2...". 注意可能由于网络问题超时失败, 重新执行命令即可.

# 初始化Pelican

## 新建一个Pelican目录
在你想要存放本地Pelican文件夹的地方新建文件夹(比如`Pelican`), 运行`cmd`进入该目录. 执行

    pelican-quickstart
        
回答一系列问题(除了基本信息以外其他都可以直接回车用默认设置, 后面还可以改). 这样就在`Pelican`目录中建立了基本的Pelican文件框架.

## 写第一个Blog页面
用任意文本编辑器新建一个文本文件, 内容为(举例):

    Title: My First Review
    Date: 2010-12-03 10:20
    Category: Review

    Following is a review of my favorite mechanical keyboard.
        
保存在`Pelican/content/keyboard-review.md`
接下来在项目根目录下(`Pelican`目录)执行

    pelican content

就成功建立了第一篇博文.

# 发布网页到Github Pages

## 新建Repository
申请Git账号就不说了, 为了使用Github的免费个人主页功能, 我们需要新建一个名为`{username}.github.io`的Repository(注意这里{username}必须和Github用户名相同). 详情可以参考[Github Help](https://help.github.com/articles/user-organization-and-project-pages/), 注意两点:

>You must use the username.github.io naming scheme.
>Content from the master branch will be used to build and publish your GitHub Pages site.

## 发布网页
打开`git bash`命令行窗口, 切换到Pelican根目录, 执行以下命里初始化Git Repo

    :::sh
    git init
    git commit -m 'init'
    git remote add origin git@github.com:{username}/{username}.github.io.git
        
利用`ghp-import`工具发布网页

    :::sh
    git branch gh-pages #只有第一次需要执行
    ghp-import -b master -p output #-b master指定分支为master(用于personal page), -p直接尝试push

这样就可以通过访问 `{username}.github.io` 访问博客网页了. 话说我第一次上传后等了十几分钟也没出现, 不得已把Repo删了重新上传一遍, 过了一会就有了...之前搞Octopress也是这样, 简直逼疯.

## 存档项目到git
为了能够在不同电脑上同步自己的Pelican, 我们顺便把整个Pelican目录同步到这个Repository里面, 只要新建一个分支就好了, 在Pelican根目录下执行

    :::sh
    git checkout -b source
    git add .
    git commit -m 'first commit'
    git push origin source

# 进阶功能

## 安装主题
1. 网上搜索到喜欢的Pelican主题之后(比如我使用的[bootstrap3](https://github.com/DandyDev/pelican-bootstrap3), 把主题下载到某个目录.

    git clone https://github.com/DandyDev/pelican-bootstrap3.git /path/to/bs3
        
2. 安装主题到Pelican中

    pelican-themes --install /path/to/bs3
        
3. 指定Pelican使用该主题(这里要注意上一步安装完并不代表会使用这个主题), 即修改配置文件`pelicanconf.py`中的`THEME`字段(或新建该字段)指向要使用的主题`/path/to/bs3`

## 自动部署修改
我们希望博客内容改动后能用一个脚本自动把改动内容上传到Git上, 避免输入上面几条很长的git命令, 可以用以下脚本实现:

上传网站

    :::sh
    read -p "input comment:" comment
    pelican content -s pelicanconf.py
    ghp-import -b master -m "$comment" output
    git push origin master:master -f #-f: force push

同步源代码
    
    :::sh
    read -p "input comment:" comment
    git add -A .
    git commit -m "$comment"
    git pull
    git push origin source
    
# BUG
1. 代码高亮功能, 如果是在一个列表条目下面就会失效, 比如下面这个

    :::sh
    echo "this is the code."
