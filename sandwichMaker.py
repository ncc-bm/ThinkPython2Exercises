import pyinputplus as pyip

price = {
    'wheat' : 15,
    'white' : 12,
    'sourdough' : 17,
    'chicken' : 23,
    'turkey' : 27,
    'ham' : 25,
    'tofu' : 20,
    'cheddar' : 19,
    'Swiss' : 21,
    'mozzarella' : 20,
    'mayo' : 7,
    'mustard' : 9,
    'lettuce' : 5,
    'tomato' : 8
}

totalPrice = 0 

print('Lets make a sandwith for you!')
print("Now let's choose the ingridients:")

breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], 'Please type the bread type:\n', numbered = True)
print('You chose %s type of bread' % breadType)
totalPrice += price[breadType]

proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 'Please type the bread type:\n', numbered = True)
print('You chose %s type of protein' % proteinType)
totalPrice += price[breadType]

withCheese = pyip.inputYesNo("Would you like to add a cheese? ")
print("You answered to the question \"Would you like to add a cheese /Yes(y)/No(n)/?\" %s" % withCheese)

if withCheese == "yes":
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], "Which cheese type you want to add?\n", numbered=True)
    print("You choose %s type of cheese" % cheeseType)
    totalPrice += price[cheeseType]

withMayo = pyip.inputYesNo("Would you like sandwich with mayo /Yes(y)/No(n)/? ")
if withMayo == "yes":
    totalPrice += price['mayo']

withMustard = pyip.inputYesNo("Would you like sandwich with mustard /Yes(y)/No(n)? ")
if withMustard == "yes":
    totalPrice += price['mustard']

withLettuce = pyip.inputYesNo("Would you like sandwich with lettuce /Yes(y)/No(n)? ")
if withLettuce == "yes":
    totalPrice += price['lettuce']
withTomato = pyip.inputYesNo("Would you like sandwich with tomato /Yes(y)/No(n)? ")

print("So your sandwich will be with mayo(%s), with mustard(%s), with lettuce(%s) and with tomato(%s)" % (withMayo, withMustard, withLettuce, withTomato))

sandwichCount = pyip.inputInt("How many sandwiches do you want? ", blank=False, min=1)

totalPrice *= sandwichCount

print("Your order will cost %s USD" % totalPrice)
