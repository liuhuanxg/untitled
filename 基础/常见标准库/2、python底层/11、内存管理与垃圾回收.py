#垃圾回收
#引用计数
#内存池机制

#一、垃圾回收
#python不像C++，java等语言一样，他们可以不用事先声明变量类型而直接对变量进行赋值。对python语言来讲，对象的类型和内存都是在运行时确定的。这也是为什么称python语言为动态类型的原因（可以把动态类型简单的归结为对变量内存地址的分配是在运行时自动判断变量类型并对变量进行赋值）

#python中使用了某些启发式算法来加速垃圾回收。例如，越晚创建的对象更有可能被回收。对象被创建之后，垃圾回收器会分配他们所属的代。每个对象都会被分配一个代，而被分配更年轻的对象是优先被处理的。


#二、引用计数
#python采用了类似windows内核对象一样的方式来对内存进行管理。每一个对象，都维护这一个对指向该对对象的引用的计数。当变量被绑定在一个对象上的时候，该变量的引用计数就是1（还有一些别的情况也会导致变量引用计数的增加），系统会自动维护这些标签，并定时扫描，当某个标签的引用计数变为0的时候，该对象就会被回收。


# 例：
x=4
y=x   #指向同一内存地址




#三、内存池机制python的内存机制以金字塔行，-1，-2层主要有操作系统进行操作。

#第0层是C中的malloc，free等内存分配和释放函数进行操作

#第1层和第2层是内存池，有python的接口函数PyMem_Malloc函数实现，当对象小于256k时由该层的直接分配内存。

#第3层是最上层，也就是对python对象的直接操作

#在C中如果频繁的调用malloc与free时，是会产生性能问题的，再加上频繁的分配与释放小块的内存会产生内存碎片，python在这里主要干的工作有：

#1、如果请求分配的内存在1到256字节之间就使用自己的内存管理系统，否则直接使用malloc，还会调用malloc分配内存地址，但是每次会分配一块大小为256k的大块内存

#经由内存池登记的内存到最后还是会会收到内存池，并不会调用C的free释放掉，以便下次使用，对于简单的python对象，例如数值、字符串，元组(tuple不允许被更改)采用的是复制的方式，也就是当将一个变量赋值给另一个变量A时，虽然A和B内存空间仍然相同，但当A的值发生变化时，会重新给A分配空间，A和B的地址变的不在相同。