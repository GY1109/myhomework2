# -*- coding: utf-8 -*-

from queue import Queue

# 作者信息
author = 'Evan'

def queue_usage(put_data):
    """
    Queue常用方法
    :param put_data: 放入的数据, 列表或元组类型
    :return:
    """
    q = Queue(maxsize=3)  # 设置队列上限为3

    for each in put_data:
        print(f'添加({each})到队列')
        q.put(each)
        print(f'当前队列大小: {q.qsize()}')
        print(f'队列是否为空: {q.empty()}')
        print(f'队列是否已满: {q.full()}')

    while not q.empty():
        print(f'从队列中取出: {q.get()}')
        q.task_done()  # 标记任务完成

    q.join()  # 阻塞调用线程, 直到队列中的所有任务被处理掉

if __name__ == '__main__':
    queue_usage(put_data=[1, 2, 3])

# coding: utf-8
from queue import Queue

# 作者信息
_author = 'Evan'

def fifo_queue(put_data):
    """
    FIFO, 先进先出队列
    :param put_data: 需要放入队列的数据, 可以是列表或元组
    :return: 无
    """
    # 确保put_data是列表或元组
    assert isinstance(put_data, (list, tuple)), 'put_data 必须是列表或元组类型'
    
    # 创建一个队列，maxsize为队列数据上限，小于或等于0则不限制
    q = Queue(maxsize=0)

    # 依次写入队列数据
    for each in put_data:
        print(f'将数据({each})加入队列')
        q.put(each)
        print(f'当前队列内容: {q.queue}')
    
    # 逐次取出所有数据
    while not q.empty():
        print(f'从队列中取出: {q.get()}')
        print(f'当前队列内容: {q.queue}')

if __name__ == '__main__':
    fifo_queue(put_data=[3, 2, 1])

# -*- coding: utf-8 -*-

from queue import LifoQueue

_author___ = 'Evan'

def lifo_queue(put_data):
    """
    LIFO, 后进先出队列
    :param put_data: 放入的数据, 列表或元组类型
    :return: 无
    """
    # 确保put_data是列表或元组
    assert isinstance(put_data, (list, tuple)), 'put_data 必须是列表或元组类型'
    
    # 创建一个后进先出队列，maxsize为队列数据上限，小于或等于0则不限制
    q = LifoQueue(maxsize=0)

    # 依次写入队列数据
    for each in put_data:
        print(f'将数据({each})加入队列')
        q.put(each)
        print(f'当前队列内容: {list(q.queue)}')
    
    # 逐次取出所有数据
    while not q.empty():
        print(f'从队列中取出: {q.get()}')
        print(f'当前队列内容: {list(q.queue)}')

if __name__ == '__main__':
    lifo_queue(put_data=[3, 2, 1])

# -*- coding: utf-8 -*-
from queue import PriorityQueue

author = 'Evan'

def priority_queue(put_data):
    """
    Priority, 优先队列, 级别越低, 越优先
    :param put_data: 放入的数据, 列表或元组类型，每个元素应为(优先级, 数据)的形式
    :return: 无
    """
    assert isinstance(put_data, (list, tuple)), 'put_data 必须是列表或元组类型'
    
    # 创建一个优先队列，maxsize为队列数据上限，小于或等于0则不限制
    q = PriorityQueue(maxsize=0)

    # 依次写入队列数据
    for each in put_data:
        print(f'将数据({each})加入队列，优先级: {each[0]}')
        q.put(each)
        print(f'当前队列内容: {list(q.queue)}')
    
    # 逐次按优先级取出所有数据
    while not q.empty():
        print(f'从队列中按优先级取出: {q.get()}')
        print(f'当前队列内容: {list(q.queue)}')

if __name__ == '__main__':
    priority_queue(put_data=[(3, 'value1'), (1, 'value2'), (2, 'value3')])

# -*- coding: utf-8 -*-
from collections import deque

author = 'Evan'

def deque_example(put_data):
    """
    Deque, 双端队列
    :param put_data: 放入的数据, 列表或元组类型
    :return: 无
    """
    assert isinstance(put_data, (list, tuple)), 'put_data 必须是列表或元组类型'
    
    # 创建一个双端队列，并将数据放入其中
    dq = deque(put_data)
    print(f'初始化的双端队列: {dq}')
    
    # 增加数据到队左
    dq.appendleft('aa')
    print(f'在队列左侧增加元素后: {dq}')
    
    # 增加数据到队尾
    dq.append('cc')
    print(f'在队列右侧增加元素后: {dq}')
    
    # 从队尾弹出一个元素
    print(f'从队列右侧弹出元素: {dq.pop()}')
    print(f'弹出元素后的队列: {dq}')
    
    # 从队首弹出一个元素
    print(f'从队列左侧弹出元素: {dq.popleft()}')
    print(f'弹出元素后的队列: {dq}')

if __name__ == '__main__':
    deque_example(put_data=['a', 'b', 'c'])
