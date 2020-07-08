import tkinter as tk
from db import mycursor

username = "John Doe"
password = "Hello12123"

def getEmpDetails():
    print("Got Employee Details")

root = tk.Tk()
root.geometry('770x400')
empDetailsFrame = tk.Frame(root)
titleFrame = tk.Frame(root)

# title
titleLabel = tk.Label(titleFrame,text="PROFILE AND STATS", fg="red",font=('Arial',20,'bold'))
titleLabel.grid(sticky=tk.N)

titleFrame.grid(sticky=tk.N)

# get user details
mycursor.execute("select * from t_users where full_name=%s",(username,))
dbDetails = mycursor.fetchall()
headers=("User Id:","Password:","Date of Joining:","Full Name:")
dbDetails.insert(0,headers)
print(dbDetails)


# table 
for i in range(len(dbDetails)): #Rows
    for j in range(len(dbDetails[0])): #Columns
        b = tk.Entry(empDetailsFrame, width=20, fg='Black',font=('Arial',16,'bold'))
        b.insert(tk.END, dbDetails[i][j])
        b.grid(row=i, column=j)

total_rows = len(dbDetails) 
total_columns = len(dbDetails[0])



# Table1 = Table(empDetailsFrame)


#table
# Example(root).pack(fill="both", expand=True)
empDetailsFrame.grid()



root.mainloop()