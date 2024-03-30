class Parrot:
    name = ""
    age = 0
    color = ""


parrot1 = Parrot()
parrot1.name = "Cyprian"
parrot1.age = 1829
parrot1.color = "Blue"

parrot2 = Parrot()
parrot2.name = "Cyril"
parrot2.age = 5
parrot2.color = "Orange"


class Eagle:
    name = ""
    age = 0
    color = ""


eagle1 = Eagle()
eagle1.name = "Athanaius"
eagle1.age = 800
eagle1.color = "bronze"

print(f"{parrot1.name} is {parrot1.age} years old")
print(f" The {eagle1.age} year old {eagle1.color} eagle name is {eagle1.name}")