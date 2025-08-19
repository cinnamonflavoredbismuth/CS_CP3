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
X Allow users to select from different lists of questions
X Allow users to create lists of questions
X User profiles (Admin users can create new lists of questions, normal users can just select from lists of questions to do)
Give different point amounts based on how quickly they answer
X Shuffle the order the answers are displayed 

KEY REMINDERS:
CSV's use a csvreader
Think carefully about the data types you want to use!
Make clear user instructions for how they answer questions
Don't forget to plan extra debugging time! You can always add more once you have an MVP!"""
import csv
import random
from tkinter import *
from tkinter import ttk



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
    def __init__(self,master_questions=[],questions=[],answers=[],ans=''):
        self.master_questions=master_questions
        self.questions=questions
        self.answers=answers
        self.ans=ans
        self.question_gather(topic="all", file="quiz-game/questions.csv")
        self.question_list()

    def question_gather(self,topic="all",file="quiz-game/questions.csv"):
        self.master_questions=[]
        self.questions=[]
        self.answers=[]
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
    
    def topic_choice(self,choice=""):
        topics=self.get_topics()
        print("Available topics:")
        for i, topic in enumerate(topics, start=1):
            print(f"{i}. {topic}")
        if choice == "":
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
    
    def answer_options(self,correct_answer=""):
        if correct_answer != "":
            options=[correct_answer]
        while len(options) < 4:
            try:
                question=random.choice(self.answers)
            except IndexError:
                print("No questions available. Please add questions.")
                return []
            if question in options:
                pass
            else:
                options.append(question)
        return self.scramble(options)
    
    def get_question(self,acc):
        question=random.choice(self.master_questions)
        if question.question in acc.questions_answered:
            return self.get_question(acc)
        else:
            acc.questions_answered.append(question.question)
            acc.edit_account()
            return question
        
    def set_ans(self,ans=""):
        self.ans = ans
        
    ''' 
    def button_interface(self,question, options): #Current problem: The last button inittilized is the one that ans is set to, not the one clicked
            self.set_ans('')  # Reset ans before using the interface
            root = Tk()
            frm = ttk.Frame(root, padding=10)
            frm.grid()
            ttk.Label(frm, text=f"{question.question}").grid(column=0, row=0)
            def buttons(option,col,r):
                ttk.Button(frm, text=f"{options[option]}", command=(self.set_ans(options[option]))).grid(column=col, row=r) 
                #print(options[option])
            buttons(0,0,1) # A
            buttons(1,1,1) # B
            buttons(2,0,2) # C
            buttons(3,1,2) # D
            ttk.Button(frm, text="Submit", command=root.destroy).grid(column=0, row=3, columnspan=4)
            ttk.Label(frm, text="Select your answer and click Submit.").grid(column=0, row=4, columnspan=4)

            root.update()'''

    def give_question(self,acc): #returns 1 for correct, 0 for incorrect. add to player score
        question=self.get_question(acc)

        options=self.answer_options(question.answer)

        def choose(question,options): #Temporary. replace with tkinter later
            ans=input(f'{question.question}\nA. {options[0]}\nB. {options[1]}\nC. {options[2]}\nD. {options[3]}\n')
            return ans
        
        #self.button_interface(question, options)

        def valid_check(answer="",question=question, options=options):
            if answer == "":
                
                answer = self.ans.lower()
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

        self.ans=valid_check(question=question, options=options)
        print(self.ans)
        if question.answer_check(self.ans) == True:
            print("Correct!")
            return 1 #returns points added
        else:
            print("Incorrect!")
            return 0 # returns points added
        
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

    def whole_quiz(self,user):
        if len(self.answers) - len(user.questions_answered) < 10:
            user.questions_answered = []
            user.edit_account()
        print("Welcome User! You can play the quiz.")
        score = 0
        for _ in range(11):
            print(f"nAnswered Questions: {user.number_answered()}")
            point=self.give_question(user)
            score += point
            user.update_score(score)
        print(f"Your final score is: {score}")

class user:
    def __init__(self,name='Guest',permissions="normal",score=0,questions_answered=[]):
        self.name=name
        self.permissions=permissions  # Default permission level
        self.score=score
        self.questions_answered=questions_answered
    
    def __str__(self):
        return f"User: {self.name}, Permissions: {self.permissions}, Score: {self.score}, Questions Answered: {(self.questions_answered)}"
    
    def create_account(self,name=""):
        if name== "":
            name = input("Enter your username: ")

        if name=="Guest":
            print("You cannot use 'Guest' as a username. Please choose another name.")
            return
        elif name in self.get_usernames():
            print(f"Username '{name}' already exists. Please choose a different username.")
            return
        else:
            self.name = name
            self.export_user()
            print(f"Account created for {self.name}.")
            self.import_user(name)

    def import_user(self,name="",file="quiz-game/user_data.csv"):
        if name == "":
            name = input("Enter your username to import: ")
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
                        self.questions_answered=[]
                        if row[3] == "" or row[3] == "0":
                            self.questions_answered = []
                        else:
                            for x in row[3].split(";"):
                                if x != "":
                                    self.questions_answered.append(x)

    def export_user(self,file="quiz-game/user_data.csv",newline=""):
        answered=""
        if len(self.questions_answered) == 0 or answered == 0:
            answered = "" 
        else:
            for x in self.questions_answered:
                answered += x + ";"
        with open(file,"a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([self.name,self.permissions,self.score,answered])

    def get_usernames(self,file="quiz-game/user_data.csv"):
        usernames=[]
        with open(file,"r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if len(row)==0:
                    pass
                else:
                    usernames.append(row[0])
        return usernames
    
    def write(self,accounts=[],file="quiz-game/user_data.csv"):
        with open(file,"w",newline='') as file:
            writer=csv.writer(file)
            writer.writerow(["Username","Permissions","Score","Questions Answered"])
            writer.writerows(accounts)

    def edit_account(self,file="quiz-game/user_data.csv"):
        with open(file,"r",newline="") as file:
            reader=csv.reader(file)
            accounts=[]
            next(reader)
            for row in reader:
                if len(row)!= 0:
                    if row[0] == self.name:
                        answered = ""
                        if len(self.questions_answered) == 0 or self.questions_answered == 0:
                            answered = "" 
                        else:
                            for x in self.questions_answered:
                                answered += x + ";"
                        account=[self.name, self.permissions, self.score,answered]
                    
                    else:
                        try:
                            account=[row[0], row[1], int(row[2]), row[3]]
                        except ValueError:
                            account=[row[0], row[1], (row[2]), row[3]]
                    accounts.append(account)
            self.write(accounts)

    def update_score(self,points):
        self.score += points
        self.edit_account()

    def get_permission(self):
        if self.permissions=="admin":
            return True
        else:
            return False
        
    def make_admin(self,password=""):
        if self.get_permission() == True:
            print(f"{self.name} is already an admin.")
        else:
            if password == "":
                password = input('what is the password to make admin? ')
            if password != "password":
                print("Incorrect password. You are not an admin.")
                return
            else:
                self.permissions="admin"
                self.edit_account()
                print(f"{self.name} is now an admin.")
    
    def number_answered(self):
        return f"{len(self.questions_answered)}/10"
    
def main(acc=user(),game=quiz()):
    
    print("Welcome to the Quiz Game!")
    print("1. Create Account")
    print("2. Import Account")
    print("3. Play Quiz")
    print("4. Add Questions (Admin Only)")
    print("5. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == '1':
        acc.create_account()
        main(acc,game)
    elif choice == '2':
        acc.import_user()
        main(acc,game)
    elif choice == '3':
        game.topic_choice()
        game.whole_quiz(acc)
        acc.questions_answered = []
        acc.edit_account()
        main(acc,game)
    elif choice == '4':
        acc.make_admin()
        game.add_questions(acc)
        main(acc,game)
    elif choice == '5':
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid choice, please try again.")
        main(acc,game)

class button():
    def __init__(self, text, command, col=0, row=0, new_label=""):
        self.txt = text
        self.command = command
        self.col = col
        self.row = row
        self.new_label = new_label

    def if_clicked(self,func):
        print(self.txt)
        self.command()
        func.label = self.new_label
        return func.screen()

    def button_update(self,func):
        ttk.Button(func.frm, text=self.txt, command=lambda:self.if_clicked(self,func)).grid(column=self.col, row=self.row,columnspan=2)
        func.frm.update()

class label():
    def __init__(self, text, col=0, row=0,colspan=1):
        self.text = text
        self.col = col
        self.row = row
        self.colspan = colspan

    def change_label(self,func):
        #ttk.Label(self.frm, text=f"                                              ")#.grid(column=0, row=0)
        ttk.Label(func.frm, text=f"{label}").grid(column=self.col, row=self.row,columnspan=self.colspan)#.grid(column=0,roq=0,columnspan=4)
        func.frm.update()


class outside_window():
    def __init__(self):
        self.buttons = [
            button("Create Account", 0, 1, "Create a new account"),
            button("Import Account", 2, 1, "Import an existing account"),
            button("Play Quiz", 0, 2, "Start the quiz game"),
            button("Add Questions (Admin Only)", 2, 2, "Add new questions to the quiz"),
            button("Exit", 1, 3, "Exit the game")
        ]
        self.labels = [label("Welcome to the Quiz Game!", 0, 0, 4)]
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
    def screen(self):
        #self.change_label(self.label)
        for x in self.labels:
            x.change_label(self)
        for x in self.buttons:
            x.button_update(self)
    def run(self):
        self.screen()      
        self.frm.mainloop()
    
    

'''
acc=user()
acc.import_user("cecily")
'''
#debug()
tester=outside_window()
tester.run()
#test.whole_quiz(user("Cecily","admin",0,[]))
#main()