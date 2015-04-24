
class List_Node():
    def __init__(self, v):
        self.Value = v
        self.Next = None
## do not write any additional code in this class,
## including do not add your netID to the class name



    

class Linked_List(object):
    def __init__(self):
        self.Head = None

## do not write any additional code in this super-class,
## including do not add your netID to the class name




class Queue(Linked_List):
    def __init__(self):
        super(Queue, self).__init__()
        self.Tail = None
        self.count = 0

    def Enqueue(self, v):
        ## Write Enqueue
        n = List_Node(v)
        self.count = self.count + 1
        if self.Head == None:
            self.Head = n
            self.Tail = n
        else:
            self.Tail.Next = n
            self.Tail = n

    def Dequeue(self):
        v = None
        ## write Dequeue
        if self.Head == None:
            print ("queue empty")
            return
        else:
            v = self.Head.Value
            self.Head = self.Head.Next
            self.count = self.count - 1
        return v
## do not write any additional code in this class,
## including do not add your netID to the class name


    


class Tree_Node_tzu088():
    def __init__(self, v):
        self.Value = v
        self.Parent = None
        self.LeftChild = None
        self.RightChild = None
        self.Predecessor = None
        self.Successor = None
        self.RankCounter = 1
## UPDATE the value of RankCounter within the constructor

    def Find_Subtree_Min(self):
        m = self
        while m.LeftChild != None:
            m = m.LeftChild
        return m

    def Find_Subtree_Max(self):
        m = self
        while m.RightChild != None:
            m = m.RightChild
        return m

    def Set_Successor(self):
        if self.RightChild != None:
            return self.RightChild.Find_Subtree_Min()
        else:
            a1 = self.Parent
            a2 = self
            while a1 != None:
                if a1.LeftChild != None and a1.LeftChild.Value == a2.Value:
                    return a1
                a1 = a1.Parent
                a2 = a2.Parent
            return None

    def Set_Predecessor(self):
        ## write Set_Predecessor
        
        if self.LeftChild != None:
            return self.LeftChild.Find_Subtree_Max()
        else:
            a1 = self.Parent
            a2 = self
            while a1 != None:
                if a1.RightChild != None and a1.RightChild.Value == a2.Value:
                    return a1
                a1 = a1.Parent
                a2 = a2.Parent
            return None
        

class Tree_tzu088():
    def __init__(self):
        self.Root = None
        self.Min = None
        self.Max = None


    def Insert(self, v):
        ## write Insert
        newNode = Tree_Node_tzu088(v)
        x = self.Root
        y = None
        successor = None
        predecessor = None

        #Look for right position of v
        while x != None:
            y = x
            if v <= x.Value:
                x = x.LeftChild         
                successor = y                    #Dynamically record .Successor
            else:
                x = x.RightChild
                predecessor = y                  #Dynamically record .Predecessor
            y.RankCounter = y.RankCounter+1      #Dynamically record .RankCounter
                

        #Update the relationship between newNode and its parent
        newNode.Parent = y
        if y == None:
            self.Root = newNode
        elif v <= y.Value:
            y.LeftChild = newNode
        else:
            y.RightChild = newNode

        #Update .Successor and .Predecessor    
        newNode.Successor = successor
        newNode.Predecessor = predecessor

        #Update attributes of newNode's successor and predecessor
        if predecessor != None:
            predecessor.Successor = newNode
        if successor != None:
            successor.Predecessor = newNode
            
        #Update .Min and .Max
        self.Min = self.Root.Find_Subtree_Min()
        self.Max = self.Root.Find_Subtree_Max()            
        



    def Search(self, v):
        ## write Search
        x = self.Root
        while x != None and v != x.Value:
            if v < x.Value:
                x = x.LeftChild
            else:
                x = x.RightChild
        if x == None:
            return False
        else:
            return True


    def BFS_Print(self):
        if self.Root == None:
            print "empty queue"
            return
        ## write BFS_Print
        q = Queue()
        q.Enqueue(self.Root)
        while q.count != 0:
            n = q.Dequeue()
            print n.Value
            if n.LeftChild != None:
                q.Enqueue(n.LeftChild)
            if n.RightChild != None:
                q.Enqueue(n.RightChild)


    def Find_Value_Of_Rank(self, r):
        if self.Root == None:
            return None
        if r < 1 or r > self.Node_Count():
            print "rank out of range"
            return
        ## write Find_Value_Of_Rank
        x = self.Root
        if x.LeftChild == None:
            rank =1
        else:
            rank = x.LeftChild.RankCounter+1

        #Divide and conquer
        while r != rank:
            if r < rank:
                x = x.LeftChild
            else:
                r = r-rank
                x = x.RightChild
            if x.LeftChild == None:
                rank =1
            else:
                rank = x.LeftChild.RankCounter+1
                
        return x.Value
        
                


    def Get_Rank_Of_Value(self, v):
        ## write Get_Rank_Of_Value
        x = self.Root
        rank = 1

        #Search for v, dynamically record rank
        while x != None and v != x.Value:
            if v < x.Value:
                x = x.LeftChild
            else:
                rank = rank + 1
                if x.LeftChild != None:
                    rank = rank + x.LeftChild.RankCounter
                x = x.RightChild
        if x == None:    
            return None
        else:
            if x.LeftChild != None:
                    rank = rank + x.LeftChild.RankCounter
            return rank



    def Node_Count(self):
        ## write Node_Count
        # #node = root.RankCounter
        if self.Root == None:
            return 0
        else:
            return self.Root.RankCounter
            








if __name__ == "__main__":

    ## test code here
    TREE = Tree_tzu088()
    
    LIST = [1063,
            2121,
            9020,
            9015,
            6802,
            1613,
            8068,
            6171,
            8986,
            6799,
            7617,
            6500,
            4780,
            7159,
            1961,
            2816,
            5772,
            8020,
            7588,
            7758,
            744,
            5639,
            8609,
            8735,
            9997,
            4805,
            7759,
            8776,
            6884,
            7673,
            8611,
            5250,
            5417,
            9640,
            3504,
            3016,
            8359,
            9498,
            240,
            6833,
            4215,
            7548,
            7487,
            5884,
            2726,
            3979,
            8083,
            1442,
            6625,
            2571,
            9112,
            4458,
            4743,
            401,
            8267,
            5338,
            6599,
            6612,
            897,
            2663,
            8240,
            2612,
            6224,
            2302,
            4681,
            1634,
            6886,
            6047,
            6713,
            7813,
            4074,
            5734,
            4569,
            8117,
            6906,
            1444,
            4313,
            9990,
            3134,
            194,
            1465,
            5032,
            3306,
            349,
            7817,
            2093,
            6642,
            5578,
            4016,
            5092,
            6552,
            1805,
            5085,
            3091,
            3366,
            3336,
            2322,
            8777,
            6779]

    for el in LIST:
        TREE.Insert(el)

    finished = True
    for el in LIST:
        if not TREE.Search(el):
            finished = False
            print str(el) + " not inserted correctly"
            break
    if finished:
        print "Found all inserted values"

    finished = True
    for not_el in [1, 10, 100, 1000, 2000, 4000, 8000]:
        if TREE.Search(not_el):
            finished = False
            print str(not_el)+ "incorrectly found in list"
            break

    if finished:
        print "No bad values found"

    

    print "\nrun 1"
    TREE.BFS_Print()

    
    LIST.sort()
    print "\nMin:\n" + str(TREE.Min.Value)
    print "\nrun 2"
    for i in range(20):
        print LIST[5*i]

    
    print "\nrun 3"
    for i in range(20):
        print str(TREE.Find_Value_Of_Rank(5*i+1))

    
    print "\nrun 4"
    for i in range(500):
        if not (i < 30 or i > 470):
            continue
        x = TREE.Get_Rank_Of_Value(10*i)
        if i%2 == 0 or type(2) == type(x):
            print str(10*i) + "; " + str(x)        

 
    print "\nrun 5"
    for i in range(1,100):
        y = TREE.Find_Value_Of_Rank(i)
        print y, TREE.Get_Rank_Of_Value(y)

                
    
    print "\nrun 6"
    x = TREE.Min
    while x != None:
        print x.Value
        x = x.Set_Successor()

