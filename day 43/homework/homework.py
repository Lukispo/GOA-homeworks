def count_items(item_list, item):
    return item_list.count(item)
items = ["apple", "banana", "orange", "apple", "kiwi"]
result = count_items(items, "apple")
print("'apple' appears " + str(result) + " times in the list.")
