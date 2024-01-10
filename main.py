from pprint import pprint

#Задание №1
#------------------------------------------------------------------------------------
def my_cook_book():
  with open('recipes.txt', 'r', encoding='utf-8') as file:
            cook_book = {}
            for line in file:
                dish = line.strip()
                ingredients_count = int(file.readline())
                ingredients = []
                for i in range(ingredients_count):
                    ingredient = file.readline().split(' | ')
                    ingredients.append({
                        'ingredient_name': ingredient[0],
                        'quantity': int(ingredient[1]),
                        'measure': ingredient[2].strip()
                    })
                cook_book[dish] = ingredients
                file.readline()
  return cook_book

#Задание №2
#------------------------------------------------------------------------------------
def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    if dish in my_cook_book():
      for ingredient in my_cook_book()[dish]:
        key, quantity, measure = ingredient.values()
        total_quantity = quantity * person_count
        if key in shop_list:
          shop_list[key]['quantity'] += total_quantity
        else:
          shop_list[key] = {
                            'quantity': total_quantity, 
                            'measure': measure, 
                            }
  return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

#Задание №3
#------------------------------------------------------------------------------------

def read_file(path1='1.txt', path2='2.txt', path3='3.txt'):
  result = []
  for path in [path1, path2, path3]:
    with open(path, 'r', encoding='utf-8') as f:
        file = f.readlines()
        result.append((path, len(file), file))
        result = sorted(result, key=lambda x: x[1])
  return result

def write_file():
  with open('4.txt', 'w', encoding='utf-8') as f:
    for name, num, text in read_file():
      f.write(f'{name}\n{num}\n{"".join(text)}\n')
    
write_file()
