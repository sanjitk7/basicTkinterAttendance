import tkinter as tk
from db import mycursor

username = "John Doe"
password = "Hello12123"

def getEmpDetails():
    print("Got Employee Details")


# class Example(tk.Frame):
#     def __init__(self, parent):
#         tk.Frame.__init__(self, parent)
#         table = tk.Frame(self)
#         table.pack(side="top", fill="both", expand=True)

#         mycursor.execute("select * from t_users where full_name=%s",(username,))
#         data = mycursor.fetchone()
#         print(data)

#         self.widgets = {}
#         row = 0
#         for u_id, password, date_joined, full_name in data:
#             row += 1
#             self.widgets[u_id] = {
#                 "u_id": tk.Label(table, text=u_id),
#                 "password": tk.Label(table, text=password),
#                 "date_joined": tk.Label(table, text=date_joined),
#                 "full_name": tk.Label(table, text=full_name)
#             }

#             self.widgets[u_id]["u_id"].grid(row=row, column=0, sticky="nsew")
#             self.widgets[u_id]["password"].grid(row=row, column=1, sticky="nsew")
#             self.widgets[u_id]["date_joined"].grid(row=row, column=2, sticky="nsew")
#             self.widgets[u_id]["full_name"].grid(row=row, column=4, sticky="nsew")

#         table.grid_columnconfigure(1, weight=1)
#         table.grid_columnconfigure(2, weight=1)
#         # invisible row after last row gets all extra space
#         table.grid_rowconfigure(row+1, weight=1)


class Table: 
      
    def __init__(self,empDetailsFrame): 
          
        # code for creating table 
        for i in range(total_columns):  
            # self.e = tk.Entry(empDetailsFrame, width=20, fg='Black', 
            #                 font=('Arial',16,'bold')) 
        
            # self.e.pack()
            # self.e.insert(tk.END, dbDetails[0][i])
            self.lw = tk.Label(empDetailsFrame, text=headers[i])
            self.lw.pack(side=tk.LEFT)
            self.l1 = tk.Label(empDetailsFrame, text=dbDetails[0][i])
            self.l1.pack(side=tk.LEFT)



root = tk.Tk()

empDetailsFrame = tk.Frame(root)
titleFrame = tk.Frame(root)

# title
titleLabel = tk.Label(titleFrame,text="Your Information", anchor=tk.CENTER)
titleLabel.pack(side=tk.TOP)

titleFrame.pack(side=tk.TOP)

# get user details
mycursor.execute("select * from t_users where full_name=%s",(username,))
dbDetails = mycursor.fetchall()
headers=["User Id:","Password:","Date of Joining:","Full Name:"]
print(dbDetails)

total_rows = len(dbDetails) 
total_columns = len(dbDetails[0])

Table1 = Table(empDetailsFrame)


#table
# Example(root).pack(fill="both", expand=True)
empDetailsFrame.pack()



root.mainloop()