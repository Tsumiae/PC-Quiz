name = input("Enter your name: ")

playing = input("do you want to play my game?: ")

if playing != "yes":
    quit()

print("welcome to my game", name, "enjoy yourself")
score = 0

answer = input("What does gpu stand for?: ")
if answer.lower() == "graphical processing unit":
    print ("correct")
    score += 1
else:
    print("incorrect!")
    

answer = input("What does ram stand for?: ")
if answer.lower() == "random access memory":
    print ("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What does PSU stand for?: ")
if answer.lower() == "power supply":
    print ("correct")
    score += 1
else:
    print("incorrect!")


    

print("you got " + str(score) + " questions right congratulations!")


   


