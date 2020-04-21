class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = l1.val + l2.val
        if sum >= 10:
            resto = 1
        result = ListNode(sum % 10)
        somma = result
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next            
            sum = l1.val + l2.val + resto
            resto = 0
            if sum >= 10:
                resto = 1
            next = ListNode(sum % 10)
            result.next = next
            result = result.next

        while l1.next:
            l1 = l1.next
            sum = l1.val + resto
            resto = 0
            if sum >= 10:
                resto = 1
            next = ListNode(sum % 10)
            result.next = next
            result = result.next
            
        while l2.next:
            l2 = l2.next
            sum = l2.val + resto
            resto = 0
            if sum >= 10:
                resto = 1
            next = ListNode(sum % 10)
            result.next = next
            result = result.next

        if not l1.next and not l2.next and resto == 1:
            next = ListNode(1)
            result.next = next
            
        return somma

def addSingleDigits(d1, d2):
    resto = 0
    sum = l1.val + l2.val
    if sum >= 10:
        resto = 1
    result = ListNode(sum % 10)
    somma = result
    return resto