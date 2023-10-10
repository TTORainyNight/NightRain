from os import system

from Code.lib.nrGPT import TalktoGPT

#这是一个调用TalktoGPT的实例，以供参考
#更加详细的参数说明，请转到文件查看注释
#本实例实现了构建虚拟人，并实现带历史的对话功能

def main():

    #参数设置，在这里设置一些需要的参数，你可以改成你的输入信息
    api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    address = "https://api.openai.com"
    history_file = "Temp//ChatHistory.txt"
    system_prompt = "# 你是一个虚拟人\n"

    #预展示内容，给出用户提示
    print("免责声明：这是基于ChatGPT的AI虚拟人，与具体角色无关。\nAI小雨：你好呀，我是小雨，很高兴能与你聊天。\n")
    #检测并展示历史，若有历史则加载，无历史则跳过
    try:
        with open(history_file, "r"):
            with open(history_file, "r", encoding="utf-8") as file:
                history = file.read()
                print(history + "\n   -----以上是历史对话-----\n")
    except FileNotFoundError:
        pass

    # 获取所有可用模型，并检测GPT-4可用性
    model = TalktoGPT({"API_Key": api_key, "API_Base": address,
        "ChatModel" :"gpt-4", "Visable": True})
    print("所有模型展示：", model.model_list())
    print("GPT-4可用性：", model.model_check())

    #调用API，写死循环，反复询问用户输入，实现一直聊天
    while True:
        # 获取用户输入
        user_input = input("你: ")
            #书写API请求实例
        model = TalktoGPT({
            "API_Key": api_key,  #OpenAI-API-Key，通过官网获取
            "API_Base": address,   # 此处可以使用镜像源，解决国内连不上openai的问题
            "System_Prompt": system_prompt,  #系统提示词
            "User_Prompt": "你的虚拟人身份是：小雨",   #用户提示词
            "History_File": history_file,    #历史对话文件，可以不存在。关闭历史时，可以不写
            "Error_File" :"Temp//ChatError.txt",  #错误信息文件地址
            "Temperature" : 1.0,         # 创造性拉满
            "ChatModel" :"gpt-3.5-turbo",    #指定ChatGPT3.5模型
            "History": True,           #开启历史功能
            "Visable": True,            #开启过程可视化
            "TimeOut": 5,              #指定调用延时。关闭可视化时，可以不写
            "Input": user_input})         #添加用户输入
        # 调用模型
        model.run()
        # 获取输出实例，此处为直接展示，你可以用作其他用途
        print("\n----已返回----\n", model.ID["Result"])

if __name__ == '__main__':
    main()