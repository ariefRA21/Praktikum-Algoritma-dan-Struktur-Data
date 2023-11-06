class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleList(object):
    head = None
    tail = None

    def add_depan(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def add_belakang(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_tengah(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.previous = None
            self.tail.next = None
        else:
            current = self.head
            mid = (self.size//2) if(self.size%2==0) else((self.size+1)//2)
                for i in range(1, mid)

    def remove(self, node_value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                #if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    #otherwise we have no prev(it's None), head is the next on
                    self.head = current_node.next
                    current_node.next.prev = None

            current_node = current_node.next

    def show(self):
        print ("Show List Data:")
        current_node = self.head
        while current_node is not None:
            print (current_node.prev.data) if hasattr(current_node.prev, "data") else None
            print ("<--- ")
            print (current_node.data)
            print (" --->")
            print (current_node.next.data) if hasattr(current_node.next, "data") else None

            current_node = current_node.next
        print ("*"*50)


d = DoubleList()

d.add_depan(5)
d.add_depan(6)
d.add_depan(50)
d.add_depan(30)

d.show()
d.add_belakang(10)
d.add_belakang(15)
d.remove(50)

d.show()
d.add_tengah(75)
