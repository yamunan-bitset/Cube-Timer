from tkinter import *
from random import randint
import builtins
import time


'''
Q = input("Do you want a time limit?(Y/n) ")
if Q == "Y" or Q =="y":
    Q_2 = int(input("how long do you want it to be? "))
else:
    print("OK")
'''


class Main:
    def __init__(self, window, a, b, c, d, e):
        self.window = window
        self.window.resizable(False,False)
        self.title = "Timer"
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        self.e = int(e)
        self.running = True
        #self.tt = StringVar()
        #self.tt.set("0:00:00")
        self.frameworkspacebar()
        self.scrambleGen()


    def update(self):
        Time.configure(text=str(self.e)+':'+str(self.d)+str(self.c)+'.'+str(self.b)+str(self.a), font="Helvetica 100 bold")
        Time.pack()

        #k = Label(self.window, text=str(self.e)+':'+str(self.d)+str(self.c)+'.'+str(self.b)+str(self.a),font="Helvetica 100 bold")
        #k.pack()

    def frameworkspacebar(self):
        self.window.title(self.title)
        self.update()
        frame.bind_all("<space>", self.run)

    def makeint(self):
        int(self.a)
        int(self.b)
        int(self.c)
        int(self.d)
        int(self.e)

    def run(self, *args):
        if args is not None:
            while self.running:
                time.sleep(0.01)
                self.makeint()
                self.a += 1
                self.update()
                if self.a == 10:
                    self.makeint()
                    self.b += 1
                    self.update()
                if self.b == 10:
                    self.makeint()
                    self.c += 1
                    self.update()
                if self.c == 10:
                    self.makeint()
                    self.d += 1
                    self.update()
                if self.d == 10:
                    self.makeint()
                    self.e += 1
                    self.update()
                if self.e == 10:
                    self.makeint()
                    kk = Label(self.windows, text="You are slow!!!", font="Helvetica 100 bold")
                    kk.pack()
                    self.update()
                Time.configure(text=str(self.e) + ':' + str(self.d) + str(self.c) + '.' + str(self.b) + str(self.a))
                frame.bind_all("<space>", self.falserun)
            self.update()


    def falserun(self):
        #print(args)
        self.running = False
        self.run()
        self.scrambleGen()



    def cutoff(self):
        time.sleep(Q_2)
        kkk = Label(self.window, text="Your time exceeds the cutoff!!!", font="Helvetica 100 bold")
        kkk.pack()
        time.sleep(2)


    @staticmethod
    def scrambleGen():
        a = ['R', 'R-', 'L', 'L-', 'U', 'U-', 'F', 'F-', 'D', 'D-', 'B', 'B-']
        b = a[randint(0, 11)]
        d = a[randint(0, 11)]
        c = a[randint(0, 11)]
        e = a[randint(0, 11)]
        f = a[randint(0, 11)]
        g = a[randint(0, 11)]
        h = a[randint(0, 11)]
        i = a[randint(0, 11)]
        j = a[randint(0, 11)]
        k = a[randint(0, 11)]
        l = a[randint(0, 11)]
        m = a[randint(0, 11)]
        n = a[randint(0, 11)]  # 13
        o = a[randint(0, 11)]
        p = a[randint(0, 11)]
        q = a[randint(0, 11)]
        r = a[randint(0, 11)]
        s = a[randint(0, 11)]
        t = a[randint(0, 11)]
        u = a[randint(0, 11)]
        label = Label(root, text=[b, d, c, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u])
        label.pack()





rr = True
root = Tk()
root['bg'] = 'light green'
frame = Frame(root, height=480, width=600, bg="light green")
frame.pack()
Time = Label(root, text='0:00.00', font="Helvetica 100 bold")
Time.pack()
a = Main(root, 0, 0, 0, 0, 0)
root.mainloop()

'''
    def start(self, *args):
        global count
        count = 0
        self.timer()

    def timer(self):
        global count
        if count == 0:
            self.d = str(self.tt.get())
            h, m, s = map(int, self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    h += 1
            if h < 10:
                h = str(0)+str(h)
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h+":"+m+":"+s
            self.tt.set(self.d)
            if count == 0:
                self.window.after(930, self.timer)

'''
