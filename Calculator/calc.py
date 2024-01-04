import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Tk, Label


calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation  += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
     global calculation
     try:
          calculation = str((eval(calculation)))
          text_result.delete(1.0, "end")
          text_result.insert(1.0, calculation)
     except:
          clear_field()
          text_result.insert(1.0, "Error")


def clear_field():
     global calculation
     calculation = ""
     text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("320x520+500+100")
root.resizable(False,False)
root.config(bg='black')
root.title('Calculator')

my_image = ImageTk.PhotoImage(file="C:/Users/CHAMPIKA/Desktop/calculator.jpg")
lb1_image = tk.Label(root, image=my_image, bd=0).place(x=0, y=0)

text_result = tk.Text(root, height=2, font=('calibri', 30, 'bold'), bg="#9e8989", fg='white', bd=0)
text_result.place(x=21, y=46, height=45, width=273)

btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation("1"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_1.place(x=26,y=130,width=35,height=35)
btn_2=tk.Button(root,text="2",command=lambda:add_to_calculation("2"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_2.place(x=100,y=130,width=35,height=35)
btn_3=tk.Button(root,text="3",command=lambda:add_to_calculation("3"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_3.place(x=174,y=130,width=35,height=35)
btn_puls=tk.Button(root,text="+",command=lambda:add_to_calculation("+"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_puls.place(x=247,y=130,width=35,height=35)

btn_4=tk.Button(root,text="4",command=lambda:add_to_calculation("4"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_4.place(x=26,y=202,width=35,height=35)
btn_5=tk.Button(root,text="5",command=lambda:add_to_calculation("5"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_5.place(x=100,y=202,width=35,height=35)
btn_6=tk.Button(root,text="6",command=lambda:add_to_calculation("6"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_6.place(x=174,y=202,width=35,height=35)
btn_minus=tk.Button(root,text="-",command=lambda:add_to_calculation("-"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_minus.place(x=247,y=202,width=35,height=35)

btn_7=tk.Button(root,text="7",command=lambda:add_to_calculation("7"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_7.place(x=26,y=274,width=35,height=35)
btn_8=tk.Button(root,text="8",command=lambda:add_to_calculation("8"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_8.place(x=100,y=274,width=35,height=35)
btn_9=tk.Button(root,text="9",command=lambda:add_to_calculation("9"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_9.place(x=174,y=274,width=35,height=35)
btn_multi=tk.Button(root,text="*",command=lambda:add_to_calculation("*"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_multi.place(x=247,y=274,width=35,height=35)

btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("("),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_open.place(x=26,y=346,width=35,height=35)
btn_0=tk.Button(root,text="0",command=lambda:add_to_calculation("0"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_0.place(x=100,y=346,width=35,height=35)
btn_close=tk.Button(root,text=")",command=lambda:add_to_calculation(")"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_close.place(x=174,y=346,width=35,height=35)
btn_devi=tk.Button(root,text="/",command=lambda:add_to_calculation("/"),font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_devi.place(x=247,y=346,width=35,height=35)

btn_clear=tk.Button(root,text="C",command=clear_field,font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_clear.place(x=55,y=435,width=35,height=35)
btn_equal=tk.Button(root,text="=",command=evaluate_calculation,font=('calibri',30,'bold'),fg='white',bg="#9e8989",bd=0,cursor='hand2',activebackground="#9e8989")
btn_equal.place(x=230,y=435,width=35,height=35)


root.mainloop()
