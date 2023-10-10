from Code.lib.nrUpadte import Update

# 这是nrUpdate更新模块的API接口实例
# 更加详细的参数说明，请转到文件查看注释
# 本实例实现了更新与获取版本相关功能

# 构建请求的文件列表
urls = ["https://XX/xxx.json", "https://XXX/xx.json"]

# 调用API对象，打开可视化
obj = Update(True)
# 获取网络上的更新数据，尝试3次
web, up_json = obj.get_update(urls, 3)
print("获取情况：", web, "\n更新数据：", up_json)

# 获取当前本地版本数据
error, beta, inf = obj.get_version(r"Temp\about.txt")
print("发生错误：", error, "内测版本：", beta, "错误信息/版本号：", inf)

#检测是否需要更新
reply = obj.is_update(up_json, inf)
print("是否需要更新：", reply)