from tkinter import *

WIDTH = 1024      #H/U 화면의 가로 사이즈, 2560
HEIGHT = 720     #H/U 화면의 세로 사이즈, 720
GAP = 32         #H/U 화면에서 가상의 Grid를 생성할 간격
GAP2 = int(GAP/2)    #간격의 1/2 값을 시작점으로 해서 GAP 만큼 더해 나감
WIDTH_NUM = int(WIDTH/GAP)
HEIGHT_NUM = int(HEIGHT/GAP)
TOTAL_MOVE = WIDTH_NUM * HEIGHT_NUM

def Print_Coordinate():
    global WIDTH
    global HEIGHT
    global HEIGHT_NUM
    global WIDTH_NUM
    global GAP
    global GAP2

    window = Tk()
    window.title("Automation Menutree Search Grid")
    canvas  = Canvas(window, height = HEIGHT, width = WIDTH)
    #canvas.create_oval(8, 8, 8+2, 8+2, fill="red")
    #canvas.create_oval(8, 24, 8+2, 24+2, fill="red")

    # for i in range(HEIGHT_NUM):
    #     for j in range(WIDTH_NUM):
    #         print("[%d, %d]" % (i * GAP + GAP2, j * GAP + GAP2), end=" ")
    #     print(" ")
    for j in range(GAP2, HEIGHT_NUM*GAP, GAP):
        for i in range(GAP2, WIDTH_NUM*GAP, GAP):
            print("[%d, %d]" % (i, j), end=" ")
            canvas.create_oval(i, j, i+2, j+2, fill="red")
        print(" ")
    canvas.pack()
    window.mainloop()

print("Automation menutree search")

print("WIDTH : %d %s" % (WIDTH, type(WIDTH)))
print("HEIGHT : %d %s" % (HEIGHT, type(HEIGHT)))
print("GAP : %d %s" % (GAP, type(GAP)))
print("GAP2 : %d %s" % (GAP2, type(GAP2)))
print("WIDTH_NUM : %d %s" % (WIDTH_NUM, type(WIDTH_NUM)))
print("HEIGHT_NUM : %d %s" % (HEIGHT_NUM, type(HEIGHT_NUM)))
print("TOTAL_MOVE : %d %s" % (TOTAL_MOVE, type(TOTAL_MOVE)))

Print_Coordinate()