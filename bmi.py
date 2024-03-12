from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("500x800")

window.configure(bg="yellow")


app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Komika Axis", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Transformers", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Your Lambai", fg="black", bg="red", font=("Cooper Black", 12),bd=1 )
height_label.place(x=20,y=120)

height_entry=Entry(window, text="", bd=2, width=30)
height_entry.place(x=150,y=120)

weight_label=Label(window, text="Motapa", fg="black", bg="red", font=("Cooper Black", 12),bd=1 )
weight_label.place(x=20,y=150)

weight_entry=Entry(window, text="", bd=2, width=30)
weight_entry.place(x=150,y=150)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

def BMI():
    w=int(weight_entry.get())
    h=int(height_entry.get())/100
    cal=w/(h**2)
    name=username.get()
    result_label.destroy()
    msg=""
    if cal<18.5:
        msg="patla hai"
    elif cal>18.5 and cal<24:
        msg="thik hai kuch mat kar lekin kaam karta rahiyo"
    elif cal>24 and cal<30:
        msg="mota hai kam khaya kar"
    elif cal>30:
        msg="abe kam kha mar jayega"
    else:
        msg="galat likh diya bhai"
    output=Label(result_frame, text=name+" Your Bmi is "+msg, bg="white", font=("Stencil",15),width=50)
    output.place(x=20,y=20)
    output.pack()

btn=Button(window, text="calculate", fg="black", bg="green", bd=5, command=BMI)
btn.place(x=230,y=500)

window.mainloop()