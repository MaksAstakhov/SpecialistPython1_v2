# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

while True:
    try:
        n = input("введите строку формата nxm: ")
        tlist = n.split("x")
        count = float(tlist[0]) // float(tlist[1])
        print(count)
        break
    except ValueError:
        print("некорректные данные")
