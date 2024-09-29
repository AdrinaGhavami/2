#برنامه ای بنویسید یک عدد از کاربر دیافت کند سپس برسی کند کامل است یا خیر 
x = int(input("enter a number:"))
sm = 0
for i in range (1,x,1):
    if x % i == 0:
        sm = sm+i
if x == sm:
        print("perfect number")   
else:
        print("not perfect number")     
