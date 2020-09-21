# Write your code here
import math

# lines = ["Starting to make a coffee",
# "Grinding coffee beans",
# "Boiling water",
# "Mixing boiled water with crushed coffee beans",
# "Pouring coffee into the cup",
# "Pouring some milk into the cup",
# "Coffee is ready!"]

# for line in lines:
#     print(line)

# print("Write how many ml of water the coffee machine has:")
# w = int(input())

# print("Write how many ml of milk the coffee machine has:")
# m = int(input())

# print("Write how many grams of coffee beans the coffee machine has:")
# b = int(input())

# print("Write how many cups of coffee you will need:")
# c = int(input())

# mw = math.floor(w / 200)
# mm = math.floor(m / 50)
# mb = math.floor(b / 15)
# mc = min([mw, mm, mb])

# if mc == c:
#     print("Yes, I can make that amount of coffee")
# elif mc < c:
#     print("No, I can make only {N} cups of coffee".format(N=mc))
# elif mc > c:
#     print("Yes, I can make that amount of coffee (and even {N} more than that)".format(N=(mc - c)))
    

# print("For {cups} of coffee you will need:".format(cups=c))
# print(c * 200, "ml of water")
# print(c * 50, "ml of milk")
# print(c * 15, "g of coffee beans")

water = 400
milk = 540
beans = 120
cups = 9
money = 550

def check(w, m, b):
    global water
    global milk
    global beans
    global cups
    global money

    if water < w:
        print("Sorry, not enough water!")
        return False
    elif milk < m:
        print("Sorry, not enough milk!")
        return False
    elif beans < b:
        print("Sorry, not enough coffee beans!")
        return False
    elif cups < 1:
        print("Sorry, not enough cups!")
        return False
    else:
        cups -= 1
        print("I have enough resources, making you a coffee!")
        return True
           

def buy():
    global water
    global milk
    global beans
    global cups
    global money
    
    print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    ba = input()
    
    if ba == '1' and check(250, 0, 16):
        water -= 250
        beans -= 16
        money += 4
    elif ba == '2' and check(350, 75, 20):
        water -= 350
        beans -= 20
        milk -= 75
        money += 7
    elif ba == '3' and check(200, 100, 12):
        water -= 200
        beans -= 12
        milk -= 100
        money += 6

def fill():
    global water
    global milk
    global beans
    global cups
    
    print("\nWrite how many ml of water do you want to add:")
    aw = int(input())
    water += aw
    
    print("Write how many ml of milk do you want to add:")
    am = int(input())
    milk += am
    
    print("Write how many grams of coffee beans do you want to add:")
    ab = int(input())
    beans += ab
    
    print("Write how many disposable cups of coffee do you want to add:")
    ac = int(input())
    cups += ac

def take():
    global money
    
    print("\nI gave you ${money}".format(money=money))
    money = 0

def remaining():
    if money == 0:
        ccy = ''
    else:
        ccy = '$'
    print("\nThe coffee machine has:")
    print("{water} of water".format(water=water))
    print("{milk} of milk".format(milk=milk))
    print("{beans} of coffee beans".format(beans=beans))
    print("{cups} of disposable cups".format(cups=cups))
    print("{ccy}{money} of money".format(ccy=ccy, money=money))

def main():
    print("\nWrite action (buy, fill, take, remaining, exit):")
    action = input()

    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()
    elif action == 'exit':
        exit()

while 1 == 1:
    main()
