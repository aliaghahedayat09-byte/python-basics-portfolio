import sys
# give informaiton about score in Afghastan 
print("Afghanistan has a specific socre range that may different from some countires in the world. Every average score is counted put of 100 and then it is catagorized as A, B, C, D. ")
# aks user if they want to understand which level is their score
respond = input('Do you want to understand your score level: in which catagories you lie? ')
if respond == "yes":
    print("That is cool!")



else: 
    print("Okey, then, goodboy")
    sys.exit()


#ask user about his/her score
score = int(input("Enter your score: "))
if score >=90 and score <=100:
    print("A: Excellent ")
elif score >= 80 and score <90:
    print("B: very good")
elif score >=70 and score <80:
    print("C")
elif score >=60 and score <70:
    print("D")
elif score <60 and score >=0:
    print("you failed, sorry")

else:
    print("There is no information about it")


