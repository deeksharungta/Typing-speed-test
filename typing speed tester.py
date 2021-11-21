from tkinter import *
import random
import keyboard

# global variables
counter = 0
running = False
keypressed = 0
wpm = 0
accuracy = 0

instruction = (
    "*************** WELCOME TO TYPING MASTER ***************\n\nKindly go through the instructions below: \n\n"
    "1. This is an app to test your typing speed.\n"
    "2. It is recommended that you should not correct the words after pressing space.\n"
    "3. The timer will start when you enter your first character in the input box.\n"
    "4. To submit press 'Enter'.\n"
    "5. You can see the result on the right side of the window.\n\n"
    "Note : Typing Master will automatically stop after 2 minutes.")

root = Tk()

with open("typing_story.txt", "r") as file:
    allText = file.read()
    para = list(map(str, allText.split('\n')))


# function to handle key event
def key(event):
    global keypressed
    global running
    keypressed += 1
    if keypressed == 1:
        running = True
        counter_label(lbl)
    if keyboard.is_pressed("enter"):
        running = False
        check_input(input_text, words_text)


# function to restart
def restarting(events):
    print("Restarting...")
    input_text.delete("1.0", "end")

    global counter
    counter = 0
    if running == False:
        lbl['text'] = '00'
    else:
        lbl['text'] = ''

    # restart time
    global keypressed
    keypressed = 0
    input_text.bind('<Key>', key)

    check_input(input_text, words_text)

    global wpm, accuracy
    wpm = 0
    accuracy = 0


# function to exit
def exiting(events):
    print("Exiting...")
    quit()


# function to print time
def custom_dialog_box():
    base = Toplevel(root)
    base.geometry("600x400+400+200")
    base.title("Instruction")
    base.focus()

    # function to exit instructions dialog box
    def exit_instr(event):
        base.destroy()

    # instructions dialog box
    dialog_f = Frame(base)
    dialog_m = Message(dialog_f, text=instruction, bg="#2A2A42", fg="floralwhite", font="roboto 15 bold", width='580')
    dialog_f.pack()
    dialog_m.pack(side=LEFT)
    btn = Button(base, text="CLICK HERE OR PRESS SPACE TO PROCEED", width=50, bg="red", fg="floralwhite",
                 font="raleway 15 bold", relief="groove", command=base.destroy)
    btn.pack(side=BOTTOM, padx=20, pady=10)
    base.bind('<space>', exit_instr)


# function for incrementing the timer
def counter_label(lbl):
    def count():
        global counter
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


# function to calculate the accuracy
def check(written, words_text):
    count = 0
    for i in range(len(written)):
        if written[i] == words_text[i]:
            count += 1
    acc = (count * 100) // len(written)
    return acc


# function to calculate wpm and print it
def check_input(write, words_text):
    global wpm, accuracy

    written = write.get("1.0", "end-1c")
    written = written.split()
    if counter != 0:
        wpm = len(written) / (counter / 60)
        accuracy = check(written, words_text)
        accuracy = str(accuracy) + "%"
        lbl_wpm = Label(canvas, text=round(wpm), font="roboto 20 bold")
        lbl_acc = Label(canvas, text=accuracy, font="roboto 20 bold")

    else:
        lbl_wpm = Label(canvas, text="00", font="roboto 20 bold")
        lbl_acc = Label(canvas, text="0%", font="roboto 20 bold")

    if wpm != 0:
        lbl_wpm.place(x=855, y=305)
        lbl_acc.place(x=705, y=305)


# setting the tkinter window
root.geometry("1000x600+300+100")
root.title("Typing Speed Test")
root.resizable(0, 0)
bg_image = PhotoImage(file="images/background.png")
canvas = Canvas(root, width=1000, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# the heading or name of the the application
canvas.create_text(500, 20, text="TYPING MASTER", fill="white", font="raleway 20 bold")
canvas.pack()

# message or paragraph
f1 = Frame(root)
story = random.choice(para)
m1 = Message(f1, text=story, fg="black", font="roboto 15", width='540')
words_text = story.split()
f1.place(x=50, y=55)
m1.pack()

# text area to type
f2 = Frame(root, relief=SUNKEN)
f2.place(x=50, y=315)
input_text = Text(f2, width=50, height=10, font="roboto 15", wrap="word")
input_text.pack()

# rectangle for words per min
canvas.create_rectangle(750, 120, 850, 170, fill="white", width=2)
canvas.create_text(800, 185, text="TIME", fill="white", font="roboto 15 bold")

# rectangle for accuracy
canvas.create_rectangle(675, 300, 775, 350, fill="white", width=2)
canvas.create_text(725, 365, text="ACCURACY", fill="white", font="roboto 15 bold")

# rectangle for time
canvas.create_rectangle(825, 300, 925, 350, fill="white", width=2)
canvas.create_text(875, 365, text="WPM", fill="white", font="roboto 15 bold")

# restart icon
restart_img = PhotoImage(file="images/restart-icon.png")
restart = Label(canvas, image=restart_img)
restart.place(x=710, y=450)
restart.bind('<Button-1>', restarting)
canvas.create_text(730, 510, text="Restart", fill="white", font="roboto 15 bold")

# delete icon
delete_img = PhotoImage(file="images/delete-icon.png")
delete = Label(canvas, image=delete_img)
delete.place(x=860, y=450)
delete.bind('<Button-1>', exiting)
canvas.create_text(880, 510, text="Exit", fill="white", font="roboto 15 bold")

lbl = Label(canvas, text="00", fg="black", font="roboto 20 bold")
input_text.bind('<Key>', key)

lbl.place(x=780, y=125, )

root.after(10, custom_dialog_box)
root.mainloop()
