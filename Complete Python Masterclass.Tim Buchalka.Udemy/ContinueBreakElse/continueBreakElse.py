# shopping_list = ["soy milk", "pasta", "silk yogurt", "bananas", "bread", "rice"]
#
# for item in shopping_list:
#     if item == 'bread':
#         break
#
#     print("Buy " + item)

meal = ["soy milk", "pasta", "silk yogurt", "bananas", "bread", "rice"]

nasty_food_item = ''

for item in meal:
    if item == "tom":
        nasty_food_item = item
        break
else:
    print("I'll have a plate of pasta")

if nasty_food_item:
    print("I dont want anything with {} in it".format(meal[4]))

