import tkinter
from guizero import App, Text, TextBox, PushButton, messagebox
app = App(title="BMI Calculator", bg="cadetblue")

txtWeight = Text(app, text="Enter Weight (in kg): ")
txtBoxW = TextBox(app)

txtHeight = Text(app, text="Enter Height (in cm): ")
txtBoxH = TextBox(app)

def calBMI():
    try:
        userWeight = float(txtBoxW.value)
        userHeight = float(txtBoxH.value)
        height = userHeight /100.0
        userBMI = userWeight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Please enter positive height")
    except ValueError:
         messagebox.showinfo("Please enter valid data")
    else:
         messagebox.showinfo("Your calculated BMI is: ", userBMI)

dispayBMI = PushButton(app, command=calBMI, text="BMI") 

app.display()