class Stack:
    """
    Abstract Data Type (ADT) representation of a stack
    
    Stack: A Last-In, First-Out (LIFO) data structure.

    Attributes:
        items (list): A list to store the elements of the stack.
    """

    def __init__(self):
        """
        Initializes a new empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Pushes an item onto the top of the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
