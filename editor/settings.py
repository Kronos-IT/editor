import tkinter
from tkinter import *
from tkinter import filedialog as fd #функции сохранить и открыть файл
from tkinter.messagebox import showerror #показ всех ошибок
from tkinter import messagebox #уведомления приложения

APP_NAME = 'Текстовый редактор'

WIDTH = 1000
HEIGH = 650

class Text_editor():

    def __init__(self, text):
        self.file_name = tkinter.NONE
        self.text = text

    def new_file(self):
        self.file_name = 'Без названия'
        self.text.delete('1.0', tkinter.END)

    def open_file(self):
        file_name = fd.askopenfilename() #вызываем функцию открытия файлов
        f = open(file_name) #открываем файл
        s = f.read() # считываем файл
        self.text.delete(1.0, tkinter.END) #удаляем все, что было в редакторе
        self.text.insert(1.0, s) #вставка информации из файла
        f.close() #закрытие файла

    def save_file(self):
        data = self.text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding="utf-8")
        output.write(data)
        output.close()

    def save_as_file(self):
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),("HTML files", "*.html;*.htm"), ("All files", "*.*")))
        f = open(file_name, "w") # открытие файла на запись
        s = self.text.get(1.0, END)
        f.write(s)
        f.close

    def get_info(self):
        messagebox.showinfo('Справка', "Информация о нашем приложении! Спасибо, что его используете")

    