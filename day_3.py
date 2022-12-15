yourName = input("Name: ")
whatYear = input("What year is it?: ")
print(yourName, "thinks it is", whatYear)

"""New Code to debug"""
print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print(rhyme)
print("There was a person called", person)
print("Who did something cool like", thing, "at the wonderful", place ,"where you'll find me", rhyme)

"""New code for Menu"""
food = input("Name a food > ")
plant = input("Name a type of plant > ")
cooking_method = input("Name a cooking method > ")
burned_des = input("What word describes a burned food? >")
diy = input("Name a DIY item > ")
print("MENU")
print(f"{cooking_method} {food} with {burned_des} {plant} on a bed of {diy}")