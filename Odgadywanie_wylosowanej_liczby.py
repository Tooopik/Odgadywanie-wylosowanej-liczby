from random import randint


def win_statement(number):
    if number == 100:
        print('\n')
        print('*'*41)
        print(f'*** Gratulacje! szukana liczba to {number} ***')
        print('*'*41)
        print('\n')
    elif number <= 9:
        print('\n')
        print('*'*39)
        print(f'*** Gratulacje! szukana liczba to {number} ***')
        print('*'*39)
        print('\n')
    else:
        print('\n')
        print('*'*40)
        print(f'*** Gratulacje! szukana liczba to {number} ***')
        print('*'*40)
        print('\n')


numberToGuess = randint(1, 100)
userChoice = 0
print('='*70)
print('Witaj w prostej grze w zgadywanie wymyślonej przezemnie liczby ;) !')
print('='*70)

while userChoice != numberToGuess:
    print('Podaj liczbę z przedziału od 1 do 100 \nJeśli chcesz zakończyć wybierz 0')
    userChoice = int(input('>>> '))

    if userChoice < numberToGuess and userChoice != 0:
        print(f'Liczba {userChoice} jest mniejsza od szukanej')
        print('Spróbuj ponownie\n')

    elif userChoice > numberToGuess and userChoice != 0:
        print(f'Liczba {userChoice} jest większa od szukanej')
        print('Spróbuj ponownie\n')

    elif userChoice == 0:
        print('Może kolejnym razem')
        break

if userChoice != 0:
    win_statement(userChoice)
else:
    print('Dozobaczenia')
