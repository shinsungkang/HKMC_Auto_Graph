from tkinter import *
from PIL import Image, ImageTk

WIDTH = 1024                            #H/U 화면의 가로 사이즈, 2560
HEIGHT = 288                            #H/U 화면의 세로 사이즈, 720
GAP = 32                                #H/U 화면에서 가상의 Grid를 생성할 간격
GAP2 = int(GAP/2)                       #간격의 1/2 값을 시작점으로 해서 GAP 만큼 더해 나감
WIDTH_NUM = int(WIDTH/GAP)              #최대 가로 이동 횟수
HEIGHT_NUM = int(HEIGHT/GAP)            #최대 세로 이동 횟수
TOTAL_MOVE = WIDTH_NUM * HEIGHT_NUM     #총 이동 횟수

def Print_Coordinate():
    global WIDTH            #함수 내에서 위에서 선언한 글로벌 변수 참조하기 위해 global 사용
    global HEIGHT
    global HEIGHT_NUM
    global WIDTH_NUM
    global GAP
    global GAP2

    window = Tk()                                       #윈도우 폼 생성
    window.title("Automation Menutree Search Grid")     #윈도우 폼 타이틀 지정
    canvas  = Canvas(window, height = HEIGHT, width = WIDTH)    #그림과 좌표 찍을 캔버스 생성
    img = Image.open("./test_24bit.bmp")                        #이미지
    photo = ImageTk.PhotoImage(img)                             #이미지 클래스
    canvas.create_image((514,146), image=photo)                 #캔버스에 이미지 출력

    #canvas.create_oval(8, 8, 8+2, 8+2, fill="red")
    #canvas.create_oval(8, 24, 8+2, 24+2, fill="red")

    # for i in range(HEIGHT_NUM):
    #     for j in range(WIDTH_NUM):
    #         print("[%d, %d]" % (i * GAP + GAP2, j * GAP + GAP2), end=" ")
    #     print(" ")
    for j in range(GAP2, HEIGHT_NUM*GAP, GAP):                  #높이 이동 횟수 만큼, GAP2을 초기값으로 GAP 만큼 더해가면서 HEIGHT_NUM*GAP 보다 작을 때까지 반복
        for i in range(GAP2, WIDTH_NUM*GAP, GAP):               #너비 이동 횟수 만큼, GAP2을 초기값으로 GAP 만큼 더해가면서 WIDTH_NUM*GAP 보다 작을 때까지 반복
            print("[%d, %d]" % (i, j), end=" ")                 #클릭하게될 좌표 출력
            canvas.create_oval(i, j, i+2, j+2, fill="red")      #캔버스 상에 클릭하게될 좌표 출력
        print(" ")                                              #줄바꿈
    canvas.pack()                                               #캔버스 출력
    window.mainloop()                                           #윈도우 폼 계속 띄우기

print("Automation menutree search")

print("WIDTH : %d %s" % (WIDTH, type(WIDTH)))
print("HEIGHT : %d %s" % (HEIGHT, type(HEIGHT)))
print("GAP : %d %s" % (GAP, type(GAP)))
print("GAP2 : %d %s" % (GAP2, type(GAP2)))
print("WIDTH_NUM : %d %s" % (WIDTH_NUM, type(WIDTH_NUM)))
print("HEIGHT_NUM : %d %s" % (HEIGHT_NUM, type(HEIGHT_NUM)))
print("TOTAL_MOVE : %d %s" % (TOTAL_MOVE, type(TOTAL_MOVE)))

Print_Coordinate()