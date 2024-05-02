import tkinter as tk
from tkinter import ttk

class TaskListApp:
    def __init__(self, master):
        self.master = master
        master.title('Task List')

        self.label = tk.Label(master, text='Gestionnaire de tâches', font=('Helvetica', 18))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.entry_label = tk.Label(master, text="Tâche :")
        self.entry_label.grid(row=1, column=0, sticky="e")

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=1, column=1, padx=5)

        self.add_button = tk.Button(master, text="Ajouter", command=self.add_task)
        self.add_button.grid(row=1, column=2, padx=5)

        self.task_list_label = tk.Label(master, text='Liste des tâches :', font=('Helvetica', 14))
        self.task_list_label.grid(row=2, column=0, columnspan=3, pady=5)

        self.task_list = tk.Listbox(master, width=50, height=10)
        self.task_list.grid(row=3, column=0, columnspan=3, padx=5)

        self.delete_button = tk.Button(master, text="Supprimer", command=self.del_task)
        self.delete_button.grid(row=4, column=0, pady=5)

        self.quit_button = tk.Button(master, text='Quitter', command=master.quit)
        self.quit_button.grid(row=4, column=1, pady=5)
      
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def del_task(self):
        selection = self.task_list.curselection()
        if selection:
            self.task_list.delete(selection)


root = tk.Tk()
app = TaskListApp(root)
root.mainloop()
