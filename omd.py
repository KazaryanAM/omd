# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Конечно, вот тот, голубой!\n'
        'Он промокнет насквозь, этот зонтик дырявый!\n'
        'Утке стало смешно.\n'
        'А потом ей опять стало грустно.\n'
        'И она снова подумала: и чего мне грустить?\n'
        'Ведь у меня есть мой любимый хозяин!\n'
        'Я его очень люблю!\n'
        'Он меня кормит, поит, купает.\n'
        'И на работу он берет, а не с работы.\n'
        'А еще у него есть такие замечательные друзья, как этот зонтик.\n'
        'Они бы тоже хотели посидеть в баре и попить пивка.\n'
        'Но хозяин не разрешает, говорит, что рано.'
    )


def step2_no_umbrella():
    print(
        'А зачем он ей?\n'
        'Ведь она и так красивая!!!!'
    )


if __name__ == '__main__':
    step1()

