# 实现对于用户数据的操作

# API请求：
# 加载user_data()对象，使用对应方法。

# user_data()类方法：
# save() 保存指定的字典到json文件，参数:
# userdata 字典。 保存目标；
# file 字符串，.json文件路径，保存文件。
# read() 从指定json文件读取字典，参数：
# file 字符串，.json文件路径，读取目标。目标json文件只能存放字典内容。
# 返回值1 字典。读取到的字典。
# check() 检测即将保存的设置参数是否存在错误。
# 输入参数列表：
# json_file, name, tempdir, voicemodel_pth, voicemodel_index, prompt, device, method, 
# upkey, temperature, address, indexrate, filter_radius, resample, rmsmix, protect
# 返回值1 error_list 字典。存在错误的参数。键：错误参数，值：错误信息
# 返回值2 rewrite_list 字典。需要纠正的参数。纠正一些可能被纠正的错误，请使用纠正列表的参数而不是原参数。键：已纠正参数，值：修正值。已经被纠正的参数不会出现在错误列表中。
'''
这是一个API请求的书写样例：
from nrData import user_data as uds
userdata = {"XX": "nxd真的好可爱"}
file = r"Temp\temp.json"
uds().save(userdata, file)
print(uds().read(file))
error_list, rewrite_list = uds().check(
        file, name, tempdir, voicemodel_pth, voicemodel_index, 
        prompt, device, method, upkey, temperature, address, 
        indexrate, filter_radius, resample, rmsmix, protect)
if error_list:
    for key, value in error_list.items():
        print(value)
else:
    prompt = rewrite_list.get('prompt', prompt)
    voicemodel_pth = rewrite_list.get('voicemodel_pth', voicemodel_pth)
    voicemodel_index = rewrite_list.get('voicemodel_index', voicemodel_index)
'''

from os.path import exists

class user_data():
    # 保存
    def save(self, userdata, file):
        from json import dump
        with open(file, "w", encoding="utf-8") as json_file:
            dump(userdata, json_file, ensure_ascii=False, indent=4)

    # 读取
    def read(self, file):
        from json import load
        with open(file, "r", encoding="utf-8") as json_file:
            return(load(json_file))

    # 检测
    def check(self, json_file, name, tempdir, voicemodel_pth, voicemodel_index, 
              prompt, device, method, upkey, temperature, address, 
              indexrate, filter_radius, resample, rmsmix, protect):
        from os.path import abspath
        from pathlib import Path
        from torch.cuda import is_available
        error_list = {}
        rewrite_list = {}
        if not(json_file.endswith(".json")):
            error_list["json_file"] = "配置文件不正确，需要指定一个.json文件"
        else:
            # 找不到文件时，尝试在.json的目录下寻找同名文件
            json_path = str(Path(json_file).parent) + "\\"
            
        if name == "":
            error_list["name"] = "虚拟人名称不正确，需要输入一个名字"

        try:
            with open(prompt, 'r', encoding='utf-8') as promptfile:
                file_temp = promptfile.read()
                if file_temp == '':
                    error_list["prompt"] = "角色设定.txt是空的，请添加内容"
        except UnicodeDecodeError:
            error_list["prompt"] = "角色设定.txt文件不是UTF-8编码"
        except FileNotFoundError:
            prompt = json_path + Path(prompt).name
            try:
                with open(prompt, 'r', encoding='utf-8') as promptfile:
                    file_temp = promptfile.read()
                    if file_temp == '':
                        error_list["prompt"] = "角色设定.txt是空的，请添加内容"
                    else:
                        rewrite_list["prompt"] = prompt
            except UnicodeDecodeError:
                error_list ["prompt"] = "角色设定.txt文件不是UTF-8编码"
            except FileNotFoundError:
                error_list["prompt"] = "角色设定不正确，需要指定一个.txt文件，它不存在"

        nrtempdir = abspath(tempdir)
        if not(exists(nrtempdir)):
            error_list["tempdir"] = "缓存目录不存在，请指定一个目录，或者使用默认值。在高级设置中修改"

        if not(exists(voicemodel_pth)):
            voicemodel_pth = json_path + Path(voicemodel_pth).name
            if not(exists(voicemodel_pth)):
                error_list["voicemodel_pth"] = "声音模型文件不存在，请指定一个.pth文件"
            else:
                rewrite_list["voicemodel_pth"] = voicemodel_pth
        if not(exists(voicemodel_index)):
            voicemodel_index = json_path + Path(voicemodel_index).name
            if not(exists(voicemodel_index)):
                error_list["voicemodel_index"] = "声音模型文件不存在，请指定一个.index文件"
            else:
                rewrite_list["voicemodel_index"] = voicemodel_index

        if ((device == 'GPU') or (method == 'crepe')) and not(is_available()):
            error_list["device"] = "您的GPU不可用，但是选择了需要GPU的模式"

        if not( (upkey >= -12) and (upkey <= 12) ):
            error_list["upkey"] = "声音变调不正确，需要输入-12到12的整数"

        if not( (temperature >= 0.0) and (temperature <= 1.0) ):
            error_list["temperatur"] = "ChatGPT的temperature不正确，需要0.0-1.0小数，请在高级设置中修改"

        if     not ((address.startswith("http://")) or (address.startswith("https://"))
          ) or (address.endswith("\\")
          ) or (address.endswith("v1")
          ) or (address.endswith("v2")):
            error_list["address"] = "ChatGPT请求地址错误，请注意开头结尾，请在高级设置中修改"

        if (not(indexrate >= 0.00 and indexrate <= 1.00)
            or not(filter_radius >= 0.0 and filter_radius <= 7.0)
            or not(resample >= 0.0)
            or not(rmsmix >= 0.00 and rmsmix <= 1.00)
            or not(protect >= 0.00 and protect <= 0.50)):
            error_list["video_path"] = "声音模型参数不规范，请在高级设置中修改"

        return error_list, rewrite_list