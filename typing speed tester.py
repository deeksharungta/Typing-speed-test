from tkinter import *
import random

counter = 0
running = False
keypressed = 0

instruction = (
            "1. Welcome to Typing master\n"
            "2.This is an app to test your typing speed\n"
            "3. It is recommended that you should not correct the words after pressing space\n")



root = Tk()

with open("typing_story.txt", "r") as file:
    allText = file.read()
    para = list(map(str, allText.split('\n')))


def key(event):
    global keypressed
    keypressed += 1
    if keypressed == 1:
        global running
        running = True
        counter_label(lbl)

def restarting(events):
    """function to restart the typing master"""

    print("Restarting...")
    input_text.delete("1.0", "end")

    global counter
    counter = 0
    if running == False:
        lbl['text'] = '00'
    else:
        lbl['text'] = ''


def exiting(events):
        """function to exit the typing master"""
        print("Exiting...")
        quit()

def custom_dialog_box():
        """function to print time"""
        base = Toplevel(root)
        base.geometry("600x400+400+200")
        base.title("instruction")

        dialog_f = Frame(base)
        dialog_m = Message(dialog_f, text=instruction, bg="#9575CD", fg="floralwhite", font="calibri 15 bold", width='580')
        dialog_f.pack()
        dialog_m.pack(side=LEFT)
        btn = Button(base, text="press space", width=50, font="calibri 15 bold", command=exit)
        btn.pack(side=BOTTOM, padx=20, pady=20)

def counter_label(lbl):
    def count():
        global running
        if running:
            global counter
            if counter == 0:
                display = "0"
            else:
                display = str(counter)
            if counter < 10:
                lbl['text'] = '0' + display
            else:
                lbl['text'] = display

            lbl.after(1000, count)
            counter += 1

            if counter == 120:
                running = False

    count()

def check(written, words_text):
    count = 0
    for i in range(len(written)):
        if written[i] == words_text[i]:
            count += 1
    acc = (count * 100) // len(written)
    return acc


def check_input(write, words_text):
    written = write.get("1.0", "end-1c")
    written = written.split()
    wpm = len(written)
    accuracy = 0
    if wpm != 0:
        accuracy = check(written, words_text)
    lbl_acc = Label(can_widget, text=accuracy, font="comicsans 15 bold")
    lbl_acc.place(x=50, y=250)

# setting the tkinter window
root.geometry("1000x600+300+100")

root.title("Typing tester")
root.resizable(0, 0)

# the heading or name of the the application
l1 = Label(root, text="Typing Speed Tester", font="comicsans 15 bold")
l1.place(x=450, y=10)

# message or paragraph
f1 = Frame(root, bg="red", borderwidth=3)
story = random.choice(para)
m1 = Message(f1, text=story, fg="black", font="calibri 15 bold", width='540')
f1.place(x=50, y=45)
m1.pack()

# text area to type
f2 = Frame(root, bg="red", borderwidth=4, relief=SUNKEN)
f2.place(x=50, y=330)
input_text = Text(f2, width=54, height=10, font="calibri 15 bold", wrap="word")
input_text.pack()

# initializing canvas
can_widget = Canvas(root, width=300, height=500, bg="white")
can_widget.place(x=650, y=55)

# oval for words per min
can_widget.create_rectangle(95, 150, 155, 180, outline="black", width=2)
can_widget.create_text(175, 165, text="wpm", font="calibri 12 bold")

# oval for accuracy
can_widget.create_rectangle(40, 250, 100, 280, outline="black", width=2)
can_widget.create_text(70, 293, text="Accuracy", font="calibri 12 bold")

# oval for time
can_widget.create_rectangle(170, 250, 230, 283, outline="black", width=2)
can_widget.create_text(193, 293, text="Time", font="calibri 12 bold")

# restart icon
restart_img = PhotoImage(file="images/restart-icon.png")
restart = Label(can_widget, image=restart_img)
restart.place(x=30, y=370)
restart.bind('<Button-1>', restarting)

can_widget.create_text(50, 430, text="restart", font="calibri 12 bold")

# delete icon
delete_img = PhotoImage(file="images/Delete-icon.png")
delete = Label(can_widget, image=delete_img)
delete.place(x=170, y=370)
delete.bind('<Button-1>', exiting)

can_widget.create_text(200, 430, text="exit", font="calibri 12 bold")

lbl = Label(
    can_widget,
    text="00",
    fg="black",
    font="Verdana 15 bold"
)
input_text.bind('<Key>', key)

lbl.place(x=175, y=251)
print(running)
words_text = story.split()

check_input(input_text, words_text)

root.after(10, custom_dialog_box)
root.mainloop()
