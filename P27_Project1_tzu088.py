

class List_Node():
    def __init__(self, v):
        self.Value = str(v)
        self.Next = None

    def __str__(self):       
        return str(self.Value) + ("" if self.Next == None else (" " + str(self.Next)))
## do not write any additional code in this class,
## including do not add your netID to the class name



    

class Linked_List(object):
    def __init__(self):
        self.Head = None

    def __str__(self):
        return ("" if self.Head == None else str(self.Head))
## do not write any additional code in this super-class,
## including do not add your netID to the class name




class Queue_tzu088(Linked_List):
    def __init__(self):
        super(Queue_tzu088, self).__init__()
        self.Tail = None

    def Enqueue(self, v):
        ## Write Enqueue
        if self.Head == None:
            self.Head = List_Node(v)
            self.Tail = self.Head
        else:
            self.Tail.Next = List_Node(v)
            self.Tail = self.Tail.Next

    def Dequeue(self):
        v = None
        ## write Dequeue
        if self.Head == None:
            return "Empty Queue"
        v = self.Head.Value
        self.Head = self.Head.Next
        return v



class Stack_tzu088(Linked_List):
    def __init__(self):
        super(Stack_tzu088, self).__init__()

    def Push(self, v):
        ## write Push
        node = List_Node(v)
        node.Next = self.Head
        self.Head = node

    def Read_Top(self):
        v = None
        ## write Read_Top
        if self.Head == None:
            return "Empty Stack"
        v = self.Head.Value
        return v

    def Pop(self):
        v = None
        ## write Pop
        if self.Head == None:
            return "Empty Stack"
        v = self.Head.Value
        node = self.Head
        self.Head = self.Head.Next
        node.Next = None
        return v




class Scheme_Object(Stack_tzu088):
    def __init__(self):
        super(Scheme_Object, self).__init__()
        self.Operator = None

    def __str__(self):
        return ("(SO-start " + str(self.Operator) + " " 
    + ("" if self.Head == None else str(self.Head)) + " SO-end) ")
## change the two references to class Stack_ to be your netID

    

def Get_Scheme_Object_tzu088(string):

    print "begin queue"
    queue = Queue_tzu088()


    ## use string operations to
    ## translate the input string into a queue of List_Nodes
    ## {one node per token}

    while string != "":
        n = ""
        while string[0] != " ":
            n += string[0]
            if string != string[-1]:
                string = string[1:]
            else:
                string = ""
                break
        if string != "":
            string = string[1:]
        queue.Enqueue(n)
        ## MAKE SURE THIS NEXT PRINT COMMAND IS PRESENT AND UNCOMMENTED
        ## WHEN YOU TURN IN YOUR FINAL SUBMISSION- IT IS REQUIRED FOR GRADING
        print queue
        ## end while-loop block



        
    print "\n begin stack"
    working = Stack_tzu088()
    ## transfer the elements of the queue to a Working Stack
    ## by using the given while-loop

    
    condition = (True)
    while condition:
        ## whenever the element just added to the Working Stack is ')',
        ## this represents the end of a scheme_object;
        ## start popping the Working Stack and placing elements into a new scheme_object
        ## {which represents a stack itself via inheritance} of List_Nodes;
        ## do this until you find the beginning of the scheme_object {element is '('}
        ## fix the scheme_object with respect to Operator and Head
        ## add the scheme_object itself back to the Working Stack
        y = queue.Dequeue()
        if y != ')':
            working.Push(y)
        else:
            scheme = Scheme_Object()
            while working.Read_Top() != '(':
                x = working.Pop()
                scheme.Push(x)
            scheme.Operator = scheme.Pop()
            working.Pop()
            working.Push(scheme)
        ## keep these next two commands at the end of your while-loop block
        ## MAKE SURE THIS NEXT PRINT COMMAND IS PRESENT AND UNCOMMENTED
        ## WHEN YOU TURN IN YOUR FINAL SUBMISSION- IT IS REQUIRED FOR GRADING
        print "\n" + str(working)
        ## set condition anew by ***Rewriting the assignment in this
        ## next line as appropriate
        condition = (queue.Head != None)
        ## end while-loop block
    
    ## after exiting the while-loop, the Working Stack should
    ## consist of a single element {a scheme_object "stack"}
    ## return a pointer to this single element

    return working.Pop()





if __name__ == "__main__":

    ## test code here
    
    ## formatted_expression is what it would look like using scheme
    ## (this is a throwaway string, it is simply easier to read)
    scheme_formatted_expression = "(inc (+ 1 2 (- 12 4) (* (- 1) 7 (+ 3 (- (half 12) 1)))))"
    
    ## assume some "pre-processing" has been done to add spaces in the convenient places as:
    scheme_expression = "( inc ( + 1 2 ( - 12 4 ) ( * ( - 1 ) 7 ( + 3 ( - ( half 12 ) 1 ) ) ) ) )"
    
    scheme_object = Get_Scheme_Object_tzu088(scheme_expression)
    print "\n"
    print scheme_object
    
