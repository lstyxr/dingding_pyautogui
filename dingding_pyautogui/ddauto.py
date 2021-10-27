import pyautogui as pg
pg.PAUSE = 2  # 每条指令间隔时间秒


x=728
y=442
news = 5  # 新闻条数
n = 0
for i in range(news):
    n += 1
    pg.click(x, y)  # 点开新闻
    pg.click(x=704, y=82)  # 返回
    y += 107  # 下一条纵坐标
    if n == 5:
        y = 442