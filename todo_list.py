import tkinter as tk
from tkinter import simpledialog, messagebox

class InputBox(tk.Toplevel):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")  # Light background

        self.task_var = tk.StringVar()
        self.due_date_var = tk.StringVar()
        
        label_task = tk.Label(self, text="Enter task:", font=("Helvetica", 14), bg="#f0f0f0")
        label_task.pack(padx=20, pady=5)

        entry_task = tk.Entry(self, textvariable=self.task_var, font=("Helvetica", 14), width=30)
        entry_task.pack(padx=20, pady=5)

        label_due_date = tk.Label(self, text="Due Date:", font=("Helvetica", 14), bg="#f0f0f0")
        label_due_date.pack(padx=20, pady=5)

        entry_due_date = tk.Entry(self, textvariable=self.due_date_var, font=("Helvetica", 14), width=30)
        entry_due_date.pack(padx=20, pady=5)

        confirm_button = tk.Button(self, text="Add Task", command=self.confirm, font=("Helvetica", 14), bg="#4CAF50", fg="white")
        confirm_button.pack(padx=20, pady=10)

    def confirm(self):
        task = self.task_var.get()
        due_date = self.due_date_var.get()
        if task:
            task_info = {"task": task, "due_date": due_date, "completed": False}
            self.result = task_info
            self.destroy()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

class TODO:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x400")
        self.root.configure(bg="#e3f2fd")  # Light blue background

        # Add heading label
        heading_label = tk.Label(root, text="To-Do List", font=("Comic Sans MS", 30, "italic"), bg="#e3f2fd")
        heading_label.pack(pady=10)

        self.tasks = []
        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=80, font=("Helvetica", 12), bg="#ffffff")
        self.task_list.pack(padx=10, pady=10)

        button_frame = tk.Frame(root, bg="#e3f2fd")
        button_frame.pack(pady=10)

        button_font = ("Helvetica", 12)

        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, font=button_font, width=15, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, font=button_font, width=15, bg="#2196F3", fg="white")
        self.edit_button.grid(row=0, column=1, padx=5)

        self.remove_button = tk.Button(button_frame, text="Remove Task", command=self.remove_task, font=button_font, width=15, bg="#f44336", fg="white")
        self.remove_button.grid(row=0, column=2, padx=5)

        self.mark_done_button = tk.Button(button_frame, text="Mark as Done", command=self.mark_done, font=button_font, width=15, bg="#FF9800", fg="white")
        self.mark_done_button.grid(row=0, column=3, padx=5)

        self.clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_tasks, font=button_font, width=15, bg="#9E9E9E", fg="white")
        self.clear_button.grid(row=0, column=4, padx=5)

    def add_task(self):
        dialog = InputBox(self.root, "Add Task")
        self.root.wait_window(dialog)
        task_info = dialog.result
        if task_info:
            self.tasks.append(task_info)
            self.update_task_list()

    def edit_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            dialog = InputBox(self.root, "Edit Task")
            task_info = self.tasks[selected_task_index]
            dialog.task_var.set(task_info["task"])
            dialog.due_date_var.set(task_info["due_date"])
            self.root.wait_window(dialog)
            updated_task_info = dialog.result
            if updated_task_info:
                self.tasks[selected_task_index] = updated_task_info
                self.update_task_list()

    def remove_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            del self.tasks[selected_task_index]
            self.update_task_list()

    def mark_done(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            task_info = self.tasks[selected_task_index]
            task_info["completed"] = True
            self.update_task_list()

    def clear_tasks(self):
        self.tasks = []
        self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task_info in self.tasks:
            task = task_info["task"]
            due_date = task_info["due_date"]
            completed = task_info["completed"]
            status = "✓" if completed else ""
            self.task_list.insert(tk.END, f"{status} Task: {task} | Due Date: {due_date}")

def main():
    root = tk.Tk()
    app = TODO(root)
    root.mainloop()

if __name__ == "__main__":
    main()
