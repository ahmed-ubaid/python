import random

options=['rock','paper','scissors']
history=[]
score=0

n=0

while(n==0):
    ch=int(input('''
    0 to keep playing 
    1 to stop
    enter your choice: '''))
    if(ch==0):
        choice=int(input('''
        Choose your fighter
        1 for rock
        2 for paper
        3 for scissors
        enter your choice: '''))
    
        compChoice=random.randint(1,3)

        if(choice==compChoice):
            history.append('draw')
            print("it was a draw")
        elif(choice==1 and compChoice==2):
            print(f'''
            you choose {options[choice-1]}
            comp choose {options[compChoice-1]}
            you lost
            ''')
            history.append('loss')
            score-=1
        elif(choice==1 and compChoice==3):
            print(f'''
            you choose {options[choice-1]}
            comp choose {options[compChoice-1]}
            you won
            ''')
            history.append('win')
            score+=1
        elif(choice==2 and compChoice==1):
            print(f'''
            you choose {options[choice-1]}
            comp choose {options[compChoice-1]}
            you won
            ''')
            history.append('win')
            score+=1
        elif(choice==2 and compChoice==3):
            print(f'''
            you choose {options[choice-1]}
            comp choose {options[compChoice-1]}
            you lost
            ''')
            history.append('loss')
            score-=1
        elif(choice==3 and compChoice==1):
            print(f'''
            you choose {options[choice-1]}
            comp choose {options[compChoice-1]}
            you lost
            ''')
            history.append('loss')
            score-=1
        elif(choice==3 and compChoice==2):
            print(f'''
            you choose {options[choice-1]}
            comp choose {options[compChoice-1]}
            you lost
            ''')
            history.append('loss')
            score-=1



    elif(ch==1):
        if(score<0):
            score=0
        print(f'''
        your score {score}
        your match history {history}
        ''')

        n=ch
    else:
        n==0

        





