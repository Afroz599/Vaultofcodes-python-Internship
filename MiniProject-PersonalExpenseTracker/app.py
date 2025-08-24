#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#creating empty lists for storing the contents
ls1=[]
ls2=[]
ls3=[]  
#defining methods for adding expenses,viewing summary,exit    
def add_expense():
    print("_________________________________") 
    exp=input("Enter the Expense type like\n Food\n Transport\n Entertainment\n").lower()
    print("__________________________________")
    if exp=='food':
        cost=int(input("Enter the cost in$\t"))
        date=input("Enter date in the format yyyy-mm-dd\t")
        ls1.append([exp,cost,date])
    elif exp=='transport':
        cost=int(input("Enter the cost in$\t"))
        date=input("Enter date in the format yyyy-mm-dd\t")
        ls2.append([exp,cost,date])
    elif exp=='entertainment':
        cost=int(input("Enter the cost in$\t"))
        date=input("Enter date in the format yyyy-mm-dd\t")
        ls3.append([exp,cost,date])
    else:
            print("Incorrect Input")
def view_summary():  
    #concatinating lists to a data variable  
    data=ls1+ls2+ls3
    #giving names to the columns
    df=pd.DataFrame(data,columns=['Category','Cost','Date'])
    #saving to the excel file
    df.to_csv("Expenses Data set.csv",index=False)
    print(df)
    print('___________________________________')
    #summing the categories individually
    df_sum = df.groupby('Category', as_index=False)['Cost'].sum()
    #using barplot for vizualization
    sns.barplot(data=df_sum, x='Category', y='Cost', errorbar=None)
    plt.title("EXPENSES:Category VS Cost")
    plt.show()
    # Daily summaries 
    df["Date"] = pd.to_datetime(df["Date"])
    daily_summary = df.groupby(df["Date"].dt.date)["Cost"].sum()
    print("\nDaily Summary:\n", daily_summary)
    #weekly summaries
    weekly_summary = df.groupby(df["Date"].dt.to_period("W"))["Cost"].sum()
    print("\nWeekly Summary:\n", weekly_summary)
def out():    
        exit()
#dictionary for mapping with the functions
options = {
    'add':add_expense,
    'view':view_summary,
    'exit':out
      }
#to run the below lines of code repetatively
while True:
    print("__________________________")
    print("\nPERSONAL EXPENSE TRACKER")
    print("__________________________")
    print(" Add\n view\n exit")
    print("__________________________")
    option=input("enter any from above\n")
    option=option.lower() #To deal with typos
    if option in options:
        #calling the functions after matching
        options[option]()          
    else:
        print("invalid choice")
