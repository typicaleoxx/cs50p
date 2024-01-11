#ask user for a greeting
#if says hello return $100
#if says greeting with word h like hey then $20
#else $0

def main():
    ask=input("Greeting? ")
    user=ask.lower().strip()
    print(reward(user))
def reward(x):
        if x.startswith("hello"):
                return "$0"
        elif x.startswith("h"):
            return("$20")
        else:
            return("$100")
    
main()
