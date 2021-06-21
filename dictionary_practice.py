Foods = {"Chicken":1.59, "Beef":1.99, "Cheese":1.00, "Milk":2.50, "Pork":2.00, "Fish":2.50, "Ham":1.00}
NBA_players = {"LeBron James":23, "Kevin Durant":35, "Stephen Curry":30, "Damian Lillard":0}
NBA_players["Luka Doncic"] = 77

chicken_price = Foods["Chicken"]
beef_price = Foods["Cheese"]
cheese_price = Foods["Cheese"]
milk_price = Foods["Milk"]
pork_price = Foods["Pork"]
fish_price = Foods["Fish"]
ham_price = Foods["Ham"]
print(chicken_price, beef_price, cheese_price, milk_price, pork_price, fish_price, ham_price)

def total_price(item1, item2):
    sum = Foods[item1] + Foods[item2]
    print("The total price of",item1, "and", item2, "is",  sum)
    return sum
total_price("Beef", "Chicken")

def price_difference(item1, item2):
    difference = Foods[item1] - Foods[item2]
    print("The difference between", item1, "and", item2, "is", abs(round(difference, 2)))
    return difference
price_difference("Beef", "Chicken")


Steph_jersey = NBA_players["Stephen Curry"]
LeBron_jersey = NBA_players["LeBron James"] = 6
Kevin_jersey = NBA_players["Kevin Durant"]
Damian_jersey = NBA_players["Damian Lillard"]
Luka_jersey = NBA_players["Luka Doncic"]
print(Steph_jersey, LeBron_jersey, Kevin_jersey, Damian_jersey, Luka_jersey)

del NBA_players["Kevin Durant"]
print (NBA_players)
del Foods["Ham"]
print(Foods)

Shoes = {"Jordan 13":1, "Yeezy":8, "Foamposite":10, "Air Max":5, "SB Dunk":20}
SB_Dunk = Shoes["SB Dunk"] = ((20 - 2) + 7) -3
Yeezy = Shoes["Yeezy"] = ((8 + 1) + 7) - 3
Jordan_13 = Shoes["Jordan 13"] = (1 + 7) - 3
Foamposite = Shoes["Foamposite"] = (10 + 7) - 3
Air_Max = Shoes["Air Max"] = (5 + 7) - 3
print(SB_Dunk, Yeezy, Jordan_13, Foamposite, Air_Max)

def Restock(shoes, amount):
    Updated_shoes = Shoes[shoes] * amount
    Shoes["Yeezy"] = Updated_shoes
    return(Shoes)
Restock("Yeezy", 2)

def Clearance_sale(shoe, amount):
    Updated_shoe = Shoes[shoe] / amount 
    Shoes["Jordan_13"] = Updated_shoe 
    return(Shoes)
Clearance_sale("Jordan_13", 5)

