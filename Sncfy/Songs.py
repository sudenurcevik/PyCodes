import sqlite3
import time


class Song():

    def __init__(self, song, singer, album, company, time):
        self.song = song
        self.singer = singer
        self.album = album
        self.company = company
        self.time = time

    def __str__(self):
        return f"Song: {self.song}\nSinger: {self.singer}\nAlbum: {self.album}\nProduction Company: {self.company}\nSong Time: {self.time}\n"



class Application():

    def __init__(self):
        self.spotify_set()

    def spotify_set(self):
        self.con = sqlite3.connect("spotify.db")
        self.cursor = self.con.cursor()

        query = "Create Table if not exists songs (song TEXT,singer TEXT,album TEXT,company TEXT,time INT)"
        self.cursor.execute(query)
        self.con.commit()

    def cutConnection(self):
        self.con.close()

    def calculate_total_time(self):
        total_time = 0
        query = "Select time From songs"
        self.cursor.execute(query)
        list = self.cursor.fetchall()
        if len(list)!=0:
            for i in list:
                total_time += i[0]
        print(f"Here is the total time: {total_time}")

    def addSong(self, song):
        query = "Insert into songs Values(?,?,?,?,?)"
        self.cursor.execute(query, (song.song, song.singer, song.album, song.company, song.time))
        self.con.commit()

    def deleteSong(self, song):
        found=self.findSong(song)

        if found:
            query = "Delete From songs where song=? "
            self.cursor.execute(query, (song,))
            self.con.commit()

        else:
            print("The chosen song is not in your playlist")

    def showSongs(self):
        query = "Select * From songs"
        self.cursor.execute(query)
        list = self.cursor.fetchall()
        if len(list) == 0:
            print("There is not any song in your playlist")
        else:
            for i in list:
                song = Song(i[0], i[1], i[2], i[3], str(i[4]))
                print(song)

    def findSong(self, song):
        found = False
        query = "Select * From songs where song = ?"
        self.cursor.execute(query, (song,))
        list = self.cursor.fetchall()
        if len(list) != 0:
            found = True
        return found

    def numOfSongs(self):
        query = "Select * From songs"
        self.cursor.execute(query)
        list=self.cursor.fetchall()
        if len(list)==0:
            print("I am sorry :( Your playlist is empty ")
        else:
            print(f"Total number of songs in your playlist is: {len(list)} :)")

    def showSong(self,song):
        query = "Select * From songs where song= ?"
        self.cursor.execute(query,(song,))
        list = self.cursor.fetchall()
        if len(list) == 0:
            print("This song is not in your playlist")
        else:
            song = Song(list[0][0], list[0][1], list[0][2], list[0][3], list[0][4])
            print(song)

