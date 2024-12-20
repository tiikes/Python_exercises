dictionary1 = {"kissa": 1,"koira": 2,"apina": 3}

dictionary2 = {"possu": 4,"lehmä": 5,"lammas": 6}

merged = dictionary1.copy()
merged.update(dictionary2)

print("Merged dictionary:", merged)