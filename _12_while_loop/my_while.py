import random

print('Повторяет цикл пока переменная не дойдет до False')
counter = 1
while counter <= 5:
    print(f'Counter is: {counter}')
    counter += 1
print()


print('Повторяет цикл пока не кончится list')
my_list = [0, 1, 2, 3, 4, 5]
while my_list:
    element = my_list.pop()
    print(f'elementL: {element}')
print(my_list)
print()

# print('Создадим повторяющийся цикл пока не напишем quit')
# while True:
#     answer = input('Enter a number ')
#     if answer == 'quit':
#         break
#     print(f'You entered: {answer}')
#     print()


# Создаем игру в монетку
HEADS = 'heads'
TAILS = 'tails'
COIN_VALUES = [HEADS, TAILS]
RULETKA = []
for i in range(19):
    RULETKA.append(COIN_VALUES[0])
    RULETKA.append(COIN_VALUES[1])



def flip_coin():
    return random.choice(RULETKA)
    

def play_martingle (*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet
    current_funds_max = []
    zero1 = 0
    heads1 = 0
    tails1 = 0
    while current_funds > 0:
        current_funds_max.append(current_funds)
       # print('======')
        steps_to_loose += 1
       #print(f'{current_funds=}')
        current_funds -= current_bet
        #print(f'{current_bet=}')
        flipped_coin_value = flip_coin()
        #if current_funds == 1000:
        #   break
        if flipped_coin_value == 'heads':
            win = current_bet * 2
            #print(f'{win=}')
            current_funds += win
            current_bet = min_bet
            heads1 += 1
        elif flipped_coin_value == 'ZERO':
            zero1 += 1
        else:
            #print('loose')
            tails1 += 1
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return steps_to_loose, max(current_funds_max), int(sum(current_funds_max) / len(current_funds_max)), zero1, heads1, tails1

# print(play_martingle(starting_funds=1000, min_bet=1, max_bet=100))


def simulate_play_martingle(*, starting_funds: int, min_bet: int, max_bet: int, n_games: int):
    total_steps_to_loose = []
    total_sum = []
    win_player = 0
    for i in range(n_games):
        step_to_loose = play_martingle(starting_funds=starting_funds, min_bet=min_bet, max_bet=max_bet)
        if step_to_loose[1] > 1000:
            win_player += 1
            #total_steps_to_loose.append(step_to_loose)
            total_sum.append(step_to_loose[1])
        
    
    return win_player, sum(total_sum) - n_games * starting_funds, total_steps_to_loose


print(simulate_play_martingle(starting_funds=100, min_bet=1, max_bet=100, n_games=10))