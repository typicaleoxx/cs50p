#input an arithmetic operation in format of x y z 
#x and z are nos and y is operation
#does the operations and output in float
def main():
    x, y, z=input("Enter the expression? ").split()
    a=result(x,y,z)
    print(f"{float(a):.1f}")
def result(a,b,c):
    if b=="*":
        return int(a)*int(c)
    if b=="+":
        return int(a)+int(c)
    if b=="-":
        return int(a)-int(c)
    if b=="/":
        return int(a)/int(c)
main()