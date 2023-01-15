stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inv):
    print(':Inventory:')
    item_total=0
    for i in inv.items():
        print(i[1],i[0])
        item_total+=int(i[1])
    print("Total items in inventory: "+ str(item_total))
    
def addtoInventory(inventory,NewItems):
    for item in NewItems:
        inventory.setdefault(item,0)
        inventory[item]=(str(int(inventory[item])+1))

displayInventory(stuff)
print("\n"+"------------------------------"+"\n")

inv = addtoInventory(stuff, dragonLoot)
displayInventory(stuff)