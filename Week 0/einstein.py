# Use the equation E=mc^2
# take m as input, use c=300000000
# calculate and print E
def main():
    userinput = input("Enter mass(m)? ")
    print("Energy(E)=", energy(userinput))


def energy(m):
    c = 300000000
    e = int(m) * pow(int(c), 2)
    return e


main()
