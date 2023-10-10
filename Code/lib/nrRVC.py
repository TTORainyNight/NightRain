# 实现语音的转化，通过RVC模块实现

# API请求过程：
# 将nrVoiceChange()类作为对象加载
# 调用上述类的pre_voicechange()方法，搭建好转化环境
# 调用voicechange()方法，进行语音转化

# pre_voicechange()参数说明：
# device 字符串，"cuda:0"或"cpu"。指定推理的设备cuda:0表示GPU(如果可用)
# is_half 布尔型。是否使用半精度，建议开启。但只有GPU支持。
# model_path 字符串，.pth文件路径。指定推理的声音模型
# visable 布尔型。用于指定是否启用请求过程可视化，为调试程序提供便利
# timeout 整型，非负整数。开启Visable时才有意义，可以不写。用于指定请求之前的延时，在此之前，展示输入信息

# voicechange()参数说明：
# input_audio 字符串，.wav/.mp3文件路径。待处理的音频文件
# f0up_key 字符串，数字，"-12"到"12"。控制转化变调，男变女+12，女变男-12，同性别0，可以微调音调
# f0method 字符串，"pm"或"harvest"或"crepe"。推理模式，pm:CPU高速低质，harvest:CPU低速高质，crepe:GPU(推荐，如果可用)
# index_path 字符串，.index文件。声音模型index文件
# index_rate 浮点数，0.00-1.00 检索特征占比
# filter_radius 浮点型，0.0-7.0 中值滤波半径，削弱哑音，>=3时会开启滤波
# resample_sr 整型。重新采样率，0表示不采样
# rms_mix_rate 浮点型，0.00-1.00 输入音源替换为输出包融合占比，值越大越倾向于使用输出包
# protect 浮点型，0.00-0.50 保护清辅音和呼吸声，拉满表示不开启。增加保护力度会削弱索引效果
# opt_path 字符串，.wav文件路径。输出文件
# visable 布尔型。用于指定是否启用请求过程可视化，为调试程序提供便利
# timeout 整型，非负整数。开启Visable时才有意义，可以不写。用于指定请求之前的延时，在此之前，展示输入信息

# 返回值为一个数组，它们分别表示[加载音频时间, 加载Huber时间, 声音转换时间]。若返回False则表示转化失败，请检查目标文件

'''
这是一个API请求的书写样例：
f0up_key = "-12"
input_audio = r"B:\temp.wav"
index_path = r"B:\test.index"
f0method = "crepe"
opt_path = r"B:\out.wav"
model_path = r"B:\test.pth"
index_rate = 0.75
device = "cuda:0"
is_half = True
filter_radius = 3
resample_sr = 0
rms_mix_rate = 0.25
protect = 0.33

model = vcm()
model.pre_voicechange(device, is_half, model_path, True, 3)
while True:
    reply = model.voicechange(input_audio, f0up_key, f0method, index_path, index_rate, filter_radius, resample_sr, rms_mix_rate, protect, opt_path, True, 3)
    input("任意键继续……")
'''

# 配置信息
class Config:
    def __init__(self, device, is_half, visable):
        if visable:
            print("--开始加载配置 … …")
        self.device = device  # 设备
        self.is_half = is_half  # 是否使用半精度
        self.n_cpu = 0  # CPU数量
        self.gpu_name = None  # GPU名称
        self.gpu_mem = None  # GPU内存
        self.x_pad, self.x_query, self.x_center, self.x_max = self.device_config(visable)
        if visable:
            print("--配置信息已加载内容：\n  --", self.x_pad, self.x_query, self.x_center, self.x_max)
        
    def device_config(self, visable) -> tuple:
        from multiprocessing import cpu_count
        from torch import backends
        from torch import cuda
        # 检查GPU可用状态
        is_GPU = cuda.is_available()
        if visable:
            print("--检测GPU可用状态：", is_GPU)
        if is_GPU:
            i_device = int(self.device.split(":")[-1])
            self.gpu_name = cuda.get_device_name(i_device)
            if (("16" in self.gpu_name and "V100" not in self.gpu_name.upper())
                or "P40" in self.gpu_name.upper()
                or "1060" in self.gpu_name
                or "1070" in self.gpu_name
                or "1080" in self.gpu_name):
                if visable:
                    print("--16系/10系/P40显卡，强制单精度\n--操作json文件 … …")
                self.is_half = False
                for config_file in ["32k.json", "40k.json", "48k.json"]:
                    with open(f"Source/rvc/{config_file}", "r") as f:
                        strr = f.read().replace("true", "false")
                    with open(f"Source/rvc/{config_file}", "w") as f:
                        f.write(strr)
            else:
                self.gpu_name = None
                if visable:
                    print("--未检测到16系/10系/P40显卡")

            self.gpu_mem = int(
                cuda.get_device_properties(i_device).total_memory
                / 1024 / 1024 / 1024 + 0.4 )
        elif backends.mps.is_available():
            if visable:
                print("没有发现支持的N卡, 使用MPS进行推理")
            self.device = "mps"
            self.is_half = False
        else:
            # 半精度half只有GPU支持
            if visable:
                print("没有发现支持的N卡, 使用CPU进行推理")
            self.device = "cpu"
            self.is_half = False

        if self.n_cpu == 0:
            self.n_cpu = cpu_count()

        if self.is_half:
            if visable:
                print("--更新：使用6GB显存配置 … …")
            x_pad = 3
            x_query = 10
            x_center = 60
            x_max = 65
        else:
            if visable:
                print("--更新：使用5GB显存配置 … …")
            x_pad = 1
            x_query = 6
            x_center = 38
            x_max = 41

        if self.gpu_mem != None and self.gpu_mem <= 4:
            if visable:
                print("--更新：使用低显存配置 … …")
            x_pad = 1
            x_query = 5
            x_center = 30
            x_max = 32
        return x_pad, x_query, x_center, x_max

# RVC声音转化
class nrVoiceChange():

    # 加载基础模型
    def load_hubert(self, device, is_half, visable):
        from fairseq import checkpoint_utils
        if visable:
            print("--开始加载基础模型 … …\n--目标：Source/rvc/hubert_base.pt … …\n--基础模型信息如下：\n")
        models, saved_cfg, task = checkpoint_utils.load_model_ensemble_and_task(["Source/rvc/hubert_base.pt"], suffix="",)
        if visable:
            print("--基础模型加载完毕，正在设置基础模型 … …")
        self.hubert_model = models[0]
        self.hubert_model = self.hubert_model.to(device)
        if (is_half):
            self.hubert_model = self.hubert_model.half()
        else:
            self.hubert_model = self.hubert_model.float()
        self.hubert_model.eval()
        if visable:
            print("--基础模型加载完毕，可以使用 … …")

    # 准备声音转化环境
    def pre_voicechange(self, device, is_half, model_path, visable, timeout):
        from os import getcwd
        from sys import path as syspath
        import torch
        from Code.lib.vc_infer_pipeline import VC
        from Code.lib.infer_pack.models import (
            SynthesizerTrnMs256NSFsid,
            SynthesizerTrnMs256NSFsid_nono,
            SynthesizerTrnMs768NSFsid,
            SynthesizerTrnMs768NSFsid_nono)
        # 获取信息
        if visable:
            from time import sleep
            print("准备声音转化环境，获取到信息：", device, is_half, model_path, visable, timeout, f"\n--开始准备转化环境，已延时：{timeout}秒 … …")
            sleep(timeout)
        self.config = Config(device, is_half, visable)
        syspath.append( getcwd() )
        self.hubert_model = None

        # 准备参数
        if visable:
            print("--开始准备模型参数 … …\n--目标模型：", model_path, "\n--以下是模型信息：\n")
        self.cpt = torch.load(model_path, map_location="cpu")
        self.tgt_sr = self.cpt["config"][-1]
        self.cpt["config"][-3] = self.cpt["weight"]["emb_g.weight"].shape[0]  # n_spk
        if_f0 = self.cpt.get("f0", 1)
        self.version = self.cpt.get("version", "v1")
        if self.version == "v1":
            if if_f0 == 1:
                self.net_g = SynthesizerTrnMs256NSFsid(visable, *self.cpt["config"], is_half=is_half)
            else:
                self.net_g = SynthesizerTrnMs256NSFsid_nono(visable, *self.cpt["config"])
        elif self.version == "v2":
            if if_f0 == 1:
                self.net_g = SynthesizerTrnMs768NSFsid(visable, *self.cpt["config"], is_half=is_half)
            else:
                self.net_g = SynthesizerTrnMs768NSFsid_nono(visable, *self.cpt["config"])
        del self.net_g.enc_q
        self.net_g.load_state_dict(self.cpt["weight"], strict=False)
        self.net_g.eval().to(device)
        if (is_half):
            self.net_g = self.net_g.half()
        else:
            self.net_g = self.net_g.float()

        # 加载基础模型
        if visable:
            print("--模型参数设置完毕，加载基础模型 … …")
        self.vc = VC(self.tgt_sr, self.config)
        self.n_spk = self.cpt["config"][-3]
        self.load_hubert(device, is_half, visable)
        self.device = device
        self.is_half = is_half
        if visable:
            print("--加载成功！\n\n--声音转化环境准备完毕！")

    # 转化声音
    def voicechange(self, input_audio, f0up_key,
                   f0_method, index_path, index_rate,
                  filter_radius, resample_sr, rms_mix_rate,
                  protect, opt_path, visable, timeout):
        from scipy.io import wavfile
        from Code.lib.audio import load_audio
        if visable:
            from time import sleep
            print("转化声音，已获取到参数如下：\n-- ", input_audio, f0up_key,
                       f0_method, index_path, index_rate,
                      filter_radius, resample_sr, rms_mix_rate,
                      protect, opt_path, visable, timeout, 
                  f"\n--即将进行准备工作，已延时{timeout}秒 … …")
            sleep(timeout)
        if input_audio is None:
            if visable:
                print("--音频文件为空或不存在，已退出 … …")
            return False
        f0_up_key = int(f0up_key)

        if visable:
            print("--处理声音文件 … …")
        audio = load_audio(input_audio, 16000)
        times = [0, 0, 0]  # [加载音频时间, 加载Huber时间, 声音转换时间]

        if self.hubert_model is None:
            if visable:
                print("--基础模型出现错误，尝试重新加载 … …")
            self.load_hubert(self.device, self.is_half, visable)  # 检查基础模型
        # 获取f0
        if_f0 = self.cpt.get("f0", 1)  # 1表示存在，0表示不存在

        # 进行声音转换
        if visable:
            print("--准备工作成功，正在转化声音 … …")
        audio_opt = self.vc.pipeline(self.hubert_model, self.net_g, 0,
                               audio, input_audio, times, 
                               f0_up_key, f0_method, index_path, 
                               index_rate, if_f0, filter_radius, 
                               self.tgt_sr, resample_sr, rms_mix_rate, 
                               self.version, protect, f0_file = None)
        if visable:
            print("--转化完毕，已返回时间值 … …\n  -- [加载音频时间, 加载Huber时间, 声音转换时间]\n  --", times, "\n--正在保存音频 … …")
        # 保存音频
        wavfile.write(opt_path, self.tgt_sr, audio_opt)
        if visable:
            print("--保存完毕，本次转化结束，已返回时间 … …")
        return times