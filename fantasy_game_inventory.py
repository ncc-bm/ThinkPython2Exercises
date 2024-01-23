dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot2 = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'tilla tanga', 'kumush tanga']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory



displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
print()
displayInventory(stuff)
print()
stuff = addToInventory(stuff, dragonLoot2)
displayInventory(stuff)