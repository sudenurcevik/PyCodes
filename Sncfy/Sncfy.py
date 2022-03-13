from Songs import *

print("""***********************************

WELCOME TO SNCFY PLAYLIST APP:)

CHOOSE THE ACTION THAT YOU WANT TO DO ;

1.CALCULATE THE TOTAL TIME OF SONGS
2.ADD SONG
3.DELETE SONG
4.SHOW SONGS
5.FIND SONG
6.CALCULATE THE NUMBER OF SONGS

PLEASE ENTER "O" TO QUIT..

    
***********************************""")

sncfy= Application()

while True:
    print("""***********************************

    WELCOME TO SNCFY PLAYLIST APP:)

    CHOOSE THE ACTION THAT YOU WANT TO DO ;

    1.CALCULATE THE TOTAL TIME OF SONGS
    2.ADD SONG
    3.DELETE SONG
    4.SHOW SONGS
    5.FIND SONG
    6.CALCULATE THE NUMBER OF SONGS

    PLEASE ENTER "O" TO QUIT..


    ***********************************\n""")

    action= input("CHOOSE THE ACTION:")
    if action=="O":
        print("SNCFY is been closing..Have a nice day:)")
        break

    elif action=="1":
        print("The process is being maintained..Please wait :)")
        time.sleep(2)
        sncfy.calculate_total_time()

    elif action=="2":
        song=input("Enter the song that you want to add: ")
        singer = input("Enter the singer of that song: ")
        album = input("Enter the album of that song: ")
        company = input("Enter the production company of that song: ")
        time_ = float(input("Enter the time of that song: "))

        new_song= Song(song,singer,album,company,time_)
        print("The song is been added please wait..")
        time.sleep(2)
        sncfy.addSong(new_song)
        print("The song has been added..:)")

    elif action=="3":
        song=input("Enter the song that you want to remove: ")
        answer= input("Are you sure to delete ? (y/n)")
        if answer=="y":
            sncfy.deleteSong(song)
            time.sleep(2)
            print("The song is removed")

    elif action=="4":
        print("Here are the songs in your playlist:")
        time.sleep(2)
        sncfy.showSongs()
    elif action=="5":
        song=input("Enter the song that you want to find: ")
        time.sleep(2)
        sncfy.showSong(song)
    elif action=="6":
        time.sleep(2)
        sncfy.numOfSongs()
    else:
        print("Wrong option :(")