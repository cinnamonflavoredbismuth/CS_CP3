#Cecily Strong Quiz game
"""
INSTRUCTIONS:
Create a quiz game that asks the user at least 10 questions (randomly selected from a csv that holds at least 50 questions [yes you can use AI to create your questions and answers]).

Let users answer (they should be multiple choice questions but make sure your user knows what to do to select their choice)

Tell the user if they got the question right or wrong

Give the overall score at the end

The program needs to run until the user selects to quit

MORE CHALLENGES:
Create a user interface with tkinter or turtle that lets users click on the answers they want
Allow users to select from different lists of questions
Allow users to create lists of questions
User profiles (Admin users can create new lists of questions, normal users can just select from lists of questions to do)
Give different point amounts based on how quickly they answer
Shuffle the order the answers are displayed 

KEY REMINDERS:
CSV's use a csvreader
Think carefully about the data types you want to use!
Make clear user instructions for how they answer questions
Don't forget to plan extra debugging time! You can always add more once you have an MVP!"""
import csv
import random

def debug():
    import trace
    import sys
    def trace_calls(frame,event,argument):
        func=frame.f_code.co_name
        """ignore=['__init__','_shutdown','ident','_stop','daemon','_maintain_shutdown_locks']
        if func in ignore:
            pass
        else:"""
        if event == 'call': #when function is called
            #f_code: the file
            #co_name: the function
            #f_code.co_name: function name
            print(f'Calling function: {frame.f_code.co_name}')

        elif event == 'line': #when a new line of code happens
            #lineno: line number
            print(f'    Executing line {frame.f_lineno} in {frame.f_code.co_name}')

        elif event == 'return': #When we return stuff
            print(f'    {frame.f_code.co_name} returned {argument}')

        elif event == 'exception': #Triggered when there is an exception
            print(f'    Exeption in {frame.f_code.co_name}: {argument}')

        return trace_calls
    sys.settrace(trace_calls)

class question:
    def __init__(self,topic,question,answer):
        self.topic=topic
        self.question=question
        self.answer=answer

    def __str__(self):
        return(f"Q: {self.question}, A: {self.answer}")
    
    def answer_check(self,ans):
        try:
            if self.answer==ans:
                return True
            else:
                return False
        except:
            print("Error with Answer check")

    def export_question(self,file="quiz-game/questions.csv"):
        with open(file,"a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([self.topic,self.question,self.answer])

class quiz:
    def __init__(self,master_questions=[],questions=[],answers=[]):
        self.master_questions=master_questions
        self.questions=questions
        self.answers=answers
        self.question_gather()
        self.question_list()

    def question_gather(self,topic="all",file="quiz-game/questions.csv"):
        with open(file,"r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if len(row)==0:
                    pass
                else:
                    if topic == "all":
                        q=question(row[0],row[1],row[2])
                        self.master_questions.append(q)
                    else: 
                        if row[0] == topic:
                            q=question(row[0],row[1],row[2])
                            self.master_questions.append(q)
                        else: pass
                    #print(q)

    def get_topics(self):
        topics=[]
        with open("quiz-game/questions.csv","r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if len(row)==0:
                    pass
                else:
                    if row[0] not in topics:
                        topics.append(row[0])
        return topics
    
    def topic_choice(self):
        topics=self.get_topics()
        print("Available topics:")
        for i, topic in enumerate(topics, start=1):
            print(f"{i}. {topic}")
        choice = input("Select a topic by number or type 'all' for all topics: ")
        if choice.isdigit() and 1 <= int(choice) <= len(topics):
            return topics[int(choice) - 1]
        elif choice.lower() == 'all':
            return "all"
        else:
            print("Invalid choice. Defaulting to 'all'.")
            return "all"

    def __str__(self):
        for question in self.master_questions:
            print(question)
        return ""
    
    def question_list(self):
        for question in self.master_questions:
            self.questions.append(question.question)
            self.answers.append(question.answer)
        return self.questions, self.answers
    def scramble(self,list):
        random.shuffle(list)
        return list
    
    def answer_options(self):
        options=[]
        while len(options) < 4:
            question=random.choice(self.answers)
            if question in options:
                pass
            else:
                options.append(question)
        return self.scramble(options)
    
    def give_question(self):
        question=random.choice(self.master_questions)
        options=self.answer_options()
        def valid_check(answer=input(f'{question.question}\nA. {options[0]}\nB. {options[1]}\nC. {options[2]}\nD. {options[3]}\n')):
            try:
                if answer.lower() == 'a':
                    answer = options[0]
                elif answer.lower() == 'b':
                    answer = options[1]
                elif answer.lower() == 'c':
                    answer = options[2]
                elif answer.lower() == 'd':
                    answer = options[3]
                else:
                    print("Invalid option. Please select A, B, C, or D.")
                    valid_check()
                return answer
            except: 
                print("Error with give question")
                valid_check()
        answer=valid_check()
        if question.answer_check(answer):
            print("Correct!")
            self.master_questions.pop(self.master_questions.index(question))  # Remove the question from the pool
            self.questions.remove(question.question)  # Remove the question from the questions list
            return 1
        else:
            print("Incorrect!")
            self.master_questions.pop(self.master_questions.index(question))  # Remove the question from the pool
            self.questions.remove(question.question)  # Remove the question from the questions list
            return 0
        
    def add_questions(self,user):
        if user.get_permission()==True:
            topic = input("Enter the topic of the question: ")
            question_text = input("Enter the question: ")
            answer = input("Enter the answer: ")
            new_question = question(topic, question_text, answer)
            self.master_questions.append(new_question)
            self.questions.append(question_text)
            self.answers.append(answer)
            new_question.export_question()
            print("Question added successfully.")

class user:
    def __init__(self,name='Guest'):
        self.name=name
        self.permissions="normal"  # Default permission level
        self.score=0
        self.questions_answered=0
    
    def __str__(self):
        return f"User: {self.name}, Permissions: {self.permissions}, Score: {self.score}, Questions Answered: {self.questions_answered}"
    
    def import_user(self,name,file="quiz-game\user_data.csv"):
        with open(file,"r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if len(row)==0:
                    pass
                else:
                    if name != row[0]:
                        pass
                    else:
                        self.name=row[0]
                        self.permissions=row[1]
                        self.score=int(row[2])
                        self.questions_answered=int(row[3])

    def export_user(self,file="quiz-game\user_data.csv"):
        with open(file,"a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([self.name,self.permissions,self.score,self.questions_answered])

    def update_score(self,points):
        self.score += points
        self.questions_answered += 1

    def get_permission(self):
        if self.permissions=="admin":
            return True
        else:
            return False
        
    def make_admin(self):
        password=input('what is the password to make admin? ')
        if password != "admin123":
            print("Incorrect password. You are not an admin.")
            return
        else:
            self.permissions="admin"
            print(f"{self.name} is now an admin.")
    
    def create_account(self):
        name = input("Enter your username: ")
        if name=="Guest":
            print("You cannot use 'Guest' as a username. Please choose another name.")
            return
        else:
            self.name = name
            self.export_user()
            print(f"Account created for {self.name}.")
            self.import_user(name)


tester=quiz()
#debug()
#tester=question("batman","Who is Batman?","Bruce Wayne")
#print(tester)
tester.question_gather()
print(tester.give_question())