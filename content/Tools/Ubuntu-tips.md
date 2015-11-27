Title: 使用Ubuntu的一些问题和解决办法 
Date: 2014-11-30 14:17:38
Tags: OS
Slug: Ubuntu-tips


好像天生克Linux系统, 使用Linux系统很少能够安全稳定用很长时间, 总会遇到各种问题, 甚至系统崩溃重装. 简单记录一些折腾Linux过程中遇到的问题.

1. Ubuntu挂载动态磁盘NTFS分区失败
1. Chromium Flash插件安装

<!-- PELICAN_END_SUMMARY -->


# Ubuntu挂载动态磁盘NTFS分区失败

如果刚刚从windows安装为Ubuntu, 之后发现整块磁盘上, 只有一个分区无法挂载, 提示`Error mounting : mount exited with exit code 12: Failed to read last sector` 以及 `Volume is corrupt, run chkdsk` 一类错误的问题, 有一个可能的原因, 就是:

**在windows下使用了动态磁盘分区, 并且有的分区占据了不连续的物理位置, 那么这个分区就会出现挂载失败的情况**

我的解决办法是, 重新进入windows系统(可能需要重装一个), 在windows下是能看到之前的这个分区的, 但是会显示成两个重名的分区(应该是不同物理位置各显示为一个), 执行 `chkdsk e: /f`('e:'是我那个有问题的盘的盘符), 等待修复完, 就能至少恢复大部分的数据了.


# Chromium Flash插件安装

安装了Adobe Flash, 用firefox可以正常看视频, 但是用Chromium提示需要安装flash插件并给出Adobe官网链接, 选择下载后转到"Ubuntu软件中心", 提示

>在您当前的软件源中没有名为 “adobe-flashplugin”的软件包。

## 解决

参考[Ubuntu 14.04安装Chromium浏览器并添加Flash插件Pepper Flash Player](http://www.linuxidc.com/Linux/2014-05/101095.htm), 安装插件即可.
