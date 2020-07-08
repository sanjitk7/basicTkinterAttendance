import tkinter as tk
from db import mycursor,mydb
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

u_id = "1"
password = "Hello12123"

def postAttendance(event):
    mycursor.execute("""insert into attendance_record(a_date,a_detail,u_id) value (%s,%s,%s)""",(formatted_date,"PRESENT",1))
    mydb.commit()
    print("ATTENDANCE POSTED!")

root = tk.Tk()
root.geometry('770x400')
empDetailsFrame = tk.Frame(root)
titleFrame = tk.Frame(root)
attdFrame = tk.Frame(root)

# title
titleLabel = tk.Label(titleFrame,text="PROFILE AND STATS", fg="red",font=('Arial',20,'bold'))
titleLabel.grid(sticky=tk.N)

titleFrame.grid(sticky=tk.N)

# get user details
mycursor.execute("select * from t_users where u_id=%s",(u_id,))
dbDetails = mycursor.fetchall()
headers=("User Id","Password","Date of Joining","Full Name")
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

# attendance button!

butt1 = tk.Button(attdFrame, text="POST TODAY'S ATTENDANCE! ABRACADABRA!")
butt1.bind("<Button-1>",postAttendance)
butt1.grid(padx=10,pady=10)

attdFrame.grid()


root.mainloop()