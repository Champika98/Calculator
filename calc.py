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