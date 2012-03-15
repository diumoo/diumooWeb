#diumooWeb
diumooWeb 是一个面向 Mac App 的在线主页,基于 django-sparkle 扩展研发而成,在后台支持 Sparkle 自动更新,包含一个展示页面,支持上传截屏和历史版本下载等功能.

#DIRECTIONS
1. 替换掉 static 文件夹下的 icon.png 为您自己应用的图标.
2. 修改 templaces/contact.html 在这里加入联系方式信息
3. 请确认您已经安装本应用依赖的south, 可以使用 `easy_install south` 来安装
4. 在项目文件夹下执行 `python manage.py syncdb --migrate`
5. 进入 Django 管理后台，添加一个新的 Application,应用简介一栏可以使用HTML代码
6. 在 Versions 一栏中新建一个版本，并上传您打包为 zip 文件的应用，具体内容请参考 django-sparkle 主页

#LINKS

1. demo [diumoo.xiuxiu.de](http://diumoo.xiuxiu.de)
2. django-sparkle [https://github.com/Mobelux/django-sparkle](https://github.com/Mobelux/django-sparkle)

#LICENSE
本应用基于 django-sparkle 开发完成，其中，sparkle文件夹内所有内容将使用原协议开源。其他部分使用 BSD 协议开源。

参见维基百科[相关词条](http://zh.wikipedia.org/wiki/BSD%E8%AE%B8%E5%8F%AF%E8%AF%81)以及LICENSE文件。