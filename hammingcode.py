while True:
    print("hello world")

    print("чтобы использовать код Хэмминга введите 1")
    print("чтобы найти ошибку в коде Хэмминга введите 0")

    #перевод числа
    menu=int(input())
    if menu==1:
        print("переводим число в код Хэмминга")
        print("введите двоичное число имеющее не более 4 разрядов")

    #делим на отдельные биты
        number = int(input())
        n1=0
        n2=0
        n3=number//1000
        n4=0
        n5=(number%1000)//100
        n6=(number%100)//10
        n7=number%10

    #получаем значения контрольных разрядов
        n1=(n3+n5+n7)%2
        n2=(n3+n6+n7)%2
        n4=(n5+n6+n7)%2

    #выводим результат
        print(n1,n2,n3,n4,n5,n6,n7)

    #поиск ошибки
    elif(menu==0):
        print("ищем ошибку в коде Хэмминга")
        print("введите семиразрядный код")

        number = int(input())

        #делим на отдельные биты
        n1=number//1000000
        n2=number//100000%10
        n3=number//10000%10
        n4=number//1000%10
        n5=(number%1000)//100
        n6=(number%100)//10
        n7=number%10

        #получаем правильные значения контрольных разрядов
        k1= (n3+n5+n7)%2
        k2 = (n3 + n6 + n7) % 2
        k3 = (n5 + n6 + n7) % 2
        where=0

        #сравниваем значения контрольных разрядов
        if(k1!=n1):
            where+=1
        if (k2 != n2):
            where+=2

        if (k3 != n4):
            where+=4

        #выводим ошибку
        if(where!=0):
            print("Ошибка на",where,"месте")

    print("Чтобы запустить скрипт заного введите любое значение - остановить Enter")
    again=input()
    if(again!=""):
        print("Запускаем заного")
    else:
        break
