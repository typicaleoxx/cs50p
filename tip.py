# tip calculator
"""def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # string input in format($##.##)
    # prints the after removing leading $, in float

def percent_to_float(p):
    # stript input in format(##%)
    # prints after removing %, in float


main()"""


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent) / 100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    remd = float(d.strip("$"))
    return remd


def percent_to_float(p):
    remp = float(p.strip("%"))
    return remp


main()
