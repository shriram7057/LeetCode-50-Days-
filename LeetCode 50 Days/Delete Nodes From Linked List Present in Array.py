class Solution(object):
    def modifiedList(self, nums, head):
        remove = set(nums)
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next:
            if cur.next.val in remove:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next