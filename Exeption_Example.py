

def divisor():
    try:        #Заграждаме блокът който смятаме за критичен (където може да възнинке изключение)
        a = float(input("a= "))
        b = float(input("b= "))
        result = a / b
        print(result)
    except ZeroDivisionError as e:
        print("На нула не се дели!")
        print(e)
    except ValueError as e:
        print("Въведете само цифри!")
        print(e)
    except Exception as e:
        print("Нещо се обърка!")
        print(e)
    finally:
        print("Примера работи!")
divisor()
