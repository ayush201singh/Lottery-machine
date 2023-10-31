import random



ROWS = 3
COLS = 3

symbol_count = {"A":2 , "B":3, "C":4, "D":5}

symbol_value = {"A":5 , "B":4, "C":3, "D":2}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)

    return winnings, winning_lines




def slot_machine(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



def deposit():
    while True:
        amount = int(input("enter the amount in digits: $"))
        if amount>0:
            break
        else:
            print("please enter an amount")
    return amount

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def get_number_of_lines():
    while True:
        lines = int(input("enter the number of lines to bet on (1-"+str(MAX_LINES)+")?"))
        if lines>=1 and lines<=MAX_LINES:
            break
        else:
            print("enter valid number of lines")
    return lines

def get_bet():
    while True:
        amount = int(input("enter the amount you would like to bet on a line? $"))
        if amount>=MIN_BET and amount<=MAX_BET:
            break
        else:
            print(f"enter the amount between ${MIN_BET}-${MAX_BET}")
    return amount

    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet>balance:
            print(f"you do not have enough balance to bet {bet} on each line, your balance is {balance}")
        
        else:
            break

    print(f"your balance is: {balance}\nnumber of lines to bet on is {lines} \nthe amount you are betting on one line is {bet}\nthe amount you are betting is {total_bet}")
    slots = slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"you win {winnings}")
    print(f"you won on line: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        game = input("press enter to start game (q to quit)")
        if game== "q":
            break
        balance += spin(balance) 
    
    print(f"you left with ${balance}")

main()



