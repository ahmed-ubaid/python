musicList=[]
n=0


    print(f"your music list {musicList}")
    choice=int(input('''press 1 to add a new song
    press 2 to delete a song'''))

    if(choice==1):
        addSong=input("Enter the name of the song you want to add to the list ")
        musicList.append(addSong)
    else:
        delSong=input("Enter the name of the song you want to remove from the list ")
        musicList.remove(delSong)

    print(f"your music list {musicList}")
