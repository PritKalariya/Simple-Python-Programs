from tkinter import *
import calendar

window = Tk()
window.title("Python GUI Calender")

year = 2021
mycal = calendar.calendar(year)

cal_year = Label(window, text=mycal, font=("Consolas 8 bold"))
cal_year.pack()

window.mainloop()