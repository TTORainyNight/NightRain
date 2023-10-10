# 实现语言模型的对话功能，通过ChatGPT实现

# API请求字典描述：
# API_Key 字符串，以"sk-"开头。填写您的Openai-API-Key，可以在Openai官网找到；
# API_Base 字符串，api网址，"https://"开头，结尾不含"/"。指定Openai的API接口或镜像网站；
# System_Prompt 字符串。书写系统级Prompt，一般是对ChatGPT的命令限制；
# User_Prompt 字符串。用户级别提示词，会被添加到历史中，参与用户设定的对话；
# History_File 字符串，.txt文件路径。开启History时才有意义，可以不写。存放对话历史，注意此处的历史是面向ChatGPT的，如果要呈现给用户，请另作修改；
# Error_File 字符串，.txt文件路径。用于保存错误信息；
# ChatModel 字符串，Openai指定，例如"gpt-3.5-turbo"。用于指定使用的模型，目前支持ChatGPT3.5与4.0系列；
# History 布尔型。用于指定是否启用历史功能；
# Temperature 浮点型，0~1。指定GPT模型回答的随机性，越大随机性越强，可能性越多；
# Visable 布尔型。用于指定是否启用请求过程可视化，为调试程序提供便利；
# TimeOut 整型，非负整数。开启Visable时才有意义，可以不写。用于指定请求之前的延时，在此之前，展示输入信息；
# Input 字符串。用户的输入内容。

# 单独调用的方法：
# model_check() 需要ChatModel Visable API_Key API_Base，检查ChatGPT的对话模型是否可用
# model_list() 需要Visable API_Key API_Base，返回所有该Key的可用模型
'''
这是一个API请求的书写样例：
x = TalktoGPT({"API_Key": "sk-XXXXXXXXXXX",
    "API_Base": "https://api.openai.com"
    "System_Prompt": "# 你是一个虚拟人\n",
    "User_Prompt": "你的虚拟人身份是：小雨",
    "History_File": "Temp//ChatHistory.txt",
    "Error_File" :"Temp//ChatError.txt",
    "Temperature" : 1.0 ,
    "ChatModel" :"gpt-3.5-turbo",  "History": True,
    "Visable": True,  "TimeOut": 3,
    "Input": "你好,你是谁？"})
x.run()
返回值：
x.ID["Result"]
单独调用：
reply = x.model_check()
reply = x.model_list()
'''

class TalktoGPT():
    def __init__(self, InputData):
        self.ID = InputData
        if InputData["Visable"]:
            print(f"----nrGPT已输入，以下是获取到的信息：\n{InputData}")

    #开始运行
    def run(self):
        if self.ID["Visable"]:
            from time import sleep
            time_temp = self.ID["TimeOut"]
            print(f"----即将开始处理，已延时：{time_temp}秒 … …\n")
            sleep(time_temp)
        #检测，加载历史
        visable = self.ID["Visable"]
        history = ""
        if (self.ID["History"]) and (self.history_dialogue("check", 0)):
            history = self.history_dialogue("load", 0)
            if visable:
                print(f"----已启用历史，读取到历史对话：\n{history}")
        else:
            if visable:
                print("----历史功能已关闭 … …")
        #加载用户信息，保存历史对话
        user_input = self.ID["Input"]
        history = history + f"\n用户: {user_input}"
        #调用ChatGPT，保存输出
        if visable:
            print("----准备已完毕，调用ChatGPT … …")
        response = self.GPT(history)
        self.ID["Result"] = response
        if (self.ID["History"]):
            history = history + f"\n你: {response}"
            self.history_dialogue("save", history)
            if visable:
                print("----历史对话保存成功 … …")
        if visable:
            print("----ChatGPT调用完毕，已存至Result中，本次调用结束 … …")

    #调用ChatGPT
    def GPT(self, history):
        import openai
        #构建系统Prompt
        #构建用户Prompt：用户 + 历史
        visable = self.ID["Visable"]
        system_prompt = self.ID["System_Prompt"]
        user_prompt = self.ID["User_Prompt"] + f"{history}\n你："
        if visable:
            print("----Prompt构建完毕，正在询问ChatGPT … …\n")
        #调用ChatGPT
        try:
            #API请求头
            openai.api_key = self.ID["API_Key"]
            openai.api_base = self.ID["API_Base"] + "/v1"
            response = openai.ChatCompletion.create(
                model = self.ID["ChatModel"] ,
                messages = [{"role": "system", "content": system_prompt} ,
                           {"role": "user", "content": user_prompt}] ,
                max_tokens = 600,   temperature = self.ID["Temperature"] ,
                n = 1,   stop=None,   timeout = 10)
            #API返回值处理
            if response and response.get('choices'):
                if visable:
                    print(f"----ChatGPT已成功返回，以下是返回信息：\n{response}\n----正在继续处理，读取返回文本 … …")
                response_text = response['choices'][0]['message']['content']
                if visable:
                    print(f"----返回文本如下：\n{response_text}\n")
                return(response_text)

        #OpenAI-API调用错误
        except openai.error.APIError as e:
            inf = "\n  OpenAI-API出现错误" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "ChatGPT错误，请稍后重试。错误信息已导出……"
        except openai.error.Timeout as e:
            inf = "\n  OpenAI-API请求超时" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "ChatGPT超时，请稍后重试。错误信息已导出……"
        except openai.error.APIConnectionError as e:
            inf = "\n  无法连接到OpenAI-API" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "无法连接到ChatGPT，请检查网络环境！错误信息已导出……"
        except openai.error.RateLimitError as e:
            inf = "\n  OpenAI-API访问速度受限" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "ChatGPT太忙了，请稍后重试。错误信息已导出……"
        except openai.error.AuthenticationError as e:
            inf = "\n  Open-API-Key无效" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "您的API-Key无效，或者已过期。错误信息已导出……"
        except openai.error.ServiceUnavailableError as e:
            inf = "\n  OpenAI服务器故障" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "找不到OpenAI了，过一段时间再试试吧。错误信息已导出……"
        except openai.error.InvalidRequestError as e:
            inf = "\n  ChatGPT模型错误" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "使用了不存在的ChatGPT模型。错误信息已导出……"
        except Exception as e:
            inf = "\n  其他错误" + str(e)
            with open(self.ID["Error_File"], "w", encoding="utf-8") as file:
                file.write(inf)
            if visable:
                print(inf)
            return "ChatGPT其他错误。错误信息已导出……"

    #处理历史对话
    def history_dialogue(self, Option, dialogue):
        #保存操作
        if Option == "save":
            with open(self.ID["History_File"], "w", encoding="utf-8") as file:
                file.write(dialogue)
        #加载操作
        elif Option == "load":
            with open(self.ID["History_File"], "r", encoding="utf-8") as file:
                history = file.read()
            return history
        #检查操作
        elif Option == "check":
            try:
                with open(self.ID["History_File"], "r", encoding="utf-8"):
                    return True
            except FileNotFoundError:
                return False

    # 检查ChatGPT模型是否可用
    def model_check(self):
        reply = self.model_list()
        if self.ID["ChatModel"] in reply:
            if self.ID["Visable"]:
                print("----GPT模型可用，已返回成功 … …")
            return True
        if self.ID["Visable"]:
                print("----GPT模型不可用，已返回失败 … …")
        return False

    # 请求所有ChatGPT模型
    def model_list(self):
        import requests
        if self.ID["Visable"]:
            print("----获取ChatGPT模型列表 … …")
        api_key = self.ID["API_Key"]
        headers = {"Authorization": f"Bearer {api_key}"}
        try:
            response = requests.get(self.ID["API_Base"] + "/v1/models", headers=headers)
            if self.ID["Visable"]:
                print("----获取完毕，已返回模型列表：\n", response)
            return(response.json())
        except Exception:
            return([])
        
        