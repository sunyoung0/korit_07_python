from turtle import Turtle, Screen
from random import Random
# turtle 모듈에서 Turtle, Screen 클래스를 import 해왔습니다.

t = Turtle()        # 터틀객체 생성했고, 객체명 t
screen = Screen()   # 스크린 객체 생성

# 이상의 경우만 작성했을 때 모니터가 깜빡이는 것을 확인할 수 있는데, 이는 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼지는 것입니다.

t.shape('turtle')       # Turtle의 메서드를 호출했는데 argument가 str
t.color('white')        #
screen.bgcolor('black')

# 랜덤 객체 생성
random = Random()
colors = [
    'dark red',
"peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
    'light yellow'
]

# t.forward(100.3)
# t.penup()
# t.forward(100.3)
# # t.forward(100.3)
# # t.pendown()
# t.forward(30)

# 점선 그리는 반복문
# for _ in range(10):
#     t.forward(15)
#     t.penup()
#     t.forward(15)
#     t.pendown()

# left(각도)
# t.left(90)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)

# 그럼 오각형 / 육각형도 그려보세요.
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
#
# for _ in range(6):
#     t.forward(100)
#     t.left(60)

# 이상을 일반화 시키기 위해서 알 수 있는 것은
'''
삼각형일 때 120
사각형일 때 90
오각형일 때 72
육각형일 때 60

십각형일 때 36
'''

# n = int(input('몇각형을 만드시겠습니까? >>> '))
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)

# 여러 개의 도형을 그리고 싶다면 도형을 그리는 반복문을 반복 -> 중첩 for문
# for i in range(3, 11) :
#     for _ in range(i):
#         t.forward(100)
#         t.left(360/i)
#     t.color(random.choice(colors))

# 근데 도형 그릴때마다 반복문 쓰는거 너무 짜증나니까 그냥 함수를 정의합니다.
# def draw_shape(n) :
#     for _ in range(n) :
#         t.forward(100)
#         t.left(360/n)
#     t.color(random.choice(colors))
#
# def draw_dotted_line():
#     for _ in range(10):
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#
# def draw_dotted_shape(n) :
#     for _ in range(n) :
#         draw_dotted_line()
#         t.left(360/n)
#     t.color(random.choice(colors))
#
# # for i in range(3, 11) :
# #     draw_shape(i)
#
# for i in range(3, 11) :
#     draw_dotted_shape(i)

# t.forward(100)
# print(t.heading())
# t.left(90)
# t.forward(100)
# print(t.heading())
# t.left(30)
# t.forward(100)
# print(t.heading())
# t.right(30)
# t.forward(100)
# print(t.heading())
# t.setheading(30)
# t.forward(100)
# print(t.heading())

# .heading()의 return 값은 float
# .setheading()의 parameter가 float / return None

# t.setheading(t.heading() + 100)

# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)

# t.color(random.choice(colors))
# t.circle(100)           # 원 그리는거 완료
# # 거북이 머리 다른 쪽으로 돌려서 다음 원이 겹치지 않게끔 하는 함수
# t.setheading(t.heading() + 10)
#
# t.color(random.choice(colors))
# t.circle(100)           # 원 그리는거 완료
# # 거북이 머리 다른 쪽으로 돌려서 다음 원이 겹치지 않게끔 하는 함수
# t.setheading(t.heading() + 10)

# for _ in range(36) :
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 10)

# 예를 들어 10번만 반복하고 싶다면

t.speed(0)
# for _ in range(10) :
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 36)

# 함수화를 위한 일반식을 main에 작성하겠습니다.
n = 10

def draw_spirograph(size_of_gap) :
    for _ in range(360 // size_of_gap) :
        t.color(random.choice(colors))
        t.circle(100)
        t.setheading(t.heading() + 360/size_of_gap)

draw_spirograph(30)
# 이상의 코드에서 문제점은
# 1. 매개변수인 size_of_gap은 n번째 원과 n+1번째 원의 각도차이를 나타내는 것 같은데,
#   실제로는 반복 횟수를 통제하고 있습니다.
# 2. 이상의 상황에서 나타나는 점은 360을 입력했을 때, 제자리에서 원이 생성되는 것이 아니라,
#   그냥 360번을 반복한다는 점입니다.
draw_spirograph(0.5)

screen.exitonclick()