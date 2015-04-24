

class List_Node():
    def __init__(self, v):
        self.Value = v
        self.Next = None
        self.Prev = None
        self.Other = None

    def __str__(self):
        return str(self.Value) + " " + str(self.Next)
## do not write any additional code in this class,
## including do not add your netID to the class name



    

class Linked_List(object):
    def __init__(self):
        self.Head = None
        self.Tail = None

    def __str__(self):
        x = str(self.Head)
        if x == "None":
            return x
        else:
            return x[:-5]


    def Insert_Node(self, list_node):
        if self.Head == None:
            self.Head = list_node
            self.Tail = list_node
            return
        list_node.Prev = self.Tail
        self.Tail.Next = list_node
        self.Tail = list_node

        
    def Search(self, v):
        x = self.Head
        while x != None:
            if x.Value == v:
                return x
            x = x.Next
        return None
## do not write any additional code in this super-class,
## including do not add your netID to the class name


def Remove_List_Node(list_object, node_pointer):
    if node_pointer.Prev == None:
        list_object.Head = node_pointer.Next
    else:
        node_pointer.Prev.Next = node_pointer.Next
    if node_pointer.Next == None:
        list_object.Tail = node_pointer.Prev
    else:
        node_pointer.Next.Prev = node_pointer.Prev


        

class Matrix_Graph_tzu088():
    
    def __init__(self, nodeCount):
        self.NodeCount = nodeCount
        self.AdjacencyMatrix = []
        for i in range (nodeCount):
            self.AdjacencyMatrix.append(nodeCount*[0])
        self.Transpose = False

    def __str__(self):
        x = ""
        for row in self.AdjacencyMatrix:
            x += str(row) + "\n"
        return x

    def Transpose_Graph(self):
        self.Transpose = not self.Transpose

    def Insert_Matrix_Edge(self, a, b):
        ## write Insert_Matrix_Edge
        if self.Transpose == False:
            self.AdjacencyMatrix[a][b]=1
        else:
            self.AdjacencyMatrix[b][a]=1


    def Check_Matrix_Edge(self, a ,b):
        ## write Check_Matrix_Edge
        if self.Transpose == False:
            if self.AdjacencyMatrix[a][b]==1:
                return True
            else:
                return False
        else:
            if self.AdjacencyMatrix[b][a]==1:
                return True
            else:
                return False
        

    def Remove_Matrix_Edge(self, a, b):
        ## write Remove_Matrix_Edge
        if self.Transpose == False:
            if self.AdjancencyMatrix[a][b]==1:
                self.AdjacencyMatrix[a][b]=0
        else:
            if self.AdjancencyMatrix[b][a]==1:
                self.AdjacencyMatrix[b][a]=0
        

    def Remove_Matrix_Node(self, a):
        ## write Remove_Matrix_Node
        for i in range (self.NodeCount):
            if self.AdjacencyMatrix[a][i]<0:
                self.AdjacencyMatrix[a][i]-=1
            else:
                self.AdjacencyMatrix[a][i]=-1
        for j in range (self.NodeCount):
            if self.AdjacencyMatrix[j][a]<0:
                self.AdjacencyMatrix[j][a]-=1
            else:
                self.AdjacencyMatrix[j][a]=-1


    def ReAdd_Edgeless_Matrix_Node(self, a):
        ## write ReAdd_Edgless_Matrix_Node
        for i in range (self.NodeCount):
            self.AdjacencyMatrix[a][i]+=1
        for j in range (self.NodeCount):
            self.AdjacencyMatrix[j][a]+=1


class Lists_Graph_tzu088():
    Neighbors = []
    Incoming = []

    def __init(self):
        self.Neighbors = []
        self.Incoming = []

    def __str__(self):
        x = ""
        x += "Neighbors\n"
        for y in self.Neighbors:
            if y == None:
                x += str(None) + "\n"
            else:
                x += str(y) + "\n"
        x += "Incoming\n"
        for y in self.Incoming:
            if y == None:
                x += str(None) + "\n"
            else:
                x += str(y) + "\n"
        return x

    def Insert_Lists_Node(self):
        ## write Insert_Lists_Node
        self.Neighbors.append(None)
        self.Incoming.append(None)
        

    def Insert_Lists_Edge(self, a, b):
        ## write Insert_Lists_Edge
        
        if self.Neighbors[a]==None:
            self.Neighbors[a]=Linked_List()
        NewNeighbor=List_Node(b)
        self.Neighbors[a].Insert_Node(NewNeighbor)
        
        if self.Incoming[b]==None:
            self.Incoming[b]=Linked_List()
        NewIncoming=List_Node(a)
        self.Incoming[b].Insert_Node(NewIncoming)

        NewNeighbor.Other=NewIncoming
        NewIncoming.Other=NewNeighbor
        
        
        
    def Check_Lists_Edge(self, a, b):
        ## write Check_Lists_Edge
        if self.Neighbors[a]==None:
            return False
        else:
            temp = self.Neighbors[a].Search(b)
            if temp == None:
                return False
            else:
                return True
            
    def Remove_Lists_Edge(self, a, b):
        ## write Remove_Lists_Edge
        if self.Neighbors[a]==None:
            return
        else:
            x = self.Neighbors[a].Search(b)
            if x == None:
                return
            else:
                Remove_List_Node(self.Neighbors[a],x)
                Remove_List_Node(self.Incoming[b],x.Other)
                
    def Remove_Lists_Node(self, a):
        ## write Remove_LIsts_Node
        if self.Incoming[a] != None:
            node = self.Incoming[a].Head
            while node != None:
                Remove_List_Node(self.Neighbors[node.Value],node.Other)
                node = node.Next
        if self.Neighbors[a] != None:
            node = self.Neighbors[a].Head
            while node != None:
                Remove_List_Node(self.Incoming[node.Value],node.Other)
                node = node.Next
        self.Incoming[a] = None
        self.Neighbors[a] = None





if __name__ == "__main__":

    print("\n")
    print("MATRIX REPRESENTATION")

    ## test code here
    M = Matrix_Graph_tzu088(5)
    print(M)

    M.Insert_Matrix_Edge(0,1)
    M.Insert_Matrix_Edge(1,4)

    print(M)

    M.Transpose_Graph()

    M.Insert_Matrix_Edge(0,2)

    M.Transpose_Graph()

    M.Insert_Matrix_Edge(3,2)

    print(M)

    print(M.Check_Matrix_Edge(2,0))
    print(M.Check_Matrix_Edge(2,2))

    M.Remove_Matrix_Node(0)

    print(M)

    M.Remove_Matrix_Node(1)

    print(M)

    M.ReAdd_Edgeless_Matrix_Node(0)

    print(M)


    print("\n")
    print("LISTS REPRESENTATION")


    L = Lists_Graph_tzu088()
    for i in range(5):
        L.Insert_Lists_Node()

    print(L)

    L.Insert_Lists_Edge(0,1)
    L.Insert_Lists_Edge(2,4)
    L.Insert_Lists_Edge(3,2)

    print(L)

    print(L.Check_Lists_Edge(0,1))
    print(L.Check_Lists_Edge(0,0))

    L.Remove_Lists_Edge(2,4)

    print(L)

    L.Insert_Lists_Edge(0,2)
    L.Insert_Lists_Edge(0,4)

    L.Insert_Lists_Node()
    L.Insert_Lists_Edge(5,0)

    print(L)

    L.Remove_Lists_Node(0)

    print(L)
    
    
