from main import *
from DES import *
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import base64

window =tk.Tk() #实例化object
window.title(' Diffie-Hellman 三方密钥交换') #窗口标题
window.geometry('1000x400') #窗口尺寸




p=''
g=''
x=''
y=''
z=''
X1=''
Y1=''
Z1=''
X2=''
Y2=''
Z2=''
k1=''
k2=''
k3=''
m=''

def buildP():
    global p
    p=BigPrime()
    text1.delete(1.0, END)
    text1.insert(1.0, str(p))
def buildg():
    global p,g
    g=random.randrange(1,10000,1)
    while gcd(p,g)!=1:
        g=random.randrange(1,10000,1)
    text2.delete(1.0, END)
    text2.insert(1.0, str(g))

def build_private_key():
    global x,y,z
    x=random.randrange(1,10000,1)#Alice
    y=random.randrange(1,10000,1)#Bob
    z=random.randrange(1,10000,1)#Carol
    text3.delete(1.0, END)
    text3.insert(1.0, str(x))
    text4.delete(1.0, END)
    text4.insert(1.0, str(y))
    text5.delete(1.0, END)
    text5.insert(1.0, str(z))

def first_distribute():
    global x,y,z,X1,Y1,Z1
    Z1=mod_fast(g, z, p)#Alice从C处收到
    X1=mod_fast(g, x, p)#Bob从A收到
    Y1=mod_fast(g, y, p)#Carol从B收到
    text6.delete(1.0, END)
    text6.insert(1.0, str(Z1))
    text7.delete(1.0, END)
    text7.insert(1.0, str(X1))
    text8.delete(1.0, END)
    text8.insert(1.0, str(Y1))
    
    
def second_distribute():
    global x,y,z,X1,Y1,Z1,X2,Y2,Z2
    Y2=mod_fast(Y1, z, p)#Alice从C处收到
    Z2=mod_fast(Z1, x, p)#Bob从A处收到
    X2=mod_fast(X1, y, p)#Carol从B处收到
    text9.delete(1.0, END)
    text9.insert(1.0, str(Y2))
    text10.delete(1.0, END)
    text10.insert(1.0, str(Z2))
    text11.delete(1.0, END)
    text11.insert(1.0, str(X2))
    
def share_key():
    global x,y,z,X1,Y1,Z1,X2,Y2,Z2,k1,k2,k3
    k1=mod_fast(Y2, x, p)#Alice计算后密钥
    k2=mod_fast(Z2, y, p)#Bob计算后密钥
    k3=mod_fast(X2, z, p)#Carol计算后密钥
    text12.delete(1.0, END)
    text12.insert(1.0, str(k1))
    text13.delete(1.0, END)
    text13.insert(1.0, str(k2))
    text14.delete(1.0, END)
    text14.insert(1.0, str(k3))

def DES_encrypt():
    global k1,k2,k3
    if text15.get(1.0, END) == '\n':
        tkinter.messagebox.showinfo('提示', '不能为空')
    else:
        m = str(text15.get(1.0, END).strip())
        k=str(k1)
        s = all_message_encrypt(m,k)
        
        out_mess = bin2str(s)
        text16.delete(1.0, END)
        text16.insert(1.0, out_mess)

def DES_decrypt():
    global k1,k2,k3
    if text16.get(1.0, END) == '\n':
        tkinter.messagebox.showinfo('提示', '不能为空')
    else:
        m = str(text16.get(1.0, END).strip())

        k=str(k1)
        s = all_message_decrypt(m, k)
        s=list(s)
        while ('\x00' in s):#删掉填充的空格
            s.remove('\x00')
        
        s=''.join(s)
        text15.delete(1.0, END)
        text15.insert(1.0, s)
        
        
        
    
if __name__=='__main__':
    
    button1 = tk.Button(window, text='生成素数P', font=('宋体', 12,), width=10, height=1, command=buildP)
    button2 = tk.Button(window, text='生成原根g', font=('宋体', 12,), width=10, height=1, command=buildg)
    button3 = tk.Button(window, text='生成私钥', font=('宋体', 12,), width=10, height=1, command=build_private_key)
    button4 = tk.Button(window, text='一轮密钥分发', font=('宋体',12,), width=11, height=2, command=first_distribute)
    button5 = tk.Button(window, text='二轮密钥分发', font=('宋体', 12,), width=11, height=2, command=second_distribute)
    button6 = tk.Button(window, text='共享密钥', font=('宋体', 12,), width=11, height=2, command=share_key)
    button7 = tk.Button(window, text='DES加密', font=('宋体', 12,), width=11, height=2, command=DES_encrypt)
    button8 = tk.Button(window, text='DES解密', font=('宋体', 12,), width=11, height=2, command=DES_decrypt)
    text1 = tk.Text(window, show=None, font=('Arial', 10))#大素数P
    text2 = tk.Text(window, show=None, font=('Arial', 10))#原根g
    text3 = tk.Text(window, show=None, font=('Arial', 10))#Alice私钥
    text4 = tk.Text(window, show=None, font=('Arial', 10))#Bob私钥
    text5 = tk.Text(window, show=None, font=('Arial', 10))#Carol私钥
    text6 = tk.Text(window, show=None, font=('Arial', 10))#Alice第一轮
    text7 = tk.Text(window, show=None, font=('Arial', 10))#Bob第一轮
    text8 = tk.Text(window, show=None, font=('Arial', 10))#Carol第一轮
    text9 = tk.Text(window, show=None, font=('Arial', 10))#Alice第二轮
    text10 = tk.Text(window, show=None, font=('Arial', 10))#Bob第二轮
    text11 = tk.Text(window, show=None, font=('Arial', 10))#Carol第二轮
    text12 = tk.Text(window, show=None, font=('Arial', 10))#Alice计算后密钥
    text13 = tk.Text(window, show=None, font=('Arial', 10))#Bob计算后密钥
    text14 = tk.Text(window, show=None, font=('Arial', 10))#Carol计算后密钥
    text15 = tk.Text(window, show=None, font=('Arial', 10))#原文
    text16 = tk.Text(window, show=None, font=('Arial', 10))#密文
    
    labe1 = tk.Label(window, text='Alice', font=('宋体', 12), width=20, height=2)
    labe2 = tk.Label(window, text='Bob', font=('宋体', 12), width=20, height=2)
    labe3 = tk.Label(window, text='Carol', font=('宋体', 12), width=20, height=2)



    text1.place(relx=0.1,rely=0.0,relwidth=0.3,relheight=0.1)
    text2.place(relx=0.6,rely=0.0,relwidth=0.3,relheight=0.1)
    text3.place(relx=0.1,rely=0.2,relwidth=0.3,relheight=0.1)
    text4.place(relx=0.4,rely=0.2,relwidth=0.3,relheight=0.1)
    text5.place(relx=0.7,rely=0.2,relwidth=0.3,relheight=0.1)
    text6.place(relx=0.1,rely=0.3,relwidth=0.3,relheight=0.1)
    text7.place(relx=0.4,rely=0.3,relwidth=0.3,relheight=0.1)
    text8.place(relx=0.7,rely=0.3,relwidth=0.3,relheight=0.1)
    text9.place(relx=0.1,rely=0.5,relwidth=0.3,relheight=0.1)
    text10.place(relx=0.4,rely=0.5,relwidth=0.3,relheight=0.1)
    text11.place(relx=0.7,rely=0.5,relwidth=0.3,relheight=0.1)
    text12.place(relx=0.1,rely=0.6,relwidth=0.3,relheight=0.1)
    text13.place(relx=0.4,rely=0.6,relwidth=0.3,relheight=0.1)
    text14.place(relx=0.7,rely=0.6,relwidth=0.3,relheight=0.1)
    text15.place(relx=0.1,rely=0.8,relwidth=0.3,relheight=0.1)
    text16.place(relx=0.6,rely=0.8,relwidth=0.3,relheight=0.1)
    button1.place(relx=0.0,rely=0.0,relheight=0.1)
    button2.place(relx=0.5,rely=0.0,relheight=0.1)
    button3.place(relx=0.0,rely=0.2,relheight=0.1)
    button4.place(relx=0.0,rely=0.3,relheight=0.1)
    button5.place(relx=0.0,rely=0.5,relheight=0.1)
    button6.place(relx=0.0,rely=0.6,relheight=0.1)
    button7.place(relx=0.0,rely=0.8,relheight=0.1)
    button8.place(relx=0.5,rely=0.8,relheight=0.1)
    
    labe1.place(relx=0.1,rely=0.1,relwidth=0.3)
    labe2.place(relx=0.4,rely=0.1,relwidth=0.3)
    labe3.place(relx=0.7,rely=0.1,relwidth=0.3)

    window.mainloop() 
