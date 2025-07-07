import customtkinter as ctk
import csv
import pandas as pd
from mb.CTkMessagebox import CTkMessagebox


def search_student():
    """
    This function help you to search for students you want
    """
    name_to_search = search_entry.get().strip()

    if name_to_search == "":
        search_result.delete("0.0", "end")
        search_result.insert("0.0", "Please enter a name to search.")
        return

    try:
        students = pd.read_csv('students.csv')
    except FileNotFoundError:
        search_result.delete("0.0", "end")
        search_result.insert("0.0", "Students file not found.")
        return

    result = students[students['Name'].str.lower() == name_to_search.lower()]

    search_result.delete("0.0", "end")

    if not result.empty:
        for i, row in result.iterrows():
            gpa = (int(row['Physics_score']) + int(row['Math_score'])) / 2
            output = f"Name: {row['Name']}\nLast name: {row['Last_name']}\nPhysics: {row['Physics_score']}\nMath: {row['Math_score']}\nGPA: {gpa:.2f}"
            search_result.insert("0.0", output)
    else:
        search_result.insert("0.0", "Student not found.")


def write_in_file():
    """
    This function writes data into csv file
    Name, Physics score, Math score
    """
    name = name_entry.get()
    last_name = last_name_entry.get()
    physics_score = physics_entry.get()
    math_score = math_entry.get()
    new_row = [name.capitalize(), last_name.capitalize(), physics_score.capitalize(), math_score.capitalize()]

    df = pd.read_csv('students.csv')
    name_column = df['Name'].str.lower()
    last_name_column = df['Last_name'].str.lower()

    if name in list(name_column) and last_name in list(last_name_column):
        CTkMessagebox(title="Error", message="This student is already registered", icon="cancel", sound=True)
        return
    if name == '':
        CTkMessagebox(title="Error", message="Please enter a name", icon="cancel", sound=True)
        return
    if last_name == '':
        CTkMessagebox(title="Error", message="Please enter a last name", icon="cancel", sound=True)
        return
    if physics_score == '':
        CTkMessagebox(title="Error", message="Please enter your physics score", icon="cancel", sound=True)
        return
    if math_score == '':
        CTkMessagebox(title="Error", message="Please enter your math score", icon="cancel", sound=True)
        return

    if int(physics_score) > 20:
        CTkMessagebox(title="Error", message="The physics number should be 20 or under", icon="cancel", sound=True)
        return
    if int(math_score) > 20:
        CTkMessagebox(title="Error", message="The math number should be 20 or under", icon="cancel", sound=True)
        return

    name_entry.delete(0, ctk.END), last_name_entry.delete(0, ctk.END), physics_entry.delete(0, ctk.END), math_entry.delete(0, ctk.END)
    with open('students.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)

    show_students()


def show_students():
    """
    This function add the students to the interface
    """
    students = pd.read_csv('students.csv')
    students['gpa'] = (students['Physics_score'] + students['Math_score']) / 2
    students['Graduation year'] = '2025'
    student_listbox.delete("0.0", "end")  # delete all text
    student_listbox.insert('0.0', students.to_string(index=False))


app = ctk.CTk()
app.title("Students Data Management")
app.geometry("700x500")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

tab_view = ctk.CTkTabview(master=app)
tab_view.pack(padx=20, pady=20, fill="both", expand=True)

# Making the tabs
add_tab = tab_view.add("➕ Add Student")
list_tab = tab_view.add("📋 List Students")
search_tab = tab_view.add("🔍 Search Student")


# -------------------------- Add Tab --------------------------


ctk.CTkLabel(add_tab, text="Add New Student", font=("Arial", 20, "bold")).pack(pady=(20, 10))

add_form = ctk.CTkFrame(add_tab)
add_form.pack(pady=10)

name_entry = ctk.CTkEntry(add_form, placeholder_text="Name", width=300)
name_entry.pack(pady=10)

last_name_entry = ctk.CTkEntry(add_form, placeholder_text="Last name", width=300)
last_name_entry.pack(pady=10)

physics_entry = ctk.CTkEntry(add_form, placeholder_text="Physics Score", width=300)
physics_entry.pack(pady=10)

math_entry = ctk.CTkEntry(add_form, placeholder_text="Math Score", width=300)
math_entry.pack(pady=10)

ctk.CTkButton(add_form, text="Add Student", command=write_in_file).pack(pady=20)


# -------------------------- List Tab --------------------------


ctk.CTkLabel(list_tab, text="All Students", font=("Arial", 20, "bold")).pack(pady=(20, 10))

ctk.CTkButton(list_tab, text="Refresh").pack(pady=20)

list_frame = ctk.CTkFrame(list_tab)
list_frame.pack(pady=10, fill="both", expand=True)

student_listbox = ctk.CTkTextbox(list_frame, width=600, height=400, font=("Courier New", 14))
student_listbox.pack(padx=10, pady=10)
student_listbox.insert("0.0", "Student list will appear here...")

show_students()

# -------------------------- Search Tab --------------------------


ctk.CTkLabel(search_tab, text="Search Student", font=("Arial", 20, "bold")).pack(pady=(20, 10))

search_frame = ctk.CTkFrame(search_tab)
search_frame.pack(pady=10)

search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter student name", width=300)
search_entry.pack(pady=10)

ctk.CTkButton(search_frame, text="Search", command=search_student).pack(pady=10)

search_result = ctk.CTkTextbox(search_frame, width=600, height=300)
search_result.pack(pady=20)
search_result.insert("0.0", "Search result will appear here...")

app.mainloop()
