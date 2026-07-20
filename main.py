from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import sqlite3

app = FastAPI()


def get_db_connection():
    """连接数据库"""
    connection = sqlite3.connect('movies.db')
    connection.row_factory = sqlite3.Row  # row['id']
    return connection


def format_movie(movie_row):
    # 处理actors字段
    movie_dict = dict(movie_row)
    if movie_dict.get('actors'):
        movie_dict['actors'] = movie_dict['actors'].split(',')
    return movie_dict


@app.get('/api/movie/random')
async def get_random_movie():
    # 从sqlite中随机筛选一条记录
    connection = get_db_connection()
    random_sql = "SELECT *FROM movies ORDER BY RANDOM() LIMIT 1"
    movie = connection.execute(random_sql).fetchone()
    connection.close()
    if not movie:
        raise HTTPException(status_code=404, detail='没有获取到电影')
    return format_movie(movie)


@app.get('/api/movie/{movie_id}')
async def get_movie_by_id(movie_id: int):
    connection = get_db_connection()
    fetch_sql = "SELECT *FROM movies where id = ?"
    movie = connection.execute(fetch_sql, (movie_id,)).fetchone()
    connection.close()
    if not movie:
        raise HTTPException(status_code=404, detail='没有获取到电影')
    return format_movie(movie)


app.mount("/", StaticFiles(directory='static', html=True), name='static')
