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
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
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
            (1, "星际穿越 (Interstellar)", "2014", "科幻 / 冒险 / 悬疑", 9.4, "在地球环境日益恶化的未来...",
             "https://picsum.photos/1920/1080?random=1", "Christopher Nolan",
             "Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine",
             "http://commondatastorage.googleapis.com"),
            (2, "盗梦空间 (Inception)", "2010", "科幻 / 悬疑 / 动作", 9.4, "道姆·柯布是一位技艺高超的盗贼...",
             "https://picsum.photos/1920/1080?random=2", "Christopher Nolan",
             "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy",
             "http://commondatastorage.googleapis.com"),
            (3, "超时空接触 (Contact)", "1997", "科幻 / 悬疑 / 剧情", 8.4, "科学家艾莉·爱罗薇毕生致力于寻找地外文明...",
             "https://picsum.photos/1920/1080?random=3", "Robert Zemeckis",
             "Jodie Foster, Matthew McConaughey, Tom Skerritt, James Woods", "http://commondatastorage.googleapis.com"),
            (4, "降临 (Arrival)", "2016", "科幻 / 剧情 / 悬疑", 7.8, "十二个神秘的外星飞船降临地球...",
             "https://picsum.photos/1920/1080?random=4", "Denis Villeneuve",
             "Amy Adams, Jeremy Renner, Forest Whitaker, Michael Stuhlbarg", "http://commondatastorage.googleapis.com"),
            (5, "火星救援 (The Martian)", "2015", "科幻 / 冒险 / 剧情", 8.5, "在一次火星任务中，宇航员马克·沃特尼被意外遗留在火星...",
             "https://picsum.photos/1920/1080?random=5", "Ridley Scott",
             "Matt Damon, Jessica Chastain, Kristen Wiig, Jeff Daniels", "http://commondatastorage.googleapis.com")
        ]
        cursor.executemany('''
            INSERT INTO movies(id, title, year, tags, score, desc, bg, director, actors, video_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', movies_data)
        conn.commit()
        conn.close()
        print("数据库创建成功！")
    else:
        print("数据库已存在")


init_database()


def get_db_connection():
    """连接数据库"""
    connection = sqlite3.connect('movies.db')
    connection.row_factory = sqlite3.Row
    return connection


def format_movie(movie_row):
    movie_dict = dict(movie_row)
    if movie_dict.get('actors'):
        movie_dict['actors'] = movie_dict['actors'].split(',')
    return movie_dict


@app.get('/api/movie/random')
async def get_random_movie():
    connection = get_db_connection()
    random_sql = "SELECT * FROM movies ORDER BY RANDOM() LIMIT 1"
    movie = connection.execute(random_sql).fetchone()
    connection.close()
    if not movie:
        raise HTTPException(status_code=404, detail='没有获取到电影')
    return format_movie(movie)


@app.get('/api/movie/{movie_id}')
async def get_movie_by_id(movie_id: int):
    connection = get_db_connection()
    fetch_sql = "SELECT * FROM movies where id = ?"
    movie = connection.execute(fetch_sql, (movie_id,)).fetchone()
    connection.close()
    if not movie:
        raise HTTPException(status_code=404, detail='没有获取到电影')
    return format_movie(movie)


# ========== 新增：前端页面路由 ==========
@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")


@app.get("/detail.html")
async def serve_detail():
    return FileResponse("static/detail.html")


# ========== 静态文件挂载 ==========
app.mount("/static", StaticFiles(directory="static"), name="static")
