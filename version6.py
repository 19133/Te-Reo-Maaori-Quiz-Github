import random
import time




def yes_no(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "yes" or user_response  == "y":   
        user_response = "yes"
        return user_response
      
    elif user_response == "no" or user_response  == "n":
        user_response = "no"
        return user_response 

    elif user_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()     

    else:
      print("Please say yes or no") 
      print("Or type xxx to quit") 


def quiz_difficulty(question):
  valid=False
  while not valid:
    user_quiz_difficulty_response = input (question) .lower()

    if user_quiz_difficulty_response == "3" or user_quiz_difficulty_response  == "three":   
        user_quiz_difficulty_response = "3"
        return user_quiz_difficulty_response
      
    elif user_quiz_difficulty_response == "2" or user_quiz_difficulty_response  == "two":
        user_quiz_difficulty_response = "2"
        return user_quiz_difficulty_response 

    elif user_quiz_difficulty_response == "1" or user_quiz_difficulty_response  == "one":
        user_quiz_difficulty_response = "1"
        return user_quiz_difficulty_response 
    
    elif user_quiz_difficulty_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()

    else:
     print("Plese pick 1, 2 or 3.")
     print("1 is easy, 2 is normal, 3 is hard")
     print("Or type xxx to quit") 




def type_of_quiz(question):
  valid=False
  while not valid:
    quiztyperesponse = input (question).lower()

    if quiztyperesponse == "multi" or quiztyperesponse == "multiple quiz" or quiztyperesponse == "multiple":
      return quiztyperesponse

    elif quiztyperesponse == "timed" or quiztyperesponse == "timed quiz" or quiztyperesponse == "time":
      return quiztyperesponse

    elif quiztyperesponse == "normal" or quiztyperesponse == "normal quiz":
      return quiztyperesponse

    


    

    elif quiztyperesponse == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()

    else:
       print("Please type multi, timed, or normal")
       print("Or type xxx to quit")






# Main routine
print("Welcome to the Te Reo Maaori quiz")
print("What is your amazing name?")
name = input ( )
print("Kia Ora " + name)

#asks user if they have played the te maaori quiz
played_before = yes_no ("Have you played the Te Reo Maori quiz " + name + "?" + "\n" )

# if yes, program continues
if played_before == "yes":
  print("program continues")
  
# if no, explains what the quiz is
elif played_before == "no":
  print("Thats ok")
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori language skill")
  print()
  print("It has many easy and hard difficulties and different types of modes such as normal, multiple choice, or timed quesions")
  print()


elif played_before == "xxx":
  print("Thanks for playing the Te Reo Maaori quiz")
  print("We hope to see you again")
  time.sleep(2)
  exit()     

else:
  print("Please say yes or no") 
  print("Or type xxx to quit") 


# asks user what difficulty they want to play, 1 is easy, 2 is moderate, 3 is hard
played_before = quiz_difficulty (name + " what difficulty do you want to play"  " 1 is easy, 2 is normal, 3 is hard " + "\n")

# if 3, The student will be given hard questions
if played_before == "3":
  print("Thats great")
  
  # asks user what type of quiz they want to play
  quiztype = type_of_quiz ("There are 3 type of quizes, Multiple choice, timed, or normal . Which one would you like to play" + "\n")

  # if multiple choice, the user will have a lot of answers to pick out of but only one of them is correct.
  if quiztype == "multi":
    print("thats good")
    print ("I hope you're ready")
    print()
    print("Make sure to type in letters")

    round = 1
    while True:
        print("Round %d" % round)
        print()
        Questionnaires = {
        "What is ocean in Te Reo Maaori? \n A. 366\n B. 365\n C. 366 \n D. 363":"b",
        "What is red in Te Reo Maaori?  \n A. 10 years \n B. 50 years \n C. 100 years \n D. 75" :"c",
        "If it is Ua it is what? \n A. 24 hours \n B. 22 hours \n C. 20 hours \n D. 21 hours ":"a",
        "? \n A. 2020 \n B. 2022 \n C. 2021 \n D. 2019" : "c"
    }   

    score = 0
    #The questions
    question = list (Questionnaires.keys())
    #input answer here 
    while True:
        if not question:
            break
        ques = random.choice(question)
        print(ques)
        while True:
            answer = input('Answer ' )
            # if correct, moves onto next question
            if answer.lower() == Questionnaires[ques]:
                print("Correct Answer")
                print ()
                score+=1
                print("total score is", score)
                print()
                break
            else:
                #if wrong, Asks the same question again
                print("Wrong Answer, try again")
                score-=1
                if score < 1:
                  score = 0
                print ("Your score is now", score)
        question.remove(ques)

    # same codes inside while loop

    exit_code = input("Would you like to play the next round (Your score will reset)")

    if exit_code == "yes":
      print ("I hope your ready for the next round")
      print()
      print()
      round += 1

    if exit_code == "no":
      print("Thanks for playing")
      exit()
        





  # if timed, the user will have a certian amount of time to answer the question. 
  elif quiztype == "timed":
    print("thats good")

  # if normal, the user will be asked questions normally. Normal means they will be asked to answer and there will be no timer nor multiple choices for the user to pick out of. 
  elif quiztype == "normal":
    print("thats good")
  
  # else, the user will be asked the question again
  else:
    print("Please type multi, timed, or normal")
    print("Or type xxx to quit")



  
  print("I hope you're ready")

elif played_before == "2":
  print("Thats great")
  
    # asks user what type of quiz they want to play
  quiztype = type_of_quiz ("There are 3 type of quizes, Multiple choice, timed, or normal . Which one would you like to play" + "\n")

  # if multiple choice, the user will have a lot of answers to pick out of but only one of them is correct.
  if quiztype == "multi":
    print("thats good")

  # if timed, the user will have a certian amount of time to answer the question. 
  elif quiztype == "timed":
    print("thats good")

  # if normal, the user will be asked questions normally. Normal means they will be asked to answer and there will be no timer nor multiple choices for the user to pick out of. 
  elif quiztype == "normal":
    print("thats good")
  
  # else, the user will be asked the question again
  else:
    print("Please type multi, timed, or normal")
    print("Or type xxx to quit")


if played_before == "1":
  print("Thats great")
  
  # asks user what type of quiz they want to play
  quiztype = type_of_quiz ("There are 3 type of quizes, Multiple choice, timed, or normal . Which one would you like to play" + "\n")

  # if multiple choice, the user will have a lot of answers to pick out of but only one of them is correct.
  if quiztype == "multi":
    print("thats good")

  # if timed, the user will have a certian amount of time to answer the question. 
  elif quiztype == "timed":
    print("thats good")

  # if normal, the user will be asked questions normally. Normal means they will be asked to answer and there will be no timer nor multiple choices for the user to pick out of. 
  elif quiztype == "normal":
    print("thats good")
  
  # else, the user will be asked the question again
  else:
    print("Please type multi, timed, or normal")
    print("Or type xxx to quit")


print()
print()  
# quiz questions (These are not the questions that will be in the quiz, these questions are here for testing purposes) and answers
round = 1
while True:
    print("Round %d" % round)
    print()
    
    Questionnaires = {
      "How many days are there in a year?":"365", 
      "How many years are in a century?":"100", 
      "How many hours are in  a day":"24",
      "What year is it":"2021"
    }   

    score = 0
    #The questions
    question = list (Questionnaires.keys())
    #input answer here 
    while True:
        if not question:
            break
        ques = random.choice(question)
        print(ques)
        while True:
            answer = input('Answer ' )
            # if correct, moves onto next question
            if answer.lower() == Questionnaires[ques]:
                print("Correct Answer")
                print ()
                score+=1
                print("total score is", score)
                print()
                break
            else:
                #if wrong, Asks the same question again
                print("Wrong Answer, try again")
        question.remove(ques)

    # same codes inside while loop

    exit_code = input("Would you like to play the next round (Your score will reset)")

    if exit_code == "yes":
      print ("I hope your ready for the next round")
      print()
      print()
      round += 1

    if exit_code == "no":
      print("Thanks for playing")
      exit()
