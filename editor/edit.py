import tkinter
from tkinter import *
from tkinter import filedialog as fd #функции сохранить и открыть файл
from tkinter.messagebox import showerror #показ всех ошибок
from tkinter import messagebox #уведомления приложения

from settings import *



app = tkinter.Tk() #создаю окно приложения
app.title(APP_NAME)
app.minsize(width=WIDTH, height=HEIGH)
app.maxsize(width=WIDTH, height=HEIGH)

text = tkinter.Text(app, width=WIDTH - 100, heigh=HEIGH, wrap='word') #создали поле текста
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) #создали скролл
scroll.pack(side="right", fill="y") #разместили скролл
text.configure(yscrollcommand=scroll.set) #связь текста со скролом
text.pack() #разместили поле с текстом

menuBar = tkinter.Menu(app) #Создание основного меню

editor = Text_editor(text)

app_menu = tkinter.Menu(menuBar) # выпадающее меню у "Файл"
help_menu = tkinter.Menu(menuBar)
app_menu.add_command(label='Новый', command=editor.new_file)
app_menu.add_command(label='Открыть', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)

help_menu.add_command(label='Обновления', command=editor.get_info)
help_menu.add_command(label='Последняя версия программы')
help_menu.add_command(label='Поддержка')

menuBar.add_cascade(label='Файл', menu=app_menu)
menuBar.add_cascade(label='Справка', menu=help_menu)
menuBar.add_cascade(label='Вставка')
menuBar.add_cascade(label='Выход', command=app.quit)

app.config(menu=menuBar)

app.mainloop()