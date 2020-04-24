import tkinter as tk

def year_selected():
    
    result_window = tk.Toplevel(root)

    result_window.mainloop()

root = tk.Tk()


YEARS = [2017, 2018]
var = tk.StringVar()
var.set("Please choose a year")

root.title("Waka Ama Competition Program")
#root.iconbitmap('waka.ico')

title = tk.Label(root, text = "Waka Ama\nCompetition", font = ("Time New Roman", 12))
title.grid(row = 0, column = 0)

year = tk.OptionMenu(root, var, *YEARS)
year.grid(row = 1, column = 0, columnspan = 2)

go_button = tk.Button(root, text = "Go", command = year_selected)
go_button.grid(row = 2, column = 0)

root.mainloop()