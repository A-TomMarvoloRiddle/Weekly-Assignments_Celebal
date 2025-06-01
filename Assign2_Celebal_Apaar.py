
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def print(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        print("Linked List: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_node(self, n):
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")
            if n <= 0:
                raise IndexError("Index should be 1 or greater.")
            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node at index {n} with value {deleted_data}")
                return
            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1
            if not current or not current.next:
                raise IndexError("Index out of range.")
            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node at index {n} with value {deleted_data}")
        except Exception as e:
            print("Error:", e)

ll = LinkedList()

ll.print()

print("\nAdding Nodes")
for value in [5, 15, 25, 35, 45, 55]:
    ll.append(value)
ll.print()

print("\nDelete Head Node")
ll.delete_node(1)
ll.print()

print("\nDelete Middle Node (3rd node)")
ll.delete_node(3)
ll.print()

print("\nDelete Last Node")
ll.delete_node(4)
ll.print()

print("\nDelete with Invalid Index (0)")
ll.delete_node(0)

print("\nDelete with Out-of-Range Index (10)")
ll.delete_node(10)

print("\nDeleting All Remaining Nodes")
ll.delete_node(1)
ll.delete_node(1)
ll.delete_node(1)
ll.print()

print("\nTry Deleting from Empty List")
ll.delete_node(1)

print("\nAdd After Emptying List")
ll.append(100)
ll.append(200)
ll.print()

print("\nDelete 2nd Node")
ll.delete_node(2)
ll.print()
