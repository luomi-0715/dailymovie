import random
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 创建模拟数据
movies_date = [
    {
        "id": 1,
        "title": "星际穿越 (Interstellar)",
        "year": "2014",
        "tags": "科幻 / 冒险 / 悬疑",
        "score": 9.4,
        "desc": "在地球环境日益恶化的未来，一组探险家利用新发现的虫洞，穿越到遥远的星系寻找人类的新家园，在探索过程中他们面临着时间扭曲和未知物理现象的挑战，每一步都牵动着全人类的命运。",
        "bg": "https://images.unsplash.com/photo-1536440133",
        "director": "Christopher Nolan",
        "actors": "Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine",
        "video_url": "http://commondatastorage.googleapis.com"
    },
    {
        "id": 2,
        "title": "盗梦空间 (Inception)",
        "year": "2010",
        "tags": "科幻 / 悬疑 / 动作",
        "score": 9.4,
        "desc": "道姆·柯布是一位技艺高超的盗贼，他的专长是在人们梦境中窃取潜意识里的秘密。为了回家见到自己的孩子，他接受了一个看似不可能的任务：在目标人物的深层梦境中植入一个想法。",
        "bg": "https://images.unsplash.com/photo-1536440133",
        "director": "Christopher Nolan",
        "actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy",
        "video_url": "http://commondatastorage.googleapis.com"
    },
    {
        "id": 3,
        "title": "超时空接触 (Contact)",
        "year": "1997",
        "tags": "科幻 / 悬疑 / 剧情",
        "score": 8.4,
        "desc": "科学家艾莉·爱罗薇毕生致力于寻找地外文明，当她接收到来自织女星的信号并成功解码，她获得了一个可能改变人类命运的星际旅行机会，但这次旅程将同时考验她的科学信仰和人性。",
        "bg": "https://images.unsplash.com/photo-1536440133",
        "director": "Robert Zemeckis",
        "actors": "Jodie Foster, Matthew McConaughey, Tom Skerritt, James Woods",
        "video_url": "http://commondatastorage.googleapis.com"
    },
    {
        "id": 4,
        "title": "降临 (Arrival)",
        "year": "2016",
        "tags": "科幻 / 剧情 / 悬疑",
        "score": 7.8,
        "desc": "十二个神秘的外星飞船降临地球，语言学家露易丝·班克斯博士受命破解外星语言。在学习过程中，她发现这种语言能改变人类的思维方式，甚至感知时间，从而揭开一个关乎人类未来的惊人秘密。",
        "bg": "https://images.unsplash.com/photo-1536440133",
        "director": "Denis Villeneuve",
        "actors": "Amy Adams, Jeremy Renner, Forest Whitaker, Michael Stuhlbarg",
        "video_url": "http://commondatastorage.googleapis.com"
    },
    {
        "id": 5,
        "title": "火星救援 (The Martian)",
        "year": "2015",
        "tags": "科幻 / 冒险 / 剧情",
        "score": 8.5,
        "desc": "在一次火星任务中，宇航员马克·沃特尼被意外遗留在火星，成为了这颗星球上唯一的人类。他必须依靠有限的资源和植物学知识，在绝境中求生，并想方设法向地球发出求救信号。",
        "bg": "https://images.unsplash.com/photo-1536440133",
        "director": "Ridley Scott",
        "actors": "Matt Damon, Jessica Chastain, Kristen Wiig, Jeff Daniels",
        "video_url": "http://commondatastorage.googleapis.com"
    }
]

#
# @app.get('/hallo')
# def read_root():
#     return {'message': 'Hallo World', 'status': 'OK'}


@app.get('/api/movie/random')
async def get_random_movie():
    return random.choice(movies_date)


@app.get('/api/movie/{movie_id}')
async def get_movie_by_id(movie_id: int):
    for movie in movies_date:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="未找到该id的电影")


app.mount("/", StaticFiles(directory='static', html=True), name='static')
