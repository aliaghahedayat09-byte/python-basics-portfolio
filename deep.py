#ask the user about Great Question of Life, the Universe and Everything
# remove the space and make it lower
respond = input("What is the answer Great Question of Life, the Universe and Everything? ").strip().lower()
# use conditional as there are two posibilities 
if respond == "42" or respond == "forty-two" or respond == "forty two":
    print("Yes")

else: 
    print("No")



