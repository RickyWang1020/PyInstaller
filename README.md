# PyInstaller
## About
工作原因，需要将Python程序打包成.exe文件，在网上搜索之后发现Pyinstaller是目前比较稳定好用的一个程序，于是果断下载，上手使用。

在此之前有过一次失败的Pyinstaller打包，是由于原文件import的包太多，加上对Pyinstaller指令不熟悉，生成的exe文件非常大而且执行时会闪退。

这次重新尝试Pyinstaller，依然遇到很多坑，但是通过不断查资料、上论坛，基本得到了解决，成功地把程序打了包（main.exe）并用.bat做了批处理，移植到其他windows电脑上也可以正常运行（64位/32位）。

在这里总结一下一些我遇到的问题以及我试的解决方案。

## Trials and Errors
1. 打包方式（-F和-D）：如果只有单个Py文件可以使用-F直接打包，但是多个文件之间有import关系要使用-D。我的程序是多个文件，之前失败的打包用了网上抄来的一段指令，生成的exe点开后会直接闪退:

        pyinstaller -F main.py -p /importfilepath/importfile1 -p /importfilepath/importfile2 ...
    
    这次换了-D的指令，exe没有出现闪退情况：
    
        pyinstaller -D main.py

2. 主文件需要import其他Python文件：之前我使用-p指令来包含需要import的文件路径，但是在命令行一个一个把文件路径拷进去非常麻烦，而且容易出错不易修改。这次使用的是在.spec文件的Analysis括号后的第一个[]内把需要import到的python文件名都写上，比较清晰而且可以反复修改。

3. 主文件需要阅读其它类型的文件：我的程序中需要阅读一个.yaml配置文件，


## References
https://blog.csdn.net/weixin_40354547/article/details/103409736?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight

https://blog.csdn.net/weixin_42052836/article/details/82315118

https://blog.csdn.net/ChanceYing/article/details/104973317
