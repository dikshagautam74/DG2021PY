"""
  LINKED LIST
  dynamic list with links created automatically with programming approach
"""

class song:
    pass

    def __init__(self,name = None,artist = None,duration = None):
        self.name = name
        self.artist = artist
        self.duration = duration

    # a self made function to print the song attribute in a better way
    # def show(self):
    #     print("{name}\t {artist}\t {duration}".format_map(vars(self)))

    # a built-in function used to print the song attributes in a better way
    def __str__(self):
        return "{name}\t {artist}\t {duration}".format_map(vars(self))


class LinkedList:

    # A variable made to calculate the size of linked list
    size = 0


    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, object):

        # accessing the class attribute 'size' with the class name
        LinkedList.size += 1

        if self.head is None:

            self.head = object
            self.tail = object

            print("OBJECT ADDED AS HEAD AND TAIL")

        else:
            self.tail.next = object
            object.previous = self.tail
            self.head.previous = object

            self.tail = object
            self.tail.next = self.head
            print("OBJECT ADDED AS TAIL")


    def iterate_forward(self):
        temporary = self.head

        # jab tak yeh sahi h
        while True:
            # print(vars(temporary))

            # if using __str__ function, you have to write only variable name need not to access it.
            # it will executed automatically.
            print(temporary)

            # accessing show function
            # temporary.show()
            temporary = temporary.next        #-> when it comes to temporary = song5.next,it goes to if loop and break bcoz song5.next = self.head

            if temporary is self.head:
                break

    # a function made to calculate the size of class Linked list
    def length(self):
        return LinkedList.size



def main():

    # object creation of class song
    song1 = song("1 Sach Keh Raha Hai", "John", 4.5)
    song2 = song("2 Bimariyan", "kim", 3.5)
    song3 = song("3 Permission to dance", "fionna", 5.0)
    song4 = song("4 kal ho na ho", "jack", 2.5)
    song5 = song("5 baarish", "nick", 4.0)


    # object creation of class linked list
    play_list = LinkedList()
    print(vars(play_list))


    # add the object
    play_list.append(song1)
    play_list.append(song2)
    play_list.append(song3)
    play_list.append(song4)
    play_list.append(song5)

    print()

    # iterating the playlist to print the songs
    play_list.iterate_forward()

    print()

    # accessing length function to print the length of linked list
    print("Length of linked list:", play_list.length())







if __name__ == '__main__':
    main()




