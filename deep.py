#ask the user answer for great question of life
#if inputs 42 forty-two or forty two return yes else no

def main():
    ask=input("The answer to the great question of life, the universe and literally everything is: ")
    user=ask.lower().strip()
    print(answer(user))
def answer(x):
    if x=="42" or x=="forty-two" :
        return("Yes")
    elif x=="forty two":
        return("Yes")
    else:
        return("No")
main()
    