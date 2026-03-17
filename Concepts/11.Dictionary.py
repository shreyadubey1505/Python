# Dictionary
# consits of key value pairs={key:value}
# key must be unique,can be of any data type

# eg:Shopping =  {"chips": 10, "coke": 20, "bread": 30}
# print(Shopping) # Output: {'chips': 10, 'coke': 20, 'bread': 30}
# print(Shopping["chips"]) # Output: 10
# print(Shopping["coke"]) # Output: 20
# print(Shopping["bread"]) # Output: 30
# print(Shopping.keys()) # Output: dict_keys(['chips', 'coke', 'bread'])
# print(Shopping.values()) # Output: dict_values([10, 20, 30])
# print(Shopping.items()) # Output: dict_items([('chips', 10), ('coke', 20), ('bread', 30)])

# shopping["chips"] = 15# Update the value of the key "chips"
# print(shopping) # Output: {'chips': 15, 'coke': 20, 'bread': 30}]

# pop = used to remove the key value pair
# shopping.pop("chips") # Remove the key value pair with the key "chips"
# print(shopping) # Output: {'coke': 20, 'bread': 30}


# Nested list = dict + list
# eg: shopping ={ "beauty":["perfume", "shompoo", "lotion"], "grocery":["chips", "coke", "bread"],"shoes":["sneakers", "sandals", "boots"], "electronics":["phone", "laptop", "tablet"]}
# print(shopping) # Output: {'beauty': ['perfume', 'shampoo', 'lotion'], 'grocery': ['chips', 'coke', 'bread'], 'shoes':  ['sneakers', 'sandals', 'boots'], 'electronics': ['phone', 'laptop', 'tablet']}
# print(shopping["beauty"]) # Output: ['perfume', 'shompoo', 'lotion']
# print(shopping["beauty"][0]) # Output: perfume
# print(shopping["beauty"][1]) # Output: shampoo


# dictionary key : value(dictionary = key : value (list))
# eg : shopping = {
#     "beauty": {"perfume":["Axe","Set Wet"], "shampoo": ["Dove","Head and Shoulder"], "lotion": ["Boroplus","Nivia","Himalayas"]},

#     "grocery": {"chips":["Lays","Kurkure"], "coke":["Coca Cola","Pepsi"], "bread":["Bread","Bun"]}
#     "shoes": {"sneakers":["Nike","Adidas"], "sandals":["Reebok","Puma"], "boots":["Bata","Woodland"]}
#     "electronics": {"phone":["Samsung","Apple"], "laptop":["Dell","HP"], "tablet":["Lenovo","Acer"]}
# }
# print(shopping) # Output: {'beauty': {'perfume': ['Axe', 'Set Wet'], 'shampoo': ['Dove', 'Head and Shoulder'], 'lotion': ['Boroplus','Nivia', 'Himalayas']}, 'grocery': {'chips': ['Lays', 'Kurkure'], 'coke': ['Coca Cola', 'Pepsi'], 'bread': ['Bread',
# 'Bun']}, 'shoes': {'sneakers': ['Nike', 'Adidas'], 'sandals': ['Reebok', 'Puma'], 'boots': ['Bata', 'Woodland']
# }, 'electronics': {'phone': ['Samsung', 'Apple'], 'laptop': ['Dell', 'HP'], 'tablet': ['Lenovo', 'Acer']}}

# print(shopping["beauty"]) # Output: {'perfume': ['Axe', 'Set Wet'], 'shampoo': ['Dove', 'Head and Shoulder'], 'lotion': ['Boroplus', 'Nivia', 'Himalayas']}

#  print(shopping["beauty"]["perfume"]) # Output: ['Axe', 'Set Wet']
# print(shopping["beauty"]["perfume"][0]) # Output: Axe
# print(shopping["beauty"]["perfume"][1]) # Output: Set Wet
