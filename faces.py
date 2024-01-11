# implement a function named"convert"
# func accepts str input
# if the input contains :) it will return it replacing :) with 🙂
# if :( then replace with 🙁
def main():
    userinput = input("How was your day ?(describe with emoji)")
    print("Your input: ", userinput)
    print("After replacing: ", show(userinput))


def show(userinput):
    replace_userinput = userinput.replace(":)", "🙂").replace(":(", "🙁")
    return replace_userinput


main()
