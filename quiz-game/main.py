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

class placeholder:
    def __init__(self,master_questions=[]):
        self.master_questions=master_questions
    def question_gather(self,file="quiz-game/questions.csv"):
        with open(file,"r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if len(row)<0:
                    pass
                else:
                    q=question(row[0],row[1],row[2])
                    self.master_questions.append(q)
                    #print(q)
    def __str__(self):
        for question in self.master_questions:
            print(question)
        return ""

tester=placeholder()
#debug()
#tester=question("batman","Who is Batman?","Bruce Wayne")
#print(tester)
tester.question_gather()
print(tester)