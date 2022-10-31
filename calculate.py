'''from tkinter import *
root=Tk()
root.title('Kalkulyator')

input1 = Entry(root,width=50,borderwidth=5)
input1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

button_1=Button(root,text='1',padx=40,pady=20)
button_2=Button(root,text='2',padx=40,pady=20)
button_3=Button(root,text='3',padx=40,pady=20)
button_4=Button(root,text='4',padx=40,pady=20)
button_5=Button(root,text='5',padx=40,pady=20)
button_6=Button(root,text='6',padx=40,pady=20)
button_7=Button(root,text='7',padx=40,pady=20)
button_8=Button(root,text='8',padx=40,pady=20)
button_9=Button(root,text='9',padx=40,pady=20)
button_add=Button(root,text='+',padx=39,pady=20)
button_equal=Button(root,text='=',padx=91,pady=20)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)

button_7.grid(row=5,column=0)
button_8.grid(row=5,column=1)
button_9.grid(row=5,column=2)
button_add.grid(row=7,column=0)
button_equal.grid(row=7,column=1,columnspan=2)

root.mainloop()'''
from tkinter import *
root=Tk()
root.title('khal1lulloh')

input1 = Entry(root,width=50,borderwidth=5)
input1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
	string=input1.get()
	input1.delete(0,END)
	input1.insert(0,str(string)+str(number))

def button_clear():
    input1.delete(0,END)

def button_add():
    raq=input1.get()
    global saqlangan_raq
    global amal
    amal='qushish'
    saqlangan_raq=int(raq)
    input1.delete(0,END)	

def button_min():
	raq=input1.get()
	global saqlangan_raq
	global amal
	amal='ayirish'
	saqlangan_raq=int(raq)
	input1.delete(0,END)

def button_kop():
	raq=input1.get()
	global saqlangan_raq
	global amal
	amal="ko'paytirish"
	saqlangan_raq=int(raq)
	input1.delete(0,END)

def button_b():	
	raq=input1.get()
	global saqlangan_raq
	global amal
	amal="bo'lish"
	saqlangan_raq=int(raq)
	input1.delete(0,END)

def button_f():
	raq=input1.get()
	global saqlangan_raq
	global amal
	amal='qoldiq'
	saqlangan_raq=int(raq)
	input1.delete(0,END)

def button_s():
	raq=input1.get()
	global saqlangan_raq
	global amal
	amal='daraja'
	saqlangan_raq=int(raq)
	input1.delete(0,END)

def button_equal():
	summa=input1.get()
	input1.delete(0,END)
	if amal=="qushish":
		input1.insert(0,saqlangan_raq+int(summa))
	if amal=='ayirish':
	    input1.insert(0,saqlangan_raq-int(summa))
	if amal=="ko'paytirish":
	    input1.insert(0,saqlangan_raq*int(summa))
	if amal=="bo'lish":
	    input1.insert(0,saqlangan_raq/int(summa))
	if amal=='qoldiq':
	    input1.insert(0,saqlangan_raq%int(summa))
	if amal=='daraja':
	    input1.insert(0,saqlangan_raq**int(summa))	

button_1=Button(root,text='1',padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(root,text='2',padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(root,text='3',padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(root,text='4',padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(root,text='5',padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(root,text='6',padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(root,text='7',padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(root,text='8',padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(root,text='9',padx=40,pady=20,command=lambda:button_click(9))
button_o=Button(root,text='0',padx=90,pady=20,command=lambda:button_click(0))

button_f=Button(root,text='%',padx=40,pady=20,command=button_f)
button_b=Button(root,text='/',padx=40,pady=20,command=button_b)
button_s=Button(root,text='^',padx=40,pady=20,command=button_s)
button_clear=Button(root,text='clear',padx=40,pady=20,command=button_clear)
button_add=Button(root,text='+',padx=39,pady=20,command=button_add)
button_min=Button(root,text='-',padx=39,pady=20,command=button_min)
button_kop=Button(root,text='*',padx=38,pady=20,command=button_kop)
button_equal=Button(root,text='=',padx=91,pady=20,command=button_equal)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_min.grid(row=4,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_add.grid(row=3,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_kop.grid(row=2,column=3)

button_o.grid(row=5,column=0,columnspan=2)
button_equal.grid(row=5,column=2,columnspan=2)

button_clear.grid(row=1,column=0)
button_s.grid(row=1,column=1)
button_f.grid(row=1,column=2)
button_b.grid(row=1,column=3)

root.mainloop()
