class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def add(self,l1,l2):
        result = ListNode(0)
        r_tail = result
        c = 0
        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            c, num = divmod(c,10)
            print(c,num)
            r_tail.next = ListNode(num)
            r_tail = r_tail.next
        return result.next

def tolistnode(l_list):
    l = ListNode(0) #head
    l_tail = l # agent for next
    for l_val in l_list:
        l_tail.next = ListNode(l_val)
        l_tail = l_tail.next
    return l.next
    
list1 = [2,3,5] #532
list2 = [2,9,8] #892
#1424
l1 = tolistnode(list1)
l2 = tolistnode(list2)
solution = Solution()
ans = solution.add(l1,l2)
