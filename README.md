
# 📘 CSV Writer - Student Management App

A simple Python GUI application to manage student data using [customtkinter](https://github.com/TomSchimansky/CustomTkinter) and `pandas`.  
This app allows you to add, view, and search students, storing their data in a CSV file.


---

## 🚀 Features

- ✅ Add student with name and scores
- 📂 Automatically writes to `students.csv`
- 📋 View all student records in a clean text/table format
- 🔍 Search students by name with GPA calculation
- 💾 Simple CSV-based data persistence
- 🧩 Built using `customtkinter` and `pandas`

---

## 📸 Screenshots

![Screenshot 2025-07-07 132247](https://github.com/user-attachments/assets/5f57304c-5039-402b-baab-db2ed4e3994f)

---

## 🛠️ Installation

Make sure Python is installed, then install required packages:

```bash
pip install customtkinter pandas
```

---

## ▶️ How to Run

```bash
python main.py
```

After running, you will see a tab-based GUI interface with the following sections:

- **Add Student**: Fill in student details and click "Add"
- **List Students**: View all students from the CSV file
- **Search Student**: Enter a name to search and view their scores and GPA

---

## 📁 File Structure

```
CSV-Writer/
│
├── students.csv       # Automatically created when adding data
├── main.py            # Main application file
└── README.md          # Project documentation
```

---

## ✍️ How to Contribute

1. Fork the repository
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add a new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💡 Credits

Made with ❤️ using Python and CustomTkinter  
Author: [@Rexlep](https://github.com/Rexlep)
