Title: Mac使用virtualbox: 分辨率调整, command快捷键映射control
Date: 2015-11-14 11:29:32
Tags: 
Slug: mac-virtualbox-conf

最近在mac系统下使用virtualbox安装了CentOS系统进行实验, 中间遇到了CentOS系统中分辨率无法调整, 无法使用CMD+C和CMD+V等组合键等问题. 解决方法都很简单, 仅作下记录.

<!-- PELICAN_END_SUMMARY -->

# virtualbox内系统分辨率调整

安装完系统后默认分辨率可能只有很低的几个档, 要想调整分辨率, 需要安装virtualbox提供的guest additions工具. 在菜单栏的'device'下选择'install guest additions', 会在内部操作系统中虚拟一个cd光驱, 安装相应内容即可.

# Command映射Control

高冷的mac特立独行地用command按键代替通用的control快捷键, 导致mac和虚拟机切换的时候快捷键比较蛋疼. 我们可以在虚拟机CentOS系统里设置command映射成control, [参考这里](http://superuser.com/questions/385748/binding-superc-superv-to-copy-and-paste).
