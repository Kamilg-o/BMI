import tkinter

def  result():
    weight = float(ent_kg.get())
    hight = float(ent_m.get())
    bmi = weight / ((hight) **2)
    lbl_bmi1 = tkinter.Label(text=round(bmi,2))
    lbl_bmi1.pack()



window = tkinter.Tk()
window.title("BMI CALCULATOR")

lbl_weight = tkinter.Label(text=" PODAJ WAGE ")
ent_kg = tkinter.Entry()
lbl_hight = tkinter.Label(text=" PODAJ WZROST ")
ent_m = tkinter.Entry()
lbl_bmi = tkinter.Label(text="TWOJE BMI")
btn = tkinter.Button(text="OBLICZ", width=10, height=3, command=result)

lbl_weight.pack()
ent_kg.pack()
lbl_hight.pack()
ent_m.pack()
btn.pack()
lbl_bmi.pack()



window.mainloop()