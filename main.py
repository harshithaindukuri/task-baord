from file_manager import *
from properties import *
from tkinter import *


class AppGui(Tk):

    def __init__(self):
        super().__init__()
        self.title("TASK BOARD")
        self.geometry("1200x800")
        self.config(bg="#FFECD6", padx=50, pady=50)
        load_files()
        add_button = Button(text="ADD TASK", font=(MAIN_FONT, 15, "bold"), width=20, bg="#006769", fg="white",
                            borderwidth=4)

        add_button.grid(row=0, column=0)
        obj = Label(self, text="TASK DETAILS", font=(MAIN_FONT, 20, "bold"), bg="#FFECD6", fg="#153448")
        obj.grid(row=0, column=2, columnspan=2)
        self.buttons_frame = Frame(self, width=40, height=500, padx=10, pady=10)
        self.buttons_frame.grid(row=2, column=0, rowspan=10)
        obj = Label(self, text="Name:", font=(MAIN_FONT, 15, "bold"), bg="#FFECD6")
        obj.grid(row=1, column=1)
        self.data_task_head = Entry(self, font=(MAIN_FONT, 15), width=40)
        self.data_task_head.grid(row=1, column=2, columnspan=2)
        obj = Label(self, text="Description:", font=(MAIN_FONT, 15, "bold"), bg="#FFECD6")
        obj.grid(row=2, column=1)
        self.data_task_desc = Text(self, font=(MAIN_FONT, 15), height=3, width=40)
        self.data_task_desc.grid(row=2, column=2, columnspan=2)
        obj = Label(self, text="No/Status:", font=(MAIN_FONT, 15, "bold"), bg="#FFECD6")
        obj.grid(row=3, column=1)
        self.data_task_id = StringVar()
        self.data_task_id.set("1")
        drop = OptionMenu(self, self.data_task_id, ["1", "2"])
        drop.config(font=(MAIN_FONT, 15), width=16, bg="#3C5B6F", fg="white")
        drop.grid(row=3, column=2)
        self.data_task_status = StringVar()
        self.data_task_status.set("None")
        drop = OptionMenu(self, self.data_task_status, *STATUS_CODES)
        drop.config(font=(MAIN_FONT, 15), width=16, bg="#3C5B6F", fg="white")
        drop.grid(row=3, column=3)
        obj = Label(self, text="Deadline:", font=(MAIN_FONT, 15, "bold"), bg="#FFECD6")
        obj.grid(row=4, column=1)
        self.data_task_deadline = Entry(self, font=(MAIN_FONT, 15), width=40)
        self.data_task_deadline.insert(0, "MM/DD/YYYY")
        self.data_task_deadline.grid(row=4, column=2, columnspan=2)
        obj = Label(self, text="Next steps:", font=(MAIN_FONT, 15, "bold"), bg="#FFECD6")
        obj.grid(row=5, column=1)
        self.data_task_nextsteps = Text(self, font=(MAIN_FONT, 15), height=3, width=40)
        self.data_task_nextsteps.grid(row=5, column=2, columnspan=2)
        obj = Button(self, text="Save", font=(MAIN_FONT, 15, "bold"), width=18, bg="#006769", fg="white",
                     command=self.save_action)
        obj.grid(row=6, column=2)
        obj = Button(self, text="Delete", font=(MAIN_FONT, 15, "bold"), width=18, bg="#006769", fg="white",
                     command=self.delete_action)
        obj.grid(row=6, column=3)
        obj = Button(self.buttons_frame, text="buttons", font=(MAIN_FONT, 15), width=15, bg="#CDE8E5")
        obj.pack()
        obj = Button(self.buttons_frame, text="buttons", font=(MAIN_FONT, 15), width=15, bg="#CDE8E5")
        obj.pack()
        obj = Button(self.buttons_frame, text="buttons", font=(MAIN_FONT, 15), width=15, bg="#CDE8E5")
        obj.pack()
        obj = Button(self.buttons_frame, text="buttons", font=(MAIN_FONT, 15), width=15, bg="#CDE8E5")
        obj.pack()
        obj = Button(self.buttons_frame, text="buttons", font=(MAIN_FONT, 15), width=15, bg="#CDE8E5")
        obj.pack()

    def delete_action(self):
        pass

    def save_action(self):
        name = self.data_task_head.get()
        name.replace(' ', '')
        data_dict1 = {
            "task_id": 0,
            "task_name": self.data_task_head.get(),
            "task_description": self.data_task_desc.get("1.0", END).replace('\n', ''),
            "task_active": "Active",
            "child_count": 0}
        data_dict2 = {
            "task_action_id": 0,
            "task_parent_id": 0,
            "task_action_name": self.data_task_nextsteps.get("1.0", END).replace('\n', ''),
            "task_deadline": self.data_task_deadline.get(),
            "task_reminder": True,
            "task_status": self.data_task_status.get()}

        save_data(data_dict1, data_dict2)


obj = AppGui()
obj.mainloop()
