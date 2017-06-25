"""
In this challenge, you must first implement a queue using two stacks. Then
process q queries, where each query is one of the following 3 types:
    1. 1 x: Enqueue element  into the end of the queue.
    2. 2: Dequeue the element at the front of the queue.
    3. 3: Print the element at the front of the queue.

Input Format
The first line contains a single integer, q, denoting the number of queries.
Each line i of the q subsequent lines contains a single query in the form
described in the problem statement above. All three queries start with an
integer denoting the query type, but only query 1 is followed by an additional
space-separated value, x, denoting the value to be enqueued.

Output Format
For each query of type 3, print the value of the element at the front of the
queue on a new line.

"""


class Queue(object):
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        self._queue.pop(0)

    def peek(self):
        print self._queue[0]

queue = Queue()

q = int(raw_input())

for i in range(q):
    query = raw_input().split()
    if query[0] == '1':
        queue.enqueue(int(query[1]))
    if query[0] == '2':
        queue.dequeue()
    if query[0] == '3':
        queue.peek()
