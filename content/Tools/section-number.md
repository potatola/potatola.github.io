Title: Pelican插件: 为文章添加章节编号(section number) 
Date: 2015-11-26 12:55:35
Tags: Blog, Pelican
Slug: section-number

# Section number

插件根据文章章节标题(`h1`/`h2`等), 为所有文章添加章节编号.

可以在设置文件中增加变量`SECTION_NUMBER_MAX`来设置最大编号层数, 默认`SECTION_NUMBER_MAX = 3`.


# 注意

插件默认第一次出现的标题作为最顶层章节, 例如第一次出现`h2`, 则`h2`作为顶层章节开始编号.

<!-- PELICAN_END_SUMMARY -->


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