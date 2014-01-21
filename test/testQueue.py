import Queue


qu = Queue.Queue()

for i in range(10):
    qu.put(i)

while not qu.empty():
    print qu.get()
