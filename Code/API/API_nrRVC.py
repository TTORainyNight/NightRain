from Code.lib.nrRVC import nrVoiceChange as vcm

# 这是nrRVC变声模块的API接口实例
# 更加详细的参数说明，请转到文件查看注释
# 本实例实现了对于语音文件的转化功能
# 参数准备
if True:
    f0up_key = "-12"  # 变调，这里是女转男
    input_audio = r"B:\NightRain\Source\people.wav"    # 待处理文件
    index_path = r"User\AIfywy.index"  # 声音模型index
    f0method = "crepe"  # 使用GPU进行推理
    opt_path = r"B:\temp\out.wav"  # 输出文件
    model_path = r"User\AIfywy.pth"  # 声音模型pth
    index_rate = 0.75    # 检索特征占比
    device = "cuda:0"  # 使用GPU设备
    is_half = True     # 打开就完了
    filter_radius = 3   # 中值滤波半径
    resample_sr = 0     # 不重新采样
    rms_mix_rate = 0.25    # 输出包融合占比
    protect = 0.33     # 保护清辅音和呼吸声

def voicechange_x():
    # 将模型加载为对象
    model = vcm()
    # 运行方法，完成环境的预处理。开启可视化并延时6秒
    model.pre_voicechange(device, is_half, model_path, True, 6)

    # 进行声音处理，这里反复进行。注意其第一次推理较慢，实际应用中，可以通过提前转化一次的操作，加快后续速度
    while True:
        print("  --正在执行变声 … …")
        # 调用方法，进行变声，开启可视化并延时6秒
        reply = model.voicechange(input_audio, f0up_key,
                       f0method, index_path, index_rate,
                      filter_radius, resample_sr, rms_mix_rate,
                      protect, opt_path, True, 6)
        # 此处是返回的三个时间，当然你可以用作其他用途，或者直接忽略
        print(f"  --已完成单次变声，返回值：{reply}\n  -----------\n")
        input("按任意键继续下一次……")

if __name__ == '__main__':
    # 留个缺口，因为RVC还有其它功能，也可能弃用
    while True:
        sel = int(input("输入功能：\n--1.变声推理\n--2.？？\n"))
        if sel == 1:
            voicechange_x()
        elif sel == 2:
            print("？？")
        else:
            print("序号错误")
        print("\n---------------\n")