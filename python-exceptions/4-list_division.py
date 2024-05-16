#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            print(f"division by 0")
            new_list.append(0)
        except TypeError:
            print(f"wrong type")
            new_list.append(0)
        except IndexError:
            print(f"out of range")
            new_list.append(0)
        finally:
            pass
    return (new_list)
