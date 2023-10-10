class Starter():
    def __init__(self):
        import subprocess
        from locale import getpreferredencoding
        # pyinstaller��װ̫�ӣ�pytorch��.dll��ffmpegҲ��
        # ���ұ����ǿ�Դ�ģ�Ҳ���±�����Դ���룬���Ծ�ֱ��Դ���װ�ˣ�����Ҳ��ά��
        reply = subprocess.Popen([r"runtime\pythonw.exe", r"bin\main.py"], 
            stdout = subprocess.PIPE, stderr = subprocess.PIPE, 
            encoding = getpreferredencoding(), shell = False, text = True)
            
        stdout, stderr = reply.communicate()
        if reply.returncode != 0:
            # ����ֵ��Ϊ0���������
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            errorinfo = f"{now}: {str(stderr)}\n"
            with open(r"bin\Temp\error.log", "a", encoding="utf-8") as file:
                file.write(errorinfo)
            # չʾ������Ϣ
            reply = subprocess.Popen([r"runtime\pythonw.exe", r"bin\bug.py"], 
                stdout = subprocess.PIPE, stderr = subprocess.PIPE, 
                encoding = getpreferredencoding(), shell = False, text = True)