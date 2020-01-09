# Node class  
# Author: Alex
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to pairwise swap elements of a linked list 
    def pairwiseSwap(self): 
        temp = self.head 
        j = self.head
        # There are no nodes in ilnked list 
        if temp is None: 
            return 
           
        # Traverse furthur only if there are at least two 
        #  left 
        while(temp is not None):
            print("first loop")
            while(j.next is not None):
                if temp.data > j.next.data:
                    print("temp.data")
                    print(temp.data)
                    print(">")
                    print("j.next.data")
                    print(j.next.data)
                    print(temp.data>j.next.data)
                    j.next.data, temp.data = temp.data, j.next.data  

                j = j.next
            j = temp
            temp = temp.next
        return self.head
        
           
         
    # Function to insert a new node at the end 
    def push(self, new_data): 
        new_node = Node(new_data) 
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        
        while(temp.next is not None):
            temp = temp.next
            
        temp.next = new_node
        return self.head
  
    # Utility function to prit the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next
# Test
llist = LinkedList()
llist.push(100)
llist.push(1)
llist.push(2)
llist.push(15)
llist.push(40)
llist.push(4)
llist.push(7)


#llist.printList()
llist.pairwiseSwap()
print("              ")
llist.printList()

