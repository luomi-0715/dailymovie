import sqlite3
import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# ========== 自动初始化数据库 ==========
def init_database():
    db_path = 'movies.db'
    if not os.path.exists(db_path):
        print("数据库不存在，正在创建...")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE movies(
                id INTEGER PRIMARY KEY,
                title TEXT,
                year TEXT,
                tags TEXT,
                score REAL,
                desc TEXT,
                bg TEXT,
                director TEXT,
                actors TEXT,
                video_url TEXT
            )
        ''')
        movies_data = [
            (1, "星际穿越 (Interstellar)", "2014", "科幻 / 冒险 / 悬疑", 9.4, "在地球环境日益恶化的未来，一组探险家利用新发现的虫洞，穿越到遥远的星系寻找人类的新家园，在探索过程中他们面临着时间扭曲和未知物理现象的挑战，每一步都牵动着全人类的命运。", "https://picsum.photos/1920/1080?random=1", "Christopher Nolan", "Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine", "http://commondatastorage.googleapis.com"),
            (2, "盗梦空间 (Inception)", "2010", "科幻 / 悬疑 / 动作", 9.4, "道姆·柯布是一位技艺高超的盗贼，他的专长是在人们梦境中窃取潜意识里的秘密。为了回家见到自己的孩子，他接受了一个看似不可能的任务：在目标人物的深层梦境中植入一个想法。", "https://picsum.photos/1920/1080?random=2", "Christopher Nolan", "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy", "http://commondatastorage.googleapis.com"),
            (3, "超时空接触 (Contact)", "1997", "科幻 / 悬疑 / 剧情", 8.4, "科学家艾莉·爱罗薇毕生致力于寻找地外文明，当她接收到来自织女星的信号并成功解码，她获得了一个可能改变人类命运的星际旅行机会，但这次旅程将同时考验她的科学信仰和人性。", "https://picsum.photos/1920/1080?random=3", "Robert Zemeckis", "Jodie Foster, Matthew McConaughey, Tom Skerritt, James Woods", "http://commondatastorage.googleapis.com"),
            (4, "降临 (Arrival)", "2016", "科幻 / 剧情 / 悬疑", 7.8, "十二个神秘的外星飞船降临地球，语言学家露易丝·班克斯博士受命破解外星语言。在学习过程中，她发现这种语言能改变人类的思维方式，甚至感知时间，从而揭开一个关乎人类未来的惊人秘密。", "https://picsum.photos/1920/1080?random=4", "Denis Villeneuve", "Amy Adams, Jeremy Renner, Forest Whitaker, Michael Stuhlbarg", "http://commondatastorage.googleapis.com"),
            (5, "火星救援 (The Martian)", "2015", "科幻 / 冒险 / 剧情", 8.5, "在一次火星任务中，宇航员马克·沃特尼被意外遗留在火星，成为了这颗星球上唯一的人类。他必须依靠有限的资源和植物学知识，在绝境中求生，并想方设法向地球发出求救信号。", "https://picsum.photos/1920/1080?random=5", "Ridley Scott", "Matt Damon, Jessica Chastain, Kristen Wiig, Jeff Daniels", "http://commondatastorage.googleapis.com")
        ]
        cursor.executemany('''
            INSERT INTO movies(id, title, year, tags, score, desc, bg, director, actors, video_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', movies_data)
        connection.commit()
        connection.close()
        print("数据库创建成功！")
    else:
        print("数据库已存在")

init_database()

# ========== FastAPI 应用 ==========
app = FastAPI()

def get_db_connection():
    connection = sqlite3.connect('movies.db')
    connection.row_factory = sqlite3.Row
    return connection

def format_movie(movie_row):
    movie_dict = dict(movie_row)
    if movie_dict.get('actors'):
        movie_dict['actors'] = movie_dict['actors'].split(',')
    return movie_dict

# ... 后面是你的 API 和路由代码 ...