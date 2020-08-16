# PyInstaller
## About
工作原因，需要将Python程序打包成.exe文件，在网上搜索之后发现Pyinstaller是目前比较稳定好用的一个程序，于是果断下载，上手使用。

在此之前有过一次失败的Pyinstaller打包，是由于原文件import的包太多，加上对Pyinstaller指令不熟悉，生成的exe文件非常大而且执行时会闪退。

这次重新尝试Pyinstaller，依然遇到很多坑，但是通过不断查资料、上论坛，基本得到了解决，成功地把程序打了包（main.exe）并用.bat做了批处理，移植到其他windows电脑上也可以正常运行（64位/32位）。

在这里总结一下一些我遇到的问题以及我尝试的解决方案。

## Trials and Errors
1. **打包方式（-F和-D）**：如果只有单个Py文件可以使用-F直接打包，但是多个文件之间有import关系要使用-D。我的程序是多个文件，之前失败的打包用了网上抄来的一段指令，生成的exe点开后会直接闪退:

        pyinstaller -F xxx.py -p /importfilepath/importfile1 -p /importfilepath/importfile2 ...
    
    这次换了-D的指令，exe没有出现闪退情况：
    
        pyinstaller -D xxx.py

2. **主文件需要import其他Python文件**：之前我使用-p指令来包含需要import的文件路径，但是在命令行一个一个把文件路径拷进去非常麻烦，而且容易出错不易修改。这次使用的是在 `.spec` 文件的Analysis括号后的第一个[]内把需要import到的python文件名都写上，比较清晰而且可以反复修改。

3. **主文件需要阅读其它类型的文件**：我的程序中需要阅读一个 `.yaml` 配置文件，但是不知道如何把它加入.exe的打包路径中，导致每次打包出的文件会报错：`.yaml`文件不存在。经过搜索了解，这类在程序中会被用到的其他类型文件需要写在 `.spec` 文件Analysis的datas一栏内，形式是tuples，每个tuple第一个元素是需要使用到的文件的路径，第二个元素是文件在即将生成的.exe文件所在的文件夹中的路径。例如：

        datas=[('config.yaml', 'configuration')]
        
    会将 `config.yaml` 复制一份放入.exe所在路径中一个新创建的 `configuration` 文件夹中。
    
4. **移植到其他机器上可能遇到路径问题**：可能在Python程序内使用了相对路径，在其他电脑上无法正常运行。我参考的是[Pyinstaller 打包发布经验总结](https://blog.csdn.net/weixin_42052836/article/details/82315118)内“冻结打包路径”中的第二种方式，通过创建一个frozen函数，可以解决相对路径存在的问题，比os.getcwd()更可靠（因为在cmd中运行程序时，当前路径不一定是程序所在的路径，用getcwd可能会报错）。

5. **打包时超过最大递归深度**：可能是某个包递归次数过多，可以在 `.spec` 文件中

        # -*- mode: python ; coding: utf-8 -*-

    
    的下一行，加上

        import sys
        sys.setrecursionlimit(1000000)
        
6. **“Fatal error detected: Failed to execute script xxx”或者双击.exe文件无法运行**：总结下来有几个可能的原因：

    1) import到主文件内的其他python文件内有 `if __name__ == '__main__'` 代码块，可能导致程序的混乱，可以尽量避免在要打包的import文件内写入这类测试代码块
        
    2) 读文件时发生路径错误，我在检查代码时发现自己把绝对路径写成了相对路径
        
    3) 程序内有在console内打印/交互的代码，但是打包出的文件没有显示console：我自己的程序用的是Tkinter的GUI，同时也需要console窗口的打印（`print`）和交互（`input()`），但是默认的 `.spec` 中，默认值为 `console=False` ，即不产生console窗口。在这种情况下，把这一参数改为 `console=True` 就可以在运行.exe文件时显示console窗口了

7. **重复配置.spec文件**：每次对 `.spec` 文件作出修改之后，需要运行：

        pyinstaller -D xxx.spec
        
    来重新生成新的打包目录，打包目录有两个文件夹：build（打包过程中生成的临时文件目录）和dist（打包结果目录，包含.exe文件）。
    
    之前重新打包的时候有时会出现 `WARNING: The output directory "/mypath/dirname" and ALL ITS CONTENTS will be REMOVED! Continue? (y/n)`，可以手动输入y，也可以在重新打包之前直接删除已有的dist和build让它再次生成两个文件夹避免出现这个warning。
    
    我自己在单位电脑上尝试的时候发现手动输入y会报错：`PermissionError: [WinError 5] Access is denied`，保险起见还是采用删除文件夹的方式。


## References
[1] [pyinstaller打包python项目（关于py文件使用相对路径导致exe闪退的解决方案）](https://blog.csdn.net/weixin_40354547/article/details/103409736?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight)

[2] [Pyinstaller 打包发布经验总结](https://blog.csdn.net/weixin_42052836/article/details/82315118)

[3] [python打包可执行文件详解（pyinstaller）](https://blog.csdn.net/ChanceYing/article/details/104973317)
