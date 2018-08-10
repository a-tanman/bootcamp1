import random

class Queue:

    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.append(item)
    
    def get(self):
        item = self.items[0]
        del self.items[0]
        return item

    def is_empty(self):
        return len(self.items) == 0

    def qsize(self):
        return len(self.items)

q1 = Queue()
for x in range(random.randint(1,10)):
    #print(x)
    q1.put(x)
#print(q1.get())
#print(q1.qsize())

def radix_sort(items):

    q_main = Queue()

    for item in items:
        q_main.put(item)

    queue_list = [Queue() for i in range(10)]

    max_digits = len(str(max(items)))
    total_length = q_main.qsize()

    for x in range(max_digits):
         
        for i in range(total_length):
           
            item = q_main.get()
            item_str = str(item)
            item_len = len(item_str)
            if item_len > x:
                last_digit = item_str[item_len - 1 - x]
            else:
                last_digit = 0
            # print(item)
            # print(last_digit)
            queue_list[int(last_digit)].put(item)
        
        for i in range(10):
            # print(queue_list[i].is_empty())
            while not queue_list[i].is_empty():
                q_main.put(queue_list[i].get())

    return q_main



result = radix_sort([154, 26, 293, 17, 377, 31, 444, 55, 620, 65])
resultlist = [result.get() for x in range(result.qsize())]
print(resultlist)