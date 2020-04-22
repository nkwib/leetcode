class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LList:
    def __init__(self):
        self.head = None
    def add(self, val):
        if self.head == None:
            self.head = ListNode(val)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = ListNode(val)

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        bin_num = ''
        while curr is not None:
            bin_num += str(curr.val)
            curr = curr.next
        print(bin_num)
        print(int(bin_num, 2))
        return int(bin_num, 2)
        
lista = LList()
for el in [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]:
    lista.add(el)

Solution().getDecimalValue(lista.head)