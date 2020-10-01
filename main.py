

from tkinter import *




expression = ""
# current_sign = ""
def get_value(value):
    global expression
    expression += value
    string_var.set(expression)
    return

def executeClear():
	global expression
	expression = ""
	string_var.set("")
	return

def executeEqual():
	global expression
	# sum = 0
	# for i in expression.split("+"):
		# sum += int(i)
	expression = eval(expression)
	expression = str(expression)
	string_var.set(expression)
	return



window= Tk()




string_var = StringVar()
# window.grid()
# label=Label(text="Abhi sys corp.",fg="grey",anchor="n")
# label.pack(side=TOP)

window.title("Calculator")
window.geometry("275x220")
window.minsize(275,220)
display_screen = Entry(window, width=15, bg="grey",state="disabled", relief=SUNKEN,textvariable=string_var, font=('Ubuntu', 24))
display_screen.grid(row=0, columnspan=4,pady=35,padx=40)




button_1 = Button(window, text="1", width=7, height=1, bg="orange",font="Helvetica 8 bold",command=lambda: get_value("1") ).grid(row=1, column=0, padx=22,pady=10)
button_2 = Button(window, text="2", width=7, height=1, bg="orange",font="Helvetica 8 bold",command=lambda: get_value("2") ).grid(row=1, column=1,padx=22)
button_3 = Button(window, text="3", width=7, height=1, bg="orange",font="Helvetica 8 bold",command=lambda: get_value("3") ).grid(row=1, column=2,padx=22)
button_plus = Button(window, text="+", width=7, height=1, font="Helvetica 8 bold",command=lambda: get_value("+") ).grid(row=1, column=3,padx=22)


button_4 = Button(window, text="4", width=7, height=1, bg="orange",font="Helvetica 8 bold",command=lambda: get_value("4") ).grid(row=2, column=0,pady=10)
button_5 = Button(window, text="5", width=7, height=1,fg="blue",font="Helvetica 8 bold",command=lambda: get_value("5") ).grid(row=2, column=1)
button_6 = Button(window, text="6", width=7, height=1,fg="blue",font="Helvetica 8 bold",command=lambda: get_value("6") ).grid(row=2, column=2)
button_minus = Button(window, text="-", width=7, height=1, font="Helvetica 8 bold",command=lambda: get_value("-") ).grid(row=2, column=3)

button_7 = Button(window, text="7", width=7, height=1, font="Helvetica 8 bold",command=lambda: get_value("7") ).grid(row=3, column=0, pady=10)
button_8 = Button(window, text="8", width=7, height=1, font="Helvetica 8 bold",fg="blue",command=lambda: get_value("8") ).grid(row=3, column=1)
button_9 = Button(window, text="9", width=7, height=1, fg="blue",font="Helvetica 8 bold",command=lambda: get_value("9") ).grid(row=3, column=2)
button_multiply = Button(window, text="*", width=7, height=1, font="Helvetica 8 bold",command=lambda: get_value("*") ).grid(row=3, column=3)

button_0 = Button(window, text="0", width=7, height=1, font="Helvetica 8 bold",command=lambda: get_value("0") ).grid(row=4, column=0, pady=10)
button_clear = Button(window, text="Clear", width=7, height=1, bg="green",font="Helvetica 8 bold",command=executeClear ).grid(row=4, column=1)
button_equals = Button(window, text="=", width=7, height=1, bg="green",font="Helvetica 8 bold",command=executeEqual ).grid(row=4, column=2)
button_divide = Button(window, text="/", width=7, height=1, bg="green",font="Helvetica 8 bold",command=lambda: get_value("/") ).grid(row=4, column=3)

window.mainloop()
