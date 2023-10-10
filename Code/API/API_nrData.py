from Code.lib.nrData import user_data as uds

# 这是一份API调用实例，展示了如何进行用户配置的读取和写入
userdata = {
    "VHumanName": "小雨",        # 字符串。虚拟人名称
    "ChatModel": "gpt-3.5-turbo",            # 字符串，OpenAI指定。ChatGPT模型
    "UserPromptFile": r"User\prompt.txt",    # 字符串，.txt文件位置。用户Prompt文件
    "TempDir": "Temp"            # 字符串，文件夹位置。Temp临时目录
}
file = r"User\userdata.json"

# 保存用户配置
uds().save(userdata, file)

# 读取用户配置
print(  uds().read(file)  )

# 添加检测参数
error_list, rewrite_list = uds().check(
        file, name, tempdir, voicemodel_pth, voicemodel_index, 
        prompt, device, method, upkey, temperature, address, 
        indexrate, filter_radius, resample, rmsmix, protect)
# 检查错误列表
if error_list:
    # 便利整个错误列表
    for key, value in error_list.items():
        # 输出错误信息
        print(value)
else:
    # 参数全部正确时，使用纠正的参数替换原值
    prompt = rewrite_list.get('prompt', prompt)
    voicemodel_pth = rewrite_list.get('voicemodel_pth', voicemodel_pth)
    voicemodel_index = rewrite_list.get('voicemodel_index', voicemodel_index)