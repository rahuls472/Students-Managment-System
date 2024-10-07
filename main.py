from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from mydb import dataset

class Student:
    def __init__(self):
        self.root = ttk.Window(themename="solar")
        self.root.title('Student Management System')
        self.root.geometry("400x600")
        self.data = dataset()
        self.options()
        self.root.mainloop()




    # Main Menu GUI
    def options(self):
        self.clear()

        label = ttk.Label(self.root, text="Student Management System", font=('san serif', 18))
        label.pack(pady=(15))

        btn1 = ttk.Button(self.root, text='Accept Students Details', width=40, bootstyle=WARNING, command=self.accept_GUI)
        btn1.pack(pady=(15))

        btn2 = ttk.Button(self.root, text='Display Student Details', width=40, bootstyle=PRIMARY, command=self.display_all_student)
        btn2.pack(pady=(15))

        btn3 = ttk.Button(self.root, text='Search Details of a Student', width=40, bootstyle=DANGER, command=self.search_student_GUI)
        btn3.pack(pady=(15))

        btn4 = ttk.Button(self.root, text='Delete Details of Student', width=40, bootstyle=INFO, command=self.delete_GUI)
        btn4.pack(pady=(15))

        btn5 = ttk.Button(self.root, text='Update Student Details', width=40, bootstyle=SUCCESS, command=self.Update_GUI)
        btn5.pack(pady=(15))

        btn6 = ttk.Button(self.root, text='Exit', width=40, bootstyle=DEFAULT, command=self.exit1)
        btn6.pack(pady=(15))



    # Clear GUI
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()



    # Accept Student GUI
    def accept_GUI(self):
        self.clear()

        label = ttk.Label(self.root, text="Student Management System", font=('san serif', 18))
        label.pack(pady=(15))

        label1 = ttk.Label(self.root, text="Enter the name", bootstyle=SUCCESS)
        label1.pack(pady=(4))

        self.name_input = ttk.Entry(self.root, width=40)
        self.name_input.pack(pady=(5), ipady=(4))

        label2 = ttk.Label(self.root, text="Roll No.", bootstyle=SUCCESS)
        label2.pack(pady=(4))

        self.roll_no_input = ttk.Entry(self.root, width=40)
        self.roll_no_input.pack(pady=(5), ipady=(4))

        label3 = ttk.Label(self.root, text="Marks of Physics", bootstyle=SUCCESS)
        label3.pack(pady=(4))

        self.physics_marks_input = ttk.Entry(self.root, width=40)
        self.physics_marks_input.pack(pady=(5), ipady=(4))

        label4 = ttk.Label(self.root, text="Marks of Maths", bootstyle=SUCCESS)
        label4.pack(pady=(4))

        self.maths_marks_input = ttk.Entry(self.root, width=40)
        self.maths_marks_input.pack(pady=(5), ipady=(4))

        btn5 = ttk.Button(self.root, text='Add', width=40, bootstyle=WARNING, command=self.add_student)
        btn5.pack(pady=(15))

        btn6 = ttk.Button(self.root, text='Go Back', width=40, bootstyle=WARNING, command=self.options)
        btn6.pack(pady=(15))





    # Add Student
    def add_student(self):
        try:
            name = self.name_input.get()
            roll = int(self.roll_no_input.get())
            mark1 = int(self.physics_marks_input.get())
            mark2 = int(self.maths_marks_input.get())

            # Call the accept_student method
            response = self.data.accept_student(name, roll, mark1, mark2)

            if response == 0:
                messagebox.showerror('Error', 'Roll Number already exists')
            elif response == 'Roll number should be an integer':
                messagebox.showerror('Error', 'Roll Number should be an integer')
            elif response == 'Name should be a string':
                messagebox.showerror('Error', 'Name should be a string')
            elif response == 'Marks should be integers':
                messagebox.showerror('Error', 'Marks should be integers')
            else:
                messagebox.showinfo('Success', 'Entry successful')

        except ValueError:
            messagebox.showerror('Error', 'Please enter valid data')





    # Search Student GUI
    def search_student_GUI(self):
        self.clear()

        label = ttk.Label(self.root, text="Student Management System", font=('san serif', 18))
        label.pack(pady=(15))

        label2 = ttk.Label(self.root, text="Enter Roll No.", bootstyle=SUCCESS)
        label2.pack(pady=(4))

        self.roll_no_input = ttk.Entry(self.root, width=40)
        self.roll_no_input.pack(pady=(5), ipady=(4))

        self.search_result = ttk.Label(self.root, text="", bootstyle=SUCCESS)
        self.search_result.pack(pady=(4))

        btn7 = ttk.Button(self.root, text='See Detail', width=40, bootstyle=WARNING, command=self.search)
        btn7.pack(pady=(15))

        btn6 = ttk.Button(self.root, text='Go Back', width=40, bootstyle=WARNING, command=self.options)
        btn6.pack(pady=(15))





    # Search student method
    def search(self):
        roll_number = self.roll_no_input.get()
        response = self.data.search(roll_number)
        self.search_result.config(text=response)



    # Delete Student GUI
    def delete_GUI(self):
        self.clear()

        label = ttk.Label(self.root, text="Student Management System", font=('san serif', 18))
        label.pack(pady=(15))

        label2 = ttk.Label(self.root, text="Enter Roll No.", bootstyle=SUCCESS)
        label2.pack(pady=(4))

        self.roll_no_input = ttk.Entry(self.root, width=40)
        self.roll_no_input.pack(pady=(5), ipady=(4))

        self.search_result = ttk.Label(self.root, text="", bootstyle=SUCCESS)
        self.search_result.pack(pady=(4))

        btn7 = ttk.Button(self.root, text='Delete Student', width=40, bootstyle=WARNING, command=self.Delete)
        btn7.pack(pady=(15))

        btn6 = ttk.Button(self.root, text='Go Back', width=40, bootstyle=WARNING, command=self.options)
        btn6.pack(pady=(15))




    # Delete student method
    def Delete(self):
        roll_no = self.roll_no_input.get()
        response = self.data.Delete(roll_no)
        if response == 1:
            messagebox.showinfo('Success', 'Data Deleted Successfully')
        else:
            messagebox.showerror('Error', 'This Roll Number Does Not Exist')




    # Update Student GUI
    def Update_GUI(self):
        self.clear()

        label = ttk.Label(self.root, text="Student Management System", font=('san serif', 18))
        label.pack(pady=(15))

        label5 = ttk.Label(self.root, text="Enter Roll No.", bootstyle=SUCCESS)
        label5.pack(pady=(4))

        self.roll1_no_input = ttk.Entry(self.root, width=40)
        self.roll1_no_input.pack(pady=(5), ipady=(4))

        self.search_result = ttk.Label(self.root, text="", bootstyle=SUCCESS)
        self.search_result.pack(pady=(4))

        btn7 = ttk.Button(self.root, text='See Detail', width=40, bootstyle=WARNING, command=self.search2)
        btn7.pack(pady=(15))

        btn6 = ttk.Button(self.root, text='Go Back', width=40, bootstyle=WARNING, command=self.options)
        btn6.pack(pady=(15))




    # Search for update
    def search2(self):
        roll_number = self.roll1_no_input.get()
        response = self.data.search(roll_number)
        self.search_result.config(text=response)
        self.upt()



    # Update student
    def upt(self):
        label1 = ttk.Label(self.root, text="Enter the name", bootstyle=SUCCESS)
        label1.pack(pady=(4))

        self.name_input = ttk.Entry(self.root, width=40)
        self.name_input.pack(pady=(5), ipady=(4))

        label3 = ttk.Label(self.root, text="Marks of Physics", bootstyle=SUCCESS)
        label3.pack(pady=(4))

        self.physics_marks_input = ttk.Entry(self.root, width=40)
        self.physics_marks_input.pack(pady=(5), ipady=(4))

        label4 = ttk.Label(self.root, text="Marks of Maths", bootstyle=SUCCESS)
        label4.pack(pady=(4))

        self.maths_marks_input = ttk.Entry(self.root, width=40)
        self.maths_marks_input.pack(pady=(5), ipady=(4))




        # Update button
        btn5 = ttk.Button(self.root, text='Update', width=40, bootstyle=WARNING, command=self.update_student)
        btn5.pack(pady=(15))

    def update_student(self):
        roll_number = self.roll1_no_input.get()
        name = self.name_input.get()
        mark1 = self.physics_marks_input.get()
        mark2 = self.maths_marks_input.get()

        # Perform the update operation
        response = self.data.update_student(roll_number, name, mark1, mark2)
        if response == 1:
            messagebox.showinfo('Success', 'Update Successful')
        else:
            messagebox.showerror('Error', 'This Roll Number Does Not Exist')

    def display_all_student(self):
        self.clear()




        # Add a label for the title
        label = ttk.Label(self.root, text="Student Management System", font=('san serif', 18))
        label.pack(pady=(15))

        # Create a Treeview widget
        columns = ("Roll No", "Name", "Physics Marks", "Maths Marks")
        tree = ttk.Treeview(self.root, columns=columns, show='headings', bootstyle=SUCCESS)




        # Define column headings and column properties
        tree.heading("Roll No", text="Roll No")
        tree.heading("Name", text="Name")
        tree.heading("Physics Marks", text="Physics Marks")
        tree.heading("Maths Marks", text="Maths Marks")

        tree.column("Roll No", anchor=CENTER, width=100)
        tree.column("Name", anchor=CENTER, width=150)
        tree.column("Physics Marks", anchor=CENTER, width=100)
        tree.column("Maths Marks", anchor=CENTER, width=100)

        tree.pack(pady=(5))




        # Fetch and debug data
        all_data = self.data.get_all_students()
        # print(all_data)  # Debugging: Check the structure of all_data

        # Insert student data into the table
        if all_data:
            for roll_no, student_data in all_data.items():
                tree.insert("", "end", values=(
                    student_data['roll'],  # Roll No
                    student_data['name'],  # Name
                    student_data['Physics'],  # Physics Marks
                    student_data['Maths']  # Maths Marks
                ))
        else:
            print("No data found")

        # Go back button
        btn6 = ttk.Button(self.root, text='Go Back', width=40, bootstyle=WARNING, command=self.options)
        btn6.pack(pady=(15))


    # Exit
    def exit1(self):
        self.root.destroy()

# Initialize the app
std = Student()
