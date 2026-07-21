# 🎬 CineDaily - 电影推荐应用

> 基于 FastAPI + Vue3 的轻量级电影推荐 Web 应用，提供随机推荐、电影详情查看功能。

**在线演示**：[https://dailymovie-production.up.railway.app](https://dailymovie-production.up.railway.app)

## ✨ 核心功能
- ✅ 首页随机推荐一部电影
- ✅ 点击「立即观看」跳转详情页
- ✅ 电影详情页展示：标题、年份、评分、标签、描述、导演、演员列表
- ✅ 详情页内置视频播放器
- ✅ 相似电影推荐（随机展示 5 部）
- ✅ 响应式设计，适配手机/平板/电脑


## 🛠️ 技术栈
| 分类 | 技术 |
|------|------|
| 后端 | FastAPI |
| 数据库 | SQLite |
| 前端 | Vue3（CDN 引入） |
| 样式 | TailwindCSS |
| 图标 | Font Awesome 6 |
| 部署 | Railway |
| 服务器 | Uvicorn |


## 📂 项目结构
CineDaily/
├── static/
│ ├── index.html # 首页（随机推荐 + 换一换）
│ └── detail.html # 详情页（视频播放 + 电影信息 + 相似推荐）
├── init_db.py # 数据库初始化脚本（含 5 部示例电影）
├── main.py # FastAPI 主程序（API + 静态文件挂载）
├── movies.db # SQLite 数据库（运行 init_db.py 后生成）
├── requirements.txt # 项目依赖
└── README.md # 项目说明

## ⚙️ 快速启动（本地运行）
### 1. 克隆项目
```bash
git clone https://github.com/luomi-0715/dailymovie.git
cd dailymovie
```

2. 安装依赖
```bash
pip install fastapi uvicorn
```
4. 初始化数据库
```bash
python init_db.py
```
看到 数据库操作成功！ 即表示完成，项目根目录会生成 movies.db 文件。

5. 启动服务
```bash
uvicorn main:app --reload
```
6. 访问项目
页面	地址
首页（随机推荐）	http://127.0.0.1:8000
详情页示例	http://127.0.0.1:8000/detail.html?id=1
自动 API 文档	http://127.0.0.1:8000/docs

🔌 API 接口
方法	路径	说明	返回示例
GET	/api/movie/random	获取一部随机电影	单条电影 JSON
GET	/api/movie/{movie_id}	根据 ID 获取电影详情	单条电影 JSON
请求示例：

# 获取随机电影
curl https://dailymovie-production.up.railway.app/api/movie/random

# 获取 ID 为 1 的电影
curl https://dailymovie-production.up.railway.app/api/movie/1
返回字段说明：

字段	类型	说明
id	int	电影 ID
title	string	电影名称（含英文原名）
year	string	上映年份
tags	string	类型标签，斜杠分隔
score	float	评分（满分 10 分）
desc	string	电影简介
bg	string	背景图 URL
director	string	导演
actors	string	主演（逗号分隔）
video_url	string	视频源地址

📸 效果展示
### 首页推荐
![首页截图](./screenshots/home.png)
### 电影详情页
![详情页截图](./screenshots/detail.png)

📝 数据来源
项目内置 5 部示例电影数据（init_db.py 中定义）：
星际穿越 (Interstellar)
盗梦空间 (Inception)
超时空接触 (Contact)
降临 (Arrival)
火星救援 (The Martian)
背景图使用 picsum.photos 随机生成，视频源为示例公共视频。

🚀 部署
本项目已成功部署至 Railway：
https://dailymovie-production.up.railway.app

📄 许可证
MIT License
Copyright (c) 2026 luomi-0715

📬 联系我
GitHub：https://github.com/luomi-0715
