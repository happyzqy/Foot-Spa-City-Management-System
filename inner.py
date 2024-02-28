import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from time import sleep
from database import *
class ini:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        self.frame_new.place(x=0, y=0, width=500, height=500)
        rb=ttk.Button(self.frame_new,text='注册',command=roll)
        xb=ttk.Button(self.frame_new,text='修改密码',command=change_pa)
        zb=ttk.Button(self.frame_new,text='注销',command=dele)
        rb.place(x=0,y=0,width=100,height=50)
        xb.place(x=0,y=100,width=100,height=50)
        zb.place(x=0,y=200,width=100,height=50)

class roll:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        self.frame_new.place(x=0, y=0, width=500, height=500)
        phone = tk.StringVar()
        password = tk.StringVar()
        password2 = tk.StringVar()
        ttk.Label(self.frame_new,text='电话').place(x=0,y=0,width=250,height=50)
        ttk.Label(self.frame_new,text='密码').place(x=0,y=100,width=250,height=50)
        ttk.Label(self.frame_new,text='确认密码').place(x=0,y=200,width=250,height=50)
        # 电话，密码的输入框
        self.en1 = ttk.Entry(self.frame_new, textvariable=phone)
        self.en1.place(x=0, y=50, width=250, height=40)
        self.en2 = ttk.Entry(self.frame_new, textvariable=password, show='*')
        self.en2.place(x=0, y=150, width=250, height=40)
        self.en3 = ttk.Entry(self.frame_new, textvariable=password2, show='*')
        self.en3.place(x=0, y=250, width=250, height=40)
        #确认按钮
        self.yes=ttk.Button(self.frame_new,text='确认注册',command=lambda:self.reg(phone.get(),password.get(),password2.get()))
        self.yes.place(x=0,y=300,width=250,height=50)
        #返回按钮
        re=ttk.Button(self.frame_new,text='返回',command=ini)
        re.place(x=450,y=0,width=50,height=50)
    def reg(self,a,b,c):
        #print(a,b,c)
        #获得注册结果k

        k=sec(a,b,c)

#明天的后天的都可以
        if k[0]==False:
            ttk.Label(self.frame_new,text=k[1]).place(x=0,y=350,width=250,height=50)
        else:
            ttk.Label(self.frame_new, text=k[1]).place(x=0, y=350, width=250, height=50)
class change_pa:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        self.frame_new.place(x=0, y=0, width=500, height=500)
        phone = tk.StringVar()
        password = tk.StringVar()
        password2 = tk.StringVar()
        password3 = tk.StringVar()
        ttk.Label(self.frame_new,text='电话').place(x=0,y=0,width=250,height=50)
        ttk.Label(self.frame_new,text='原密码').place(x=0,y=100,width=250,height=50)
        ttk.Label(self.frame_new,text='新密码').place(x=0,y=200,width=250,height=50)
        ttk.Label(self.frame_new,text='确认新密码').place(x=250,y=200,width=250,height=50)
        # 电话，密码的输入框
        self.en1 = ttk.Entry(self.frame_new, textvariable=phone)
        self.en1.place(x=0, y=50, width=250, height=40)
        self.en2 = ttk.Entry(self.frame_new, textvariable=password, show='*')
        self.en2.place(x=0, y=150, width=250, height=40)
        self.en3 = ttk.Entry(self.frame_new, textvariable=password2, show='*')
        self.en3.place(x=0, y=250, width=250, height=40)
        self.en4 = ttk.Entry(self.frame_new, textvariable=password3, show='*')
        self.en4.place(x=250, y=250, width=250, height=40)
        #确认按钮
        self.yes=ttk.Button(self.frame_new,text='确认修改',command=lambda:self.c_pa(phone.get(),password.get(),password2.get(),password3.get()))
        self.yes.place(x=0,y=300,width=250,height=50)
        #返回按钮
        re=ttk.Button(self.frame_new,text='返回',command=ini)
        re.place(x=450,y=0,width=50,height=50)
    def c_pa(self,a,b,c,d):
        print(a,b,c,d)
        #获得修改结果k

        k=alter_pas_guanli(a,b,c,d)
        if k[0]==False:
            ttk.Label(self.frame_new,text=k[1]).place(x=0,y=350,width=250,height=50)
        else:
            ttk.Label(self.frame_new, text=k[1]).place(x=0, y=350, width=250, height=50)
class dele:
    def __init__(self):
        self.frame_new = tk.Frame(root, bg='white')
        self.frame_new.place(x=0, y=0, width=500, height=500)
        phone = tk.StringVar()
        password = tk.StringVar()
        password2 = tk.StringVar()
        ttk.Label(self.frame_new,text='电话').place(x=0,y=0,width=250,height=50)
        # 电话，密码的输入框
        self.en1 = ttk.Entry(self.frame_new, textvariable=phone)
        self.en1.place(x=0, y=50, width=250, height=40)
        #确认按钮
        self.yes=ttk.Button(self.frame_new,text='确认注销',command=lambda:self.de(phone.get()))
        self.yes.place(x=0,y=300,width=250,height=50)
        #返回按钮
        re=ttk.Button(self.frame_new,text='返回',command=ini)
        re.place(x=450,y=0,width=50,height=50)
    def de(self,a):
        print(a)
        #获得注销结果k
        k=de_g(a)
        if k[0]==False:
            ttk.Label(self.frame_new,text=k[1]).place(x=0,y=350,width=250,height=50)
        else:
            ttk.Label(self.frame_new, text=k[1]).place(x=0, y=350, width=250, height=50)
root = tk.Tk()
# 网页名称大小背景色
root.title('山青阁足疗城内部程序')
root.geometry('500x500')
root.attributes('-alpha', 1)
ini()
root.mainloop()