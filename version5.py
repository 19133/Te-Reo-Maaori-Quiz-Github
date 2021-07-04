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
    
    if user_quiz_difficulty_response == "xxx":
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
    quiztyperesponse = input (question) .lower()

    if quiztyperesponse == "multiple choice" or quiztyperesponse  == "multi" or quiztyperesponse  == "multi choice":   
        quiztyperesponse = "multiple"
        return quiztyperesponse
      
    elif quiztyperesponse == "Timed quiz" or quiztyperesponse  == "timed" or quiztyperesponse  == "time":   
        quiztyperesponse = "timed"
        return quiztyperesponse

    if quiztyperesponse == "normal quiz" or quiztyperesponse  == "normal" or quiztyperesponse  == "normal question":   
        quiztyperesponse = "normal questions"
        return quiztyperesponse
    
    if quiztyperesponse == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()

    else:
      print("type normal, multiple, or timed")
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
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori skill")
  print("It has many easy and hard difficulties and different types of modes such as normal, multiple choice, or timed quesions")

# asks the user to say yes or no and repeats question
else:
  print("Please say yes or no")
  print("Or type xxx to quit") 



# asks user what difficulty they want to play, 1 is easy, 2 is moderate, 3 is hard
played_before = quiz_difficulty (name + "what difficulty do you want to play"  " 1 is easy, 2 is normal, 3 is hard " + "\n")

# if 3, The student will be given hard questions
if played_before == "3":
  print("Thats great")
  
  # asks user what type of quiz they want to play
  quiztype = type_of_quiz ("There are 3 type of quizes, Multiple choice, timed, or normal . Which one would you like to play" + "\n")
  # if multiple choice, the user will have a lot of answers to pick out of but only one of them is correct.
  if quiztype == "multiple choice":
      print("Thats amazing!")
      print("You will be given multiple choice and you will have to pick one")
      

  # if timed, the user will have a certian amount of time to answer the question. 
  if quiztype == "timed":
      print("Thats amazing")
      print("You will be given a amount of time to answer questions")

  # if normal, the user will be asked questions normally. Normal means they will be asked to answer and there will be no timer nor multiple choices for the user to pick out of. 
  if quiztype == "normal":
      print("Program continues")

  # else, the user will be asked to 
  else:
    print("Please type multi, timed, or classic")
    print("Or type xxx to quit") 


# if 2, Then the student will be given moderate level questions
elif played_before == "2":
  print("Thats awesome")
  quiztype = type_of_quiz ("There are 3 type of quizes, Multiple choice, timed, or normal . Which one would you like to play" + "\n")

  # if multiple choice, the user will have a lot of answers to pick out of but only one of them is correct.
  if quiztype == "multiple choice":
      print("Thats amazing!")
      print("You will be given multiple choice and you will have to pick one")
      

  # if timed, the user will have a certian amount of time to answer the question. 
  if quiztype == "timed":
      print("Thats amazing")
      print("You will be given a amount of time to answer questions")

  # if normal, the user will be asked questions normally. Normal means they will be asked to answer and there will be no timer nor multiple choices for the user to pick out of. 
  if quiztype == "normal":
      print("Program continues")

  # else, the user will be asked to 
  else:
    print("Please type multi, timed, or classic")
    print("Or type xxx to quit") 

# if 1, then user will be asked easy questions
elif played_before == "1":
  print("Thats great")
  quiztype = type_of_quiz ("There are 3 type of quizes, Multiple choice, timed, or normal . Which one would you like to play" + "\n")
  # if multiple choice, the user will have a lot of answers to pick out of but only one of them is correct.
  if quiztype == "multiple choice":
      print("Thats amazing!")
      print("You will be given multiple choice and you will have to pick one")
      

  # if timed, the user will have a certian amount of time to answer the question. 
  if quiztype == "timed":
      print("Thats amazing")
      print("You will be given a amount of time to answer questions")

  # if normal, the user will be asked questions normally. Normal means they will be asked to answer and there will be no timer nor multiple choices for the user to pick out of. 
  if quiztype == "normal":
      print("Program continues")

  # else, the user will be asked to 
  else:
    print("Please type multi, timed, or classic")
    print("Or type xxx to quit") 



# quiz questions (These are not the questions that will be in the quiz, these questions are here for testing purposes) and answers
QnA= {
"How many days are there in a year?":"365", 
"How many years are in a century?":"100", 
"How many hours are in a day":"24",
"What year is it":"2021"
}   
#The questions
question = list(QnA.keys())
#input answer here 
while True:
    if not question:
        break
    ques = random.choice(question)
    print(ques)
    while True:
        answer = input('Answer ' )
        # if correct, moves onto next question
        if answer == QnA[ques]:
            print("Correct Answer")
            print("Next question")
            break
        else:
            #if wrong, Asks the same question again
            print("Wrong Answer, try again")
            do_you_want_a_clue = input("would you like a clue")
            if do_you_want_a_clue == "yes" or do_you_want_a_clue == "y":
              print("It is between the number 362 and 366")
    question.remove(ques)
