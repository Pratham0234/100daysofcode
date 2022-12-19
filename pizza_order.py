print("welcome to pizza ordering cmd")
size=input("please enter size of pizza(s,m,l)")
pepperoni=input("do you need pepperoni (yes/no")
extra_chees=input("do you want extra cheese (yes/no)")

if size=='s' and pepperoni=='yes' and extra_chees=='yes':
    print("you have ordered small pizza with extra pepperoni and cheese. and your bill is 18$")
elif size=='s' and pepperoni=='yes' and extra_chees=='no':
    print('you have ordered small pizza with extra pepperoni and your bill is 17$')
elif  size=='s' and pepperoni=='no' and extra_chees=='no':
    print('you have ordered small pizza and your bill is 15$')
elif size=='m' and pepperoni=='yes' and extra_chees=='yes':
     print("you have ordered medium pizza with extra pepperoni and cheese. and your bill is 24$")
elif size=='s' and pepperoni=='yes' and extra_chees=='no':
    print('you have ordered medium pizza with extra pepperoni and your bill is 23$')
elif size=='s' and pepperoni=='no' and extra_chees=='no':
     print('you have ordered medium pizza and your bill is 20$')
elif size=='l' and pepperoni=='yes' and extra_chees=='yes':
    print("you have ordered large pizza with extra pepperoni and cheese. and your bill is 29$")
elif size=='s' and pepperoni=='yes' and extra_chees=='no':
    print("you have ordered large pizza with extra pepperoni . and your bill is 28$")
elif size=='s' and pepperoni=='yes' and extra_chees=='yes':
    print("you have ordered large pizza. and your bill is 25$")
else:
    print("value error :you ahve entered wrong wrong value")