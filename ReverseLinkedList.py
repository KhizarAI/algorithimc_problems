# Reverse the linked list
#Input: head = 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #Time Complextiy O(N)
    #Space COmplexity O(1)
    def reverseList(head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev