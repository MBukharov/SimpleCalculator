import tkinter as tk
import re

def enter_symbol(symb):
    global flag_new_calculation
    # если вводить числа после расчета, то строка должна стереться
    if flag_new_calculation:
        clear_entry()
        flag_new_calculation = False

    #Вставка символа в конец строки
    entry.insert(tk.END,symb)

def calculate():
    global flag_new_calculation

    # Разделяем введенную строку по знакам математических операций
    data = re.split(r'(\+|\-|\*|/)', entry.get())

    result = 0
    operation = "+"    # начальная операция для первого числа просто +

    #пробегаем по всем элементам списка, полученного из введенной строки
    for el in data:
        try:
            # пробуем преобразовать элемент в число и производим математическую операцию с ним
            el = float(el)
            result = result + el if (operation == "+") else result
            result = result - el if (operation == "-") else result
            result = result / el if (operation == "/") else result
            result = result * el if (operation == "*") else result

        # если элемент символ математической операции, то запоминаем ее
        except ValueError:
            operation = el

    # Очищаем строку ввода и вставляем результат вычислений
    entry.delete(0, tk.END)
    entry.insert(0,str(result))

    # Чтобы при следующем нажатии на кнопку строка очистилась, устанавливаем флаг в значение True
    flag_new_calculation = True

# Функция для очистки строки ввода
def clear_entry():
    entry.delete(0,tk.END)

# Функция проверки вводимых данных. Только цифры, знаки мат. операций и точка разрешены
def validate_entry(s):
    # Паттерн для проверки, что строка содержит только цифры, знаки операций и точку
    pattern = r'^[\d+\-*/.]+$'
    # Используем re.fullmatch для проверки всей строки
    if bool(re.fullmatch(pattern, s)) or s == "":
        return True
    else:
        return False

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x280")

#Метод root.register оборачивает функцию для использования в качестве команды валидации.
validate_command = root.register(validate_entry)

flag_new_calculation = True

entry = tk.Entry(root, width = 23, font = 20, bg = "azure2", validate="key", validatecommand=(validate_command,"%P"))
#Параметр validatecommand принимает кортеж: первый элемент это зарегистрированный валидатор,
# а далее именованные параметры, которые он принимает ('%P' это новый вводимый текст).

entry.place(relx = 0.02, rely = 0.02)

#Кнопки цифр и операций
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
