from tkinter import *
from tkinter import messagebox
import json
# Password genertor
import random
alphabet_list = [chr(i) for i in range(97, 123)]
symbol = ["!","@","#","$,","%","^","&","*"]

number_of_alpha = 3
number_of_integer = 3
number_of_symbol = 3

random_no_list = []
for i in range(number_of_integer):
    random_no = str(random.randint(0,9))
    random_no_list.append(random_no)


random_alpha_list = []
for i in range(number_of_alpha):
    random_alpha = random.choice(alphabet_list)     
    random_alpha_list.append(random_alpha)


random_symbol_list = []
for i in range(number_of_symbol):
    random_symbol = random.choice(symbol)
    random_symbol_list.append(random_symbol)


password_list = []
for number in random_no_list:
    password_list.append(number)

for alpha in random_alpha_list:
    password_list.append(alpha)

for symbol in random_symbol_list:
    password_list.append(symbol)

random.shuffle(password_list)
password ="".join(password_list)
   

def gen_password():
    global password
    input3.insert(0,password)

def add_():
    users_web = input1.get()
    users_email = input2.get()
    users_pass = input3.get()

    new_data = {users_web : {
        "email" : users_email,
        "password" : users_pass
    }}
    is_ok = messagebox.askokcancel(title = "website",message=f"these are the details given by you \n\nweb = {users_web}\nemail = {users_email}\npassword = {users_pass}")
    if is_ok:
        try:
            with open(file="file.json",mode="r") as file:
                data = json.load(file)
                data.update(new_data)
            with open(file = "file.json",mode = "w") as file:
                json.dump(data,file,indent=4)                
        except:
            with open(file = "file.json",mode = "w") as file:
                json.dump(new_data,file,indent=4) 

        input1.delete(0,END) 
        input2.delete(0,END) 
        input3.delete(0,END)  
def search():
        users_web = input1.get()

        with open(file = "file.json",mode="r") as file:
            data = json.load(file)

            if users_web in data:
                users_email = data[users_web]["email"]
                users_pass = data[users_web]["password"]
                messagebox.showinfo(title="information",message=f"email : {users_email}\npassword : {users_pass}")
            else:
                messagebox.showinfo(title="information",message = "no data exist for this web")


window = Tk()
window.minsize(height=450,width=500)
window.title("Password manager")

canvas = Canvas(height=250,width=400)
pic = PhotoImage(file = "pass1.png")
canvas.create_image(250,125,image = pic)
canvas.grid(row = 0,column = 0,columnspan=2,pady=20)

web = Label(text="Website",font=("Arial",10,"bold"))
email = Label(text = "Email",font = ("Arial",10,"bold"))
password_ = Label(text = "Password",font = ("Arial",10,"bold"))

web.grid(row = 1,column=0,pady = 10,padx=10)
email.grid(row = 2,column=0)
password_.grid(row=3,column=0,pady=10)

input1 = Entry(width=25)
input1.grid(row=1,column=1)

input2 = Entry(width=45)
# prefilled email with a default value 
input2.insert(0,"abc@gmail.com")
input2.grid(row=2,column=1,columnspan=2)

input3 = Entry(width=25)
input3.grid(row=3,column=1)

button_g = Button(text = "generate pass",fg="red",background="pink",width=15,command=gen_password)
button_g.grid(row = 3,column=2)

button_a = Button(text = "Add",fg="red",background="cyan",width=30,command=add_)
button_a.grid(row = 4,column=1,columnspan=2) 

button_s = Button(text = "search",fg="red",background="pink",width=15,command=search)
button_s.grid(row = 1,column=2)

window.mainloop()
