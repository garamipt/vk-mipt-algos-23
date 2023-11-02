class lincked_list_node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class lincked_list:
    def push_back(self, data):
        self.tail.next = lincked_list_node(data)
        self.tail = self.tail.next

    def __init__(self, *data) -> None:
        if len(data) >= 2:
            self.head = lincked_list_node(data[0])
            self.tail = lincked_list_node(data[1])
            self.head.next = self.tail
            if len(data) > 2:
                for elem in data[2:]:
                    self.tail.next = lincked_list_node(elem)
                    self.tail = self.tail.next
        elif len(data) == 1:
            self.head = lincked_list_node(data[0])
            self.tail = lincked_list_node(data[0])

    def __repr__(self) -> str:
        node = self.head
        data = list()
        while node:
            data.append(str(node.data))
            node = node.next
        return " ".join(data)

    def reverse(self):
        prev = None
        node = self.head
        tail_flag = True
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            if tail_flag:
                self.tail = node
                tail_flag = False
            node = next_node
        else:
            self.head = prev
        
    def has_cycle(self) -> bool:
        slow = self.head
        fast = self.head.next
        while fast:
            if fast != slow:
                if fast.next:
                    fast = fast.next.next
                    slow = slow.next
                else:
                    return False
            else:
                return True
        return False
    
    def remove(self, val):
        dummy = lincked_list_node(None)
        dummy.next = self.head
        prev = dummy
        cur = self.head
        while cur:
            if cur.data == val:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
        if dummy.next != self.head:
            self.head = dummy.next

    def __getitem__(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.data
