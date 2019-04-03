from queue import LifoQueue #LIFO队列
lifoQueue = LifoQueue()
lifoQueue.put(1)
lifoQueue.put(2)
lifoQueue.put(3)
print('LIFO队列',lifoQueue.queue)
a=lifoQueue.get() #返回并删除队列尾部元素
print(a)
print(lifoQueue.queue)

cout=list(map(lambda x: x.replace('a','b'), ['asa','dgsa']))
print(cout)
print(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))