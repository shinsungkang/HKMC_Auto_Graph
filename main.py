#python 3.6
from tkinter import *                               # tkinter 모듈의 메소드를 모두 import, tkinter 생량하고 사용
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

import os                                           # OS 인터페이스 모듈, 파일 리스트 얻기 위해 사용
import numpy as np

# main window
mainwin = Tk()                                      # tkinter의 Tk() 객체 인스턴스화, mainapp 변수에 할당
mainwin.title("HKMC Auto Graph Generator v1.0")     # 창 타이틀
mainwin.geometry("1000x600+200+100")                # 창 크기 및 시작 위치, 가로 500, 세로 500, x 200, y 100
mainwin.resizable(0,1)                              # 창 크기 변동 여부(가로,세로), TRUE (1) 변동, FALSE (0) 고정

# Exit callback
def _quit():
    mainwin.quit()
    mainwin.destroy()
    exit()

# About callback
def _about():
    messagebox.showinfo(title="About", message="HKMC Auto Graph Generator v1.0\nBy ShinSung Kang")

# main window menu bar
mainwin_menu_bar = Menu(mainwin)                    # Menu 모듈 클래스 생성자 호출, mainwin 인자로 전달
mainwin.config(menu=mainwin_menu_bar)               # GUI용 메뉴로 사용하도록 설정

# File Menu
file_menu = Menu(mainwin_menu_bar, tearoff=0)               # mainwin_menu_bar에 들어갈 File의 하위메뉴 생성
file_menu.add_command(label="New")                          # File (상위메뉴) 의 하위메뉴 New 항목 생성
file_menu.add_command(label="Exit", command=_quit)          # File (상위메뉴) 의 하위메뉴 Exit 항목 생성
mainwin_menu_bar.add_cascade(label="File", menu=file_menu)  # File (상위메뉴) 의 하위메뉴(수직정렬)로 연결

# Help Menu
help_menu = Menu(mainwin_menu_bar, tearoff=0)               # mainwin_menu_bar에 들어갈 Help의 하위메뉴 생성
help_menu.add_command(label="About", command=_about)        # Help (상위메뉴) 의 하위메뉴 About 항목 생성
mainwin_menu_bar.add_cascade(label="Help", menu=help_menu)  # Help (상위메뉴) 의 하위메뉴(수직정렬)로 연결

"""
# LabelFrame 1
labelframe1 = ttk.LabelFrame(mainwin, text="Info", width=100, height=100)
labelframe1.grid(column=0, row=0, padx=10, pady=10)

ttk.Label(labelframe1, text="Label1").grid(column=0, row=0, sticky=W)
ttk.Label(labelframe1, text="Label2").grid(column=1, row=0, sticky=W)
ttk.Label(labelframe1, text="Label3").grid(column=2, row=0, sticky=W)

# LabelFrame 2
labelframe2 = ttk.LabelFrame(mainwin, text="Info2")
labelframe2.grid(column=0, row=1, padx=10, pady=10)

ttk.Label(labelframe2, text="Label1").grid(column=0, row=0, sticky=W)
ttk.Label(labelframe2, text="Label2").grid(column=1, row=0, sticky=W)
ttk.Label(labelframe2, text="Label3").grid(column=2, row=0, sticky=W)
"""
var_directory_path = StringVar()
var_directory_path.set("C:/Users/kang/Desktop/test/")

def button_path_click():
    messagebox.showinfo("button_path_click OK", "button_path_clicked")
    var_path = filedialog.askdirectory(initialdir = "D:/")
    print(var_path)
    var_directory_path.set(var_path)

def button_generate_click():
    messagebox.showinfo("button_generate_click OK", "button_generate_clicked")
    dir_path = var_directory_path.get()
    print(var_directory_path.get())

    """
    1. 해당 경로에서 파일 리스트 및 갯수 파악
    1. 파일에서 행 갯수 파악
    2. CPU, Memory, 앱별 CPU / Memory 데이터 확인
    3. 각각 데이터 그래프 그리기(Memory는 1행, CPU는 2행)
    4. 한개의 그래프에 모든 CPU 데이터 그리기
    5. 한개의 그래프에 모든 Memory 데이터 그리기
    """


    files = os.listdir(var_directory_path.get())        #해당 경로의 파일 리스트
    print("file number : %d" % len(files))
    col = 0

    for i in files:
        path = dir_path+"/" + i
        app = str(i[0:-4])
        print("%d = full file name : %s, only file name : %s, path : %s " % (col, i, app, path))
        data = np.loadtxt(path, dtype=np.int)
        print(type(data))
        col = col + 1
        count = 0
        for k in data:
            count = count + 1

        print("문서 라인 갯수 : %d" % count)
        x = np.arange(0, count, 1)

        """
        f = Figure(figsize=(3, 2), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, data)
        a.title('aaa')
        a.xlabel('Hour')
        a.ylabel('KB')
        """
        f = plt.figure(figsize=(3,2), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, data)
        plt.title(app)
        plt.xlabel('Minute')
        plt.ylabel('KB')

        plt.axis([0, 12, 0, 500])
        canvas1 = FigureCanvasTkAgg(f, master=frame4)
        canvas1.draw()
        canvas1.get_tk_widget().grid(column=col, row=0)
        canvas1.get_tk_widget().configure(width=700, height=500)


def graph_display(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=950, height=500)

# Frame1
frame1 = Frame(mainwin)
#frame1 = Frame(mainwin, width=500, height=20)
#frame1 = Frame(mainwin, background="red", width=500, height=20)
frame1.grid(column=0, row=0, padx=10, pady=5, sticky=W)

label = ttk.Label(frame1, text="Select a directory").grid(column=0, row=0, padx=5, pady=5)
entry_path = ttk.Entry(frame1, textvariable=var_directory_path, width=50).grid(column=1, row=0, padx=5, pady=5)
button_path = ttk.Button(frame1, text="Browse...", command=button_path_click).grid(column=2, row=0, padx=5, pady=5)
button_generate = ttk.Button(frame1, text="Generate", command=button_generate_click).grid(column=3, row=0, padx=5, pady=5)

# Frame2
frame2 = Frame(mainwin)
#frame2 = Frame(mainwin, background="yellow", width=300, height=20)
frame2.grid(column=0, row=1, padx=10, pady=0, sticky=W)

label_x = ttk.Label(frame2, text="X 축 시간(Hour)").grid(column=0, row=0, padx=5, pady=5)
number_x = StringVar()
combobox_axis_x = ttk.Combobox(frame2, width=10, textvariable=number_x, state='readonly')
combobox_axis_x['values'] = (12, 24, 48, 96)
combobox_axis_x.grid(column=1, row=0, padx=5, pady=5)
combobox_axis_x.current(2)
label_y = ttk.Label(frame2, text="Y 축 메모리(KB)").grid(column=2, row=0, padx=5, pady=5)
number_y = StringVar()
combobox_axis_y = ttk.Combobox(frame2, width=12, textvariable=number_y, state='readonly')
combobox_axis_y['values'] = ('300,000(KB)', '500,000(KB)', '1,000,000(KB)', '1,500,000(KB)')
combobox_axis_y.grid(column=3, row=0, padx=5, pady=5)
combobox_axis_y.current(2)

# Frame3
frame3 = Frame(mainwin)
#frame3.grid(column=0, row=2, padx=0, pady=0, sticky=W)
frame3.grid(column=0, row=2, sticky=W)

#canvas = Canvas(frame3, background="red")
canvas = Canvas(frame3)
canvas.grid(column=0, row=0, padx=0, pady=0)


frame_scrollbar_x = Scrollbar(frame3, orient=HORIZONTAL, command=canvas.xview)
frame_scrollbar_x.grid(column=0, row=1, sticky=E+W)
frame_scrollbar_y = Scrollbar(frame3, orient=VERTICAL, command=canvas.yview)
frame_scrollbar_y.grid(column=1, row=0, sticky=N+S)

canvas.configure(xscrollcommand=frame_scrollbar_x.set)
canvas.configure(yscrollcommand=frame_scrollbar_y.set)

frame4 = Frame(canvas, background="black", width=300, height=300)
canvas.create_window((0,0), window=frame4, anchor='nw')
frame4.bind("<Configure>", graph_display)
"""
f = Figure(figsize=(3, 2), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
canvas1 = FigureCanvasTkAgg(f, master=frame4)
canvas1.draw()
canvas1.get_tk_widget().grid(column=0, row=0, padx=1, pady=1)

canvas2 = FigureCanvasTkAgg(f, master=frame4)
canvas2.draw()
canvas2.get_tk_widget().grid(column=0, row=1, padx=1, pady=1)
"""
"""
scrollbar_x = Scrollbar(frame3, orient=HORIZONTAL)
scrollbar_x.grid(column=0, row=1, sticky=E+W)

#scrollbar_y = Scrollbar(frame3)
#scrollbar_y.grid(column=1, row=0, sticky=N+S)

#canvas = Canvas(frame3, scrollregion=(0, 0, 700, 700), xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set, bg='yellow', height=500, width=500)
canvas = Canvas(frame3, scrollregion=(0, 0, 2000, 500), xscrollcommand=scrollbar_x.set, bg='yellow', height=500, width=975)
canvas.grid(column=0, row=0, sticky=N+S+E+W)
canvas.create_rectangle(250, 250, 400, 400, fill="blue")

scrollbar_x.config(command=canvas.xview)
#scrollbar_y.config(command=canvas.yview)




frame4 = Frame(canvas, background="red")
frame4.grid(column=0, row=0)

f = Figure(figsize=(2, 2), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
c1 = FigureCanvasTkAgg(f, master=frame4)
c1.draw()
c1.get_tk_widget().grid(column=0, row=1)

"""

# mainwin start
mainwin.mainloop()                                  # 창 종료되지 않고 계속 유지