#How can we add the family pet, "Dino", to the following list?
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# method hunting to add to the end
flintstones.append('Dino')
print(flintstones)

# method hunting to add to the start.
flintstones.insert(0,'Dino')
print(flintstones)

# using a new list element to mutate an existing list.
flintstones = flintstones + ['Dino']
print(flintstones)

