from tkinter import *
import os
import sys
import winsound


def countdown(count):
    # change text in label
    label['text'] = "restart in \n {}s".format(count)
    frequency = int(440)  # Set Frequency To 2500 Hertz
    duration = int(500)  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

    if count > 0:
        # call countdown again after 1000ms (1s)
        win.after(1000, countdown, count-1)
    else:
        print("neustart")
        os.system("shutdown /r /t {}".format(10))


if __name__ == '__main__':

    wartezeit = 60

    win = Tk()
    # Set the geometry of the window
    win.geometry("700x350")
    # Create a frame widget
    frame = Frame(win, width=700, height=350)
    frame.grid(row=0, column=0, sticky="NW")
    # Create a label widget
    label = Label(win, text="blub", font='Arial 100 bold')
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    # call countdown first time
    countdown(wartezeit)
    # win.after(0, countdown, 5)
    win.mainloop()


