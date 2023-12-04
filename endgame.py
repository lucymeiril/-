import tkinter
import random
import tkinter.messagebox
import datetime

key = ""
xmouse = 0
ymouse = 0
clmouse = 0
count = 0
xpoint = 0
ypoint = 0
lon = 0
score = 0
def kdown(w):
    global key
    key = w.keysym 
def kup(w):
    global key
    key = ""
def mmove(w):
    global xmouse, ymouse, xpoint, ypoint
    xmouse = w.x
    ymouse = w.y
    xpoint=int(xmouse / 160)
    ypoint=int(ymouse / 72)
def mpress(w):
    global clmouse
    clmouse = 1
def mrelease(w):
    global clmouse
    clmouse = 0
    checkin()
def mpoint():
    global xpoint, ypoint
    xpoint=int(xmouse / 160)
    ypoint=int(ymouse / 72)
def ppoint():
    global ynowPaper, xnowPaper, xpaper, ypaper
    xnowPaper = wdw.coords("paper")
    ynowPaper = wdw.coords("paper")
    xpaper=int(xnowPaper / 160)
    ypaper=int(ynowPaper / 72)  
def endZone():             
    if xmouse > 500 and xmouse < 780 and ymouse > 320 and ymouse < 500:        
        wdw.create_rectangle(500, 320, 510, 500, fill="yellow", width=0, tag="getZone")
        wdw.create_rectangle(500, 318, 790, 330, fill="yellow", width=0, tag="getZone")
        wdw.create_rectangle(780, 320, 790, 500, fill="yellow", width=0, tag="getZone")
        wdw.create_rectangle(500, 488, 790, 500, fill="yellow", width=0, tag="getZone")
    else:
         wdw.delete("getZone")   
    moniter.after(100, endZone)
   
Npaper = 0
now = 0
mov = 10
def moving(): 
    global count, xonAir, yonAir, Npage, x, y, nx, ny
    global Npaper, now
    wdw.delete("print")
    if key == 'k':
        fnt = ("Times New Roman", 40, "bold")
        wdw.create_text(650, 100, text="현재 모은 페이지\n", fill="black", font=fnt, tag="print")
        wdw.create_text(650, 200, text=str(end)+' p', fill="black", font=fnt, tag="print")  
        wdw.create_text(200, 100, text="최고 점수! 현재... "+str(cscore)+" 점!", fill="yellow", font=("Times New Roman", 30, "bold"), tag="print")  
    if Npaper == 0:
        xlist = [128, 256, 384, 412, 896, 1024, 1152, 1280]
        ylist = [72, 720]
        xonAir = random.choice(xlist)   
        yonAir = random.choice(ylist)
        Npage = random.choice(page)
        if xonAir < 640 :
            if yonAir > 360:
                wdw.create_image(xonAir, yonAir, image = LUpaper, tag = "paper")
            wdw.create_image(xonAir, yonAir, image = LDpaper, tag = "paper") 
        if yonAir > 360:
            wdw.create_image(xonAir, yonAir, image = RUpaper, tag = "paper")
        wdw.create_image(xonAir, yonAir, image = RDpaper, tag = "paper")
        Npaper = 1  
        x, y = wdw.coords("paper")[:2]
        nx = int(x/160)
        ny = int(y/72)     
    if now == 0:
        if xonAir < 640 :
            if yonAir > 360:
                wdw.move("paper", mov, -mov)
                if ny < 0 or ny > 10:
                    count = 1
            else:  
                wdw.move("paper", mov, mov)
                if ny < 0 or ny > 10:
                    count = 1
        else:
            if yonAir > 360:
                wdw.move("paper", -mov, -mov)
                if ny < 0 or ny > 10:
                    count = 1
            else:
                wdw.move("paper", -mov, mov)
                if ny < 0 or ny > 10:
                    count = 1
    x, y = wdw.coords("paper")[:2]
    nx = int(x/160)
    ny = int(y/72) 
    if count == 1:
            wdw.delete("paper")
            count = 0  
            Npaper = 0
    if xpoint == nx and ypoint == ny:
        now = 1
        wdw.delete("paper")
        wdw.create_image(x, y, image = Npage, tag = "paper")
        if clmouse == 1:    
            movein()                          
    if now == 1 and not(xpoint == nx and ypoint == ny):
        wdw.delete("paper")
        xypaper() 
        now = 0   
    moniter.after(20, moving)    

def movein():
        if clmouse == 1:
            wdw.delete("paper")
            if xonAir < 640 :
                if yonAir > 360:
                    wdw.create_image(xmouse, ymouse, image = LUpaper, tag = "paper")
                wdw.create_image(xmouse, ymouse, image = LDpaper, tag = "paper") 
            if yonAir > 360:
                wdw.create_image(xmouse, ymouse, image = RUpaper, tag = "paper")
            wdw.create_image(xmouse, ymouse, image = RDpaper, tag = "paper")
            moniter.after(20, movein) 
def xypaper():
    if xonAir < 640 :
        if yonAir > 360:
            wdw.create_image(x, y, image = LUpaper, tag = "paper")
        wdw.create_image(x, y, image = LDpaper, tag = "paper") 
    if yonAir > 360:
        wdw.create_image(x, y, image = RUpaper, tag = "paper")
    wdw.create_image(x, y, image = RDpaper, tag = "paper") 
end = []
cscore = 0
score = 0
def checkin():
    global end, Npaper, start_t, score, cscore
    if clmouse == 0 and (xmouse > 500 and xmouse < 780 and ymouse > 320 and ymouse < 500) and (x > 500 and x < 780 and y > 320 and y < 500): 
        wdw.delete("paper")
        if Npage == page[0] and '1' not in end:        
            end.insert(0, '1')
        elif Npage == page[1] and '2' not in end:
            end.insert(1, '2')
        elif Npage == page[2] and '3' not in end:
            end.insert(2, '3')
        elif Npage == page[3] and '4' not in end:
            end.insert(3, '4')    
        elif Npage == page[4] and '5' not in end:
            end.insert(4, '5')
        elif Npage == page[5] and '6' not in end:
            end.insert(5, '6')
        elif Npage == page[6] and '7' not in end:
            end.insert(6, '7')           
        elif Npage == page[7]:
            end = []         
        Npaper = 0
        if '1' in end and '2' in end and '3' in end and '4' in end and '5' in end and '6' in end and '7' in end:
            end_t = datetime.datetime.now()
            tkinter.messagebox.showinfo("전부 모았어!\n", (str((end_t - start_t).seconds) + "초 걸렸어!"))
            end = []
            score = 150 - int((end_t-start_t).seconds)
            if score < 0:
                score = 0
            if score >= cscore:
                cscore = score
                last = tkinter.messagebox.askyesno(str(cscore) + " 점 획득!", "그만 할까?")
            else:   
                last = tkinter.messagebox.askyesno(str(score) + " 점 획득!", "그만 할까?")    
            if last == True:
                exit()
            start_t = datetime.datetime.now()    
    
moniter = tkinter.Tk()
moniter.bind("<Motion>", mmove)  
moniter.bind("<ButtonPress>", mpress)    
moniter.bind("<ButtonRelease>", mrelease)
moniter.bind("<KeyPress>", kdown)
moniter.bind("<KeyRelease>", kup)
wdw = tkinter.Canvas(moniter, width = 1290, height= 720, bg = "white")
moniter.title("The Secret of KN Library")
moniter.resizable(width= False, height = False)
wdw.pack()
lib =tkinter.PhotoImage(file = "p\\ilb.png")
wdw.create_image(640, 360, image =  lib, tag = "map")
def EX():
    global lon
    lon+=1
    if lon == 1:    
        text.insert(tkinter.END, "지금부터 게임을 설명할게!\n\n") 
        text.insert(tkinter.END, "얼마 전, 못된 관람객들이 도서관 책들의 페이지를 찢어버렸어...\n\n")
    if lon == 2:
        text.delete("1.0", "end")
        text.insert(tkinter.END, "지금부터 잃어버린 페이지를 되찾는 거야!\n\n")
    if lon == 3:
        text.delete("1.0", "end")
        text.insert(tkinter.END, "마우스를 날아다니는 종이에 가져다 놓으면 몇 페이지인지를 확인할 수 있어!\n\n")
    if lon == 4:
        text.delete("1.0", "end")
        text.insert(tkinter.END, "종이에 마우스를 얹고, 클릭한 채로 움직여봐!\n\n")
    if lon == 5:
        text.delete("1.0", "end")
        text.insert(tkinter.END, "그러다 보면 책의 노란 선이 나타날 거야. 거기서 마우스를 놓으면...\n\n참고로 '꽝'은 조심하는 게 좋아! 뭐, 겪어보면 알겠지만!\n\n")
    if lon == 6:
        text.delete("1.0", "end")
        text.insert(tkinter.END, "모은 페이지는 k 키를 눌러 확인할 수 있어!\n\n")
    if lon == 7:
        text.delete("1.0", "end")
        text.insert(tkinter.END, "그럼 시작한다?")
    if lon == 8:    
        bt.destroy()
        bt2.destroy()
        text.destroy()
def EX2():
    global lon
    if lon > 1:
        lon-=1
        if lon == 1:    
            text.delete("1.0", "end")
            text.insert(tkinter.END, "지금부터 게임을 설명할게!\n\n") 
            text.insert(tkinter.END, "얼마 전, 못된 관람객들이 도서관 책들의 페이지를 찢어버렸어...\n\n")
        if lon == 2:
            text.delete("1.0", "end")
            text.insert(tkinter.END, "지금부터 잃어버린 페이지를 되찾는 거야!\n\n")
        if lon == 3:
            text.delete("1.0", "end")
            text.insert(tkinter.END, "마우스를 날아다니는 종이에 가져다 놓으면 몇 페이지인지를 확인할 수 있어!\n\n")
        if lon == 4:
            text.delete("1.0", "end")
            text.insert(tkinter.END, "종이에 마우스를 얹고, 클릭한 채로 움직여봐!\n\n")
        if lon == 5:
            text.delete("1.0", "end")
            text.insert(tkinter.END, "그러다 보면 책의 노란 선이 나타날 거야. 거기서 마우스를 놓으면...\n\n참고로 '꽝'은 조심하는 게 좋아! 뭐, 겪어보면 알겠지만!\n\n")
        if lon == 6:
            text.delete("1.0", "end")
            text.insert(tkinter.END, "모은 페이지는 k 키를 눌러 확인할 수 있어!\n\n")
        if lon == 7:
            text.delete("1.0", "end")
            text.insert(tkinter.END, "그럼 시작한다?") 
bt = tkinter.Button(text="다음", font = ("Times New Roman", 30, "bold"), command=EX)
bt2 = tkinter.Button(text="이전", font = ("Times New Roman", 30, "bold"), command=EX2)
text=tkinter.Text(font = ("Times New Roman",30), bg = "gray")
text.place(x = 250, y = 2, width= 800, height= 260)
bt.place(x = 750, y = 250, width=300, height=100)
bt2.place(x = 250, y = 250, width=300, height=100)
LDpaper = tkinter.PhotoImage(file = "p\\LDpaper.png")
LUpaper = tkinter.PhotoImage(file = "p\\LUpaper.png")
RDpaper = tkinter.PhotoImage(file = "p\\RDpaper.png")
RUpaper = tkinter.PhotoImage(file = "p\\RUpaper.png")
page = [
        tkinter.PhotoImage(file = "p1.png"),
        tkinter.PhotoImage(file = "p2.png"),
        tkinter.PhotoImage(file = "p3.png"),
        tkinter.PhotoImage(file = "p4.png"),
        tkinter.PhotoImage(file = "p5.png"),
        tkinter.PhotoImage(file = "p6.png"),
        tkinter.PhotoImage(file = "p7.png"),
        tkinter.PhotoImage(file = "p0.png")
        ]
start_t = datetime.datetime.now()
endZone()
moving()
moniter.mainloop()