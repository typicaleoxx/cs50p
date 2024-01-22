#ask time in format #:## or ##:##
#make convert function where if 7:30 converts in 7.30
#output breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

def main():
    user=input("What's the time ? in 24hr format eg 13:34 :")
    t=convert(user)
    print(f"{meal(t)} time")

def convert(time):
    hour,min=time.split(":")
    y=float(hour)+(float(min)/60)
    return y

def meal(h):
        if 7<=h<=8:
            return "breakfast"
        elif 12<=h<=13:
            return "lunch"
        elif 18<=h<=19:
            return "dinner"
if __name__ == "__main__":
    main()
