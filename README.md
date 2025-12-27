# 📝 To-Do List Application

> A simple, elegant command-line interface (CLI) application for managing your daily tasks

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 About

This To-Do List application is a lightweight CLI tool that helps you organize and track your tasks efficiently. Built with Python, it features an intuitive menu-driven interface with color-coded task status indicators for enhanced user experience.

**Project Type:** Coding Temple Computer Software Engineering Course - Mini Project

---

## ✨ Features

- ✅ **Add Tasks** - Quickly add new tasks to your list
- 👀 **View Tasks** - Display all tasks with color-coded status (🔴 Incomplete | 🟢 Complete)
- ✔️ **Mark Complete** - Update task status when completed
- 🗑️ **Delete Tasks** - Remove tasks from your list
- 🚫 **Duplicate Prevention** - Automatic detection of duplicate tasks
- 🛡️ **Error Handling** - Robust input validation and error management

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Terminal/Command Prompt access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CT_Mini_Project_To_Do_List.git
```

2. Navigate to the project directory:
```bash
cd CT_Mini_Project_To_Do_List
```

3. Run the application:
```bash
python Todo_List_App.py
```

---

## 💻 Usage

Upon launching the application, you'll be greeted with a welcome message and a main menu with the following options:

### Main Menu Options

| Option | Feature | Description |
|--------|---------|-------------|
| **1** | Add a task | Create a new task (default status: incomplete) |
| **2** | View tasks | Display all tasks with color-coded completion status |
| **3** | Mark complete | Change a task's status to complete |
| **4** | Delete a task | Permanently remove a task from the list |
| **5** | Quit | Exit the application |

### Color Coding

- 🔴 **Red text** = Incomplete task
- 🟢 **Green text** = Completed task

### Example Workflow

```
Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit

Please input the number for the feature you'd like to use: 1
What is the task you'd like to add to the Todo List? Buy groceries
New task: 'Buy groceries' added to the To Do List
```

---

## 🏗️ Technical Details

### Data Structure

Tasks are stored as tuples within a Python list:
```python
[(task_name: str, completion_status: bool), ...]
```

### Error Handling

The application implements comprehensive error handling using:
- `try/except/else/finally` blocks
- Input validation for all user interactions
- Graceful error messages for invalid inputs
- Empty list detection before operations

---

## 🤝 Contributing

This is a educational project, but suggestions and feedback are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Matthew Arney**
- GitHub: [@MArney86](https://github.com/MArney86)
- Project: [CT_Mini_Project_To_Do_List](https://github.com/MArney86/CT_Mini_Project_To_Do_List)

---

## 🙏 Acknowledgments

- Coding Temple Computer Software Engineering Course
- Python Software Foundation

---

*Built with ❤️ using Python*