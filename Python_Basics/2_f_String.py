# Without f string
letter = "My name is {} and i am from {}"

name = "Anand"
country = "India"

print(letter.format(name, country))

letter = "My name is {0} and i am from {1}"

name = "Anand"
country = "India"

print(letter.format(country, name))

# With f string

letter = f"My name is {name} and i am from {country}"

print(letter)

# With f string and dictionary

person = {
    "name": "Anand",
    "country": "India"
}

letter = f"My name is {person['name']} and i am from {person['country']}"
print(letter) 