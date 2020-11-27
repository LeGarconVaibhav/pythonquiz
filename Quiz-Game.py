from tkinter import *

import json
import random

root = Tk()
root.geometry("660x320")
root.resizable(False, False)
var = StringVar()
chk = random.randint(0, 4)
count = 0
total = 1

with open("content.json") as jsonFile:
    data = json.load(jsonFile)


def json_convert():
    lst = list()
    for i in data["question_pack1"]:
        lst.append(i)
    return lst


def json_fetch():
    global chk, count
    lst = json_convert()
    dic = lst[chk]
    lst1 = list()
    lst1.append(dic["question"])
    for j in(dic["options"]):
        lst1.append(j)
    lst1.append(dic["answer"])
    chk += 2
    count += 1
    return lst1


def first_page():
    root.title("Python Quiz Game - Welcome Page")
    Label(text="WELCOME TO\nPYTHON QUIZ GAME", bg="black", fg="white", width="150", height="35",
          font=("Albertus", 32)).pack()
    outer_menu()


def help_window():
    root.title("Python Quiz Game - Help")
    global chk, count
    count = 0
    chk = random.randint(0, 4)
    for widget in root.winfo_children():
        widget.destroy()
    outer_menu()
    txt = "This is a simple Python Quiz Game.\nAt a time you can attempt 15 question in  one go.\n" \
          "After every correct attempt you will be redirected to a new question window." \
          "\nIf attempted wrong, you will be out of the game.\nAttempt wisely.\nHappy Learning :)"
    Label(root, text=txt, justify=CENTER, padx=10, bg="black", fg="white", width="150", height="35",
          font=("Times New Roman", 14)).pack(expand=TRUE)


def outer_menu():
    menu = Menu(root)
    file = Menu(menu, tearoff=0)
    file.add_command(label="Game", command=question_window)
    file.add_command(label="Help", command=help_window)
    file.add_command(label="Exit", command=root.quit)
    menu.add_cascade(label="File", menu=file)
    root.config(menu=menu)


def question_window():
    for widget in root.winfo_children():
        widget.destroy()
    global count

    def menu_bar():
        menubar = Menu(root)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="Help", command=help_window)
        file.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file)
        root.config(menu=menubar)
    root.title("Python Quiz Game - Game")
    lst = json_fetch()

    def next_que():
        lst1 = json_fetch()
        radio_button(lst1)

    def on_wrong():
        root.title("Python Quiz Game - Thanking Page")
        for widget in root.winfo_children():
            widget.destroy()
        total = count - 1
        str2 = "Thanks for being a part of the game.\nYour score is "+str(total)+"!!"
        label = Label(text=str2, bg="black", fg="white", width="150", height="35", font=("Times New Roman", 15)).pack()
        button = Button(label, text="Exit", command=root.quit)
        button.place(x=300, y=185)

    def final_window():
        root.title("Python Quiz Game - BullsEye!!")
        for widget in root.winfo_children():
            widget.destroy()
        label = Label(root, text="BullsEye!!\nYou attempted\nall questions correctly!!", justify=CENTER, padx=10, bg="black", fg="white", width="150", height="35",
              font=("Buckingham", 24)).pack(expand=TRUE)
        button = Button(label, text="Exit", command=root.quit)
        button.place(x=300, y=225)

    def radio_button(lst):

        str1 = "Question " + str(count) + " of 15"
        for widget in root.winfo_children():
            widget.destroy()
        menu_bar()
        label_frame = LabelFrame(root, text=str1)
        label_frame.pack(expand='yes', fill='both')

        def check():
            global total
            if str(var.get()) == lst[5]:
                if total != 15:
                    button = Button(label_frame, text="Next", command=next_que)
                    button.place(x=20, y=210)
                else:
                    button = Button(label_frame, text="Next", command=final_window)
                    button.place(x=20, y=210)
                total += 1

            else:
                button = Button(label_frame, text="Next", command=on_wrong)
                button.place(x=20, y=210)

        question = Label(label_frame, text=lst[0])
        question.place(x=16, y=35)

        option1 = Radiobutton(label_frame, text=lst[1], variable=var, tristatevalue="x", value=lst[1], command=check)
        option1.place(x=20, y=70)
        option1.deselect()

        option2 = Radiobutton(label_frame, text=lst[2], variable=var, tristatevalue="x", value=lst[2], command=check)
        option2.place(x=20, y=105)
        option2.deselect()

        option3 = Radiobutton(label_frame, text=lst[3], variable=var, tristatevalue="x", value=lst[3], command=check)
        option3.place(x=20, y=140)
        option3.deselect()

        option4 = Radiobutton(label_frame, text=lst[4], variable=var, tristatevalue="x", value=lst[4], command=check)
        option4.place(x=20, y=175)
        option4.deselect()
    radio_button(lst)


first_page()

mainloop()
