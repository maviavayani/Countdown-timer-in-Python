import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Time Counter")
root.config(bg='black')

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(width=3, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.place(x=70, y=30)
hourEntry.config(bg='yellow')

minuteEntry = Entry(width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=130, y=30)
minuteEntry.config(bg='yellow')

secondEntry = Entry(width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=190, y=30)

secondEntry.config(bg='yellow')


def submit():
    try:

        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")

        temp -= 1


btn = Button(root, text='Set Time Countdown', bd='5',
             command=submit)
btn.place(x=90, y=130)
btn.config(bg='yellow')
root.mainloop()