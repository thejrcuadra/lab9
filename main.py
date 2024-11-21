class Queue:
    def __init__(self):
        # Initialize an empty list to store queue items
        self.items = []
        return

    def enqueue(self, value):
        # Add new item to back of queue
        self.items.append(value)
        return
    
    def dequeue(self):
        # Remove and return first item of queue
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)
        
    def isEmpty(self):
        # Returns True if the queue is empty, False if not
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def first(self):
        # Return the first item of queue without removing
        if len(self.items) == 0:
            return None
        else:
            return self.items[0]
        
    def last(self):
        # Return the last item of queue without removing
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]
        
    def queueSize(self):
        return len(self.items)
    

''' BALANCED PARENTHESES CHECKER '''

        
def isBalanced(expression):
    # Create a queue instance
    queue1 = Queue()

    # Defining the characters
    open = "({["
    closing = ")}]"

    # Loop through each character in expression
    for character in expression:
        # Check if the character is an open parenthesis
        if character in open:
            # Enqueue character
            queue1.enqueue(character)
        elif character in closing:
            # If the stack is empty or the first item in queue does not match
            # the corresponding parenthesis, the list is not balanced
            if queue1.isEmpty() == True:
                return False
            # Dequeue the correct item from front of list
            else:
                queue1.dequeue()
    # If queue is empty return True, all parenthesis were correctly
    # matched. Otherwise, return False
    return queue1.isEmpty()

# Test cases 
expression1 = "({X+Y}*Z)"
expression2 = "{X+Y}*Z)"
expression3 = "({X+Y}*Z"
expression4 = "([A+B]*({X+Y})*Z)"

# Expected output: True, False, False, True respectively
print(isBalanced(expression1))
print(isBalanced(expression2))
print(isBalanced(expression3))
print(isBalanced(expression4))


''' PRINT ORDER QUEUE '''


def simulatePrintEnqueue(jobs):
    # Create a queue iteration
    queue2 = Queue()

    # Loop through each print job
    for job in jobs:
        # Enqueue each job
        queue2.enqueue(job)

    # Loop through each print job
    for job in jobs:
        # Dequeue each job
        dequeue = queue2.dequeue()
        # Print the result
        print(dequeue)

# Creating Print Jobs Examples
job1 = "Michael: Financial Report"
job2 = "Michael: Criminal Report"
job3 = "Jeanette: Q3 Earnings Report"
job4 = "Rachel: Sales Report"
job5 = "Rudy: Status Update Report"

# Creating Print Job Combinations Exampls
jobs = [job1, job2, job3, job4, job5]
jobs2 = [job2, job2, job1, job3, job5]
jobs3 = [job5, job4, job3, job2, job1]
jobs4 = [job1, job1, job1, job1, job1]
jobs5 = [job1, job2, job5, job2, job3]

# Simulating the print enqueues and adding space between each iteration
print()
simulatePrintEnqueue(jobs)
print()
simulatePrintEnqueue(jobs2)
print()
simulatePrintEnqueue(jobs3)
print()
simulatePrintEnqueue(jobs4)
print()
simulatePrintEnqueue(jobs5)