# 1 计算机系统漫游

## 1.2 程序被其它程序翻译成不同的格式

预处理器，cpp -> 编译器，ccl -> 汇编器，as -> 链接器，ld

### 1.4.1 系统的硬件组成

I/O设备通过控制器或适配器与I/O总线连接

控制器：主板上的芯片组

适配器：插在主板插槽上的卡

指令集架构描述的是每条机器代码指令的效果

而微体系结构描述的是处理器实际上是如何实现的

利用直接存储器存取（DMA）技术，数据可以不通过处理器而直接从磁盘到达主存

### 1.7.1 进程 

操作系统实现这种交错执行的机制称为上下文切换

### 1.7.2 线程

尽管通常我们认为一个进程只有单一的控制流，但是在现代系统中，一个进程实际上可以由多个称为线程的执行单元组成，每个线程都运行在进程的上下文中，并共享同样的代码和全局数据。