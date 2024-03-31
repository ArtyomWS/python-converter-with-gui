import tkinter

window = tkinter.Tk()
window.title("Converter")
#Input
input = tkinter.Entry(width=10)
input.grid(row=0, column=1)

#Label
label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_res = tkinter.Label(text="0")
label_res.grid(row=1, column=1)

label_km = tkinter.Label(text="Km")
label_equal.grid(row=1, column=2)
#Button
def button_clicked():
    res = float(input.get())*1.6
    label_res.config(text=res)

button = tkinter.Button(text="Convert", command=button_clicked)
button.grid(row=2, column=2)

window.mainloop()