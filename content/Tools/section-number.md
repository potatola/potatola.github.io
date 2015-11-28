Title: Pelican插件: 为文章添加章节编号(section number) 
Date: 2015-11-26 12:55:35
Tags: Blog, Pelican
Slug: section-number


插件名: 'section number'

对于Pelican生成的静态博客, 根据其章节层级(默认包括`<h1> - <h6>`六种不同层级的章节标题), 为标题添加章节编号, 格式为`X.X.X 标题`.

可以在设置文件中增加变量`SECTION_NUMBER_MAX`来设置最大编号层数, 默认`SECTION_NUMBER_MAX = 3`.

插件已经添加到 Pelican "官方"插件库中, 访问地址为 [getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins).

<!-- PELICAN_END_SUMMARY -->

# 例

	# section
	blabla
	## subsection
	blabla
	## subsection
	blabla
	# section
	blabla

在文章中效果为

>1 section
>
>blabla
>
>1.1 subsection
>
>blabla
>
>1.2 subsection
>
>blabla
>
>2 section
>
>blabla

# 注意

插件默认第一次出现的标题作为最顶层章节, 例如第一次出现`h2`, 则`h2`作为顶层章节开始编号.


# 以下是测试样例

## 二级标题

段落内容

### 三级标题

段落内容

#### 四级标题

段落内容

##### 五级标题

段落内容

##### 五级标题

段落内容

## 二级标题

段落内容

#### 四级标题

段落内容

#### 四级标题

段落内容