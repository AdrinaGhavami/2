#  BMI برنامه ی نویسید که قد و وزن را از کاربر بگیرد سپس
# را حساب کند 
weight=float(input("enter your weight in (kg):"))
hight=float(input("enter your hight in (m):"))
bmi= weight/hight**2
print(f"your bmi is {round(bmi,2)}")
if 0<bmi<18.5:
    print(" underweight")
elif bmi>25:
    print(" overweight") 
elif 18.5<bmi<25:
    print(" normalweight")  
         