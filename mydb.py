import json

class dataset:

    #Accepting student method
    def accept_student(self, name, roll, mark1, mark2):
        db_path = '/home/ghost/Python DS/Student managment system/db.json'
        with open(db_path, 'r') as rf:
           database = json.load(rf)
           

            # Convert roll number to string for consistency (both in storage and validation)
        roll_str = str(roll)

        # Check if roll number already exists
        if roll_str in database:
            return 0
        # Type validation
        elif not isinstance(roll, int):
            return 'Roll number should be an integer'
        elif not isinstance(name, str):
            return 'Name should be a string'
        elif not isinstance(mark1, int) or not isinstance(mark2, int):
            return 'Marks should be integers'
        else:
            # Add the student details to the database
            database[roll_str] = {'name': name, 'roll': roll_str, 'Physics': mark1, 'Maths': mark2}
            with open(db_path, 'w') as wf:
                json.dump(database, wf, indent=4)

        return 1
    

    def search(self, roll):
        db_path = '/home/ghost/Python DS/Student managment system/db.json'
        
        # Open and load the database
        with open(db_path, 'r') as rf:
            database = json.load(rf)
        
        # Check if the roll exists in the database
        if roll not in database:
            return "Student not found"
        
        final = ''

        # Concatenate details of the student
        for key, value in database[roll].items():
            final += f"{key} -> {value}\n"  # Using f-string to format the output

        return final


    def Delete(self,roll):
        db_path = '/home/ghost/Python DS/Student managment system/db.json'

        with open(db_path, 'r') as rf:
            database = json.load(rf)
        
        # Check if the roll exists in the database
        if roll in database:
            del database[roll]


                # Write the updated database back to the file
            with open(db_path, 'w') as wf:
                json.dump(database, wf, indent=4)  # indent for better readability
        
            return 1
        else:
            return 0
        

    def update(self, roll, name, mark1, mark2):
        db_path = '/home/ghost/Python DS/Student managment system/db.json'

        with open(db_path, 'r') as rf:
            database = json.load(rf)

        # Check if the roll exists in the database
        if roll in database:
            # Update only the fields that have values provided (non-empty)
            if name:
                database[roll]['name'] = name
            if mark1:
                database[roll]['Physics'] = mark1
            if mark2:
                database[roll]['Maths'] = mark2    

            # Save the updated data back to the JSON file
            with open(db_path, 'w') as wf:
                json.dump(database, wf, indent=4)

            return 1
        else:
            return 0
        

    def get_all_students(self):
        db_path = '/home/ghost/Python DS/Student managment system/db.json'

        with open(db_path, 'r') as rf:
            database = json.load(rf)

        return database

        