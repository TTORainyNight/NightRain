# 别看了，这里只是个入口。
# 因为程序员都会习惯性的找main()，所以放了个main.py

# 启动器入口
#if __name__ == '__main__':
#    from Code.lib.nrStarter import Starter
#    Starter()

# 主程序启动入口
#if __name__ == '__main__':
#    from os import path as opath, getcwd, chdir
#    from sys import path as spath
#    # 将工作目录修改为..\bin目录
#    work_dir = opath.join(getcwd(), "bin")
#    chdir(work_dir)
#    spath.append(work_dir)
#    from Code.NightRain import NightRain
#    NightRain()
    
# 错误报告程序入口
#if __name__ == '__main__':
#    from os import path as opath, getcwd, chdir
#    from sys import path as spath
#    # 将工作目录修改为..\bin目录
#    work_dir = opath.join(getcwd(), "bin")
#    chdir(work_dir)
#    spath.append(work_dir)
#    from Code.NightRain import Bug
#    Bug()

# 开发环境入口
if __name__ == '__main__':
    from Code.NightRain import NightRain
    NightRain()