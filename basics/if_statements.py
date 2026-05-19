#day1 (if)

my_money = 80
item_price = 80

# after every (if) we have to add (:) this to end
if my_money >= item_price:
    print("i can afford this")

    # We can put (if) inside an (if)
    if my_money == item_price:
        print("...but i will have zero left")
    
