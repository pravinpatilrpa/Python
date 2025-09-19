'enumerate - In simpler terms, it allows you to count objects in a collection. '
'The enumerate function works by iterating through each item in a collection and '
'returning the indexes of each object in that group.'
'The enumerate() function is mostly used in for loops.'

random_list = ["swing", "jump", "run", "crawl"]
for index, value in enumerate(random_list):
    print(f"Index: {index}, Value: {value}")

fruit_pair = {"A": "apple", "B": "banana", "C": "cherries", "D": "dragonfruit"}
for index, (key, value) in enumerate(fruit_pair.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

set_of_objects = {"calipers", "dividers", "compasses"}
for index, value in enumerate(set_of_objects):
    print(f"Index: {index}, Value: {value}")

random_tuple = ("Louise", "Clair", "Sam", "Chad")
for index, value in enumerate(random_tuple):
    print(f"Index: {index}, Value: {value}")