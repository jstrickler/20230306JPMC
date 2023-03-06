actor = "Chris Hemsworth"
print(actor.upper())
print(actor)
print(len(actor))
a = actor.upper()
print(a)
print(actor.count('h'))
print(actor.count('H'))
print(actor.count('z'))
print(actor.count('is'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("Hem" in actor)
print("Wombat" in actor)

print(actor.removesuffix('worth'))
print(actor.removeprefix("Ch"))

file_path = "foo.txt"
print(file_path.removesuffix('.txt'))

print(actor.find("Hem"))
print(actor.find("Chris"))
print(actor.find("Liam"))
print(actor.replace("Chris", "Liam"))
print(actor.replace("Hems", ""))
print(actor.replace("Hems", "").replace("Ch", "K").title())

record = "Francis\tSinatra"
fields = record.split()
print(fields)
record = "Frank Sinatra"
fields = record.split()
print(fields)
record = "Frank#Sinatra"
fields = record.split('#')
print(fields)

s = "            Fly Me To the Moon          "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")

s = "hhhyyyylllllooooolllyFly Me To the Moonyyyyhhllollloooollllyyy"
print(s)
print(s.lstrip("holy"))  # remove any of 'h', 'o', 'l', 'y'
print(s.rstrip("holy"))
print(s.strip("holy"))


amount = "$123.45"
amount = amount.lstrip("$")
print(amount)

country = "Bulgaria"
print(country.upper())
x = country.lower()
print(x)
print(country)

print(actor.replace("Hems", "").replace("Ch", "K").title())

a = "winter"
b = "green"
c = "s"
print(a + b + c)







