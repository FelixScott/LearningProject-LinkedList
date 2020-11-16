# --------------------------------------------- Linked List Demonstration ---------------------------------------------
# As python does not have pointers this program uses the index values of a normal list to reference stored data.
# The data input for this program is csv.
# Two lists are created, the first is an unlinked indexed list containing each card transaction and all associated data.
# The second is a linked list of nodes containing a name and the index value of the data in the unlinked list
# Each node stores a previous and next value to navigate the lists.
# To retrieve data from a name the linked list will be scanned for the name jumping from node to its next node until
# the tail is reached.
# --------------------------------------------- Linked List Demonstration ---------------------------------------------

class CardTransaction:
    def __init__(self, UniqueIdentifier, SeriesReference, Period, DataValue, Status, Units, Magnitude, Subject, Group, SeriesTitle1, SeriesTitle2):
        # Creates all stored values for each card transaction
        self.UniqueIdentifier = UniqueIdentifier
        self.SeriesReference = SeriesReference
        self.Period = Period
        self.DataValue = DataValue
        self.Status = Status
        self.Units = Units
        self.Magnitude = Magnitude
        self.Subject = Subject
        self.Group = Group
        self.SeriesTitle1 = SeriesTitle1
        self.SeriesTitle2 = SeriesTitle2

    def DataInput(self, FileName, TransactionsLinkedList, TransactionsUnlinkedList):
        # Reads the file of CSV and creates the linked and unlinked lists
        import csv
        with open(FileName, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            i = 0
            for line in csv_reader:
                TransactionsLinkedList.Insert(i, line[0])
                TransactionsUnlinkedList.append(
                    CardTransaction(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                                    line[9], line[10]))
                i += 1


class LinkedListNode:
    def __init__(self, Value, Name):
            self.Value = Value
            self.Name = Name
            self.NextNode = None
            self.PreviousNode = None


class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None

    def Insert(self, Value, Name):
        Node = LinkedListNode(Value, Name)
        if self.Head is None:
            self.Head = Node
        elif self.Tail is None:
            self.Tail = Node
            self.Tail.PreviousNode = self.Head
            self.Head.NextNode = Node
            Node.PreviousNode = self.Head
        else:
            self.Tail.NextNode = Node
            Node.PreviousNode = self.Tail
            self.Tail = Node

    def PrintLinkedList(self):
        CurrentNode = self.Head
        while CurrentNode != self.Tail:
            print (str(CurrentNode.Name) + " -> ")
            CurrentNode = CurrentNode.NextNode
        print(str(CurrentNode.Name))

    def FindEntry(self, NodeName):
        CurrentNode = self.Head
        while CurrentNode.Name != NodeName and CurrentNode is not self.Tail:
            CurrentNode = CurrentNode.NextNode
        if CurrentNode.Name == NodeName:
            return CurrentNode.Value
        else:
            return 0


def ReturnNode (LinkedList, UnlinkedList, NodeName):
    # Returns the whole dataset with this name, you must also ask for the value you want when you call it for instance:
    # ReturnNode(TransactionsLinkedList, TransactionsUnlinkedList, 'Transaction 6466').DataValue
    # This would return the DataValue for Transaction 6466
    return UnlinkedList[LinkedList.FindEntry(NodeName)]

# Declares the linked and unlinked lists
TransactionsLinkedList = LinkedList()
TransactionsUnlinkedList = []
# Calls the csv file
FileName = 'CardTransactions.csv'
# Uses the csv file to fill the two lists
CardTransaction.DataInput('', FileName, TransactionsLinkedList, TransactionsUnlinkedList)

print(ReturnNode(TransactionsLinkedList, TransactionsUnlinkedList, 'Transaction 6466').DataValue)

# -----------------------------------------Avenues for improvement available------------------------------------------
# * A node replace function
# -----------------------------------------Avenues for improvement available------------------------------------------
