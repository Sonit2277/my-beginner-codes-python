a=int(input("enter your marks (out of 100): "))

if 0>a or a>100:
    print("invalid input")
elif a>=90:
    print("grade: A")

elif a>=80:
    print("grade: B")   
elif a>=70:
    print("grade: C")
elif a>=60:
    print("grade: D")
else:    
    print("grade: F")