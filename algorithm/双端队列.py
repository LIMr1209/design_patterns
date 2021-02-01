import time
import queue
import threading


q = queue.Queue(10)  # 生成一个队列，用来保存“包子”，最大数量为10


# 生产者
def productor(i):
    # 厨师不停地每2s做一个包子
    while True:
        q.put("厨师%s做的包子!" % i)
        time.sleep(2)


def consumer(i):
    # 顾客不停地每1s吃一个包子
    while True:
        print("顾客%s吃了一个%s" % (j, q.get()))
        time.sleep(1)


# 实例化3个生产者（厨师）
for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()

# 实例化10个消费者
for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()