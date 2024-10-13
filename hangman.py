from random_word import RandomWords
import random


play=True

while play:
    playing=input('''
    press w to start the game
    press a to quit 
    :''').lower()

    if(playing=='w'):
        mode=input('''
        press 1 for easy mode
        press 2 for hard mode
        :''')
        if(mode=='1'):
            word_list=['gills','food','bees','sheep']
            random_int=random.randint(0,len(word_list)-1)
            guess_word=word_list[random_int]
            
            dash=[]
            for n in range(len(guess_word)):
                dash+="_"
            print(dash)
            keep=len(dash)
            life=5

            while keep>0 :
                print(f"You have {life} left")
                letter=input("guess the letter: ")
                present=False
                
                d=0
                while d<len(guess_word):
                    if(dash[d]=="_"):
                        if(letter==guess_word[d]):
                            dash[d]=letter
                            keep-=1
                            present=True
                    d+=1

                if(present==False):
                    print("wrong")
                    life-=1

                print(dash)

                if(life==0):
                    print("YOU LOST!")
                    break


        elif(mode=='2'):
            r = RandomWords()
            guess_word_random=r.get_random_word()
            print(guess_word_random)
      
        else:
            print('INVALID')


    elif(playing=='a'):
        print(playing)
        play=False
    else:
        print('INVALID')

print('outside')


