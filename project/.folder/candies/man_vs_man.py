import random 

def WhoPlaysFirst ():
    player1 = str(input('Игрок №1, ваш выбор: орел или решка? Ответ: '))
    player2 = ''
    if player1 == 'орел':
        player2 = 'решка'
    elif player1 == 'решка':
        player2 = 'орел'
    print(f'Игрок №2, вы выбрали вариант {player2}.')

    orel = [0,'орел']
    reshka = [1,'решка']
    a = random.randrange(0,2)
    print('*Подкидываем воображаемую монетку*')
    if a == orel[0]:
        if orel[1] == player1:
            answer = 'Орел! Первым ходит Игрок №1'
        if orel[1] == player2:
            answer = 'Орел! Первым ходит Игрок №2'

    if a == reshka[0]:
        if reshka[1] == player1:
            answer = 'Решка! Первым ходит Игрок №1'
        if reshka[1] == player2:
            answer = 'Решка! Первым ходит Игрок №2'
    return answer

def Play(res):
  first =  "1" in res
  all_in_all = 2021
  player1 = 0
  player2 = 0
  print(f'\nПриступим!\nНа столе лежит 2021 конфета.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n ')
  while all_in_all > 0:
    if first == True:
        print("Игрок №1, делайте ход.")
        step1 = GetNumber(1)
        player1+=step1
        all_in_all -=step1
        print(f'\nИтого: {all_in_all}\nПервый игрок:{player1}\nВторой игрок:{player2}')
        first = False
    else:
        print("Игрок №2, делайте ход.")
        step2 = GetNumber(1)
        player2+=step2
        all_in_all-=step2
        print(f'\nИтого: {all_in_all}\nПервый игрок:{player1}\nВторой игрок:{player2}')
        first = True
    
    if all_in_all == 0:
        if first == True:
            player2 += player1
            player1 = 0
            print(f'\n Поздравляем! Победил Игрок №2\nПервый игрок:{player1}\nВторой игрок:{player2}')
        if first == False:
            player1+=player2
            player2 = 0
            print(f'\nПоздравляем! Победил Игрок №1\nПервый игрок:{player1}\nВторой игрок:{player2}')

def GetNumber(x): 
    num = 0
    for i in range (x):
        smt = False
        while not smt:
            try:
                number = int(input("Выберите число от 1 до 28: "))
                num = number
                smt = True
                if number < 1 or number > 28:
                    smt = False
                    print("Выберите число от 1 до 28!")
            except ValueError:
                print("Вы ошиблись. Введите число!")
    return num

res = WhoPlaysFirst()
print(res)
Play(res)

