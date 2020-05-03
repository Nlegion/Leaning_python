import json
import pickle

my_favourite_group = {'name': 'Г.М.О.', 'tracks': ['Последний месяц осени', 'Шапито'],'Albums': [{'name': 'Делать панк-рок','year': 2016}, {'name': 'Шапито','year': 2014}]}

print(my_favourite_group)

j_group = json.dumps(my_favourite_group)
print(j_group)

p_group = pickle.dumps(my_favourite_group)
print(p_group)

with open('group.json','w',encoding='utf-8') as f:
   json.dump(my_favourite_group,f)

with open('group.pickle', 'wb') as f:
   pickle.dump(my_favourite_group,f)
