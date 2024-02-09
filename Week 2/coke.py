# A bottle of coke costs 50 cents
# only accept coins of: 25,10,5
# implement a program that prompt a user to insert a coin
# inform amount due each time
# after user put total of 50 cents, print due
# assume user input only integers and ignore any integer that isn't 25,10,5
def main():
    while True:
        user_coin = int(input("Insert the coin(25,10,5): "))
        print(f"Your due amount :{amount_due(user_coin)}")
        if amount_due(user_coin) != 0:
            continue


def amount_due(cents):
    if (cents == 25 or cents == 10) or cents == 5:
        coin = coin + cents
        return 50 - coin
    else:
        return 50


main()
