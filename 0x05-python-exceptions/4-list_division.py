#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            division = a / b
        except IndexError:
            print("outof range")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        finally:
            nlst.append(division)
    return nlst
