height=float(input("enter you height(IN Meter)"))
weight=float(input("enter your weight (In Kg)"))
BMI=weight/height**2
print("your bmi is ",BMI)
if BMI <18.5:
    print("you are underweight")
else:
    if BMI >18.5 and BMI<25:
        print("your weight is normal")
    elif BMI>25 and BMI<30:
        print("you are slightly overweight,its fine!!")
    elif BMI>30 and BMI<35:
        print("you are obase! you should do exercise")
    else:
        print("you need to decrease some weight you are clinically obase")
