
队列概念

队列可以并发的分派多个线程,并按指定的顺序进行处理,把请求的数据放入队列容器中,线程不需要等待,当队列处理完数据 后,线程再准时来取数据即可。请求数据的线程只与这个队列容器存在关系,处理数据的线程down掉不会影响到请求数据的线程, 队列会派给其他线程处理这份数据,它实现了解耦,提高效率。当在多个线程或进程之间需要安全得交换信息或共享资源时,就需 要使用队列。
Python四种类型的队列:
1. Queue:FIFO 即 first in first out 先进先出
2. LifoQueue:LIFO 即 last in first out 后进先出
3. PriorityQueue: 优先队列,级别越低,越优先
4. deque:双端队列


Queue常用方法
![image](https://github.com/user-attachments/assets/9549cf3d-0bc8-4769-a0f6-32e500507ca9)

輸出結果
![image](https://github.com/user-attachments/assets/fac4bbaa-e80b-4b21-9325-8dbd3e360d19)

四種對列用法

1.Queue先進先出
![image](https://github.com/user-attachments/assets/2ebe276a-6c26-4793-bde8-435e625a81b0)

輸出結果
![image](https://github.com/user-attachments/assets/7353b574-b50b-46d4-8e0d-c40078f7853b)

2.LifoQueue 後進先出
![image](https://github.com/user-attachments/assets/e9ce673f-d259-4529-a59f-8962625d75a1)

輸出結果
![image](https://github.com/user-attachments/assets/8f0f1a0f-ab85-4b73-8ef5-8c147f035f9c)

3.PriorityQueue 優先對列
![image](https://github.com/user-attachments/assets/f383e15b-a2bd-4e5e-bd99-5871edc22bff)

輸出結果
![image](https://github.com/user-attachments/assets/9fdd2597-feff-41f5-bd8d-47c76be76b9b)

4.deque 雙端隊列
![image](https://github.com/user-attachments/assets/1f10891f-b46b-47f0-93e8-180127cd2445)

輸出結果
![image](https://github.com/user-attachments/assets/082e8b39-8855-47ba-95c5-887fa6e973c1)


