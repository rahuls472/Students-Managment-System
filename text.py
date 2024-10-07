import ttkbootstrap as tk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from mydb import dataset
import json

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#72BF78")
        self.data = dataset()  # Assuming dataset() is imported from mydb.py

    def clear(self):
        # Clears all widgets from the window
        for widget in self.root.pack_slaves():
            widget.destroy()

    def display_all_student(self):
        self.clear()

        # Fetch the student data from another file (e.g., `mydb.py`)
        student_data = self.data.get_all_students()
        print(f"Debug - Student data: {student_data}")  # For debugging, check the data structure

        if not student_data:
            print("No student data found!")  # Debug message
            return

        # Create a table with ttkbootstrap Tableview
        headers = ["Roll Number", "Name", "Physics", "Maths"]
        table = Tableview(
            master=self.root,
            coldata=headers,
            paginated=True,      # Pagination enabled for large datasets
            rowsperpage=5,        # Show 5 rows per page
            bootstyle=PRIMARY     # Styling for the table
        )

        # Insert student data into the table
        for roll, data in student_data.items():
            try:
                table.insert_row([roll, data["name"], data["Physics"], data["Maths"]])
            except KeyError as e:
                print(f"Error - Missing key in data: {e}")  # Debug message

        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # Back button to return to the main menu
        back_button = tk.Button(
            master=self.root,
            text="Back",
            bootstyle=SUCCESS,
            command=self.options   # Return to the main menu
        )
        back_button.pack(pady=10)



# Tkinter Window Initialization
root = tk.Window(themename="journal")
app = Student(root)
root.mainloop()
