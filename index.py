print("WELCOME TO MY COMPUTER QUIZ GAME 🙏")
print("Enter y for yes and n for no ")
playing=input("Do you want to play:-")
if playing=="y" or playing=="Y":
    print()
    print("Okay! let's play!")
    score=0
    print()
    Question1=input("Who developed Python Programming Language? \n (a) Wick van Rossum \n (b) Rasmus Lerdorf \n (c) Guido van Rossum \n (d) Niene Stom \n Answer:-")
    if Question1=="c":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question2=input(" Which of the following is the correct extension of the Python file? \n (a) .python \n (b) .pl \n (c) .py \n (d) .p \n Answer:-")
    if Question2=="c":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question3=input("What will be the value of the following Python expression? \n 4 + 3 % 5 \n (a) 7 \n (b) 2 \n (c) 4 \n (d) 1 \n Answer:-")
    if Question3=="a":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question4=input("Which keyword is used for function in Python language? \n (a) Function \n (b) def \n (c) Fun \n (d) Define \n Answer:-")
    if Question4=="b":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question5=input("Single-line comments in Python? \n (a) // \n (b) # \n (c) ! \n (d) /* \n Answer:-")
    if Question5=="b":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question6=input(" What will be the output of the following Python expression? \n round(4.576) \n (a) 4 \n (b) 4.6 \n (c) 5 \n (d) 4.5 \n Answer:-")
    if Question6=="c":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question7=input("What is output of print(math.pow(3, 2))? \n (a) 9.0 \n (b) None \n (c) 9 \n (d) None of the mentioned \n Answer:-")
    if Question7=="c":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question8=input("How is a code block indicated in Python? \n (a) Brackets \n (b) Indentation \n (c) Key \n (d) none \n Answer:-")
    if Question8=="b":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question9=input("Which of the following concepts is not a part of Python? \n (a) Pointer \n (b) loop \n (c) Dynamin type \n (d) All of above \n Answer:-")
    if Question9=="a":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    Question10=input("What will be the result of the following expression in Python “2 ** 3 + 5 ** 2”? \n (a) 22 \n (b) 33 \n (c) 169 \n (d) none \n Answer:-")
    if Question10=="b":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    print("YOUR TOTAL SCORE",score)
    print()
    print("THANK YOU FOR PLAYING THIS GAME")
    
else:
    print("Thank you for visiting")















