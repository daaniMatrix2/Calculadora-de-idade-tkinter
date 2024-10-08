from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date 

color1 = "#3b3b3b"  # Preta 
color2 = "#333333"  # Preta
color3 = "#ffffff"  # Branco
color4 = "#fcc058" # Laranja

windows = Tk() 
windows.title("Calculadora de Idade") 
windows.geometry("310x410") 
windows.configure(bg=color1)

style = ttk.Style(windows) 
style.theme_use("clam")

# Frames 
top_frame = Frame(windows, width=310,
                  height=140, pady=0,padx=0,
                  relief="flat",bg=color2)
top_frame.grid(row=0,column=0)
bottom_frame = Frame(windows, width=310,
                     height=410, pady=0,padx=0,
                     relief="flat",bg=color1)
bottom_frame.grid(row=1,column=0, sticky=NW)

#Labels Top Frame
app_calculator = Label(top_frame, text="Calculadora de Idade", width=25, height=1, padx=3, relief="flat", anchor="center", font=("Ivy 15 bold"), bg=color2, fg=color3)
app_calculator.place(x=0, y=30)

# app_of_rage = Label(top_frame, text="Idade", width=11, height=1, padx=0, relief="flat", anchor="center", font=("Arial 35 bold"), bg=color2, fg=color4)
# app_of_rage.place(x=0, y=70)  # Corrigido aqui, de app_calculator para app_of_rage

l_initial_date = Label(bottom_frame, text="Data Atual", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=("Ivy 9"), bg=color1, fg=color3)
l_initial_date.place(x=50, y=30)

Cal_initial_date = DateEntry(bottom_frame, height=10, background="darkblue", foreground="white", borderwidth=2, date_pattern="mm/dd/y", year=2024)
Cal_initial_date.place(x=170, y=30)

l_birth_date = Label(bottom_frame, text="Data de Aniversario", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=("Ivy 9"), bg=color1, fg=color3)
l_birth_date.place(x=50, y=70)

Cal_birth_date = DateEntry(bottom_frame, height=10, background="darkblue", foreground="white", borderwidth=2, date_pattern="mm/dd/y",
                            year=2000)
Cal_birth_date.place(x=170, y=70)

app_years = Label(bottom_frame, text="0", height=1, padx=0, pady=0, relief="flat", anchor=CENTER, font=("Ivy 11 bold"),
                         bg=color1, fg=color3)
app_years.place(x=60,y=135)

app_label_years = Label(bottom_frame, text="Anos", height=1, padx=0, pady=0, relief="flat", anchor=CENTER, font=("Ivy 11 bold"),
                         bg=color1, fg=color3)
app_label_years.place(x=50,y=175)

app_months = Label(bottom_frame, text="0", height=1, padx=0, pady=0, relief="flat", anchor=CENTER, font=("Ivy 11 bold"),
                         bg=color1, fg=color3)
app_months.place(x=140,y=135)

app_label_months = Label(bottom_frame, text="Meses", height=1, padx=0,  relief="flat", anchor=CENTER, font=("Ivy 11 bold"),
                         bg=color1, fg=color3)
app_label_months.place(x=130,y=175)

app_days = Label(bottom_frame, text="0", height=1, padx=0,  relief="flat", anchor=CENTER, font=("Ivy 11 bold"),
                         bg=color1, fg=color3)
app_days.place(x=210,y=135)

app_label_days = Label(bottom_frame, text="Dias", height=1, padx=0,  relief="flat", anchor=CENTER, font=("Ivy 11 bold"),
                         bg=color1, fg=color3)
app_label_days.place(x=210,y=175)

# Função para Calcular idade
def calculate_age():
    initial_date_str = Cal_initial_date.get()
    l_birth_date = Cal_birth_date.get()

    month_1,day_1, year_1 = [int(f) for f in initial_date_str.split('/')]
    initial_date = date(year_1,month_1,day_1 )

    month_2,day_2, year_2 = [int(f) for f in l_birth_date.split('/')]
    l_birth_date = date(year_2,month_2,day_2 )

    years = relativedelta(initial_date, l_birth_date).years
    months = relativedelta(initial_date, l_birth_date).months
    days = relativedelta(initial_date, l_birth_date).days

    app_years["text"] = years
    app_months["text"] = months
    app_days["text"] = days

# Botão Calcular
b_calculate_age = Button(bottom_frame, text="Calcular Idade", width=20, height=1, bg=color1, fg=color3, font=("Ivy 10 bold"),
                          relief=RAISED, overrelief=RIDGE, command=calculate_age)
b_calculate_age.place(x=60,y=225)

windows.mainloop()


