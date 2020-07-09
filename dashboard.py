import tkinter as tk
from db import mycursor,mydb
from datetime import datetime

now = datetime.now().date()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

u_id = "1"
password = "Hello12123"

def checkAttendance():
    checkFlag=0
    mycursor.execute("""select * from attendance_record where a_date=%s and u_id=%s""",(formatted_date,u_id))
    dbAttdCheck = mycursor.fetchall()
    if (dbAttdCheck!=[]):
        print("Attendance Already Posted")
        checkFlag=1
    return checkFlag

def postAttendance(event):
    checkFlag = checkAttendance()
    if(checkFlag==1):
        return
    mycursor.execute("""insert into attendance_record(a_date,a_detail,u_id) value (%s,%s,%s)""",(formatted_date,"PRESENT",u_id))
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

titleFrame.grid(row=0,sticky=tk.N)

# get user details
mycursor.execute("select * from t_users where u_id=%s",(u_id,))
dbDetails = mycursor.fetchall()
headers=("User Id","Password","Date of Joining","Full Name")
dbDetails.insert(0,headers)
print("DB DETAILS OF CURRENT USER FETCHED:",dbDetails)

# get attendance details
mycursor.execute("select * from attendance_record where u_id=%s",(u_id,))
dbAttd = mycursor.fetchall()
headers2=("Date","Attendance Detail")
dbAttd.insert(0,headers2)
print("ATTENDANCE OF CURRENT USER FETCHED:",dbAttd)

# table emp details
for i in range(len(dbDetails)): #Rows
    for j in range(len(dbDetails[0])): #Columns
        b = tk.Entry(empDetailsFrame, width=20, fg='Black',font=('Arial',16,'bold'))
        b.insert(tk.END, dbDetails[i][j])
        b.grid(row=i, column=j)

empDetailsFrame.grid(row=1)

# table emp attendance
for i in range(len(dbAttd)): #Rows
    for j in range(len(dbAttd[0])): #Columns
        c = tk.Entry(attdFrame, width=33, fg='Black',font=('Arial',16,'bold'))
        c.insert(tk.END, dbAttd[i][j])
        c.grid(row=i, column=j)

attdFrame.grid(row=3,pady=10)
#table
# Example(root).pack(fill="both", expand=True)


# attendance button!

butt1 = tk.Button(attdFrame, text="POST TODAY'S ATTENDANCE! ABRACADABRA!")
butt1.bind("<Button-1>",postAttendance)
butt1.grid(padx=10,pady=10)

attdFrame.grid()


root.mainloop()