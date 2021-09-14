"""
   SONG is an object
     track,artist,duration,next_song,previous_song
"""

class song:

    def __init__(self,name = None,artist = None,duration = None,next_song = None,previous_song = None):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.next_song = next_song
        self.previous_song = previous_song


song1 = song("sach keh raha hai","john",3.55)
song2 = song("bimariyan" ,"kim",4.5)
song3 = song("permission to dance","jack",5.0)


song1.next_song = song2
song1.previous_song = song3

song2.next_song = song3
song2.previous_song = song1

song3.next_song = song1
song3.previous_song = song2

"""
This is how we can print the list of songs.
song = [
    {
      "SONG1"
        "name": "kal ho na ho",
        "artist": "sonu",
        "duration": 3.4
    },
    {
    "SONG2"
        "name": "yeh baby",
        "artist": "garry",
        "duration": 3.0

    },
    {
     "SONG3"
        "name": "sip sip",
        "artist": "jasmin",
        "duration": 4.5
    }

]

for i in song:
    print(i)"""



# to see data in your objects
print("data for song1:", vars(song1))
print("data for song2:", song2.__dict__)

# here also we are printing the list of songs,but we can more good.Above I have tried by making a list.
# Reference copy
song = song1
song.date = 12
print("data for song1:",vars(song1))
print("data for song1:",vars(song))

while song.next_song != song1:
    print("-" * 30)
    print("{}\t{}\t{}".format(song.name, song.artist, song.duration))
    print("-" * 30)
    print()


    song = song.next_song

print("-" * 30)
print("{}\t{}\t{}".format(song.name, song.artist, song.duration))
print("-" * 30)
print()



"""
this is a big method

song1.name = "sach keh raha hai" 
song1.artist = "john"
song1.duration = 3.55
song1.next_song = song2
song1.previous_song = song3

song2.name = "bimariyan" 
song2.artist = "kim"
song2.duration = 4.5
song2.next_song = song3
song2.previous_song = song1

song3.name = "permission to dance"
song3.artist = "jack"
song3.duration = 5.0
song3.next_song = song1
song3.previous_song = song2



# song1,song2,song3 are reference variables
# they are referring to the objects in memory

print(song1)
print(song2)
print(song3)"""


