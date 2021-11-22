user =['Иванов Иван Иванович', '1965', 'Москва', 'Сельхоз академия',
       'Тракторист']

user1 = {'Имя':'Сидоров Сергей Иванович',
        'Родился':'1985',
        'Город':'Пермь',
        'Учился':'ПНИПУ',
        'Работа':'Менеджер'}


def information(user):
    print('Введите данные: ')
    a = input()
    for a in range(len(user)):
        print(str(a) + ' ' + user[a])


def information1(user1):
    print('Введите данные: ')
    b = input()
    if b in user1:
        print(user1[b])


information(user)
information1(user1)