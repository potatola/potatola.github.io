Title: Mediastreamer2-2.11 windows VS2010 编译 
Date: 2015-10-20 07:23:54
Tags: Video streaming, Coding
Slug: Mediastreamer2-compilation

之前一直在用Linphone软件下的开源库Mediastreamer2-2.8版本做实时视频传输中码率自适应的实验, 在底层oRTP库里面实现了一些自己的算法, 虽说问题不少, 也还算取得了一点成果. 最近准备在FEC冗余保护方面做一些系统实现, 依然选择在Mediastreamer2上做. 不过考虑到社区一直对Linphone进行更新, 可能已经做了很多改进和修复, 所以决定下载最新版本的Mediastreamer2进行实验. 没想到光是编译就用了好几天时间, 自己对Windows程序的编译/链接等过程确实没太多了解, 主要用了低效率的暴力尝试法(瞎试), 这里简单记录下过程.

<!-- PELICAN_END_SUMMARY -->

## 环境准备

首先当然是在Linphone官网 [下载页面](http://www.linphone.org/technical-corner/mediastreamer2/downloads) clone代码, 下载Mediastreamer2后, 还要根据`README`里的指示下载好`oRTP`模块和`linphone-deps`部分. README中windows相关说明如下:

>   * **Windows XP and later with Visual Studio 2010**
	1) Make a directory where you have together:
		oRTP (clone from git://git.linphone.org/ortp.git )
		mediastreamer2 (clone from git://git.linphone.org/mediastreamer2.git)
		linphone-deps (directory to be created).
	2) Download latest linphone-deps-win32 zip from http://download-mirror.savannah.gnu.org/releases/linphone/misc/ and unpack it in the linphone-deps directory.
	3) open build/win32native/mediastreamer2.sln
	
注意直接按照里面的要求做完之后还会有很多问题, 下面一一解决.

## 编译问题及解决

整个解决方案包含三个项目, 分别是`mediastreamer`, `mediastreamer2`和`oRTP`, 这时候直接启动调试会发现一堆编译错误.

### 启动项设置

我们的目标是生成Mediastreamer2.exe用于视频传输的测试, 打开sln之后启动项目是mediastreamer2库项目, 需要把mediastreamer设为启动项目.(右键->设为启动项目)

### oRTP问题: 缺失文件
oRTP生成过程主要报错

>	fatal error C1083: 无法打开源文件:“..\..\src\zrtp.c”: No such file or directory

包括`zrtp.c`, `stun.c`等几个文件都提示找不到, 感觉这几个文件应该是移动到mediastreamer2里了, 但是oRTP配置里面没有删. 直接把几个找不到的文件从项目索引里移除.

另外还有报错

>	fatal error C1083: 无法打开包括文件:“inttypes.h”: No such file or directory

搜一下发现`ortp\include\MSVC`目录下面有此文件, 而oRTP项目的附加包含目录里没有这个目录, 添加之. (右键->属性->C/C++->附加包含目录)

### mediastreamer2问题: 缺失文件

>	error C2065: “HAVE_NON_FREE_CODECS”: 未声明的标识符

直接在用的地方先定义一下这个变量, 搜到文件`configure.ac`里面对这个变量的说明是`whether non free codecs are allowed in the build`, 这里就定义成`0`好了...

>	error C2054: 在“inline”之后应输入“(”
	error C2085: “payload_header_set”: 不在形参表中

在错误位置之前加入

	:::c++
	#if defined(WIN32) && !defined(__cplusplus)
	#define inline __inline
	#endif

参考 http://blog.csdn.net/wl_fln/article/details/8672782

>	fatal error C1083: 无法打开源文件:“..\..\src\audiofilters\msconf.c”: No such file or directory

好像没有用到这个文件, 直接从项目索引里移除.

### mediastreamer2问题: 无法解析的外部符号

上述问题解决之后, 就会出来五十多个 `error LNK2019: 无法解析的外部符号`的问题. 这个问题的原因是项目生成lib文件的时候声明了这些函数, 但是没有把他们的实现文件(.c文件)加入到文件索引里.
我的方法是用`grepWin`软件在mediastreamer2文件夹内查找到对应函数的实现, 然后在mediastreamer2项目中添加这个文件(右键->添加->现有项...), 涉及到的文件包括：

	mediastreamer2:
	mediastreamer2\include\mediastreamer2\msfactory.c
	mediastreamer2\src\crypto\{all}
	mediastreamer2\src\utils\stream_regulator.c
	mediastreamer2\src\voip\stun.c
	mediastreamer2\src\voip\rfc4103_textstream.c
	mediastreamer2\src\videofilters\videoenc.c
	mediastreamer2\src\voip\video_preset_high_fps.c
	mediastreamer2\src\base\msvideopresets.c
	mediastreamer2\src\voip\stun_udp.c
	ortp:
	ortp\src\extremum.c
	mediastreamer:
	mediastreamer2\tools\common.c


注意类似下面的几条日志需要特殊处理:

>	msvolume.obj : error LNK2019: 无法解析的外部符号 __imp__ortp_extremum_init，该符号在函数 _volume_init 中被引用

对应函数`ortp_extremum_init`要在oRTP项目中搜索相应.c文件并添加到ortp项目文件索引里.

>	2>msvoip.obj : error LNK2001: 无法解析的外部符号 _ms_snow_enc_desc
	2>msvoip.obj : error LNK2001: 无法解析的外部符号 _ms_conf_desc

是因为定义它们的文件`videoenc.c`中, 相关代码被`#ifdef`部分屏蔽掉了. 我感觉这几个函数应该没用到, 直接在`viopdescs.h`文件里把相关声明删除了.

### mediastreamer问题: 缺失文件

少了`common.h`等文件, 解决方法同上.

## 运行

上述问题都解决之后就可以运行程序了, 注意运行的时候需要添加一些命令行参数, 否则窗口就直接关闭了. 如果想直接用调试模式运行程序, 测试功能, 可以在项目设置里添加参数, (右键->属性->调试->命令参数)
比如参数 `--local 5000 --remote 127.0.0.1:5000 --payload 103`