class Starter():
    def __init__(self):
        import subprocess
        from locale import getpreferredencoding
        # pyinstaller封装太坑，pytorch丢.dll，ffmpeg也丢
        # 而且本来是开源的，也不怕别人拿源代码，所以就直接源码封装了，后面也好维护
        reply = subprocess.Popen([r"runtime\pythonw.exe", r"bin\main.py"], 
            stdout = subprocess.PIPE, stderr = subprocess.PIPE, 
            encoding = getpreferredencoding(), shell = False, text = True)
            
        stdout, stderr = reply.communicate()
        if reply.returncode != 0:
            # 返回值不为0，程序出错
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            errorinfo = f"{now}: {str(stderr)}\n"
            with open(r"bin\Temp\error.log", "a", encoding="utf-8") as file:
                file.write(errorinfo)
            # 展示错误信息
            reply = subprocess.Popen([r"runtime\pythonw.exe", r"bin\bug.py"], 
                stdout = subprocess.PIPE, stderr = subprocess.PIPE, 
                encoding = getpreferredencoding(), shell = False, text = True)