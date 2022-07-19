from tkinter import *
import random

global password, counter


# select checkbox and put the selection in a string
def select():
    char_num = char_num_entry.get()
    global password, counter
    password = ""
    temp = ""
    counter = 0
    if len(char_num_entry.get()) == 0 or int(char_num) > 40:
        result['text'] = "password length in not valid"
        return None
    if var.get() == 0 and var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
        result['text'] = "you did not check any boxes"
        return None

    if var.get() == 1:
        number = random.choice(num)
        password += number
        counter += 1
        temp += num
    if var1.get() == 1:
        u_let = random.choice(u_letter)
        password += u_let
        counter += 1
        temp += u_letter
    if var2.get() == 1:
        l_let = random.choice(l_letter)
        password += l_let
        counter += 1
        temp += l_letter
    if var3.get() == 1:
        sp_ch = random.choice(special_ch)
        password += sp_ch
        counter += 1
        temp += special_ch
    char_num = int(char_num) - counter
    for x in range(char_num):
        password += random.choice(temp)
# shuffle the string
    ''.join(random.sample(password, len(password)))
# add the string to result label
    result['text'] = password


num = "123456789"
u_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_letter = "abcdefghijklmnopqrstuvwxyz"
special_ch = "!#$%&'()*+,-./\:;<=>?@[]^_`{|}~"

root = Tk()
root.title('Password Generator')
root.geometry('400x350')
# variable for each checkbox
var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

enter_label = Label(root, text="Password Generator")
enter_label.grid()

num_checkbox = Checkbutton(root, text='1 2 3 4 5 6 7 8 9', variable=var)
u_letter_checkbox = Checkbutton(root, text="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", variable=var1)
l_letter_checkbox = Checkbutton(root, text="a b c d e f g h i j k l m n o p q r s t u v w x y z", variable=var2)
special_ch_checkbox = Checkbutton(root, text="! # $ % & ' ( ) * + \ , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~ ' ", variable=var3)

num_checkbox.grid(row=1, column=0, sticky=W, pady=10, padx=10)
u_letter_checkbox.grid(row=2, column=0, sticky=W, pady=10, padx=10)
l_letter_checkbox.grid(row=3, column=0, sticky=W, pady=10, padx=10)
special_ch_checkbox.grid(row=4, column=0, sticky=W, pady=10, padx=10)

char_num_entry = Entry(root)
char_num_entry.grid()

generate_btn = Button(root, text="Generate", command=select, padx=10, pady=10)
generate_btn.grid()

result = Label(root, width=35, padx=5, pady=5)
result.grid()

root.mainloop()
