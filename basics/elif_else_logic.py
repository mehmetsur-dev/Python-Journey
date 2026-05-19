# (else), (elif), day 2  
#the logistics logic

weight = 99

if weight < 10:
    print("Light")

elif weight <= 50:
    print("Medium")

elif weight <= 100:
    print("Heavy")

#this catches anything over 100
else: 
    print("Extreme")
