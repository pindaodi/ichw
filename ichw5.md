### 一、网络
该单位的网络号：162.105.80.128  
该单位理论上可容纳多少主机：62  
北大可以有多少个这样的子网:2^16-2  
### 二、三次握手
这个问题的本质是, 信道不可靠, 但是通信双发需要就某个问题达成一致. 而要解决这个问题, 无论你在消息中包含什么信息, 三次通信是理论上的最小值. 所以三次握手不是TCP本身的要求, 而是为了满足"在不可靠信道上可靠地传输信息"这一需求所导致的. 请注意这里的本质需求,信道不可靠, 数据传输要可靠. 三次达到了, 那后面你想接着握手也好, 发数据也好, 跟进行可靠信息传输的需求就没关系了. 因此,如果信道是可靠的, 即无论什么时候发出消息, 对方一定能收到, 或者你不关心是否要保证对方收到你的消息, 那就能直接发送消息就可以了。
### 三、恶意软件
计算机病毒：一类寄生于其它可执行代码或文档上、可自我复制进行传播的程序。  
分类：木马，间谍软件，广告软件。  
如何防范：  
安装杀毒软件/安全防护软件, 及时打补丁  
使用防火墙, 禁止外部计算机通过网络访问本机  
不随便下载运行可执行程序  
不打开未知的邮件附件  
U 盘 通常带毒, 打开前要先查毒  
不随便暴露自己的 email、生日、手机等重要信息  
不以 Administrator 权限操作计算机
