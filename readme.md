- 声音、动作、形象、背景。DIY一个专属于自己的虚拟人。

# 夜雨为伴

![主界面](./mainform.jpg)

## 简介

- 你有没有想过，按照自己的意愿定制虚拟人？性格、故事、爱好？甚至声音和音色、动作。这里都可以满足！
- 夜雨为伴，由人工智能大语言模型和人工智能音色推理模型驱动，拥有对于多种角色、多种情况的适应能力。

## 开始使用

![下载地址](https://github.com/TTORainyNight/NightRain/releases)

- 下载安装软件（前往releases），并准备好你的OpenAI API Key

- 完成上述步骤后，我们可以进入正题了。

- 不会使用？没关系，为您准备了一份非常详细的《夜雨为伴使用说明书》
下载，配置，安装，使用，进阶……非常详细。它放在首页的“用户与开发者文档”文件夹中。

## 配置需求

| 配置项 | 最低要求 | 建议要求 |
| :----: | :----: | :----: |
| CPU | Intel i3-10100F 64 位 CPU | Intel i5-11400H 及以上 64 位 CPU |
| 内存 | 6GB | 16GB |
| 显卡（GPU） | GTX 1050 （Nvidia10系）| RTX 3050 （Nvidia30、40系）|
| 显存 | 2GB | 4GB |
| 系统 | Windows 10 x64 Windows 11 x64|


## 对于用户

- 去看看《夜雨为伴使用说明书》吧，如果你还有其它问题，欢迎在Issues中反馈。

# 进行开发
基于Python和PyTorch的虚拟人生成器。

## 前言

- 对于开发者，为您准备了一份非常详细的《夜雨为伴开发者文档》
- 从源代码、环境配置、功能模块，介绍的非常详细。它放在首页的“用户与开发者文档”文件夹中。

- 我们强烈建议所有开发者，根据文档的指引进行源代码的查阅，这会节省您很多的时间哦~

- 完成上述步骤后，我们可以进入正题了，以下是简单的介绍。

## 开发环境部署

- 在开始开发之前，您需要配置好开发环境。以下是一些配置步骤的简要说明：

### Python 环境
- 确保您已获取完整的代码包。
- 安装 Python 3.8-3.10 版本，建议使用 Anaconda 创建 Python 环境。
- 激活创建的虚拟环境。

### PyTorch 与 GPU 环境
- 安装 CUDA 和 cuDNN，根据您的 GPU 支持的 CUDA 版本和 PyTorch 所支持的 CUDA 版本进行安装。
- 安装 PyTorch 的 GPU 开发环境，可以参考 PyTorch 官网提供的教程。

### 其他依赖项
- pytorch安装完毕后。
- 安装项目所需的依赖项，可以通过运行 `pip install -r requirements.txt` 命令一次性安装所有的依赖项。
- 前往本项目的releases中，下载`hubert_base.pt`模型，以及至少一个资源包。
- `hubert_base.pt`文件，需要放置在`\Source\rvc`目录中。

### 开发环境检查
- 使用您喜欢的编辑器打开项目文件夹。
- 运行环境检测文件 `Code/main.py`，确保所有依赖项都已正确安装。

## 运行入口
- 在配置好开发环境后，您可以尝试运行夜雨为伴的功能。
- 进入工作目录，找到 `Code/main.py` 文件，并将其设置为启动文件。
- 请注意，在运行之前，请确保您已注释掉除了“开发环境入口”之外的所有入口。

## 项目结构介绍
夜雨为伴的项目结构如下所示：

- Temp：临时文件夹，存放一些临时文件。
- Source：存放程序运行所必要的资源文件、相关协议和 UI 设计。
- Code：存放程序的代码部分，是整个项目的核心文件夹。
    - UI：存放通过 Qt Designer 转换后的 UI 文件。
    - Lib：存放程序的核心功能类库。
    - API：存放与 Lib 中的每个 API 相关的文件，提供详细的注释和使用说明。

具体的文件结构和功能模块的实现逻辑，请详细阅读开发者文档中的相关部分。

## 未来功能
下面是一些计划中的功能，将在后续版本中添加：

- 流传输模式：提升用户体验。
- 抛弃 pygame：使用其他声音模块替代。
- 抛弃 Edge-TTS：直接使用 AI 模型转化语音。
- 优化“设置”机制。
- 添加新手指引。
- 优化启动速度。
- 精简应用大小。

## 相关协议
- 《夜雨为伴用户使用协议》
- 《ApacheLicense2.0》