class LinkedList:

    # A variable made to calculate the size of linked list
    size = 0
    idx = 0


    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, object):

        # accessing the class attribute 'size' with the class name
        LinkedList.size += 1

        object.index = LinkedList.idx
        LinkedList.idx += 1

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

        # jab tak yeh sach h
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

    # Linear Search Algorithm
    def get_object(self,idx):

        object = None

        temporary = self.head


        while True:
            # value of idx gets stored in index
            if temporary.index == idx:
                object = temporary
                break

            temporary = temporary.next

            if temporary is self.head:
                break

        return object


    # to remove the first element from the menu
    def remove_first(self):

        # passing head element in first object
        first_object = self.head
        # saving first object ka next element in head
        self.head = first_object.next
        # now saving tail element in head's previous
        self.head.previous = self.tail
        # passing head in tail ka next
        self.tail.next = self.head

        # now deleting the first object
        del first_object

        # self.update_indexes(0)


    # to remove the last element from the menu
    def remove_last(self):

        # not necessary to write
        # LinkedList.size -= 1
        # LinkedList.idx -= 1

        # logic
        last_object = self.tail
        self.tail = last_object.previous
        self.tail.next = self.head
        self.head.previous = self.tail

        del last_object


   # to remove any element from the menu by passing it's index
    def remove(self, index):

        if index == 0:
            self.remove_first()
        elif index == LinkedList.size - 1:
            self.remove_last()
        else:
            # putting the indexded object in object to delete
            object_to_delete = self.get_object(index)
            # saving next element of object to delete in object to delete's place by this logic
            object_to_delete.previous.next = object_to_delete.next

            # delete the object you want to delete
            del object_to_delete


            # manage indexing in this





