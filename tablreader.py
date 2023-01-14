#Импортируем библиотеку для работы с таблицами
from pandas import read_csv

#Эта функция обрабатывает данные из таблицы 1
def Tab(Tab, anser, value, required):
    #Задаём номер строки
    line=None
    #Читаем файл таблицы
    article_read = read_csv(Tab, ";")
    #Перебераем все значения известной переменной
    for i in range(len(article_read[anser])):
        #Если значение найдено сохраняем номер строки
        if article_read[anser][i] == value:
            #сохраняем номер строки
            line=i
    #Если значение не найдено
    if line==None:
        #Перебераем все значения известной переменной
        for i in range(len(article_read[anser])):
            #Находим первое значение, большее чем известное
            if article_read[anser][i] > value:
                #Предположив что хначение искомой переменой изменяются линейно определяем её значение
                return (article_read[required][i]+(article_read[anser][i]-value)*((article_read[required][i - 1]-article_read[required][i])/(article_read[anser][i]-article_read[anser][i-1])))
    else:
        #Выводим значение искомой переменной
        return (article_read[required][line])