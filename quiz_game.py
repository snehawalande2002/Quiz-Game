print("Welcome to my computer quiz..")

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit()

print("Okay! lets play :)")
score = 0

answer = input("What does CPU stand for?  ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1    # score = score+1
else:
    print("Incorrect!")

y= input("Do you want to continue? ")
if y.lower() != "yes":
    print("You will not get your score until you finish the quiz..")
    quit()


answer = input("What does GPU stand for?  ")
if answer.lower() == "graphics processing unit":
        print("Correct! ")
        score += 1
else:
    print("Incorrect!")

y= input("Do you want to continue? ")
if y.lower() != "yes":
    print("You will not get your score until you finish the quiz..")
    quit()

answer = input("What does RAM stand for?  ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

y= input("Do you want to continue? ")
if y.lower() != "yes":
    print("You will not get your score until you finish the quiz..")
    quit()

answer = input("What does PSU stand for?  ")
if answer.lower() == "power supplay uint":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

print("Thanks for completing the quiz")

print("You got  " + str(score) + " questions correct")
print("You got " + str((score / 4) * 100) + " %")


















