#импортируем библиотеки, необходимые для работы генератора. csv нужен для работы с файлами csv, random для генерации случайной комбинации элементов, tkinter для создания интерфейса, а os для управления файлами и координацией
import csv
import random
import tkinter as tk
import os

def generate_cinema_password(special_words, length): #создаем функцию, которая проясняет рамки генератора. в скобках переменные, необходимые для составления комбинации. special_words - данные, взятые из база данных, length - длина самого пароля
    password = '' #в эту пустую строку будет собираться наш пароль
    while len(password) < length: #условие генерации пароля в установленных рамках (длина)
        word = random.choice(special_words) #выбор случайного слова из предлагаемого списка слов

        if len(password) + len(word) <= length:   #добавляем выбор случайного слова к паролю, в случае если кол-во символов не превышает заданную длину
            password += word + random.choice(['', '!', '@', '#', '$', '%'])  #добавляем случайный символ для большей вариативности паролей

    return password[:length]  #обрезаем пароль до требуемой длины

def generate_password(): #вводим функцию generate_password, которая будет вызываться при нажатии кнопки для генерации пароля
    length_str = length_entry.get() #с помощью этой строки получаем текст, введенный пользователем в поле ввода length_entry, и сохраняем его в переменной length_str

    if length_str.isdigit(): #метод str.isdigit() проверяет, чтобы length_str состояла только из цифр. если это так, код идет дальше
        length = int(length_str) #преобразуем строку в целое число и сохраняем в переменной length
        if length < 12 or length > 18: #второй шаг. проверяем, удовлетворяет ли число условию и выводим соответствующий месседж пользователю через строчку в интерфейсе
            result_label.config(text="Количество символов не должно быть меньше 12 и больше 18.")
            return #если длина не соответствует критериям, функция завершается
    else:
        result_label.config(text="Пожалуйста, введите корректное число.")
        return #если в строке не только числа, функция завершается

#после получения данных о количестве символов и их соответствию критериям, переходим к самому паролю. сохраняем все нашего богатство в переменной password
    password = generate_cinema_password(special_words, length) #вызываем функцию с переданными специальными словами и длиной, чтобы сгенерировать пароль и сохранить его в переменной
    result_label.config(text=f"Сгенерированный киношный пароль: {password}") #выводим его в интерфейсе

special_words = [] #инициализируем пустой список special_words, который будет заполняться словами из csv файла

#проверка существования файла перед его открытием
if os.path.exists('HollywoodMovies2.csv'): #метод os.path.exists проверяет, существует ли файл HollywoodMovies2.csv, чтобы программа могла пойти дальше
    with open('HollywoodMovies2.csv', newline='', encoding='utf-8') as f: #открываем наш файл для чтения с указанной кодировкой utf-8 и создаем объект файла f
        reader = csv.reader(f) #объект reader читает строки из CSV файла
        for row in reader:
            special_words.extend(row) #добавляем каждую строку (которая является списком слов) в список special_words

if not special_words: #проверяем наполненность списка special_words. если он пустой, информируем об этом
    result_label.config(text="Упс. Что-то случилось с файлом.")

#создаем окно с помощью tkinter, в котором будет работать программа. Задаем ей название, размеры и цвет заливки фона
window = tk.Tk()
window.title("Генератор киношных паролей")
window.geometry ("600x480")
window["bg"] = "blue"

#далее вводим элементы интерфейса. создаем надпись, форматируем и выбираем цвет
length_label = tk.Label(window, text="Введите длину пароля (12-18):")
length_label.pack(pady=10)
length_label["bg"] = "orange"
length_label["fg"] = "white"

#добавляем окно для ввода количества символов командой entry
length_entry = tk.Entry(window)
length_entry.pack(pady=10)

#делаем кнопку "сгенерировать пароль" методом button. аналогично форматируем (pady = 10) и красим.
generate_button = tk.Button(window, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(pady=10)
generate_button["bg"] = "orange"
generate_button["fg"] = "white"

#создаем строку для вывода результата, форматируем
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

#запускаем цикл
window.mainloop()
