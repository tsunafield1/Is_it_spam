import pandas as pd
import joblib
from tkinter import *

col = joblib.load('D:\งาน\KMITL\ปี3\ปี3เทอม1\ML\Project\EXE\COL.sav')
std = joblib.load('D:\งาน\KMITL\ปี3\ปี3เทอม1\ML\Project\EXE\STD.sav')
model = joblib.load('D:\งาน\KMITL\ปี3\ปี3เทอม1\ML\Project\EXE\MLP.sav')
count = {}
for colu in col:
    count[colu] = 0

def changeResult():
    inp = text.get('1.0', END)
    if inp == '\n':
        result.config(text='Please fill email in textbox...')
    else:
        new_inp = inp.replace('\n',' ')
        for k in count.keys():
            count[k] = new_inp.count(k)
        df = pd.DataFrame(columns=count.keys())
        df = df.append(count, ignore_index=True)
        df_std = std.transform(df)
        predict = model.predict(df_std)
        if predict[0] == 1:
            result.config(text='This email is spam')
        else:
            result.config(text='This email is not spam')

def clear():
    text.delete('1.0', END)
    result.config(text='Please fill email in textbox...')

root = Tk()
root.title('IsItSpam?')

title = Label(root,text='Spam mail?',font=('BOLD',35)).pack(anchor='center',pady=20)

text = Text(root,font=30,width=80,height=30)
text.pack(anchor='center')

frame = Frame()
btn1 = Button(frame,text='Check',font=30,height=2,width=10,command=changeResult).grid(row=0,column=0,padx=50)
btn2 = Button(frame,text='Clear',font=30,height=2,width=10,command=clear).grid(row=0,column=1,padx=50)
frame.pack(pady=30)

result = Label(root,text='Please fill email in textbox...',font=('BOLD',25))
result.pack(anchor='center')

root.geometry('800x800')
root.mainloop()