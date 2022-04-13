# Python 并发编程实战，用多线程、多进程、多协程加速程序运行

[视频链接]https://www.bilibili.com/video/BV1bK411A7tV?p=1

Python线程、进程、协程的区别

+ 一个进程中可以启动多个线程
+ 一个线程中可以启动多个协程
+ Python中多线程由于GIL的存在，无法利用多核，只能并发

多进程Process（multiprocessing）

+ 优点：
    + 可以利用多核CPU**并行计算**
+ 缺点：
    + 占用资源多，可以启动的数目比线程少
+ 适合：
    + CPU密集型计算

多线程Thread（threading）

+ 优点：
    + 相比进程，更轻量，占用资源少
+ 缺点：
    + 相比进程，**多线程只能并发执行**，不能利用多核CPU
    + 相比协程，启动数目有限制，内用资源，有切换开销
+ 适合： IO密集型计算，同时运行的任务数目要求不多

多协程Coroutine（asyncio）

+ 优点：
    + 内存开销最小，启动数目最多
+ 缺点：
    + 支持的库有限制（requests不支持，只能使用aiohttp），代码实现复杂
+ 适用：
    + IO密集型，需要超多任务运行，有现成库支持

Python在特殊场景下，可能比C++慢100~200倍。

queue.Queue是一个线程安全的通信队列

Queue.put() # 添加元素

item = Queue。get() # 获取元素