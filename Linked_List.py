class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self,index,data):
        if index < 0:
            print('Index must be non-negative')
            return

        if index==0:
            self.insert_first(data)
            return  # to exit the function after inserting at the beginning
        
        position=0
        next_node = self.head
        while next_node!=None and position+1!=index:
            position=position+1
            next_node = next_node.next
        if next_node is not None:
            new_node=Node(data)
            new_node.next=next_node.next
            next_node.next=new_node
        else:
            print('enter valid position') 

    def insert_at_end(self,data):
        if self.head is None:
            self.insert_first(data) 
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node=current_node.next
        new_node=Node(data)
        current_node.next=new_node               
  
    def update_node(self,index,data):
        if index < 0:
            print('Index must be non-negative')
            return
        
        position=0
        current_node = self.head
        while current_node!=None and position!=index:
            position+=1
            current_node = current_node.next
        if current_node is not None:
            current_node.value=data
        else:
            print('enter valid position') 

    def del_data(self,data):
        if self.head is None:
            return 'LL is empty'
        
        if self.head.value==data:
            self.head=self.head.next

        current_node=self.head
        while current_node is not None and current_node.next is not None and current_node.next.value != data:
            current_node = current_node.next

        if current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print('Enter valid data')
                
    def print_list(self):
        if self.head is None:
            return 'empty LL'
        
        next_node = self.head
        while next_node:
            print(next_node.value, end='->')
            next_node = next_node.next
        print('None')

    def len_of_LL(self):
        if self.head is None:
            return 0
        size=0
        next_node = self.head
        while next_node:
            size+=1
            next_node = next_node.next
        return f'size is {size}'    

linked_list = LinkedList()
linked_list.insert_first(3)
linked_list.insert_first(2)
linked_list.insert_first(1)
linked_list.print_list()
linked_list.insert_at_index(-3,0)
linked_list.print_list()
#linked_list.del_data(5)
#linked_list.print_list()
print(linked_list.len_of_LL())
