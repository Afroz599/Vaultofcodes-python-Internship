import tkinter as tk
import pandas as pd
root=tk.Tk()
root.geometry('500x300')
root.title("personal-todo-list")
def urgent():
    global e2,t1,x
    l2=tk.Label(root,text='Add the task',font=('Arial',10))
    l2.pack(padx=2)
    e2=tk.Entry(root,)
    e2.pack(padx=2)
    l3=tk.Label(root,text='Add discription',font=('Arial',10))
    l3.pack(padx=2)
    t1=tk.Text(root,height=2,width=30)
    t1.pack(padx=2)
    x=tk.StringVar()
    r1=tk.Radiobutton(root,text='Completed',value='Completed',variable=x)
    r1.pack(padx=2)
    r2=tk.Radiobutton(root,text='In progress',value='In progress',variable=x)
    r2.pack(padx=2)
    b2=tk.Button(root,text='save',command=save,cursor='hand2')
    b2.pack()
def personal():
    global e2,t1
    l2=tk.Label(root,text='Add the task',font=('Arial',10))
    l2.pack(padx=2)
    e2=tk.Entry(root,)
    e2.pack(padx=2)
    l3=tk.Label(root,text='Add discription',font=('Arial',10))
    l3.pack(padx=2)
    t1=tk.Text(root,height=2,width=30)
    t1.pack(padx=2)
    x=tk.StringVar()
    r1=tk.Radiobutton(root,text='Completed',value='Completed',variable=x)
    r1.pack(padx=2)
    r2=tk.Radiobutton(root,text='In progress',value='In progress',variable=x)
    r2.pack(padx=2)
    b2=tk.Button(root,text='save',command=save,cursor='hand2')
    b2.pack()
def work():
    global e2,t1
    l2=tk.Label(root,text='Add the task',font=('Arial',10))
    l2.pack(padx=2)
    e2=tk.Entry(root,)
    e2.pack(padx=2)
    l3=tk.Label(root,text='Add discription',font=('Arial',10))
    l3.pack(padx=2)
    t1=tk.Text(root,height=2,width=30)
    t1.pack(padx=2)
    x=tk.StringVar()
    r1=tk.Radiobutton(root,text='Completed',value='Completed',variable=x)
    r1.pack(padx=2)
    r2=tk.Radiobutton(root,text='In progress',value='In progress',variable=x)
    r2.pack(padx=2)
    b2=tk.Button(root,text='save',command=save,cursor='hand2')
    b2.pack()
def show():
    l10=tk.Label(root,text='Assig').pack()
work={
    'urgent':urgent,
    'personal':personal,
    'work':work
}
l1=tk.Label(root,text='Enter the category',font=('Arial',12,'italic')).pack(padx=2)
l4=tk.Label(root,text='urget | personal | work ',font=('Arial',10)).pack(padx=2)
e1=tk.Entry(root)
e1.pack(padx=2)
def run():
    go=e1.get()
    go=go.lower()
    if go in work:
        work[go]()
    else:
        pass
def save():
        data=[{'Category':e1.get(),'Task':e2.get(),'Discription':t1.get('1.0',tk.END).strip(),'Status':x.get()}]
        df=pd.DataFrame(data)
        df.to_csv('To-do list.csv',index=False)
b1=tk.Button(root,text='SUBMIT',command=run,cursor='hand2').pack(padx=2)
root.mainloop()

