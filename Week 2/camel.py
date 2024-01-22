#implement a progam that prompts user for name
#of a variable in camel case and outputs in snake case
def main():
    user_name=str(input("Enter a variable name in camel case: "))
    snake_case(user_name)
def snake_case(name):
    for i in name:
        if i.isupper():
            print("_"+ i.lower(),end="")#using end"" so that it doesn't print in new line everytime
        else:
            print(i,end="")#end makes it print in same line
main()
    