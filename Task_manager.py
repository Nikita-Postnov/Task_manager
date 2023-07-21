import tkinter as tk
from tkinter import simpledialog


class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date


class TaskPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Планировщик задач")
        self.tasks = []

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        add_button = tk.Button(root, text="Добавить задачу", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=10)

        remove_button = tk.Button(root, text="Удалить задачу", command=self.remove_task)
        remove_button.pack(side=tk.LEFT, padx=10)

        edit_button = tk.Button(root, text="Редактировать задачу", command=self.edit_task)
        edit_button.pack(side=tk.LEFT, padx=10)

        self.load_tasks()

    def add_task(self):
        title = simpledialog.askstring("Добавить задачу", "Введите название задачи:")
        if title:
            due_date = simpledialog.askstring("Добавить задачу", "Введите срок выполнения задачи:")
            task = Task(title, due_date)
            self.tasks.append(task)
            self.update_listbox()
            self.save_tasks()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_listbox()
            self.save_tasks()

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks[task_index]
            title = simpledialog.askstring("Редактировать задачу", "Введите новое название задачи:",
                                           initialvalue=task.title)
            if title:
                due_date = simpledialog.askstring("Редактировать задачу", "Введите новый срок выполнения задачи:",
                                                  initialvalue=task.due_date)
                task.title = title
                task.due_date = due_date
                self.update_listbox()
                self.save_tasks()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task.title} - {task.due_date}")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    title, due_date = line.strip().split(",")
                    task = Task(title, due_date)
                    self.tasks.append(task)
            self.update_listbox()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.due_date}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskPlanner(root)
    root.mainloop()
