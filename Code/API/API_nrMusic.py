from Code.lib.nrMusic import nrmusic

# 这是一份nrMusic模块的API调用实例，您可以根据需求进行修改

def main():
    #展示如何将文字信息，转化为音频文件
    text = "山不在高，有仙则名。水不在深，有龙则灵。孔子云：编程好累。"   #指定转化内容
    voicesource = "zh-CN-XiaoxiaoNeural"      #指定音源，通过命令查看可选项
    voicefile = r"Temp\voice.mp3"       #指定转化后的文件位置
    rate = "-10%"           #语速控制
    #调用库中的文字转语音方法
    nrmusic().TexttoVoice(text, voicesource, voicefile, rate)

    #调用库中的音频播放方法
    nrmusic().PlayVoice(voicefile)  #指定播放的文件内容

    #调用库中的音频混流方法
    nrmusic().VoiceMix(voicefile, r"Temp\temp.mp3", r"Temp\mix.mp3")  #三个都是文件路径，注意加r防止转义字符的影响

if __name__ == '__main__':
    main()