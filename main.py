from time import sleep
from tkinter import *
from random import randint


class Display:
    def __init__(self, a, b, c, d, e):
        self.scramble = Label(root, text=self.sequence())
        self.scramble.pack()
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.type = ["'", '2', '']

    def collect(self):
        f.bind_all('<space>', self.run)

    def run(self, event=None):
        root.after(1000 , self.scramble.destroy)
        time.configure(text=str(self.c) + '.' + str(self.d))
        x = True
        while x == True:
            sleep(0.1)
            self.d += 1
            if self.d == 10:
                self.d = 0
                self.c += 1
            if self.c == 60:
                self.c = 0
                self.b += 1
            if self.b == 60:
                self.a += 1
            if self.a == 24:
                break
            if self.e == 1:
                x = False
            if self.a == 0:
                if 0 < self.c < 10:
                    time.configure(text=str(self.b) + ':0' + str(self.c) + '.' + str(self.d))
                else:
                    time.configure(text=str(self.b) + ':' + str(self.c) + '.' + str(self.d))
                if self.c == 0:
                    time.configure(text=str(self.b) + ':0' + str(self.c) + '.' + str(self.d))
                if 10 > self.b > 0:
                    time.configure(text='0' + str(self.b) + ':' + str(self.c) + '.' + str(self.d))
                elif self.b > 10:
                    time.configure(text=str(self.b) + ':' + str(self.c) + '.' + str(self.d))
            elif self.a > 0:
                if self.c < 10:
                    time.configure(text=str(self.a) + ':' + str(self.b) + ':0' + str(self.c) + '.' + str(self.d))
                elif self.c > 10:
                    time.configure(text=str(self.a) + ':' + str(self.b) + ':' + str(self.c) + '.' + str(self.d))
                if self.b < 10:
                    time.configure(text=str(self.a) + ':0' + str(self.b) + ':' + str(self.c) + '.' + str(self.d))
                elif self.b > 10:
                    time.configure(text=str(self.a) + ':' + str(self.b) + ':' + str(self.c) + '.' + str(self.d))
            f.bind_all('<space>', self.end)
            root.update()
        self.sequence()
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.rerun()

    def end(self, *args):
        self.e += 1

    def rerun(self):
        self.e -= 1
        root.after(1000 , self.scramble.destroy)
        self.scramble = Label(root, text=self.sequence())
        self.scramble.pack()
        f.bind_all('<space>', self.run)

    def recordings(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    record = Label(root, text='0.' + self.d)
                else:
                    record = Label(root, text=self.c + '.' + self.d)
            else:
                record = Label(root, text=self.b + ':' + self.c + '.' + self.d)
        else:
            record = Label(root, text=self.a + ':' + self.b + ':' + self.c + '.' + self.d)
        record.pack()

    def sequence(self):
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
        return b, d, c, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u


print('|████████████████████████████████|')
g = 3
root = Tk()
root['bg'] = '#0000ff'
root.title('Timer')
f = Frame(root, height=500, width=600, bg='#0000ff')
f.pack()
time = Label(root, text='0:00:00.00', font='Verdana 50')
time.pack()
run = Display(0, 0, 0, 0, 0)
run.collect()
root.mainloop()
