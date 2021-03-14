class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    first = None
    sec = None
    carry = 0

    while l1 is not None or l2 is not None:
        value = carry

        if l1 is not None:
            value += l1.val
            l1 = l1.nxt
        if l2 is not None:
            value += l2.val
            l2 = l2.nxt

        carry_value = ListNode(value % 10)
        carry = value // 10

        if sec is None:
            sec = first = carry_value

        else:
            sec.nxt = carry_value
            sec = sec.nxt
    if carry > 0:
        sec.nxt = ListNode(carry)

    return first
