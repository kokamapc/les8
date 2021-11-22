person_data =['Иванов Иван Иванович', '1965', 'Москва', 'Сельхоз академия',
       'Тракторист']

person_data1 = {'Имя':'Сидоров Сергей Иванович',
        'Родился':'1985',
        'Город':'Пермь',
        'Учился':'ПНИПУ',
        'Работа':'Менеджер'}


def information(person_data):
    print('Введите данные: ')
    a = input()
    for a in range(len(person_data)):
        print(str(a) + ' ' + person_data[a])


def information_1(person_data1):
    print('Введите данные: ')
    b = input()
    if b in person_data1:
        print(person_data1[b])


information(person_data)
information_1(person_data1)
