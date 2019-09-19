class Node:
    def __init__(self,next=None, random=None, data=None):
        self.next=next
        self.random=random
        self.data=data


class List:

    clone_node=None
    def __init__(self, original_node):
        self.original_node=original_node
    
    def clone_singly_linked_list(self):

        while True:
            new_node=Node(data=self.original_node.data)
            if List.clone_node is None:
                List.clone_node=new_node
                
            else:
                new_node=Node(data=self.original_node.data)
                List.clone_node.next=new_node  

            if self.original_node.next == None:
                break
            else:
                self.original_node=self.original_node.next

    def clone_random_links(self):

        while True:
            List.clone_node.random=self.original_node.random
            if self.original_node.next == None:
                break
            else:
                self.original_node=self.original_node.next




