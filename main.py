import tkinter as tk
import re

def enter_symbol(symb):
    entry.insert(tk.END,symb)

def calculate():
    data = re.split(r'(\+|\-|\*|/)', entry.get())
    result = 0
    operation = "+"
    for el in data:
        try:
            el = int(el)
            result = result + el if (operation == "+") else result
            result = result - el if (operation == "-") else result
            result = result / el if (operation == "/") else result
            result = result * el if (operation == "*") else result
        except ValueError:
            operation = el

    entry.delete(0, tk.END)
    entry.insert(0,str(result))

def clear_entry():
    entry.delete(0,tk.END)

def validate_entry(s):
    # Паттерн для проверки, что строка содержит только цифры, знаки операций и точку
    pattern = r'^[\d+\-*/.]+$'
    # Используем re.fullmatch для проверки всей строки
    if bool(re.fullmatch(pattern, s)) or s == "":
        return True
    else:
        return False

root = tk.Tk()

root.title("Калькулятор/khkkjh")
root.geometry("300x280")

#Метод root.register оборачивает функцию для использования в качестве команды валидации.
validate_command = root.register(validate_entry)

entry = tk.Entry(root, width = 23, font = 20, bg = "azure2", validate="key", validatecommand=(validate_command,"%P"))
#Параметр validatecommand принимает кортеж: первый элемент это зарегистрированный валидатор,
# а далее именованные параметры, которые он принимает ('%P' это новый вводимый текст).
entry.place(relx = 0.02, rely = 0.02)

b1 = tk.Button(root, width = 6, height = 2, text = '1',font = 20, command = lambda: enter_symbol("1"))
b1.place(relx = 0.02, rely = 0.18)
b2 = tk.Button(root, width = 6, height = 2, text = '2',font = 20, command = lambda: enter_symbol("2"))
b2.place(relx = 0.26, rely = 0.18)
b3 = tk.Button(root, width = 6, height = 2, text = '3',font = 20, command = lambda: enter_symbol("3"))
b3.place(relx = 0.50, rely = 0.18)
b4 = tk.Button(root, width = 6, height = 2, text = '4',font = 20, command = lambda: enter_symbol("4"))
b4.place(relx = 0.02, rely = 0.37)
b5 = tk.Button(root, width = 6, height = 2, text = '5',font = 20, command = lambda: enter_symbol("5"))
b5.place(relx = 0.26, rely = 0.37)
b6 = tk.Button(root, width = 6, height = 2, text = '6',font = 20, command = lambda: enter_symbol("6"))
b6.place(relx = 0.50, rely = 0.37)
b7 = tk.Button(root, width = 6, height = 2, text = '7',font = 20, command = lambda: enter_symbol("7"))
b7.place(relx = 0.02, rely = 0.56)
b8 = tk.Button(root, width = 6, height = 2, text = '8',font = 20, command = lambda: enter_symbol("8"))
b8.place(relx = 0.26, rely = 0.56)
b9 = tk.Button(root, width = 6, height = 2, text = '9',font = 20, command = lambda: enter_symbol("9"))
b9.place(relx = 0.50, rely = 0.56)
b10 = tk.Button(root, width = 6, height = 2, text = '.',font = 20, command = lambda: enter_symbol("."))
b10.place(relx = 0.02, rely = 0.75)
b11 = tk.Button(root, width = 6, height = 2, text = '0',font = 20, command = lambda: enter_symbol("0"))
b11.place(relx = 0.26, rely = 0.75)
b10 = tk.Button(root, width = 6, height = 2, text = '=',font = 20, command = calculate)
b10.place(relx = 0.50, rely = 0.75)
b11 = tk.Button(root, width = 6, height = 2, text = '+',font = 20, command = lambda: enter_symbol("+"))
b11.place(relx = 0.76, rely = 0.18)
b12 = tk.Button(root, width = 6, height = 2, text = '-',font = 20, command = lambda: enter_symbol("-"))
b12.place(relx = 0.76, rely = 0.37)
b13 = tk.Button(root, width = 6, height = 2, text = '/',font = 20, command = lambda: enter_symbol("/"))
b13.place(relx = 0.76, rely = 0.56)
b14 = tk.Button(root, width = 6, height = 2, text = '*',font = 20, command = lambda: enter_symbol("*"))
b14.place(relx = 0.76, rely = 0.75)
b15 = tk.Button(root, width = 6, height = 1, text = 'C',font = 20, command = clear_entry)
b15.place(relx = 0.76, rely = 0.02)


root.mainloop()
