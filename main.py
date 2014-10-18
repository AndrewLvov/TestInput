# -*- coding: utf-8 -*-


def main():
    name = input("Назовитесь: ")
    try:
        if len(name) == 0:
            raise ValueError("Жаль, что вы не захотели представится")
        print("Hello, {}".format(name))
    except ValueError as e:
        print(e)
        exit()

    try:
        age = int(input("Возраст: "))
        if age > 40:
            print("Зарядку делаете??")
        else:
            print("Эх, молодой ещё!")
    except ValueError as e:
        print("Скрываете возраст? Ну и зря")
        exit()

main()
