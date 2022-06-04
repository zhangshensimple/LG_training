pizza_inventory=['durian','chicken','durian']
for i in pizza_inventory:
    if i == 'bacon':
        pizza_inventory.remove(i)
        print('A bacon pizza was deleted from list.')
        break
    else:
        print('There is really no bacon in pizza_inventory!')
