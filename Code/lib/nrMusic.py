# 音频处理类，包含如下的模块：
    # 音乐人声分离RVC接口 to do
    # 音频混流 VoiceMix()
    # 文字转语音 TexttoVoice()
    # 音频播放 PlayVoice()
# 因为代码少，简单，所以就没有做Visable可视化内容 … …
class nrmusic():
    # 文字转语音mp3文件
    def TexttoVoice(self, text, voicesource, voicefile, rate):
        # 需要网络，调用微软的API接口
        # text 字符串。要转换的文本内容；
        # voicesource 字符串。指定edge-tts语音模型，可以通过python命令"edge-tts --list"查看，复制name后面的那一串；
        # voicefile 字符串，.mp3文件路径。指定保存到的文件；
        # rate 字符串。百分比语速控制。
        from asyncio import new_event_loop, set_event_loop
        loop = new_event_loop()
        set_event_loop(loop)
        try:
            loop.run_until_complete(self.TexttoVoice_run(text, voicesource, voicefile, rate))
        finally:
            loop.close()
    # TexttoVoice的执行子函数
    async def TexttoVoice_run(self, text, voicesource, voicefile, rate_value) -> None:
        from edge_tts import Communicate
        voice = Communicate(text, voicesource, rate = rate_value)
        await voice.save(voicefile)

    # mp3文件播放
    def PlayVoice(self, voicefile):
        # voicefile 字符串，.mp3文件路径。指定要播放的mp3文件；
        # 请注意，该进程会执行到音频结束后退出。
        from os.path import exists, getsize
        from pygame import mixer
        from pygame.time import wait
        i = 0
        while i <= 3:
            if exists(voicefile) and getsize(voicefile) > 0:
                mixer.init()
                sound = mixer.Sound(voicefile)
                sound.play()
                wait(int(sound.get_length() * 1000))
                i = 4
            else:
                i = i + 1
                wait(500)

    # 音频文件混流
    def VoiceMix(self, file_1, file_2, outputfile):
        # 需要ffmpeg支持库，请将其存放到代码中的指定位置；
        # file_1 字符串，.mp3文件路径。指定需要混流的文件；
        # file_2 同上；
        # outputfile 字符串，.mp3文件路径。混流后的导出文件；
        from pydub import AudioSegment
        mp3_1 = AudioSegment.from_mp3(file_1)
        mp3_2 = AudioSegment.from_mp3(file_2)
        mixed = mp3_1.overlay(mp3_2, position=0, gain_during_overlay=0)
        mixed.export(outputfile, format="mp3")