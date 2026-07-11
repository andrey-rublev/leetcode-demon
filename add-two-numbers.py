class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ret = ListNode(0)
        cur = ret
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value//10
            temp = ListNode(value%10)
            cur.next = temp
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            cur = cur.next
        return ret.next