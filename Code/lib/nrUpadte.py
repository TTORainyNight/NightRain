# 更新模块，请求新版本

# API方法说明：
# get_update()：从网络上获取更新json；
# is_update()：对比版本信息，检测是否存在新版本；
# get_version()：从当前文件获取版本信息。
# API参数：
# Update(visable)：visable 布尔型。指定是否开启访问过程中的可视化。

# get_update()参数说明：
# urls 数组，元素为网址。指定获取json的网址；
# max_frequency 整数。最大尝试次数。
# 返回值1 布尔型。是否获取到更新，如果为False请检查网络状态；
# 返回值2 字典。获取到的更新json。

# is_update()参数说明：
# update_json 字典，网络上的更新字典；
# version 浮点数，数字，当前的版本号。
# 返回值1 布尔型。代表是否需要更新。

# get_version()参数说明：
# about_file 字符串，指定一个.txt文件路径。一般为本地about.txt，第一行存放版本信息；
# 返回值1 is_error 布尔型，是否出现错误；
# 返回值2 beta 布尔型，是否为内测beta版本；
# 返回值3 information is_error = True时，字符串，存放错误信息；is_error = False时，浮点型，存放版本号。

'''
这是一个API请求的书写样例：
urls = ["https://xx1/xx.json", "https://xx2/xx.json"]
obj = Update(True)
get_web, up_json = obj.get_update(urls, 3)
print(get_web, up_json)
error, beta, inf = obj.get_version(r"Source\text\about.txt")
print(error, beta, inf)
reply = obj.is_update(up_json, inf)
print(reply)
'''

class Update():
    def __init__(self, visable) -> None:
        self.visable = visable
        if self.visable:
            print("\n  --nrUpdate：已开启可视化……")
    
    # 获取更新json
    def get_update(self, urls, max_frequency):
        if self.visable:
            print("\n  --正在从网络上获取更新文件……")
        import requests
        from json import loads
        data = None
        attempt = 0
        for url in urls:
            if attempt < max_frequency:
                try:
                    response = requests.get(url)  
                    content = response.text
                    data = loads(content)
                    if self.visable:
                        print(f"\n  --获取成功，地址为：{url}")
                        print(f"\n  --所用次数：{attempt}")
                    break
                except:
                    attempt += 1
                    if self.visable:
                        print("\n  --获取失败，再次尝试……")
                    continue
            else:
                break
        if data is None:
            if self.visable:
                print("\n  --结束，已返回错误信息……")
            return False, None
        else:
            if self.visable:
                print("\n  --结束，已返回正确信息……")
            return True, data
    # 检测更新
    def is_update(self, update_json, version):
        if self.visable:
            print("\n  --正在根据已有信息检测更新……")
        new_versoin = float(update_json["Version"])
        version = float(version)
        if self.visable:
            print("\n  --检查结束，已返回……")
        if new_versoin > version:
            return True
        return False
    # 获取版本
    def get_version(self, about_file):
        # 初始化
        if self.visable:
            print("\n  --正在获取本地文件信息……")
        is_error = False
        beta = False
        information = None
        # 尝试打开文件
        try:
            with open(about_file, "r", encoding="utf-8") as f:
                if self.visable:
                    print("\n  --打开成功，正在处理文件信息……")
                first_line = f.readline()
                first_line = first_line.strip("V")
                # 检测beta
                if "beta" in first_line:
                    beta = True
                # 获取版本号
                version = "".join(c for c in first_line if c.isdigit() or c == ".")
                information = float(version)
        except Exception as e:
            if self.visable:
                print("\n  --发生错误，已返回错误信息……")
            is_error = True
            information = e
        if self.visable:
                print("\n  --结束，已返回版本号……")
        return is_error, beta, information