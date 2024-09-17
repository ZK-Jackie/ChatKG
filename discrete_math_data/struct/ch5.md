# 第五章 关系模型与理论  

我们知道，日常生活或工作中的各种对象之间存在着千丝万缕的联系，包括人与人之间、人与物之间、物与物之间的联系。这种联系通常称之为关系，例如人与人之间的关系有兄弟关系、姻亲关系、朋友关系、同学关系、同事关系等等。这些关系反映了人与人之间各种错综复杂的活动，以这些关系为基础便可进一步衍生出许许多多不同的含义。事实上，一个人社会关系的宽泛程度通常标志着这个人某种能力的大小、威望的高低等等。同样，计算机领域的各种对象之间也存在诸多错综复杂的关系，例如计算机程序中输入与输出之间的关系、数据库中各种数据属性之间的关系、计算机语言中各种标识符之间的关系等等。要想让计算机系统能够自动、高效、正确地处理好这些关系，就必须建立一套完备严谨的关系模型与理论，为数据结构、数据库、信息检索、算法设计与分析、操作系统等计算机专业课程中各种对象之间关系的表达和处理提供有效的基础工具。  

正如计算机不能正确理解和处理基于自然语言表达的形式逻辑，计算机同样不能正确理解和处理用自然语言表达的关系模型与理论。因此，就像使用数理逻辑表达和处理形式逻辑问题一样，我们必须使用数学方法来表达和处理关系问题，面向关系问题建立一整套完备严谨的数学模型与数学理论。事实上，关系问题也是数学学科的一个重要研究对象，处理关系的数学理论诞生于著名数学家豪斯道夫1914 年出版的著作《集论基础》。经过100 多年的发展，关系数学理论已与集合论、数理逻辑、组合学、图论和布尔代数等多个数学分支交叉融 合，并通过吸收、借鉴这些数学分支的相关内容形成了一套相对完备的关系数学理论。  

关系的数学理论以集合论为基础，旨在描述给定集合上元素与元素之间的二元或多元关系，并考察集合中元素之间在一定次序下是否具备某些特定关系。从本章开始的连续三章将系统地介绍和讨论关系的数学模型与理论，本章着重介绍关系数学模型与理论的基本知识，包括关系的数学模型、关系的基本运算、关系的基本性质、关系集合的闭包等。  

## § 5.1 关系的数学模型  

从数学角度看，有些关系比较容易用数学符号表达。例如，自然数集合上自然数的大小比较关系，可用符号≤进行表示。但在很多时候，问题并没有这么简单，例如要表示某班每个学生与其籍贯之间的关系，这就涉及到该班学生集合与地域集合这两个集合元素之间的一种对应关系。此时，要想用数学符号表示这种对应关系，就需要一些巧妙的设计。事实上，可分别将学生集合和地域集合看成是两个在不同维度上的一维空间，并将这两个一维空间进行有序组合张成一个二维空间。此时，对于学生集合中任意一个给定的学生，将这个学生与其籍贯进行有序绑定后，就形成了这个二维空间中的一个点。所有这样的点构成的集合显然就准确地表示了该班每个学生与其籍贯之间的关系。由此可见，我们其实得到一种刻画两个集合中元素之间关系新方法，即首先将这两个集合组合成一个高维空间，然后用高维空间中点的集合来表示两个集合元素之间的关系。显然，这种新方法比前述用符号≤表示大小关系的传统方法更具普适性。本节着重介绍使用这种新方法构建的关系数学模型，为此首先介绍由两个集合组合成一个高维空间的数学机制，即元素的序偶与集合的笛卡尔积。  

### 5.1.1  序偶与笛卡尔积  

要用数学方式表达关系模型，首先必须建立有一种有效的数学机制将来自相同集合或不同集合的两个元素绑定在一起，以表明它们之间具体某种特定的关系。为此，下面给出二元组的相关概念来实现这种机制。  

【定义5.1】假设𝐴和$B$是任意给定的两个集合，则对于分别来自这两个集合中的元素$x$和𝑦，可将它们组合成一个整体并称之为二元组。如果这个二元组为无序二元组，则称其为无序偶对，简称为无序偶，通常记为$(x,y)$；如果这个二元组为有序二元组，则称其为有序偶对，简称为序偶，通常记为$\langle x,y\rangle$，并称$\cdot x\in A$为第一元素，$y\in B$为第二元素。  

在关系的数学理论中，通常使用序偶的概念绑定具有某种确定联系的两个元素。事实上序偶的用途非常广泛，日常生活和工作中的很多问题或概念都可用序偶表示。例如，平面上点$A$ 的横坐标是$x$，纵坐标是$y$，可用序偶表示为$\langle x,y\rangle$，$x,y\in R$；合肥是安徽的省会、南京是江苏的省会，可分别用序偶表示为〈合肥, 安徽〉，〈南京, 江苏〉；数学书在桌上、英语书在床上，可分别用序偶表示为〈数学书, 桌上〉，〈英语书,床上〉。  

由序偶的定义容易知道，序偶可以看作是具有两个元素的集合，但序偶中的两个元素是具有确定次序的，如果两个含有两个元素的集合相等，并不意味着这两个集合元素构成的序偶相等，因此即使成立$\{a,b\}=\{b,a\}$，在$a\neq b$的情况下会有：成立$\langle a,b\rangle\neq\langle b,a\rangle$。例如，对于前述的序偶〈合肥, 安徽〉，从集合的角度看，显然有{合肥, 安徽}$\}=$ {安徽,合肥}，但是序偶〈合肥, 安徽〉和〈安徽, 合肥〉显然代表的是两个不同的含义：前者表示合肥是安徽的省会，前者表示安徽是合肥的省会。因此，有：〈合肥, 安徽〉 $\neq$〈安徽,合肥〉。  

下面给出两个序偶相等的具体定义：  

【定义5.2】假设$\langle a,b\rangle$和$\langle c,d\rangle$是任意给定的两个序偶，如果$a=b$，$c=d$，那称这两个序偶相等，记为：$\langle a,b\rangle=\langle c,d\rangle$。  

从上述定义可知，两个序偶相等当且仅当这两个序偶在对应位置上的元素相等。例如，若有$\langle2x-3y,3x+2y\rangle=\langle1,3\rangle$，则有$2x-3y=1$且$3x+2y=3$；反之亦然。  

显然，可将上述序偶及其相等的相关定义自然推广到多个元素的情形。例如，对于任意给定的三个元素$x,y,z$，则可根据如下递归方式定义由这三个元素组成的有序三元组：  

$$
\langle x,y,\mathrm{z}\rangle=\langle\langle x,y\rangle,\mathrm{z}\rangle\tag{5-1}
$$

从上式可以看出，所谓有序三元组，其实就是序偶的序偶。一般地，可得到如下关于$^{\cdot n}$元有序组的相关定义：  

【定义5.3】由$n$个元素$a_{1}$ ,$a_{2},\dotsc,a_{n}$组成 $n$元有序组由$n-1$元有序组$\langle a_{1}\;\,,a_{2},\dots,a_{n-1}\rangle$和元素$a_{n}$组成的序偶，记作$\langle a_{1}\ ,a_{2},\ldots,a_{n}\rangle$。即：$\langle a_{1}\;\;,a_{2},\ldots,a_{n}\rangle=\langle\langle a_{1}\;\;,a_{2},\ldots,a_{n-1}\rangle,a_{n}\rangle$。  

【定义5.4】假设$\langle a_{1}\ ,a_{2},\ldots,a_{n}\rangle$和$\langle b_{1},b_{2},\dots,b_{n}\rangle$是任意给定的两个$ n$元有序组，如果$a_{i}=$$b_{i}$，$i=1,2,\dots,n$，则称它们相等，记为：$\langle a_{1}\,\ ,a_{2},\ldots,a_{n}\rangle=\langle b_{1},b_{2},\ldots,b_{n}\rangle\,.$。  

【例题5.1】用$n$元有序组描述下列语句： 

中国安徽合肥合肥工业大学计算机与信息学院； 学号为S001 的学生张亮选修了课程号为C002 的离散数学课，成绩为90；

2016 年6 月20 日22 点11 分56 秒；

20 加5 减7 再除以2 等于9。  

【分析】序偶中的元素是具有确定次序的，故第（1）题中的中国、安徽、合肥、合肥工业大学、计算机与信息学院五个元素的次序是不可交换的。第（2）、（3）、（4）题同理。  

【解】（1）〈中国,安徽, 合肥,合肥工业大学, 计算机与信息学院〉；  

​            （2）〈S001,张亮, C002, 离散数学,90〉 

​            （3）〈2016,6, 20, 22,11, 56〉； 

​            （4）〈20,5, 7, 2, 9〉。

下面使用序偶的概念来定义两个集合的笛卡尔积运算。为此，我们考察下列实例：在棋类游戏中有一种叫斗兽棋的游戏。该游戏一共有十六颗的棋子，分为红黄两组，各八个，由双方各执一组。具体如下：  

​                                     红方：象、狮、虎、豹、狼、犬、猫、鼠 

​                                     黄方：象、狮、虎、豹、狼、犬、猫、鼠  

令：集合$\scriptstyle A=\left\{\begin{array}{l l}{\begin{array}{r l r}\end{array}}\end{array}\right.$红，黄}表示棋子的颜色；  

​       集合$B{=}\{$象，狮，虎，豹，狼，犬，猫，鼠}表示棋子的名称。
则斗兽棋的每个棋子均由颜色和名称这两个属性的维度构成。  

因此，可将集合$A$ 中的任意元素与集合$B$ 中的任意元素进行组合构成相应的序偶，每一种可能的组合所形成的序偶就代表一个具体的棋子，所有可能的组合所形成的所有序偶就构成了斗兽棋的所有棋子，一共有16 个序偶，具体如下  

{〈 红 , 象 〉, 〈 红 , 狮 〉 ， 〈 红 , 虎 〉, 〈 红 , 豹 〉, 〈 红 , 狼 〉, 〈 红 , 犬 〉, 〈 红 ,  猫 〉,〈 红 ,  鼠 〉,   〈黄,象〉, 〈黄, 狮〉,〈黄, 虎〉, 〈黄,豹〉，〈黄,狼〉, 〈黄,犬〉, 〈黄,猫〉, 〈黄,鼠〉}。  

以这16 个序偶为元素，可以构成一个新的集合。这个集合其实是使用$A$ 和$B$ 这两个集合构造出来的一个集合。由此可知，上述过程实际上是构造了关于两个集合的一种新的运算方式，即两个集合的笛卡尔积运算。下面给出笛卡尔积运算的具体定义：  

【定义5.5】设$A,B$是任意给定的两个集合，用$A$中任意一个元素为第一元素、$B$中任任意一个元素为第二元素构成的所有可能的序偶组成的集合，称为$A$ 与$B$ 的笛卡尔积，亦称为$A$ 与$B$ 的直积，记为$A\times B$。即有：$A\times B=\{\langle x,y\rangle|(x\in A)\land(y\in B)\}$。  

由上述定义可知，集合$A$ 与$B$ 的笛卡尔积运算结果$A\times B$仍是一个集合，并且$A\times B$中的每个元素都是一个序偶，序偶中第一个元素取自集合$A$、第二个元素取自集合$B$。  

【例题5.2】令$A$ 为某大学所有学生的集合，$B$ 表示该大学开设的所有课程的集合。试给出$A$ 和$B$ 的笛卡尔积$A\times B$的含义？  

【解】笛卡尔积$A\times B$由形为$\langle a,b\rangle$的所有序偶组成，其中$a$ 表示某个学生，$b$ 表示该校开的一门课。集合${A\times B}$表示该校学生选课所有可能的情况。 

【例题5.3】设$A=\{a\},B=\{b,c\},C=\emptyset,D=\{1,2\}$，写出下列笛卡尔积中的元素：  

​            （1）$A\times B,\;\;B\times A;\;\;(\,2\,)\;\;A\times C,\;\;C\times A;$

​            （3）$A\times(B\times D),\;\;(A\times B)\times D$；  

【解】（1）$A\times B=\big\{\langle a\,,\ b\rangle\,,\ \langle a\,,\ c\rangle\big\},\ B\times A=\big\{\langle b\,,\ a\rangle\,,\ \langle c\,,\ a\rangle\big\};$     

​           （2）$A\times C=\phi,\;\;C\times A=\phi$；      

​           （3）${B}\times{D}=\{\langle b,1\rangle,\;\langle b,2\rangle,\;\langle c,1\rangle,\;\langle c,2\rangle\}; $
​                            $ A\times(B\times D)=\{\langle a,\langle b,1\rangle\rangle,\ \langle a,\langle b,2\rangle\rangle,\ \langle a,\langle b,1\rangle\rangle,\ \langle a,\langle c,2\rangle\rangle\}$。  
​                            $$(A\times B)\times D=\{\langle\langle a,b\rangle,1\rangle,\ \langle\langle a,b\rangle,2\rangle,\ \langle\langle a,c\rangle,1\rangle,\ \langle\langle a,c\rangle,2\rangle\}$$
由上例可以看出，在一般情况下$A\times B\neq B\times A$且$A\times(B\times D)\neq(A\times B)\times D$，即集合的笛卡尔集运算既不满足交换律也不满足结合律。  

假设根据笛卡尔积的定义，不难证明笛卡尔积运算满足如下几条基本性质：  

（1）假设$A$,$B$是任意给定的两个集合，则有：$A\times\emptyset=B\times\emptyset=\emptyset$；

（2）假设 $A$, $B$ 是任意给定的两个集合，则有 $A\times B=\emptyset$ ，当且仅当 $A=\emptyset$ 或 $B=\emptyset$；

（3）当$A,B$是有限集合时，有：$|A\times B|=|B\times A|=|A||B|$ 

  下面定理表明笛卡尔积运算对集合的并运算和交运算均满足分配律：  

【定理5.1】设$A$、$B$、$C$ 是任意集合，则有：  

$A\times(B\cup C)=(A\times B)\cup(A\times C);\quad A\times(B\cap C)=(A\times B)\cap(A\times C);$    

$(A\cup B)\times C=(A\times C)\cup(B\times C);\quad(A\cap B)\times C=(A\cup C)\times(B\times C)\,$。  

【证明】这里仅证明$A\times(B\cup C)=(A\times B)\cup(A\times C)$，其它三个等式可类似证明。  

对于任意$\langle x,y\rangle\in A\times(B\cup C)$，有$x\in A$且$y\in B\cup C$；由并运算的定义，有$y\in B$或$y\in C$.故有$x\in A$且$y\in B$或$x\in A$且$y\in C$。从而有：  
$$
\langle x,y\rangle\in A\times B或\langle x,y\rangle\in A\times C
$$
即$\langle x,y\rangle\in(A\times B)\cup(A\times C)$。从而有$ A\times(B\cup C)\subseteq(A\times B)\cup(A\times C)\,$。  

另一方面，对于任意$\langle x,y\rangle\in(A\times B)\cup(A\times C)$，则有$\langle x,y\rangle\in A\times B$或$\langle x,y\rangle\in A\times C$。又由笛卡尔积定义有$x\in A$且$y\in B$或$x\in A$且$y\in C$。从而有$ x\in A$且$y\in B\cup C$，即有：$\langle x,y\rangle\in$$A\times(B\cup C)$。故有：$(A\times B)\cup(A\times C)\ \ \subseteq\ \ A\times(B\cup C)\,$。  

综合以上两点，有：$A\times(B\cup C)=(A\times B)\cup(A\times C)$。

例如，设$A=\{1\},\;B=\{1,\!2\},\;C=\{2,\!3\},$  则有：

​      $A\times(B\cup C)=\ \{1\}\times\{1,\!2,\!3\}=\{\langle1,\!1\rangle,\langle1,\!2\rangle,\langle1,\!3\rangle\}$                                     $\begin{array}{r l}{(A\times B)\cup(A\times C)}&{=\{1\}\times\{1,2\}\cup\{1\}\times\{2\,,\ 3\}=\left\{\langle1\,,\ 1\rangle\,,\ \langle1\,,\ 2\rangle\,,\ \langle1\,,\ 3\rangle\right\}}\end{array}$ 

故有：$A\times(B\cup C)=(A\times B)\cup(A\times C)$  
​           $A\times(B\cap C)=\{1\}\times\{2\}=\{\langle1,2\rangle\}$
$\begin{array}{r l}{(A\times B)\cap(A\times C)}&{=\{\langle1,1\rangle,\langle1,2\rangle\}\cap\{\langle1,2\rangle,\langle1,3\rangle\}=\{\langle1,2\rangle\}}\end{array}。$                                          故有：$A\times(B\cap C)=(A\times B)\cap(A\times C)$  

【定理5.2】设$A$、${B}、{C}$ 是任意集合且$C\neq\emptyset$，则有：  
$$
A\subseteq B\Leftrightarrow(A\times C\subseteq B\times C);\,\,\,A\subseteq B\Leftrightarrow(C\times A\subseteq C\times B)
$$
【证明】仅证明$A\subseteq B\Leftrightarrow(A\times C\subseteq B\times C)$，可类似证明$A\subseteq B\Leftrightarrow(C\times A\subseteq C\times B)$。必要性：$\langle x,y\rangle\in A\times C\Leftrightarrow x\in A\land y\in C\Longrightarrow x\in B\land y\in C\Leftrightarrow<x,\;\;y>\in B\times C$ 故有：$A\times C\subseteq B\times C$。  

充分性：因为$C\neq\emptyset$，所以存在$y\in C$，对于任意的$x$，成立：  

$x\in A\Rightarrow\;\;x\in A\land y\in C\Leftrightarrow\langle x,y\rangle\in A\times C\Rightarrow\langle x,y\rangle\in B\times C\Leftrightarrow\;\;x\in B\land y\in C\Rightarrow\;\;x\in B$ 故有： $A\subseteq B$ 。

【定理5.3】设$A、\ B、C、D$为非空集合，则有：  
$$
A\subseteq C\land B\subseteq D\Leftrightarrow A\times B\subseteq C\times D
$$
【证明】充分性：对$\forall x\in A$，$y\in B$，有$\langle x,y\rangle\in A\times B$。又因为$A\times B\subseteq C\times D$，所以$\langle x,y\rangle\in$$C\times D$。根据笛卡尔积的定义有$x\in C$且$y\in D$，从而有：$A\subseteq C\land B\subseteq D$。  

必要性：$\forall\langle x,y\rangle\in A\times B$，有$\forall x\in A$且$y\in B$。又因为$A\subseteq C\land B\subseteq D$，故根据包含的定义有$x\in C$且$y\in D$，即$\langle x,y\rangle\in C\times D$，从而有：$A\times B\subseteq C\times D$。 

【例题5.4】设$A=\{1,2\}$，求$\rho(A)\times A$  

$\rho(A)=\{\emptyset,\ \{1\},\ \{2\},\ \{1,2\}\}$ $\rho(A)\times A=\{\langle\emptyset,1\rangle,\langle\emptyset,2\rangle,\{\{1\},1\rangle,\langle\{1\},2\rangle,\langle\{2\},1\rangle,\langle\{2\},2\rangle,\{\{1,2\},1\rangle,\langle\{1,2\},2\rangle\}\}$。 

【例题5.5】设$A$，$B$，$C$，$D$ 为任意集合，判断以下命题是否为真，并说明理由。 

(1)  $A\times B=A\times C\Rightarrow B=C;$ ；         (2)  $A-\left(B\times C\right)=\left(A-B\right)\times\left(A-C\right)$ 

(3) $A=B\land C=D\Rightarrow A\times C=B\times D$； (4)存在集合$A$，使得$A\subseteq A\times A$  

【解】(1）不一定为真，当$A=\emptyset$，$B=\{1\}$，$C=\{2\}$时有$A\times B=A\times C=\varnothing$，但 $B\neq$$C$。(2)不一定为真，当$A=B=\{1\}$，$C=\{2\}$时有：  
$$
A-\left(B\times C\right)=\{1\}-\left\{\langle1,2\rangle\right\}=\ \left\{\,1\,\right\}
$$

$$
(A-B)\times(A-C)=\varnothing\times\{1\}=\varnothing
$$
(3) 为真，由恒等置换的原理可证。  (4) 为真，当 $A=\emptyset$ 时，有 $A\subseteq A\times A$ 。 

可以将关于两个集合的笛卡尔积直接推广到多个集合的情形。为保证多元笛卡尔积运算结果的唯一性，特做如下约定：  
$$
A_{1}\times A_{2}\times A_{3}=(A_{1}\times A_{2})\times A_{3};
$$

$$
A_{1}\times A_{2}\times A_{3}\times A_{4}=(A_{1}\times A_{2})\times A_{3}\times A_{4}\,=\left((A_{1}\times A_{2})\times A_{3}\right)\times A_{4}
$$
$\cdots\cdots\cdots\cdots\cdots\cdots$
$$
A_{1}\times A_{2}\times\cdots\times A_{n}=(A_{1}\times A_{2}\times\cdots\times A_{n-1})\times A_{n}
$$
特别地，$A\times A\times\cdots\times A=A^{n}$，称$A^{n}$为$A$ 的$n$元笛卡尔积。

【定理5.4】假设集合$\cdot A_{1},A_{2},\cdots,A_{n}$均为有限集合，则有：  
$$
|A_{1}\times A_{2}\times\cdots\times A_{n}|=|A_{1}|\times|A_{2}|\times\cdots\times|A_{n}|
$$
【分析】因为$n$个集合的笛卡尔积由$n$重有序组构成，要构造一个$n$重有序组需要$n$个步骤：第一步从$A_{1}$中任意选一个元素，有$|A_{1}|$|种选法，第二步从$A_{2}$中任意选一个元素，有$|A_{2}|$种选法，直到第$n$步。由乘法原理知，$A_{1}\times A_{2}\times\cdots\times A_{n}$的基数为$|A_{1}|\times|A_{2}|\times\cdots\times|A_{n}|.$。  

【证明】有乘法原理可得：$|A_{1}\times A_{2}\times\cdots\times A_{n}|=|A_{1}|\times|A_{2}|\times\cdots\times|A_{n}|\,$。 

【例题5.6】假如某班学生的信息可用如下集合进行描述：

 $A_{1}=$｛201617001,201617002, 201617003,201617004｝；  

$A_{2}=$ ｛苏杰 ,  魏晨 ,  鲍勃 ,  海伦｝； 

  $A_{3}=$  ｛男 ,  女｝  

 $A_{4}=\mathrm{~~{~\left\{~19,~20,~21\right\}~}~}$ ；   $A_{5}=$ ｛北京，上海，广州｝  

试给出$A_{1}\times A_{2}\times A_{3}\times A_{4}\times A_{5}$中元素的个数和实际含义。

假设表5-1 是该班学生实际信息，试说明这些信息与$A_{1}\times A_{2}\times A_{3}\times A_{4}\times A_{5}$的关系。  

​                                                      表5-1 例题5.6 数据关系表 
![](images/8653377daa775dcaeb323cd0fbde2d422854657291b347fac606fb38905b8865.jpg)  

【解】$A_{1}\times A_{2}\times A_{3}\times A_{4}\times A_{5}$是$|A_{1}|\times|A_{2}|\times|A_{3}|\times|A_{4}|\times|A_{5}|=288$个有序5 元组的集合。表示的是学号、姓名、性别、年龄和籍贯这5 个属性所有可能的组合状态。  

显然，表5-1 中数据构成的集合R:

$R=\{\langle201617001$ ,  鲍勃 ,  男 , 21, 上海 〉 ， 〈20161201617002,  海伦 , 女 , 19,  北京 〉  

<201617003,苏杰,男, 20, 北京〉，〈201617004,魏晨, 女, 19,广州〉}  

是$A_{1}\times A_{2}\times A_{3}\times A_{4}\times A_{5}$的一个子集。 

事实上，$A_{1}\times A_{2}\times\cdots\times A_{5}$的任意一个子集都可以表示学号、姓名、性别、年龄和籍贯这5 个属性之间的一种特定关系。下面具体讨论这个问题。  

### 5.1.2  关系的概念  

现在我们使用序偶与笛卡尔积这两个概念建立表示两个元素之间二元关系的数学模型。首先考察一个具体实例：假设某个班级正在上离散数学课，教室里有100 个座位和85 名学生，那么教室里有些座位有学生坐、有些座位没有学生坐，如果某个座位被某个学生坐了，则称这个座位与这个学生有关系，否则称这个座位与这个学生没有关系，现在考虑要用什么样的数学模型来表示或定义这种学生与座位之间的二元关系。  

令集合$A$表示该教室所有学生组成的集合，集合B表示该教室所有座位组成的集合，则根据乘法原理，$A$与$B$的笛卡尔集$A\times B$就表示将这85 名学生分布到100 个座位上所有可能发生的状态，$A\times B$中每个元素$\langle x,y\rangle$就表示学生$x$与座位𝑦之间可能发生的一种关系，即学生$x$坐在座位𝑦上的一种可能发生的状态。显然，一共有$85\times100=8500$可能的状态。但是，这些状态一般不会都发生，事实上，此时实际发生的只有85 个状态，即学生和座位之间实际发生关系的有且只有$A\times B$中的85 个元素。因此，可以将$A\times B$中这85 个实际发生的状态作为集合来表示这85 名学生和100 个座位之间的关系。换句话说，这85 名学生和100 个座位之间的二元关系其实就是$A$与$B$的笛卡尔集$A\times B$的某个子集。  

也可以从另外一个角度理解这个问题：将集合$𝐴$和$B$分别看成是学生维度和座位维度这两个一维空间，则$𝐴$与$B$的笛卡尔集$A\times B$就表示由这两个维度的元素组合而成的二维空间。现从𝐴中任选一位学生$x$，从$B$中任选一个座位𝑦，让学生$x$坐到座位𝑦上，由此形成一个序偶$\langle x,y\rangle$。这个序偶对应着$A\times B$所形成二维空间的一个点，所有这样的点或者序偶显然构成了这个二维空间的一个子集合。另外一方面，所有这样的点或序偶组成的集合完全枚举了学生与座位实际发生的关系，故可将学生与座位之间的二元关系就定义为所有这样的序偶组成的集合。因此，座位和学生之间的二元关系其实就是$𝐴$与$B$的笛卡尔集$A\times B$的某个子集。  

在实际生活中，还有很多类似的例子。再如机票和座位之间对号关系，若令$X$为机票的集合，Y 为座位号的集合， $R$ 表示对号关系，则对任意$x\in X$和$y\in Y$，$x$与$y$ 之间有对号和不对号两种状态。若将$R$ 看成是一些序偶的某个集合或$X$与$Y$ 的笛卡尔集$X\times Y$的某个子集，则对于任意一个序偶$\langle x,\ y\rangle$， $x$与$y$具有对号关系当且仅当$\langle x,y\rangle\in R$。因此，可将这里的对号关系定义为序偶的某个集合或$X\times Y$的某个子集合。  

通过以上分析发现，可用序偶的集合或者笛卡尔集的某个子集合来构造二元关系的数学模型。据此得到如下关于二元关系的定义：  

【定义5.6】设$𝐴$, $B$是任意给定的两个非空集合，$R$是$A\times B$的任何一个给定的子集合，则称$R$ 是一个从$𝐴$到$B$的二元关系，简称为关系。也就是说，若$R\subseteq A\times B$，则称$R$是$𝐴$到$B$的一个二元关系，若$\ R\subseteq A\times A$，则称$R$是$𝐴$上的一个二元关系。特别地，若$R=\emptyset$，则称$R$ 为空关系；若$R=A\times B$，则称$R$ 为全关系。  

【定义5.7】设$𝐴$, $B$是任意给定的两个非空集合，$R$是$𝐴$到$B$的一个二元关系，对于$A\times B$中的任意一个序偶$\langle x,y\rangle$，若$\langle x,y\rangle\in R$，这称集合$𝐴$中的元素$x$与集合$\ B$中的元素$𝑦$之间具有关系$R$；若$R$是$𝐴$上的一个二元关系且$\langle x,y\rangle\in R$，则称集合𝐴中的元素$x$与$𝑦$之间具有关系$R$。  

由上述两个定义可以看出，我们以集合为基本工具通过确定关系外延的方式给出关系概念的数学定义。这样就不必用数学符号来表示关系概念的内涵。事实上，对于有些关系，即使用自然语言也无法清楚表达其复杂的内涵。  

【例题5.7】令$A=\{a,b\}$，$B=\{c,d\}$，写出从$A$ 到$B$ 的所有关系。  

【解】因为$A=\{a,b\}$，$B=\{c,d\}$，所以$A\times B=\left\{\langle a,c\rangle,\ \langle a,d\rangle,\ \langle b,c\rangle,\ \langle b,d\rangle\right\}$，于是$A\times B$的所有不同子集为：  

1 个0-元子集：$\varnothing$；4 个1-元子集：$\{\langle a,c\rangle\},\{\langle a,d\rangle\},\{\langle b,c\rangle\},\{\langle b,d\rangle\}$；

6 个2-元子集： $\{\langle a,c\rangle,\langle a,d\rangle\},\{\langle a,c\rangle,\langle b,c\rangle\},\{\langle a,c\rangle,\langle b,d\rangle\},\{\langle a,d\rangle,\langle b,c\rangle\},\{\langle a,d\rangle,\langle b,d\rangle\},\{\langle b,c\rangle,\langle b,d\rangle\};$ 4 个3-元子集： $\{\langle a,c\rangle,\langle a,d\rangle,\langle b,d\rangle\},\{\langle a,c\rangle,\langle b,d\rangle,\langle b,c\rangle\},\{\langle a,c\rangle,\langle a,d\rangle,\langle b,c\rangle\},\{\langle a,d\rangle,\langle b,d\rangle,\langle b,c\rangle\};$ 1  个 4- 元子集： $\{\langle a,c\rangle,\langle a,d\rangle,\langle b,c\rangle,\langle b,d\rangle\}$ 。  

需要注意的是，当集合$A,\,B$ 都是有限集时，$A\times B$共有$2^{|A|\cdot|B|}$个不同的子集，即从$A$ 到$B$ 的所有不同的关系总数共有$2^{|A|\cdot|B|}$个。  

【例题5.8】令集合$A=\{1,\!2,\!3,\!4\}$，$A$上的关系$R=\big\{\langle a,b\rangle\big|a$整除$b\}$，试枚举$\ R$中元素。  

【解】$\langle a,b\rangle\in R$当且仅当$a$ 和$b$ 是不超过4 的正整数且$a$ 整除$b$，故有：$R=\{\langle1,1\rangle,\langle1,2\rangle,\langle1,3\rangle,\langle1,4\rangle,\langle2,2\rangle,\langle2,4\rangle,\langle3,3\rangle,\langle4,4\rangle\}$

设集合$A=\{a_{1},a_{2},a_{3},a_{4},a_{5}\},\;\;B=\{b_{1},b_{2},b_{3},b_{4}\},\;\;C=\{a_{2},a_{3},a_{4}\},\;\;D=\{b_{3},b_{4}\},$ 序偶的集合 ${R}=\{\langle a_{2},b_{3}\rangle,\langle a_{2},b_{4}\rangle,\langle a_{3},b_{3}\rangle,\langle a_{4},b_{4}\rangle,\langle a_{4},b_{3}\rangle\}$。显然有$R\subseteq A\times B$，故$R$ 是从$A$ 到$B$的一个二元关系。  

![](images/f21a296fae3e098faaa3900cc4615cee3ba4531b4f17c607a85fa8fb673d5d95.jpg)  
                                                                  图5-1 关系的五个域  

如图5-1 所示，集合$C$和$D$满足：$C=\{x|\langle x,y\rangle\in R\}$；$D=\{y|\langle x,y\rangle\in R\}$。此时称$C$为$R$ 的定义域，记为$C=\mathsf{d o m}R$；称$D$为$R$ 的值域，记为$D=ranR$；$A$ 为$R$ 的前域，$B$ 为$R$ 的后域，并称$\mathrm{fld}R=D\cup C$为$R$ 的域。一般地，我们有如下定义：  

【定义5.8】设$𝐴$, $B$是任意给定的两个非空集合，$R$是$𝐴$到$B$的一个二元关系，则有：称$A$是$R$的前域， $B$是$R$的后域；由$R$ 中所有序偶的第一元素构成的集合称为$R$ 的定义域，记作$dom𝑅$，即有$\mathrm{dom}R=\{x|\langle x,y\rangle\in R\}$；由$R$ 中所有序偶的第二元素构成的集合称为$R$ 的值域，记作$ran𝑅$，即有$\mathrm{ran}R=\{y|\langle x,y\rangle\in R\}$；称$\mathrm{fld}R=\mathrm{dom}R\cup\mathrm{ran}R$为$R$ 的域。  

【例题5.9】设$A=\{a,b,c,d,e,f\}$, $B=\left\{\alpha,\beta,\gamma,\delta,\eta\right\}$，从$A$到$B$上的关系$R$定义为：$R=\{\langle a,\alpha\rangle,\langle a,\delta\rangle,\langle b,\alpha\rangle,\langle b,\beta\rangle,\langle c,\gamma\rangle,\langle e,\alpha\rangle,\langle f,\gamma\rangle\}$  

试求 $dom𝑅$ ，$ ran𝑅 $，$ fld𝑅  $。

【解】$\mathrm{dom}R=\{a,b,c,e,f\},\ \ \mathrm{ran}R=\{\alpha,\beta,\gamma,\delta\},\ \ \mathrm{fld}R=\{a,b,c,e,f,\alpha,\beta,\gamma,\delta\}$。显然，可将二元关系自然推广到多元关系，读者可自己给出相关内容，这里不再赘述。本书后续内容中所指的关系，若非特别说明，均为二元关系。  

### 5.1.3 关系的表示  

如前所述，我们使用集合定义一个二元关系，即任何一个二元关系都是笛卡尔积集合的某个特定子集。既然关系是一种集合，那么自然就可用表示集合的方法来表示关系。但是，关系的集合表示法有时候不能直观地展现关系的特点和性质，也不便于计算机处理。因此，有时需要使用图模型或矩阵来表示关系。由此得到关系的图示法和矩阵表示法。下面具体介绍和讨论关系的这些表示方法。  

#### 1、集合表示法（枚举法和描述法）  

关系的集合表示法主要有枚举法和描述法两种。所谓枚举法，就是将作为关系的集合中所有序偶一一枚举出来；所谓描述法，就是用集合的描述法表示作为关系的集合。例如，对于集合$A=\{1,2,3,4\}$上的整除关系$R$，如果用描述法表示，则有：${R=\{\langle a,b\rangle|a|b\}}$；如果用$R=\{\langle1,1\rangle,\langle1,2\rangle,\langle1,3\rangle,\langle1,4\rangle,\langle2,2\rangle,\langle2,4\rangle,\langle3,3\rangle,\langle4,4\rangle\}.$  

【例题5.10】考察如下整数集合的关系：  
$$
\begin{array}{l l}{{R_{1}=\{\langle a,b\rangle|a\leq b\}\quad}}&{{R_{2}=\{\langle a,b\rangle|a>b\}}}\\ {{R_{3}=\{\langle a,b\rangle|a=b或a=-b\}\quad}}&{{R_{4}=\{\langle a,b\rangle|a=b\}}}\\ {{R_{5}=\{\langle a,b\rangle|a=b+1\}\quad}}&{{R_{6}=\{\langle a,b\rangle|a+b\leq3\}}}\end{array}
$$
其中哪些关系包含$\langle1,1\rangle$、$\langle1,2\rangle$、$\langle2,1\rangle$、$\langle1,-1\rangle$、$\langle2,2\rangle$的序偶？  

【解】$\langle1,1\rangle$在$R_{1},R_{3},R_{4},R_{6}$中；$\langle1,2\rangle$在$R_{1},R_{6}$中；$\langle2,1\rangle$在$R_{2},R_{5},R_{6}$中；$\langle2,2\rangle$在$R_{1},R_{3},R_{4}$中。  

【例题5.11】设集合$A=\{1,2,3\}$，试用枚举法表示下列𝐴上二元关系： $R_{1}=\big\{\langle x,y\rangle\big|x$是𝑦的倍数}；$R_{2}=\{\langle x,y\rangle|x-y\in A\}$；                                 

$R_{3}=\big\{\langle x,y\rangle\big|x\,/\,y是素数;\,\,\,R_{4}=\big\{\langle x,y\rangle\big|x\neq y\big\}$  

【解】这些关系的枚举表示法如下：  

$R_{1}=\{\langle3,3\rangle,\langle3,1\rangle,\langle2,2\rangle,\langle2,1\rangle,\langle1,1\rangle\};\;\;R_{2}=\{\langle3,1\rangle,\langle3,2\rangle,\langle2,1\rangle\};$ $R_{3}=\{\langle3,1\rangle,\langle2,1\rangle\};\;\;R_{4}=\{\langle3,2\rangle,\langle3,1\rangle,\langle2,3\rangle,\langle2,1\rangle,\langle1,3\rangle,\langle1,2\rangle\}。$  

#### 2、有向图表示法  

图是一种非常重要的数学模型，是问题表示和求解的基本工具。本书将在后续相关内容专门介绍和讨论图模型的基本理论及应用。这里主要给出二元关系的一种图模型表示方法。一般来说，图模型由一些结点和一些联结结点的边构成，一条边关联且仅关联两个结点。对于任意给定的一条边，如果将关联这条边的其中一个结点确定为起点，另外一个结点确定为终点，则称该边为有向边，若一个图中的每条边都是有向边，则称该图为有向图。在一般情况下，有向图只能表示有限集合上的二元关系。下面给出二元关系的一种有向图表示方法，通常称表示关系的有向图为关系图。  

假设𝐴, $B$是任意给定的两个非空有限集合，$R$是$𝐴$到$B$的一个二元关系： （1）当$A\ne B$时，不妨设$A=\{a_{1},a_{2},\cdots,a_{n}\}$，$B=\{b_{1},b_{2},\cdots,b_{m}\}$，则可将$𝐴,$ $B$中每个元素分别看成是有向图的一个结点，用“ ∘”表示，并将$𝐴$中元素$a_{1},a_{2},\cdots,a_{n}$对应的结点放在左边一列作为有向边的起点，将$B$中元素$\cdot b_{1},b_{2},\cdots,b_{m}$对应的结点放在右边一列作为有向边的终点。对于关系$R$中的每个序偶，则构成有向图中的一条有向边，也就是说，对于$𝐴$中的任一元素$a_{i}$和$B$中的任一元素$b_{j}$组合而成的序偶$\langle a_{i},b_{j}\rangle$，当且仅当$\langle a_{i},b_{j}\rangle\in R$时，以$a_{i}$对应的结点为起点、以$b_{j}$对应的结点为终点画出一条有向边，由此得到$R$的关系图。  

（2）当$A=B$时，设$A=B=\{a_{1},a_{2},\cdots,a_{n}\}$，此时$R$ 是集合$𝐴$上的关系，则将$𝐴$中的每个元素分别看成是有向图中的一个结点，用“ ∘”表示，对于任意一个序偶$\langle a_{i},a_{j}\rangle$：  

如果$a_{i}$和$a_{j}$对应的不是同一个结点，则当且仅当$\langle a_{i},a_{j}\rangle\in R$时，使用以$a_{i}$对应的结点为起点、以$b_{j}$对应的结点为终点的有向边联结$a_{i}$和$a_{j}$对应的两个结点；如果$a_{i}$和$a_{j}$对应的是同一个结点，即$a_{i}$和$a_{j}$是$𝐴$中同一个元素，则当且仅当$\langle a_{i},a_{i}\rangle\in R$时，则在$a_{i}$对应的结点上画一个从该结点出发并回到该结点的有向小圆环。  

下面举例说明关系图的构造方法：  

【例题5.12】令$A=\{1,\!2,\!3,\!4\}$, $B=\{a,b,c\},R_{1}$和$R_{2}$均为从𝐴到$B$的二元关系：  

$R_{1}=\{\langle1,a\rangle,\langle1,c\rangle,\langle2,b\rangle,\langle3,a\rangle,\langle4,c\rangle\};\;\;R_{2}=\{\langle1,1\rangle,\langle1,4\rangle,\langle2,3\rangle,\langle3,1\rangle,\langle3,4\rangle,\langle4,1\rangle,\langle4,2\rangle\}$ 试用关系图表示${\bf}R_{1}$和$R_{2}$。  

【解】示$R_{1}$和$R_{2}$的关系图分别如图5-2 (a)和5-2 (b)所示：  

![](images/164e12a8d966a58da4bccd96243b92f115237bcf2360a7a3c90b09245cfb596d.jpg)  
                                                图5-2 例题5.12 中 $R_{1}$和$R_{2}$的关系图  

【例题5.13】试用关系图表示下列关系：  

（1）设$A=\{2,\!3,\!4\}$，$B=\{3,\!4,\!5,\!6\}$，$A$ 到$B$ 之间的整除关系；（2）设$C=\{1,\!2,\!3,\!4\}$，$C$上的小于等于关系。  

![](images/472c489fcb249768b665ed4fbb680e7c320e3886f7cab8f8434a1a12c589b5a3.jpg)  
图5-3 集合 A 到集合B 的关系图  

![](images/1a8372b112c3c194c5273427a45a30933bd75922106aff701bbf5229d53fb2c1.jpg)  
图5-4  集合C 上的关系图  

【解】设${ R}_{1}$是$A$ 到$B$ 之间的一种整除关系，$R_{2}$是 $C$ 上的小于等于关系，则有：  

(1)$R_{1}=\{\langle2,4\rangle,\langle2,6\rangle,\langle3,3\rangle,\langle3,6\rangle,\langle4,4\rangle\}$

 (2)$R_{2}=\{\langle1,1\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle4,4\rangle,\langle1,2\rangle,\langle1,3\rangle,\langle1,4\rangle,\langle2,3\rangle,\langle2,4\rangle,\langle3,4\rangle\}$  

$R_{1}$和$R_{2}$的关系图分别如图5-3 和图5-4 所示。  

【例题5.14】试用集合的方式表示图5-5 所示的关系图：  

![](images/55aa50af0107f21967ac4377803258b5780959414d945fd1de1f8006a54a6aa6.jpg)  
图5-5例题5.14 的关系图  

【解】令图5-5 所示关系图表示的关系为$R$，则$R$的集合表示如下： $R=\{\langle a,b\rangle,\langle b,b\rangle,\langle b,c\rangle,\langle b,f\rangle,\langle c,d\rangle,\langle d,d\rangle,\langle d,e\rangle,\langle e,a\rangle,\langle e,e\rangle,\langle e,f\rangle,\langle f,b\rangle,\langle f,e\rangle\}\,$  

#### 3、矩阵表示法  

在使用关系的数学模型对实际问题进行建模的时候，通常需要对关系模型进行一些定量的数值计算以实现对实际问题的求解，此时无论是关系的集合表示方法和关系图法，都不方便实现对关系模型定量的数值计算。为此，我们引入二元关系的矩阵表示法。  

假设$\boldsymbol A=\{a_{1},a_{2},\cdots,a_{n}\}$, $B=\{b_{1},b_{2},\cdots,b_{m}\}$是任意给定的两个非空有限集合，$R$是$A$到$B$的一个二元关系，则按下列方式定义的$m\times n$阶矩阵$M_{R}=(r_{i j})_{m\times n}$称为$R$的关系矩阵：  
$$
r_{ij}=\begin{cases}1\text{,若}\langle a_i,b_j\rangle\in R\\0\text{,若}\langle a_i,b_j\rangle\not\in R\end{cases}\quad(1\leq i\leq m,1\leq j\leq n)\quad\text{(5-3)}
$$
其中$A$中元素$a_{i\cdot}$序号对应矩阵元素的行下标，$B$中元素$b_{j}$序号对应矩阵元素的列下标。

【例题5.15】设$A=\{1,2,3,4\}$, $B=\{a,b,c\}$，关系$R_{1}$和 $R_{2}$的定义如下：  
$$
R_{1}=\{\langle1,a\rangle,\langle1,c\rangle,\langle2,b\rangle,\langle3,a\rangle\langle3,a\rangle,\langle4,c\rangle\}
$$

$$
R_{2}=\{\langle1,1\rangle,\langle1,4\rangle,\langle2,3\rangle,\langle3,1\rangle,\langle3,4\rangle,\langle4,1\rangle,\langle4,2\rangle\}
$$
试写出$R_{1},\ R_{2}$的关系矩阵。  

【解】根据题意及关系矩阵的概念，易知$R_{1},\ R_{2}$的关系矩阵如下：  
$$
M_{R_{1}}={\left(\begin{array}{l l l}{1}&{0}&{1}\\ {0}&{1}&{0}\\ {1}&{0}&{0}\\ {0}&{0}&{1}\end{array}\right)},\quad M_{R_{2}}={\left(\begin{array}{l l l}{1}&{0}&{0}&{1}\\ {0}&{0}&{1}&{0}\\ {1}&{0}&{0}&{1}\\ {1}&{1}&{0}&{0}\end{array}\right)}
$$
解毕！

【例题5.16】设$A=\{1,\!2,\!3,\!4\}$，对于𝐴上的整除关系$R$ 和相等关系$S$，要求：  

（1）写出$R$ 和$S$的所有元素；（2）写出$R$ 和$S$ 的关系矩阵。  

【解】（1）根据整除关系和等于关系的定义，有： $\begin{array}{r}{R=\{\langle1,1\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle4,4\rangle,\langle1,2\rangle,\langle1,3\rangle,\langle1,4\rangle,\langle2,4\rangle\};\quad S=\{\langle1,1\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle4,4\rangle\}\,}\end{array}$ （2）设$R$ 和$S$ 的关系矩阵分别为${M}_{R},{M}_{S}$，则有：  
$$
M_{R}={\left(\begin{array}{l l l}{1}&{1}&{1}&{1}\\ {0}&{1}&{0}&{1}\\ {0}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\end{array}\right)},\;\;\;\;\;\;M_{S}={\left(\begin{array}{l l l}{1}&{0}&{0}&{0}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\end{array}\right)}
$$
解毕！  

值得注意的是：由关系矩阵的定义可知，关系矩阵的元素有且仅有0 和1 这两种状态，这样的矩阵一般称之为布尔矩阵，主要用于一些逻辑演算，在运算规则上与普通矩阵有一些差异。为满足后续内容学习的需要，在此简要介绍布尔矩阵的若干基本运算，具体包括并运算、交运算、补运算和布尔积运算，其具体定义如下：  

【定义5.9】设$A=\left(a_{i j}\right)$和$B=\left(b_{i j}\right)$是两个$m\times n$布尔矩阵，则$𝐴$和$B$的并矩阵定义为如下$m\times n$布尔矩阵：$A\lor B=C=\left(c_{i j}\right)$，其中：  

$c_{ij}=\begin{cases}1\text{,如果}a_{ij}=1\text{ 或}b_{ij}=1\\0\text{,如果}a_{ij}=0\text{ 且}b_{ij}=0\end{cases}(1\leq i\leq m,1\leq j\leq n)\quad\text{(5-4)}$      （5-4）  

【定义5.10】设$A=\left(a_{i j}\right)$和$B=\left(b_{i j}\right)$是两个$m\times n$布尔矩阵，则$A$和$B$的交矩阵定义为如下一个$m\times n$布尔矩阵：$A\land B=C=\left(c_{i j}\right)$，其中：  
$$
c_{ij}=\begin{cases}1\text{,如果}a_{ij}=1\text{ 且}b_{ij}=1\\0\text{,如果}a_{ij}=0\text{ 或}b_{ij}=0\end{cases}(1\leq i\leq m,1\leq j\leq n)\quad\text{(5-5)}
$$
【定义5.11】设$A=\left(a_{i j}\right)$任意给定的一个$m\times n$布尔矩阵，则𝐴的补矩阵定义为如下$m\times$$n$布尔矩阵：$\bar{A}=C=\left(c_{i j}\right)$，其中：  
$$
c_{ij}=\begin{cases}1\text{,如果}a_{ij}=0\\0\text{,如果}a_{ij}=1\end{cases}\quad(1\leq i\leq m,1\leq j\leq n)\quad\text{(5-6)}
$$
【定义5.12】设$A=\left(a_{i j}\right)$是$m\times p$矩阵，$B=\left(b_{i j}\right)$是$p\times n$矩阵，则$𝐴$和$B$的布尔积矩阵定义为如下$m\times n$布尔矩阵：$A\odot B=C=\left(c_{i j}\right)$，其中：  

$$
c_{ij}=\begin{cases}1\text{,如果}a_{ij}=0\\0\text{,如果}a_{ij}=1\end{cases}\quad(1\leq i\leq m,1\leq j\leq n)\quad\text{(5-6)}
$$
需要注意的是：两个布尔矩阵可进行布尔或和布尔与运算的前提是这两个矩阵具有相同的行数和列数，可进行布尔积运算的前提是前一个矩阵的列数等于后一个矩阵的行数。  

【例题5.17】令$A=\left(\begin{array}{l l l}{1}&{0}&{1}\\ {1}&{1}&{1}\\ {1}&{0}&{0}\\ {0}&{0}&{1}\end{array}\right),\ B=\left(\begin{array}{l l l}{0}&{0}&{0}\\ {1}&{0}&{1}\\ {1}&{1}&{0}\\ {0}&{1}&{1}\end{array}\right),\ C=\left(\begin{array}{l l l}{0}&{0}&{0}&{1}\\ {1}&{0}&{1}&{1}\\ {1}&{1}&{0}&{0}\end{array}\right)$  

计算：（1）$A\lor B$；（2）$𝐴∧𝐵$；（3）$𝐴⨀𝐵$。  

【解】根据两个布尔矩阵的布尔或、布尔与和布尔积的概念，容易得到：  
$$
A\vee B={\left(\begin{array}{l l l}{1}&{0}&{1}\\ {1}&{1}&{1}\\ {1}&{1}&{0}\\ {0}&{1}&{1}\end{array}\right)},\;\;(\,2\,)\;\;A\wedge B={\left(\begin{array}{l l l}{0}&{0}&{0}\\ {1}&{0}&{1}\\ {1}&{0}&{0}\\ {0}&{0}&{1}\end{array}\right)},\;\;(\,3\,)\;\;A\odot B={\left(\begin{array}{l l l}{1}&{1}&{0}&{1}\\ {1}&{1}&{1}&{1}\\ {0}&{0}&{0}&{1}\\ {1}&{1}&{0}&{0}\end{array}\right)}
$$
解毕！  

在学习了二元关系的三个基本表示方法后，下面我们考察空关系、完全关系和恒等关系这三个常用特殊关系的关系矩阵和关系图各有什么特点：  

(1) 空关系$\varnothing$  因为$\emptyset\subseteq A\times B$(或$\emptyset\subseteq A\times A)$)，所以$\varnothing$也是一个从$𝐴$到$B$(或$𝐴$上)的关系，称之为空关系，即无任何元素的关系。空关系的关系图中只有结点，无任何边，且关系矩阵中的元素全是0  

(2) 完全关系（全域关系） $A\times B$或(或$A\times A)$本身也是一个从$𝐴$到$B$(或$𝐴$上)的关系，称之为完全关系，即含有全部序偶的关系。完全关系的关系图中所有结点之间都有有向边互联，关系矩阵中的元素全是1。  

(3) 恒等关系 $I_{A}$  $I_{A}\subseteq A\times A$，则$I_{A}=\{\langle x,x\rangle|x\in A\}$为$A$上的恒等关系。完全关系的关系图中所有结点都有一个有向环，不同结点之间无任何有向边联结。  

![](images/9a95167e68610708edb7fef0f0474b8284d349dcc5f3b662d3280809d00fbf1e.jpg)  
图5-6 空关系、全关系与恒等关系  

设$A=\left\{1,\ 2,\ 3\right\}$，则$A$ 上的空关系∅、完全关系$A\times A$及恒等关系$I_{A}$的关系图如图5-6 所示，下面三个布尔矩阵分别是它们的关系矩阵：  

$M_{\emptyset}=\left(\begin{array}{ccc}0&0&0\\0&0&0\\0&0&0\end{array}\right)\quad M_{A\times A}=\left(\begin{array}{ccc}1&1&1\\1&1&1\\1&1&1\end{array}\right)\quad M_{I_A}=\left(\begin{array}{ccc}1&0&0\\0&1&0\\0&0&1\end{array}\right)$

## § 5.2 关系的基本运算  

本节在关系概念的基础上考察关系的基本运算。首先，关系作为一种特殊的集合，可以按集合的概念进行交、并、差、补等集合运算。此外，从关系图可以看出，从集合$𝐴$到集合$B$的关系是一种从此到彼的方向性联系，故此可将两个关系通过适当的方式进行合成或串接形成一个新的关系，由此得到关系的复合运算。由关系的集合运算与复合运算还可进一步衍生出关系的幂运算、逆运算，以及面向数据库操作的连接、投影等专用关系运算。  

### 5.2.1 关系的集合运算  

二元关系是以序偶为元素的集合，因此可以对它进行集合的运算，通过集合的交、并、差、补等运算而产生新的集合。这些新的集合显然也是由序偶组成的集合，因而也是关系。具体地说，如果$R、{S}$ 是$X$到$Y$的二元关系，那么$R\cup S$，$R\cap S$，$R-S$，$\bar{R}$也是$X$到$Y$的二元关系。具体定义如下：  

【定义5.13】设$R$、$S$都是从集合$A$ 到$B$ 的两个关系，则可按下列方式定义它们的交、并、差、补运算：  
$$
R\cup S=\{\langle x,y\rangle|(x R y)\lor(x S y)\};\quad R\cap S=\{\langle x,y\rangle|(x R y)\land(x S y)\}
$$

$$
R-S=\{\langle x,y\rangle|(x R y)\wedge(x S y)\};\quad\bar{R}=\{\langle x,y\rangle|(x S y)\}
$$
有关集合交、并、差、补运算的性质，对上述定义的关系集合运算显然也是成立的，这些性质就不再一一赘述了。这里就需要注意的是：对于任意一个从集合$A$ 到$B$ 的二元关系$R$，从集合的角度看$A\times B$是相对于$R$ 的全集，故有：  
$$
\bar{R}=A\times B-R;\;\;\bar{R}\cup R=A\times B;\;\;\bar{R}\cap R=\emptyset;\;\;\bar{R}=R;\;\;S\subseteq R\Leftrightarrow\bar{R}\subseteq\bar{S}
$$
不难看出，关系的交、并、差、补运算结果还可以通过关系矩阵的计算得到：  
$$
M_{H\cup S}=M_{H}\lor M_{S};\,\,\,M_{H\cap S}=M_{H}\land M_{S};\,\,\,M_{\bar{H}}=\bar{M}_{H};\,\,\,M_{H-S}=M_{H}\land\bar{M}_{S}
$$
【例题5.18】设$A=\{a,b,c,d\}$，$A$ 上关系$R$ 和$S$ 定义如下：  
$$
R=\{\langle a,b\rangle,\langle b,d\rangle,\langle c,c\rangle\};\,\ S=\{\langle a,c\rangle,\langle b,d\rangle,\langle d,b\rangle\}
$$
计算（1）$R\cup S$，（2）$R\cap S$，（3）$R–S$  

【解】（1）$R\cup S=\{\langle a,b\rangle,\langle a,c\rangle,\langle b,d\rangle,\langle c,c\rangle,\langle d,b\rangle\};$； $R\cap S=\{\langle x,y\rangle|(x R y)\land(x S y)\}=\{\langle d,b\rangle\};$ $R\!\!-\!\!S=\{\langle x,y\rangle|(x R y)\wedge(x S y)\}=\{\langle a,b\rangle,\langle c,c\rangle\}\,$  

【例题5.19】设$A=\{1,\!2,\!3,\!4\}$，$A$上的关系$H,\ S$定义为：

 $H=\left\{\langle x,y\rangle\big|(x{\cdot}y)\,/\,2\right\}$ 是整数}；$S=\left\{\langle x,y\rangle\big|(x-y)\,/\,3\right.$ 是整数}  

【解】（1）先写出关系：  
$$
\begin{array}{c}{{H=\{\langle1,1\rangle,\langle1,3\rangle,\langle2,2\rangle,\langle2,4\rangle,\langle3,1\rangle,\langle3,3\rangle,\langle4,2\rangle,\langle4,3\rangle,\langle2,4\rangle,\langle3,4\rangle,\langle2,2\rangle,\langle2,4\rangle,\langle3,3\rangle,\langle4,4\rangle\}}}\\ {{{\cal S}=\{\langle1,1\rangle,\langle1,4\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle4,1\rangle,\langle4,4\rangle\}}}\end{array}
$$
（2）再做集合运算，得到：  
$$
\begin{array}{r l}&{H\cup S=\{\langle1,1\rangle,\langle1,3\rangle,\langle1,4\rangle,\langle2,2\rangle,\langle2,4\rangle,\langle3,1\rangle,\langle3,3\rangle,\langle4,1\rangle,\langle4,2\rangle,\langle4,4\rangle\}}\\ &{\ H\cap S=\{\langle1,1\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle4,4\rangle\};}\\ &{\ \overline{{H}}=\{\langle1,2\rangle,\langle1,4\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,2\rangle,\langle3,4\rangle,\langle4,1\rangle,\langle4,3\rangle\};}\\ &{\ S-H=S\cap\overline{{H}}=\{\langle1,4\rangle,\langle4,1\rangle\}}\end{array}
$$
解毕！  

### 5.2.2 关系的复合运算  

日常生活和工作中很多关系问题仅用关系的集合运算不能得到有效的解决。例如：假设集合$𝐴$表示某家族的全部成员构成的集合，在$𝐴$上定义如下两个关系$R$和$𝑆$：  

$R$表示$A$上的兄弟关系，$\langle x,y\rangle\in R$,当且仅当$x$是$y$的兄弟;

 $S$表示 $A$ 上的父子关系，$\langle y,z\rangle\in S$,当且仅当$y$ 是$z$ 的父亲。

则可通过元素$y$的中间媒介或传递作用，在$x$与$z$之间产生一个新的关系，即叔侄关系。换句话说，叔侄关系是由兄弟关系和父子关系的合成。  

![](images/8ed5b0cc3c8222133404e26aeb757d647b1fb51cdae3d0c7fbf0c3754976758e.jpg)  
图5-7 叔侄关系图  

例如，假设在小说《红楼梦》中人物的兄弟关系为𝑅、父子关系为𝑆，则有：  
$$
\begin{aligned}&R=\left\{\langle\text{贾宝玉},\text{贾环}\rangle,\langle\text{贾政},\textbf{贾赦}\rangle,\cdots\right\};\\&S=\left\{\langle\text{贾政},\text{贾宝玉}\rangle,\langle\text{贾政},\text{贾环}\rangle,\langle\textbf{贾赦 贾琏}\rangle,\cdots\right\}\end{aligned}
$$
如图5-7 所示，在上述$R$和$𝑆$这两个二元关系中，贾政和贾琏之间通过贾赦的中间媒介或传递作用建立了叔侄关系。一般地，将关系这种合成机制进行抽象，用数学语言进行表达，就得到如下关系复合运算的定义：  

【定义5.14】假设$A$、$B$、$C$ 是三个非空集合，$R$ 是从$A$ 到$B$ 的关系，$S$ 是从$B$ 到$C$的关系，则$R$ 与$S$ 的复合关系$R\circ S$定义为如下从$A$ 到$C$的关系：  

$$R\circ S=\{\langle x,z\rangle|x\in A\land z\in C\land(\exists y)(y\in B\land x R y\land y S z)\quad\text{(5-5)}$$  

运算“ ∘”称为复合运算。  

从上述定义可知：不是任意两个关系都能进行复合运算，当且仅当$R$ 的后域是$S$的前域时，$R$ 和$S$ 才可复合；$R\circ S$的前域是$R$ 的前域$A$，$R\circ S$的后域是$S$ 的后域$C$。  

任何一个关系都有集合、关系图和矩阵这三种表现形式，复合运算在这三种不同表现形式下分别具有相应的具体计算方法，下面分别介绍这三种复合计算方法。  

令$A=\{a_1,a_2,\cdots,a_m\},B=\{b_1,b_2,\cdots,b_n\},C=\{c_1,c_2,\cdots,c_t\},R$ 是$A$ 到$B$ 的关系，$S$ 是$B$ 到 $C$ 的关系，即有$R$$\subseteq{A}\times{B}$, $S$$\subseteq{B}\times{C}$, 则$R\circ S$可按下列方法进行计算. 

1 ．集合法    由复合运算的定义可知，对于任意的 $a_{i}\in A,c_{j}\in C$ ，若 $\langle a_{i},c_{j}\rangle\in R\circ S$ ，则 必然存在某个$b_{k}\in B$，使得$\langle a_{i},b_{k}\rangle\in R$并且$\langle b_{k},c_{j}\rangle\in S$。故对于$R$中每个给定的序偶$\langle a_{i},b_{k}\rangle$，要在$S$中寻遍第一元素为$b_{k}$的序偶$\langle b_{k},c_{j}\rangle$，若存在$\langle b_{k},c_{j}\rangle\in S$，则取$R$中$\langle a_{i},b_{k}\rangle$的第一元素，以及$S$中对应序偶$\langle b_{k},c_{j}\rangle$的第二元素，形成一个新的序偶$\langle a_{i},c_{j}\rangle$，该序偶即为$R\circ S$中的一个元素。同理可找出$R\circ S$中的所有元素。  

2. 关系图法  由复合运算的定义可知，对于分别属于关系$R$ 和$S$的两个序偶，它们之间能够复合的关键在于能够在这两个序偶之间找到一个桥梁$b_{k}$，使得$b_{k}$既是前一个序偶($R$中序偶)的第二元素，同时又是后一个序偶(S 中序偶)的第一元素。因此，在画复合关系的关系图时，首先应该在$R$ 和$S$ 这两个关系的关系图中搭起这个桥梁，然后拆掉中间的桥梁，直接联结经过该桥梁的两个结点，便可得到$R\circ S$的关系图。  

3.关系矩阵法  将$R$ 和$S$ 的关系矩阵做布尔积运算$\odot$，即可得到$\mathrm{~\tt~R~o~}S$的关系矩阵，然后根据该矩阵写出$R\circ S$中元素即可。也就是说，令$R$ 和$S$ 的关系矩阵分别为：  
$$
M_{R}=\begin{pmatrix}\langle a_1,b_1\rangle&\langle a_1,b_2\rangle&\cdots\langle a_1,b_n\rangle\\\langle a_2,b_1\rangle&\langle a_2,b_2\rangle&\cdots\langle a_2,b_n\rangle\\\vdots\\\langle a_m,b_1\rangle\langle a_m,b_2\rangle&\cdots\langle a_m,b_n\rangle\end{pmatrix};\quad M_{S}=\begin{pmatrix}\langle b_1,c_1\rangle&\langle b_1,c_2\rangle&\cdots&\langle b_1,c_t\rangle\\\langle b_2,c_1\rangle&\langle b_2,c_2\rangle&\cdots&\langle b_2,c_t\rangle\\\vdots\\\langle b_n,b_1\rangle\langle b_n,c_2\rangle&\cdots\langle b_n,c_t\rangle\end{pmatrix}
$$
则有：  
$$
M_{R\circ S}=M_{R}\odot M_{S}=\left(\begin{array}{c}{{\langle a_{1},c_{1}\rangle\ \langle a_{1},c_{2}\rangle\ \cdots\ \langle a_{1},c_{t}\rangle}}\\ {{\langle a_{2}.\,c_{1}\rangle\ \langle a_{2},c_{2}\rangle\ \cdots\ \langle a_{2},c_{t}\rangle}}\\ {{\vdots}}\\ {{\langle a_{m},c_{1}\rangle\langle a_{m},c_{2}\rangle\cdots\langle a_{m},c_{t}\rangle}}\end{array}\right)
$$
【例题5.20】令$A=\{1,\!2,\!3\}$, $B=\{1,\!2,\!3,\!4\}$, $C=\{1,\!2,\!3,\!4,\!5\}$，$R$ 和$S$ 分别是$A$ 到$B$ 和$B$到$C$的关系： $\begin{array}{r}{R=\ \{\langle1,2\rangle,\langle2,3\rangle,\langle2,4\rangle,\langle3,1\rangle\};\,\ S=\{\langle1,2\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,4\rangle,\langle4,2\rangle,\langle4,5\rangle\}.}\end{array}$ 用集合法、关系矩阵法和关系图法计算$R\circ S$。  

【解】首先使用集合法计算$R\circ S$，得到：  
$$
R\circ S=\{\langle1,1\rangle,\langle1,3\rangle,\langle2,2\rangle,\langle2,4\rangle,\langle2,5\rangle,\langle3,2\rangle\}
$$
再使用关系图法。由题意，关系$R$ 和$S$的关系矩阵分别为：  
$$
M_{R}=\left(\!\!\begin{array}{c c c}{{0}}&{{1}}&{{0}}&{{0}}\\ {{0}}&{{0}}&{{1}}&{{1}}\\ {{1}}&{{0}}&{{0}}&{{0}}\end{array}\!\!\right)\;\;\;\;\;M_{S}=\left(\!\!\begin{array}{c c c}{{0}}&{{1}}&{{0}}&{{0}}\\ {{1}}&{{0}}&{{1}}&{{0}}\\ {{0}}&{{0}}&{{0}}&{{1}}\\ {{0}}&{{1}}&{{0}}&{{0}}\end{array}\!\!\right)
$$
则有：  
$$
M_{R\odot S}=M_{R}\odot M_{S}=\left(\!\!\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{1}\\ {1}&{0}&{0}&{0}\end{array}\!\!\right)\odot\left(\!\!\begin{array}{l l l l}{0}&{1}&{0}&{0}&{0}\\ {1}&{0}&{1}&{0}&{0}\\ {0}&{0}&{0}&{1}&{0}\\ {0}&{1}&{0}&{0}&{1}\end{array}\!\!\right)=\left(\!\!\begin{array}{l l l l}{1}&{0}&{1}&{0}&{0}\\ {0}&{1}&{0}&{1}&{1}\\ {0}&{1}&{0}&{0}&{0}\end{array}\!\!\right)
$$
因此，根据复合关系$R\circ S$的关系矩阵$M_{R\circ S}$，得到$R\circ S$的集合表示为：  
$$
R\circ S=\{\langle1,1\rangle,\langle1,3\rangle,\langle2,2\rangle,\langle2,4\rangle,\langle2,5\rangle,\langle3,2\rangle\}
$$
最后使用关系图法，具体过程和结果如图5-8 所示。□  

![](images/b997f2698e7abcd4dd51351bbd180f9d3c9785d56d7413a26fd01f2c048dcd54.jpg)  
图$5{\mathrm{-}}8\ \ R\circ S$复合关系图  

【例题5.21】设$\begin{array}{r}{A=\{1,\!2,\!3,\!4\},\ R=\{\langle1,\!2\rangle,\langle2,\!2\rangle,\langle3,\!4\rangle\},\ S=\{\langle2,\!4\rangle,\langle3,\!1\rangle,\langle4,\!2\rangle\},}\end{array}$ $T=\{\langle1,4\rangle,\langle2,1\rangle,\langle4,2\rangle\}$是$A$ 上的三个关系，试计算：  

$(1)R\circ S和S\circ R;   (2)(R\circ S)\circ T和R\circ(S\circ T)$

【解】
$$
（1）\begin{array}{r}{R\circ S=\{\langle1,2\rangle,\langle2,2\rangle,\langle3,4\rangle\}\circ\{\langle2,4\rangle,\langle3,1\rangle,\langle4,2\rangle\}=\{\langle1,4\rangle,\langle2,4\rangle,\langle3,2\rangle\};}\end{array}
$$

$$
S\circ R=\{\langle2,4\rangle,\langle4,2\rangle\}\circ\{\langle1,2\rangle,\langle2,2\rangle,\langle3,4\rangle\}=\{\langle3,2\rangle,\langle4,2\rangle\}\circ
$$

$$
(2)(R\circ S)\circ T=\{\langle1,4\rangle,\langle2,4\rangle,\langle3,2\rangle\}\circ\{\langle1,4\rangle,\langle2,1\rangle,\langle4,2\rangle\}=\{\langle1,2\rangle,\langle2,2\rangle,\langle3,1\rangle\}
$$

$$
S\circ T=\{\langle2,2\rangle,\langle3,4\rangle,\langle4,1\rangle\}。
$$
故有：$R\circ(S\circ T)=\{\langle1,2\rangle,\langle2,2\rangle,\langle3,1\rangle\}=(R\circ S)\circ T\,。$

从上述例题可以看出，关系的复合运算不满足交换律，但满足结合律，即有：  

【定理5.5】设$A$、$B$、$C$ 和$D$ 是任意四个集合，$R$、$S$和$T$ 分别是从$A$ 到$B,\ B$到$C$和$C$ 到$D$ 的二元关系，$I_{A}$和$I_{B}$分别是$A$ 和$B$ 上恒等关系，则有：  
$$
(1) (R\circ S)\circ T=R\circ(S\circ T);\quad(2) I_A\circ R=R\circ I_B=R
$$
【分析】关系是集合，复合关系也是集合，因此就是要证明两个集合相等。

【证明】（1）对于任意$\langle a,d\rangle\in(R\circ S)\circ T$，存在$c\in C$，使得：  
$$
\langle a,c\rangle\in R\circ S,\ \ \langle c,d\rangle\in T
$$
对于$\langle a,c\rangle\in R\circ S$，同样至少存在一个$b\in B$，使得：$\langle a,b\rangle\in R$，$\langle b,c\rangle\in S$。故由$\langle b,c\rangle\in$𝑆，$\langle c,d\rangle\in T$可得：$\langle b,d\rangle\in S\circ T$。又由$\langle a,b\rangle\in R$和$\langle b,d\rangle\in S\circ T$知，有：  
$$
\langle a,d\rangle\in R\circ(S\circ T)
$$
故有  
$$
(R\circ S)\circ T\subseteq R\circ(S\circ T)
$$
同理可证：$R\circ(S\circ T)\subseteq(R\circ S)\circ T$。由集合性质知：$\left(R\circ S\right)\circ T=R\circ\left(S\circ T\right)\circ T$。  

（2）任取$\langle a,b\rangle\in I_{A}\circ R$，则存在$a\in A$，使得$\langle a,a\rangle\in R$，从而有：$I_{A}\circ R\subseteq R$。反之，任取$\langle a,b\rangle\in R$，由$\langle a,a\rangle\in{I}_{A}$知，有：$\langle a,b\rangle\in I_{A}\circ R$.从而有：$R\subseteq I_{A}\circ R$。  

故有： $I_{A}\circ R=R$ 。同理可证： $R\circ I_{B}=R$ ，于是 $I_{A}\circ R=R\circ I_{B}=R$ 得证。  

上述定理的第（1）条表明，关系的复合运算满足结合律.此外，该定理的第（2）条表明，对于集合上的任何关系，恒等关系对关系的复合运算是没有贡献的。这里的恒等关系所起的作用，就相当于数的普通乘法中整数1 的作用一样，是复合运算的单位元。关于运算单位元的有关概念和性质，将在代数结构的相关内容中做专门介绍和讨论。  

下面的定理给出了关系的集合运算与复合运算之间的关系：复合运算对并运算具有完全的分配律，而复合运算对交运算只有有半分配律。  

【定理5.6】设$A$、$B$、$C$和$D$ 是任意四个集合，$R$ 是$A$ 到$B$ 的关系，$S_{1},\ S_{2}$是从$B$ 到$C$的关系，$T$是从$C$ 到$D$ 的关系，则有：  

（1）$R\circ(S_{1}\cup S_{2})=(R\circ S_{1})\cup(R\circ S_{2});\,\,\,(2)\,\,\,R\circ(S_{1}\cap S_{2})\subseteq(R\circ S_{1})\cap(R\circ S_{2});$ （3）$(S_{1}\cup S_{2})\circ T=(S_{1}\circ T)\cup(S_{2}\circ T);\ \ (4)\ \ (S_{1}\cap S_{2})\circ T\subseteq(S_{1}\circ T)\cap(S_{2}\circ T)。$  

【证明】仅对（4）给出证明，其余证明由读者自己完成。

 对任意$\langle b,d\rangle\in(S_{1}\cap S_{2})\circ T$，存在$c\in C$，满足$\langle b,c\rangle\in(S_{1}\cap S_{2})\circ T$；$\langle c,d\rangle\in T$。 即：

  $\langle b,c\rangle \in S_{1}且\langle b,c\rangle \in S_{2}$

故由$\langle b,c\rangle\in S_{1}$且$\langle c,d\rangle\in T$，有$\langle b,d\rangle\in(S_{1}\circ T)$，又由$\langle b,c\rangle\in S_{2}$且$\langle c,d\rangle\in T$，有：  
$$
\langle b\,,\,\,\,d\rangle\in(S_{2}\circ T)
$$
故有 $\langle b\,,\,\,\,d\rangle\in(S_{1}\circ T)\cap(S_{2}\circ T)$ 。

【例题5.22】试说明下面的包含关系不一定成立

$（1）(R\circ S_{1})\cap(R\circ S_{2})\subseteq R\circ(S_{1}\cap S_{2});\;\;(2)\;\;(S_{1}\circ T)\cap(S_{2}\circ T)\subseteq(S_{1}\cap S_{2})\circ T\circ S$ 【分析】如要说明某一事实不一定成立，则可举一反例加以说明。  

【解】（1）设$A=\{a\},\quad B=\{b_{1},b_{2}\},\,\,\,C=\{c\}$，关系 $R,S_{1},S_{2}$定义如下：$R=\{\langle c,b_{1}\rangle,\langle c,b_{2}\rangle\},\quad S_{1}=\{\langle b_{1},a\rangle\},\quad S_{2}=\{\langle b_{2},a\rangle\}$  

由$S_{1}\cap S_{2}=\emptyset$，知$R\circ(S_{1}\circ S_{2})=R\circ\emptyset=\emptyset$，但：  
$$
(R\circ S_{1})=\{\langle c,a\rangle\},\quad(R\circ S_{2})=\{\langle c,a\rangle\}
$$
故有：$\left(R\circ S_{1}\right)\cap\left(R\circ S_{2}\right)=\left\{\langle c,\ \ a\rangle\right\}$，即：$\begin{array}{r}{(R\circ S_{1})\cap(R\circ S_{2})\not\subseteq~~R\circ(S_{1}\cap S_{2})\,.}\end{array}$  

（2）设$A=\{a\},\quad B=\{b_{1},b_{2}\},\,\,\,C=\{c\}$，关系$R,S_{1},S_{2}$定义如下： $S_{1}=\left\{\left\langle a,b_{1}\right\rangle\right\},\ \ \ S_{2}=\left\{\left\langle a,b_{2}\right\rangle\right\},\ \ T=\left\{\left\langle b_{1},c\right\rangle,\ \left\langle b_{2},c\right\rangle\right\}$  

由$S_{1}\cap S_{2}=\emptyset$知：$(S_{1}\cap S_{2})\circ T=\emptyset\circ T=\emptyset$；由$S_{1}\circ T=\{\langle a,c\rangle\},S_{2}\circ T=\{\langle a,c\rangle\},$知：$(S_{1}\circ T)\cap(S_{2}\circ T)=\{\langle a,c\rangle\}$，即有$(S_{1}\circ T)\cap(S_{2}\circ T)\not\subset(S_{1}\cap S_{2})\circ T$。  

上述定理和例题表明，复合运算对并运算具有完全的分配律，即分配律是以集合相等的方式出现，但复合运算对交运算不具备完全分配律，只有半分配律，也就是说，分配律是以集合包含的方式出现。如果要将关系的这些运算与数的相关运算做一些类比的话，那么关系的复合运算就比较类似于数或矩阵的乘法运算，而关系的并运算就比较类似于数或矩阵的加法运算。事实上，从复合运算和并运算的关系矩阵运算特点上，就可看出它们与数乘、数加以及矩阵乘、矩阵加的类似之处。  

### 5.2.3 幂关系与逆关系  

如前所述，关系的复合运算满足结合律。也就是说，如果有多个关系进行复合运算，只要不交换它们的运算次序，不管哪个先参与合成，最后结果都一样。由此可见，对于某个集合上的一个二元关系，如果它可以不断地与自己做复合运算，那么运算结果只与该关系以及复合运算次数有关，而与复合的次序无光。由此可得如下关系方幂运算的概念：  

【定义5.15】设$R$ 是集合$A$ 上的关系，则可归纳定义$R$ 的$n$次方幂${R^{n}}$运算如下：  

$（1）R^{0}=I_{A}=\left\{\langle a,\ a\rangle\big|a\in A\right\};\quad(\,2\,)\,\ R^{1}=R;\ (\,3\,)\,\ R^{n+1}=R^{n}\circ R=R\circ R^{n}\circ R.$    方幂运算的结果也显然也是$A$ 上的二元关系，即对于任何自然数$k$，有$R^{k}\subseteq A\times A$。通常称为$R$的方幂关系或幂关系，不难证明方幂运算满足如下运算法则：  
$$
R^{m}\circ R^{n}=R^{m+n};\,\,\,(R^{m})^{n}=R^{m n}
$$
【例题5.23】设$A=\{1,\!2,\!3,\!4,\!5,\!6\}$，$A$上的关系： $R=\{\langle1,2\rangle,\langle2,1\rangle,\langle4,5\rangle,\langle5,6\rangle,\langle6,4\rangle\};\,\,\,S=\{\langle1,2\rangle,\langle2,3\rangle,\langle3,4\rangle,\langle4,5\rangle,\langle5,6\rangle\}$ 计算： $R^{n}$和$S^{n}$。  

$\begin{aligned}&\text{【解】}R^{1}=R;\quad R^{2}=R\circ R=\{(1,1),(2,2),(4,6),(5,4),(6,5)\};\\&R^{3}=\quad R\circ R\circ R=R^{2}\circ R=\{(1,2),(2,1),(4,4),(5,5),(6,6)\};\\&R^{4}=\quad R^{3}\circ R=\{(1,1),(2,2),(4,5),(5,6),(6,4)\};\\&R^{5}=\quad R^{4}\circ R=\{(1,2),(2,1),(4,6),(5,4)),(6,5)\};\\&R^{6}=\quad R^{5}\circ R=\{(1,1),(2,2),(4,4),(5,5),(6,6)\};\\&R^{7}=R^{6}\circ R=R;\quad\cdots\\&\text{故有:}R^{1}=R^{r}(n=6k+r,\quad r=0,1,2,3,4,5)\\&S^{1}=S;\quad S^{2}=S\circ S=\{(1,3),(2,4),(3,5),(4,6)\};\\&S^{3}=\quad S\circ S\circ S=S^{2}\circ S=\{(1,4),(2,5),(3,6)\};\\&S^{4}=\quad S^{3}\circ S=\{(1,5),(2,6)\};\\&S^{5}=S^{4}\circ S=\{(1,6)\};\quad S^{6}=\quad S^{5}\circ S=\emptyset;\quad S^{7}=\emptyset;\quad\cdots\\&\text{故有:}S^{n}=\emptyset (n>5) \text{。}\end{aligned}$
由上述例题可以看出：   

（1）幂集$R^{n}$的基数$\vert{R}^{n}\vert$并非随着$n$ 的增加而增加，而是呈递减趋势；

（2）当$n\geq|A|$时，则$R^{n}$出现循环取值或退化为空关系。 下面的定理给出了上述结论的一个解释：  

【定理5.7】设𝐴是一个具有${n}$个元素的有限集合，$R$ 是$𝐴$上的二元关系，则必存在自然数$s$ 和$t$，使得$R^{s}=R^{t}$，$0\leq s<t\leq2^{n^{2}}$。  

【证明】由于$R$ 是$𝐴$上的二元关系，故对于任何自然数$k$，由复合关系的定义知$R$ 的$k$次幂$R^{k}$仍是$𝐴$上的二元关系，即$R^{k}\subseteq A\times A$。 另一方面，根据二元关系的定义，$𝐴$上的任意二元关系都是是$A\times A$的一个子集合，由于$|A\times A|=n^{2}$，故𝐴上的二元关系有且仅有$2^{n^{2}}$种。列出$R$ 的各次幂$R^{0}$，$R^{1}$，$R^{2}$，⋯，${R^{2}}^{n^{2}}$，共有$2^{n^{2}}+1$。因此，根据鸽巢原理，必存在自然数$s$ 和$t$，使得$R^{s}=R^{t}$，$0\leq s<t\leq2^{n^{2}}$。  

上述定理表明，对于任意一个有限集合，该集合上的二元关系总共只有有限多个，而对于该集合上的二元关系，其方幂运算则可以无限地进行下去且运算结果均为该集合上的二元关系。因此，在一定次数的方幂运算之后，后续的方幂运算结果自然是以某种循环的方式出现，或者以恒等于某个特定关系的方式出现。  

【例题5.24】假设$A=\{a,b,c,d\}$，$R=\{\langle a,b\rangle,\langle b,a\rangle,\langle b,c\rangle,\langle c,d\rangle\}$，求试分别用关系矩阵和关系图求$R$的各次方幂。  

【解】$R$ 的关系矩阵为：  
$$
M=\begin{pmatrix}0&1&0&0\\1&0&1&0\\0&0&0&1\\0&0&0&0\end{pmatrix}
$$
则$R^{2}$的关系矩阵为：  
$$
M^{2}={\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {1}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{0}&{0}\end{array}\right)}\odot{\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {1}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{0}&{0}\end{array}\right)}={\left(\begin{array}{l l l l}{1}&{0}&{1}&{0}\\ {0}&{1}&{0}&{1}\\ {0}&{0}&{0}&{0}\\ {0}&{0}&{0}&{0}\end{array}\right)}
$$
同理可得$\cdot R^{3}$和$R^{4}$的关系矩阵为：  
$$
M^{3}={\left(\begin{array}{l l l l}{0}&{1}&{0}&{1}\\ {1}&{0}&{1}&{0}\\ {0}&{0}&{0}&{0}\\ {0}&{0}&{0}&{0}\end{array}\right)},\;\;M^{4}={\left(\begin{array}{l l l l}{1}&{0}&{1}&{0}\\ {0}&{1}&{0}&{1}\\ {0}&{0}&{0}&{0}\\ {0}&{0}&{0}&{0}\end{array}\right)}
$$
可以看出：$M^{4}=M^{2}$，故有：$R^{4}=R^{2}$。由此可得：  
$$
R^{2}=R^{4}=R^{6}=\cdots,\,\,\,R^{3}=R^{5}=R^{7}=\cdots
$$
而$R^{0}$，即$I_{A}$的关系矩阵是：  
$$
M^0=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
$$
用关系图的方法得到$R^{0}$$R^{1},\ \ R^{2},\ \ .$$R^{3}$，⋯的关系图如图5-9 所示。

![](images/ac90746583588b1f67a1d4416b337286eeda8ec1b9949bba5d9f84bdbac748b9.jpg)  
图5-9 关系幂运算的关系图法  

我们知道，二元关系是以序偶$\langle x,y\rangle$为元素的集合，而序偶中第一元素${x}$和第二元素$𝑦$之间是一种有序的绑定。若将序偶$\langle x,y\rangle$中第一元素$x$和第二元素$y$互换位置，则可由此得到一个新的序偶$\langle y,x\rangle$，当$x\neq y$时，显然有$\langle x,y\rangle\neq\langle y,x\rangle$。  

根据以上分析，得到如下关系逆运算的相关概念：

【定义5.16】设$A,\ B$ 是任意两个集合，$R$ 是$A$ 到$B$ 的关系，则从$B$ 到$A$ 的关系：  
$$
R^{-1}=\{\langle b,a\rangle|\langle a,b\rangle\in R\}\quad\text{(5-9)}
$$
称为$R$ 的逆关系，运算“-1”称为关系的逆运算。  

关于逆关系概念的理解，需要注意如下几个要点：（1）关系是序偶的集合，逆关系也是序偶的集合；（2）如果$R$ 是一个关系，则其逆关系$R^{-1}$和补关系$\bar{R}$都是关系，但是两者是完全不同的两个关系，千万不要混淆；（3）显然有$(R^{-1})^{-1}=R$，$\varnothing^{-1}=\varnothing$。  

【例题5.25】设$A=\{1,\!2,\!3,\!4\}$，$B=\{a,b,c,d\}$，$C=\{2,\!3,\!4,\!5\}$， $R$ 是$A$ 到$B$上的一个关系，$S$是$B$ 到$C$ 的一个关系，即有：  
$$
R=\{\langle1,a\rangle,\langle2,c\rangle,\langle3,b\rangle,\langle4,b\rangle,\langle4,d\rangle\};\,\ S=\{\langle a,2\rangle,\langle b,4\rangle,\langle c,3\rangle,\langle c,5\rangle,\langle d,5\rangle\}
$$
（1）计算$R^{-1}$$，画出$R$ 和$$R^{-1}$的关系图与关系矩阵；（2）计算$(R\circ S)^{-1}$和$S^{-1}\circ R^{-1}$

【解】（1）根据逆关系的定义，有：$R^{-1}=\{\langle a,1\rangle,\langle c,2\rangle,\langle b,3\rangle,\langle b,4\rangle,\langle d,4\rangle\}$。$R$ 和$R^{-1}$  

的关系如图5-10 所示：  

![](images/c1cf4e4c4d9aece094022fd4590239d85c341dfcf196aa967479589e325e8fe6.jpg)  
图$5–10\:R$ 和$R^{-1}$的关系图  

$R$ 和$R^{-1}$的关系矩阵为：  
$$
M_{R}={\left(\begin{array}{l l l}{1}&{0}&{0}&{0}\\ {0}&{0}&{1}&{0}\\ {0}&{1}&{0}&{0}\\ {0}&{1}&{0}&{1}\end{array}\right)},\qquad M_{R^{-1}}={\left(\begin{array}{l l l}{1}&{0}&{0}&{0}\\ {0}&{0}&{1}&{1}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{0}&{1}\end{array}\right)}
$$
（2）易知$|R\circ S=\{\langle1,2\rangle,\langle2,3\rangle,\langle2,5\rangle,\langle3,4\rangle,\langle4,4\rangle,\langle4,5\rangle\}$，故有：  
$$
(R\circ S)^{-1}=\{\langle2,1\rangle,\langle3,2\rangle,\langle5,2\rangle,\langle4,3\rangle,\langle4,4\rangle,\langle5,4\rangle\}
$$
又因为：  
$$
R^{-1}=\{\langle a,1\rangle,\langle c,2\rangle,\langle b,3\rangle,\langle b,4\rangle,\langle d,4\rangle\};\;\;S^{-1}=\{\langle2,a\rangle,\langle4,b\rangle,\langle3,c\rangle,\langle5,c\rangle,\langle5,d\rangle\}
$$

$$
S^{-1}\circ R^{-1}=\{\langle2,1\rangle,\langle3,2\rangle,\langle5,2\rangle,\langle4,3\rangle,\langle4,4\rangle,\langle5,4\rangle\}\circ
$$
根据上述例题，可以看出具有如下结论：（1）将$R$ 的关系图中有向边方向取反方向即得$R^{-1}$的关系图，反之亦然；(2）将$R$ 的关系矩阵转置即得${ R}^{-1}$的关系矩阵，即$R和R^{-1}$的关系矩阵为互为转置矩阵；（3）$R^{-1}$的前域与后域正好是$R$ 的后域和前域，即$\mathrm{dom}R{=}\mathrm{ran}R^{-1}$，$\mathrm{dom}R^{-1}{=}\mathrm{ran}R$；（4）$|R|=|R^{-1}|;\ \ (5)\ \,(R\circ S)^{-1}=S^{-1}\circ R^{-1}$。  

上述结论不难证明和理解，下面仅以给出结论（5）的证明。  

【定理5.8】设$A$，$B$ 和$C$是任意三个集合，$R$，$S$ 分别是从$A$ 到$B$ 和$B$ 到$C$的二元关系，则有：$(R\circ S)^{-1}=S^{-1}\circ R^{-1}$  

【证明】任取$\langle c,a\rangle\in(R\circ S)^{-1}$，则有$\langle a,c\rangle\in R\circ S$，即有$b\in B$，得到：  
$$
\langle a,b\rangle\in R;\qquad\langle b,c\rangle\in S_{\circ}
$$
从而有$\langle b,a\rangle\in R^{-1},\langle c,b\rangle\in S^{-1}$，亦即$\langle c,a\rangle\in S^{-1}\circ R^{-1}$，故有：  
$$
(R\circ S)^{-1}\subseteq S^{-1}\circ R^{-1}
$$
反之，任取$\langle c,a\rangle\in S^{-1}\circ R^{-1}$，则存在$b\in B$，使得：$\langle c,b\rangle\in S^{-1}$，$\langle b,a\rangle\in R^{-1}$.故有：  
$$
\langle a,b\rangle\in R,\;\;\langle b,c\rangle\in S.
$$
从而有$\langle a,\ \,c\rangle\in R\circ S$，即$\langle c,\ a\rangle\in(R\circ S)^{-1}$，亦即$S^{-1}\circ R^{-1}\subseteq(R\circ S)^{-1}$  

故有： $(R\circ S)^{-1}=S^{-1}\circ R^{-1}$ 。  

可以看出，复合关系的逆关系等于它们逆关系的反复合。要注意$(R\circ S)^{-1}\neq R^{-1}\circ S^{-1}$，因为$R^{-1}$是从$B$ 到$A$ 的关系，而$S^{-1}$是从$C$ 到$B$ 的关系，因此$S^{-1}$与$R^{-1}$之间是可复合的，而$R^{-1}$与$S^{-1}$之间是不可复合的。  

下面定理给出了关系逆运算与关系集合运算之间的分配运算律：

【定理5.9】设$R,\ S$是从集合$A$ 到集合$B$ 的关系，则有如下分配律：  
$$
(R\cup S)^{-1}=R^{-1}\cup S^{-1};\;\;(R\cup S)^{-1}=R^{-1}\cup S^{-1};\;\;(R-S)^{-1}=R^{-1}-S^{-1}
$$
【证明】下面仅证明 $(R\cup S)^{-1}=R^{-1}\cup S^{-1}$，其余证明类似，读者可自己写出。  

设对任意一个序偶$\langle x,y\rangle$，若$\langle x,y\rangle\in\mathsf(R\cup S)^{-1}$，则$\langle y,x\rangle\in R\cup S$。即$\langle y,x\rangle\in R$或者$\langle y,x\rangle\in{S}$。根据逆关系的定义，有$\langle x,y\rangle\in R^{-1}$或$\langle x,y\rangle\in S^{-1}$，即$\langle x,y\rangle\in R^{-1}\cup S^{-1}$。故有：  
$$
(R\cup S)^{-1}\subseteq R^{-1}\cup S^{-1}
$$
同理可证：$R^{-1}\cup S^{-1}\subseteq\ \ (R\cup S)^{-1}$。故有： $(R\cup S)^{-1}=R^{-1}\cup S^{-1}$。  

对于任意给定的集合𝐴和$B$，目前所讨论的二元关系有两种基本类型，一种是集合$𝐴$到集合$ B$上的二元关系，另外一种是集合𝐴上的二元关系。事实上，这两种关系没有本质上的区别，因为若令$C=A\cup B$，则集合$𝐴$到集合$B$上的二元关系就可以看成是$C\times C$的几个子集合，或者说是$C$上的二元关系。因此，在后续内容中所说的关系，若非特别说明，均为某个集合上的关系而不是从某个集合到另外一个集合上的关系。  

## § 5.3 关系的基本性质  

现实世界中的关系错综复杂、种类繁多，这给我们使用关系的数学模型表示和解决关系问题带来一定的困难。因此，为了比较方便地研究和使用关系的数学模型，本节建立考察关系特性的若干标准并将这些标准看成是关系的基本性质。对于任意给定的一个关系，就可以使用这些标准来考察或评判该关系满足或不满足这几个标准中的哪几条，换句话说，就是考察该或评判该关系具有哪些基本性质。这样就可以依据这些标准将所有的关系划分为若干类型进行分门别类的研究。关系的这些考察标准或基本性质一共有五个，即自反性、反自反性、对称性、反对称性和传递性，本节具体介绍这些基本性质的概念及判定方法。  

### 5.3.1 关系的自反与反自反  

日常生活和工作中的很多关系，如同学关系、实数的相等关系、正整数的整除关系等，每个元素都与其自身之间具有这种关系，此时称这些关系具有自反性质。具体定义如下：  

【定义5.17】设$R$ 是集合$A$ 上的关系，若对$\forall x\in A$，都有$\langle x,x\rangle\in R$，则称$R$ 在$A$ 上是自反关系，或称$R$ 具有自反性。即：

$(\forall x)(x\in A\to\langle x,x\rangle\in R)\Leftrightarrow R\text{为自反关系}\quad\text{(5-10)} $

与之相反的是，对于有些关系，例如父子关系、实数的小于关系、夫妻关系等，每个元素都不可能与其自身之间具有这种关系，此时称这些关系具有反自反性质。具体定义如下：  

【定义5.18】设$R$ 是集合$A$ 上的关系，若对$\forall x\in A$，都有$\langle x,x\rangle\notin R$，则称$R$ 在$A$ 上是反自反关系，或称$R$ 具有反自反性。即：  

【例题5.26】设$A=\{a,b,c\},\;\;R_{1},\;\;R_{2},\;\;R_{3},$，$R_{4}$是$A$ 上的关系，其中：  

$R_{1}=\{\langle a,a\rangle,\langle a,b\rangle,\langle b,b\rangle,\langle c,c\rangle;\;\;R_{2}=\{\langle a,a\rangle,\langle b,b\rangle\};\;\;R_{3}=\{\langle a,b\rangle,\;\;\langle b,c\rangle,\;\;\langle c,a\rangle\}$ 判断$R_{1}$，$R_{2}$，$R_{3}$是否具有自反性或反自反性。  

【解】由关系的对称和反对称的定义知，$R_{1}$只具有自反性，$R_{2}$既不具有自反性也不具有反自反性，$R_{3}$具有反自反性。  

【例题5.27】$集合A=\{1,\!2,\!3\}，\begin{array}{r}{R_{1}=\{\langle1,1\rangle,\langle1,2\rangle,\langle2,2\rangle,\langle3,3\rangle\},\quad R_{2}=\{\langle1,2\rangle,\langle2,3\rangle,\langle3,1\rangle\},}\end{array}$分析$R_{1}$和$R_{2}$自反性或反自反性，并分析它们关系矩阵和关系图的特征。  

【解】根据关系自反性和反自反性的定义，容易判定$R_{1}$具有自反性，$R_{2}$具有反自反性。令$R_{1}$和${\boldsymbol{R}}_{2}$的关系矩阵分别为${{M}_{R_{1}}}$和$M_{R_{2}}$，则有：  
$$
M_{R_{1}}={\left(\begin{array}{l l l}{1}&{1}&{0}\\ {0}&{1}&{0}\\ {0}&{0}&{1}\end{array}\right)};\;\;M_{R_{2}}={\left(\begin{array}{l l l}{0}&{1}&{0}\\ {0}&{0}&{1}\\ {1}&{0}&{0}\end{array}\right)}
$$
显然，${{M}_{{{R}_{1}}}}$的主对角线元素全为1，$M_{R_{2}}$的主的主对角线元素全为0。  

![](images/4b4cf171cc908f5ab0140ad1b6a46d6d2e20a0416c52e771e8afbd26ae3a7842.jpg)  
图5-11 例题5.27 中$R_{1}$  

![](images/01ecda8f6aab8bb20846dd13e7bcdfd06f5f97dde87288cc14ac21d63c9549a2.jpg)  
5.27 中$R_{2}$的关系图  

图5-11 和图5-12 分别是$R_{1}$和$R_{2}$的关系图。显然，在$R_{1}$的关系图中每个结点都有一个自环，而$R_{2}$的关系图中每个结点都没有自环。  

通过上述例题，不难得出如下结论：  

（1）如果关系$R$ 是自反的，那么该关系一定不是反自反的；关系$R$ 是反自反的，则该关系一定不是自反的。 

（2）存在既不是自反也不是反自反的关系；  

（3）关系$R$ 是自反的，当且仅当系图中每个结点都有一个自环；关系$R$ 是反自反的，当且仅当图中每个结点都没有自环； 

（4）关系$R$ 是自反的，当且仅当其关系矩阵的主对角线上全为1；关系$R$ 是反自反的，当且仅当其关系矩阵的主对角线上全为0。  

【例题5.28】设集合$|A|=n$，试分别计算$A$ 上具有自反性和反自反性的关系个数。  

【分析】自反性关系至少包含所有$\langle x,x\rangle$，$x{\in}A$。因此，求解$A$ 上所有具有自反性关系的个数等价于求解$A\times A-I_{A}$中所有不同子集的个数。根据反自反性定义，$A$上所有反自反性关系为集合$B=A\times A-I_{A}$的所有子集。因此，$A$上自反性和反自反性关系的个数相等。  

【解】$A$上具有自反性关系的个数为：  
$$
C(0,n(n-1))+C(1,n(n-1))+\cdots+C(n(n-1,n(n-1))=2^{n(n-1)}
$$
设$B=A\times A-I_{A}$，则$|B|=n(n-1)$，故$B$上所有子集个数为$2^{n(n-1)}$，即$A$上具有反自反性关系的个数一共为$2^{n(n-1)}$。  

### 5.3.2 关系的对称与反对称  

有很多关系具有一些对称的性质，例如对于同学关系，如果张三是李四的同学，那么李四必然是张三的同学，还有很多其它关系，例如两条直线之间的平行关系、兄弟关系、实数的相等关系等等，也都具有这种对称性质。关系对称性的具体定义如下：  

【定义5.19】设$R$ 是集合$A$ 上的关系，对任意$x,y\in A$，若$\langle x,y\rangle\in R$，则有$\langle y,x\rangle\in R$，则称关系$R$ 是对称关系，或称关系$R$ 具有对称性。即有：  

$(\forall x)(\forall y)(x\in A\land y\in A\land\langle x,y\rangle\in R\rightarrow\langle y,x\rangle\in R)\Leftrightarrow R$为对称关系；$\quad\text{(5-12)}$

还有一些集合上的关系，集合中的所有元素与其自身之外任何元素之间的关系都不具有对称性，例如正整数的整除关系，对于任意两个正整数，除非这两个整数相等，否则它们之间不可能相互整除，也就是说，对于任意两个正整数$a$和$b$，如果$a|b$且$b|a$，则必有$a=b$。关系的这种性质称为反对称性，具体定义如下：  

【定义5.20】设$R$ 是集合$A$ 上的关系，若对任意$x,y\in A$，满足$\langle x,y\rangle\in R$且$\langle y,x\rangle\in R$  

则有$a=b$，则称关系$R$ 是反对称关系，或称$R$ 具有反对称性。即有：$(\forall x)(\forall y)(x\in A\land y\in A\land\langle x,y\rangle\in R\land\langle y,x\rangle\in R\to x=y)\Leftrightarrow R$为反对称关系  （5-13）【例题5.29】设$A=\{a,b,c\}$， $R_{1}$，$R_{2}$，$R_{3}$，$R_{4}$是$A$ 上的关系，其中：  
$$
R_{1}=\{\langle a,a\rangle,\langle b,b\rangle,\langle c,c\rangle\};\,\,\,R_{2}=\{\langle a,a\rangle,\langle b,c\rangle,\langle c,b\rangle\}
$$

$$
R_{3}=\{\langle a,b\rangle,\langle a,c\rangle\};\,\,\,R_{4}=\{\langle a,b\rangle,\langle b,c\rangle,\langle c,a\rangle\}
$$
判断$R_{1}$，$R_{2}$，$R_{3}$，$R_{4}$是否具有对称性或反对称性。  

【解】由关系的对称和反对称的定义知，$R_{1}$具有对称性和反对称性，$R_{2}$只具有对称性，$R_{3}$只具有反对称性，$R_{4}$既不具有对称性也不具有反对称性。  

【例题5.30】集合$A=\{1,\!2,\!3\}$， 𝑅1 = {〈1,1〉, 〈1,2〉,〈2,1〉}， $R_{2}=\{\langle1,\!2\rangle,\langle1,\!3\rangle\}$。分析R_{1}$和$R_{2}$对称性和反对称性，并分析它们关系矩阵和关系图的特征。  

【解】根据对称性和反对称性的定义，易知${|R_{1}}$只具有对称性，$R_{2}$只具有反对称性。令$R_{1}$和${R_{2}}$的关系矩阵分别为${{M}_{R_{1}}}$和$M_{R_{2}}$，则有：  
$$
M_{R_{1}}={\left(\begin{array}{l l l}{}&{1}&{1}&{0}\\ {}&{1}&{0}&{0}\\ {}&{0}&{0}&{0}\end{array}\right)};\;\;M_{R_{2}}={\left(\begin{array}{l l l}{0}&{1}&{1}\\ {0}&{0}&{0}\\ {0}&{0}&{0}\end{array}\right)}
$$
可以看出：${{M}_{{{R}_{1}}}}$是一个对称矩阵； $M_{R_{2}}$是一个不对称矩阵，并且关于主对角线对称的两个元素中最多有一个元素等于1。  

图5-13 和图5-14 分别是$R_{1}$和${\boldsymbol{R}}_{2}$的关系图。可以看出：在$R_{1}$的关系图中，两个不同结点之间若有边，则必然同时存在方向相反的两条边；而$R_{2}$的关系图中，任何一对结点之间至多有一条边。  

![](images/619dcb40abf0ef9e5e65826c827ef4f2ef091bbe56ed8732da9e543672079ebc.jpg)  

通过上述例题，不难得出如下结论：  

（1）存在既不是对称也不是反对称的关系，也存在既是对称也是反对称的关系。

 （2）关系$R$ 是对称的当且仅当关系图中任何一对结点之间，要么存在方向相反的两条边，要么无任何边；关系$R$ 是反对称的当且仅当关系图中任何一对结点之间至多有一条边。

（3）关系$R$ 是对称的当且仅当$R$的关系矩阵为对称矩阵；关系$R$ 是反对称的当且仅当$R$ 的关系矩阵为反对称矩阵，即对称的两个元素中最多有一个等于1。  

【例题5.31】试判断下列关系是否具有对称性和反对称性。

（1）对任意集合$A$，其幂集$\textit{Q}\left(\boldsymbol{A}\right)$上的包含关系；（2）整数集$Z$上的整除关系。  

【分析】（1）当两个集合不相等时，如果有其中一个集合包含于另一个，则反过来必然没有包含关系，故有反对称性但没有对称性；（2）当整数$a$ 和整数$b$ 不等时，若$a$ 整除$b$，则必有$b$ 不能整除$a$，故有反对称性但没有对称性。  

【解】对任意集合$A$，其幂集$P(A)$上的包含关系具有反对称性；整数集$Z$上的整除关系具有反对称性。  

### 5.3.3 关系的传递性  

日常工作和生活中的很多关系都具有某种传播或传递性质，例如：对于同学关系，如果  

张三四是李四的同学，李四又是王五的同学，那么张三必然是王五的同学；对于两条直线之间的平行关系，如果直线$a$ 与直线$b$ 平行，而直线$b$ 又与直线c 平行，那么必有直线$a$ 与直线$c$ 平行；对于两个整数之间的整除关系，如果整数$m$ 能够整除整数$n$，整数$n$ 又能整除$k$，那么$m$ 必然能整除整数$k$，等等。将这些不同具体关系所具有传播性质或传递性质进行抽象，得到如下关于关系传递性质的概念：  

【定义5.21】设$R$ 是集合$A$ 上的关系，对于任意$x,y,z\in A$，若从$\langle x,y\rangle\in R$且$\langle y,z\rangle\in R$这两个条件中推出$\langle x,z\rangle\in R$，则称关系$R$ 是传递关系，或称关系$R$具有传递性。即有： $(\forall x)(\forall y)(\forall z)(x\in A\land y\in A\land z\in A\land\langle x,y\rangle\in R\land\langle y,z\rangle\in R\to\langle x,z\rangle\in R)\Leftrightarrow R$为传递关系$\quad\text{(5-14) }$

【例题5.32】设$A=\{a,b,c\}$，$R_{1},R_{2},R_{3},R_{4}$是$A$ 上的关系，其中：  
$$
R_{1}=\{\langle a,a\rangle,\langle b,b\rangle,\langle c,c\rangle\};\,\,\,R_{2}=\{\langle a,b\rangle,\langle b,c\rangle\};\,\,\,R_{3}=\{\langle b,c\rangle\}
$$
判断$R_{1}$，$R_{2}$，$R_{3}$是否具有传递性。  

【解】由关系传递的定义知，$R_{1}$和$R_{3}$具有传递性，$R_{2}$不具有传递性。  

【例题5.33】设$A=\{1,\!2,\!3\}$，$R_{1},R_{2},R_{3},R_{4}$是𝐴上的关系，其中： $R_{1}=\{\langle1,1\rangle,\langle1,2\rangle,\langle2,3\rangle,\langle1,3\rangle\};\,\,\,R_{2}=\{\langle3,2\rangle\};$                                               𝑅 $R_{3}=\{\langle1,1\rangle,\langle1,2\rangle,\langle2,3\rangle\};\,\,\,R_{4}$ $\mathbf=\{\langle1,2\rangle,\langle2,3\rangle,\langle1,3\rangle,\langle2,1\rangle\}$  

判断它们是否具有传递性，并分析它们关系矩阵和关系图的特征。  

【解】在关系$R_{1}$中，对于$\forall x,y,z\in A$，当$\langle x,y\rangle\in R_{1}$，$\langle y,z\rangle\in R_{1}$时，必有$\langle x,z\rangle\in R_{1}$。因此，关系$R_{1}$具有传递性。关系$R_{2}$中仅有一个元素〈3,2〉，由关系传递性定义知$R_{2}$具有传递性。在关系$R_{3}$中，存在$𝐴$中的元素$x=1,y=2,z=3$，使得$\langle1,2\rangle\in R_{3}$且$\langle2,3\rangle\in R_{3}$，但$\langle1,3\rangle\not\in R_{3}$。因此， $R_{3}$不具有传递性。同理可知，关系$R_{4}$不具有传递性。  

下面考察关系$R_{1},R_{2},R_{3},R_{4}$的关系矩阵和关系图的特点。令$R_{1},R_{2},R_{3},R_{4}$的关系矩阵分别为$M_{R_{1}},M_{R_{2}},M_{R_{3}}$和${{M}_{{{R}_{4}}}}$，则有：  
$$
M_{R_{1}}={\left(\begin{array}{l l l}{1}&{1}&{1}\\ {0}&{0}&{1}\\ {0}&{0}&{0}\end{array}\right)},\;\;M_{R_{2}}={\left(\begin{array}{l l l}{0}&{1}&{0}\\ {0}&{0}&{0}\\ {0}&{0}&{0}\end{array}\right)},\;\;M_{R_{3}}={\left(\begin{array}{l l l}{1}&{1}&{0}\\ {0}&{0}&{1}\\ {0}&{0}&{0}\end{array}\right)},\;\;M_{R_{4}}={\left(\begin{array}{l l l}{0}&{1}&{1}\\ {1}&{0}&{1}\\ {0}&{0}&{0}\end{array}\right)}
$$
可以验证，如果关系满足传递性，则对于在该关系传递矩阵中的任意三个元素$r_{i j},r_{j k}$和$r_{i k}$，如果$r_{i j}=r_{j k}=1$，那么必有$r_{i k}=1$。反之亦然。  

![](images/3e5b25cb1a0d17c05cc1148bcb2af8baf870ecd021be822eb79d68b9c7205787.jpg)  

$R_{1},R_{2},R_{3},R_{4}$的关系图如图5-15 所示。可以看出，如果一个关系是传递的，则对于该关系所对应关系图中的任何三个结点$x,y,z$（结点可以相同），若从结点$x$到结点𝑦有一条有向边且从结点𝑦到结点$z$有一条有向边，那么从结点$x$到结点$Z$之间必有一条有向边。  

由上述例题可知，从关系图和关系矩阵中不太容易看清其表示的关系是否具有传递性。  

因此，一般需要直接根据传递定义检查元素之间的关系传递性质。检查时要注意当$\langle x,y\rangle\in$$R$与$\langle y,z\rangle\in R$中有一个为假时，则认为$\langle x,z\rangle$的传递是成立的，即成立$\langle x,z\rangle\in R$。  

### 5.3.4 关系性质的判定  

前面学习了关系的五个基本性质，在关系图和关系矩阵上都能够找到表征这些性质的相关图特征和矩阵特征。因此，对于一个任意给定的二元关系，可以使用关系图或关系矩阵的相关特征判定该关系是否具备关系的哪些基本性质。从本质上看，关系是以序偶为元素的集合。下面介绍和讨论如何从集合的角度判定关系的基本性质。  

【定理5.10】设$R$ 是集合$A$ 上的二元关系，则有：  

（1）$R$ 是自反的$\iff I_{A}\subseteq R$；  （2）$R$ 是反自反的$\iff R\cap I_{A}=\emptyset$； 

（3）$R$ 是对称的$\Leftrightarrow R=R^{-1}$； （4）$R$ 是反对称的$\iff R\cap R^{-1}\subseteq I_{A}$

（5）$R$ 是传递的$\Longleftrightarrow R\circ R\subseteq R$。  

【分析】由于集合$A$ 上的关系$R$ 是抽象的，故可通过定义进行证明。下面只证明（4）和（5），其余的可类似证明。  

【证明】（4）必要性：设$R$ 是反对称的。对$\forall\langle a,b\rangle\in R\cap R^{-1}$，则有：  
$$
\langle a,b\rangle\in R\land\langle a,b\rangle\in R^{-1}
$$
即有$\left\langle a,b\right\rangle\in R\land\left\langle b,a\right\rangle\in R$。由于$R$ 是反对称的，故$a=b$。故有：  
$$
\langle a,b\rangle=\langle a,a\rangle\in I_{A}\mathbb{B}\mathbb{I}R\cap R^{-1}\subseteq I_{A}
$$
充分性：设$R\cap R^{-1}\subseteq I_{A}$。对$\forall a,b\in A$，若：$\left\langle a,b\right\rangle\in R\land\left\langle b,a\right\rangle\in R$，则有：

$\langle a,b\rangle\in R\wedge\langle a,b\rangle\in R^{-1}, \text{即有:}\langle a,b\rangle\in R\cap R^{-1}$

又因$R\cap R^{-1}\subseteq I_{A}$，故$\langle a,b\rangle\in{I}_{A}$，即有：$a=b$。因此，$R$是反对称的。

(5）必要性：设$R$ 是传递的。对任意$\langle a,c\rangle\in R\circ R$，则必存在$b\in A$，使得：  
$$
\left\langle a,b\right\rangle\in R\land\left\langle b,c\right\rangle\in R
$$
由$R$ 的传递性知，有$\langle a,c\rangle\in R$。故有$R\circ R\subseteq R$

充分性：设$R\circ R\subseteq R$，则对任意$a,b,c\in A$，若有$\langle a,b\rangle\in R$且$\langle b,c\rangle\in R$，则有：  
$$
\langle a,c\rangle\in R\circ R
$$
因为$R\circ R\subseteq R$，故$\langle a,c\rangle\in R$，即$R$ 是传递的。  

下面定理表明，对于关系一些基本性质在某些运算下仍然能够保持，此时称关系性质在该运算下具有封闭性。例如，如果$A$ 上$d$ 两个关系都是对称的，那么这两个关系的并运算也是对称的。也就是说，关系的对称性质在关系并运算下是封闭的。  

【定理5.11】设$R$、$S$是定义在$A$ 上的二元关系，则：  

（1）若$R$、$S$是自反的，则$R^{-1}$，$R\cup S$，$R\cap S$，$R\circ S$也是自反的；

（2）若$R$、$S$是反自反的，则$R^{-1}$，$R\cup S$，$R\cap S$也是反自反的； 

（3）若$R$、$S$是对称的，则$R^{-1}$，$R\cup S$，$R\cap S$也是对称的； 

（4）若$R$、$S$是反对称的，则$R^{-1}$，$R\cap S$也是反对称的； 

（5）若$R$、$S$是传递的，则$R^{-1}$，$R\cap S$也是传递的。  

【证明】这些结论的证明都比较简单，读者可自己给出全部结论的证明。这里仅给出自反、对称和传递关系在∩运算下的封闭性。  

假设$R$ 和$S$ 是集合$A$ 上的自反二元关系，则有$I_{A}\subseteq R$；$I_{A}\subseteq S$。故有：$I_{A}\subseteq R\cap S$。因此，$R\cap S$是$A$ 上的自反二元关系。  

假设$R$ 和$S$是集合$A$ 上的对称二元关系，则有：$R=R^{-1}$；$S=S^{-1}$。故有：  
$$
(R\cap S)^{-1}=R^{-1}\cap S^{-1}=R\cap S
$$
因此，$R\cap S$也是集合$A$ 上的对称二元关系。  

假设$R$ 和$S$ 是集合$A$ 上的传递二元关系，则有：$R\circ R\subseteq R$；$S\circ S\subseteq S$。根据复合关系对交运算的半分配律，有：  

$(R\cap S)\circ(R\cap S)\ \subseteq\ \ R\circ R\cap R\circ S\cap S\circ R\cap S\circ S\subseteq(R\cap S)\cap(R\circ S\cap S\circ R)\subseteq(R\cap S)$ 因此，$R\cap S$也是集合$A$ 上的传递二元关系。  

下面的例题表明，对称性、反对称性和传递性对合成运算都不是封闭的：  

【例题5.34】试举例说明下列事实：  

（1）$R$ 和$S$是反自反、反对称和传递的，但是$R\circ S$不一定具有反自反性和反对称性；R∪S 不一定具有反对称性和传递性；  

（2）$R$ 和$S$ 是自反、对称和传递的，但是$R\circ S$不一定具有对称性和传递性；$R{-}S$ 不一定具有自反性和传递性。  

【解】（1）设$A=\{1,\!2,\!3\}$，$R$和$S$是定义在𝐴上的两个关系：  
$$
R=\{\langle1,2\rangle,\langle2,3\rangle,\langle1,3\rangle\};\quad S=\{\langle3,2\rangle,\langle3,1\rangle,\langle2,1\rangle\}
$$
显然$R,\ S$ 都是反自反的、反对称和传递的。但$R\circ S=\{\langle1,1\rangle\langle2,2\rangle\langle2,1\rangle\langle1,2\rangle\}$不具有反自反性和反对称性；R∪S={〈1,2〉, 〈2,3〉,〈1,3〉,〈3,2〉, 〈3,1〉, 〈2,1〉}不具有反对称性和传递性。  

（2）设$A=\{1,\!2,\!3\}$，$R$和𝑆是定义在$𝐴$上的两个关系：  
$$
R=\{\langle1,1\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle1,2\rangle,\langle2,1\rangle\};\quad S=\{\langle1,1\rangle,\langle2,2\rangle,\langle3,2\rangle,\langle2,3\rangle\}
$$
显然$R$，$S$ 都是自反、对称和传递的。但是：  
$$
\begin{array}{r}{R\circ S=\{\langle1,1\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle2,3\rangle,\langle3,2\rangle\langle1,2\rangle,\langle2,1\rangle,\langle1,3\rangle\}}\end{array}
$$
不具有对称性和传递性；$R{-}S{=}\{\langle1,2\rangle,\langle2,1\rangle\}.$不具有自反性和传递性。 

【例题5.35】试判断下列图5-16 中的关系的性质。  

![](images/7a4cda66b567017e1a3d6f72d20f9fd93f6c8f0fd085b4b87482f4f9051939d4.jpg)  
图 5-16 例题5.35 的关系图  

【解】图$G_{1}$的关系在集合{1,2,3}上是对称的，因为结点1 与2，1 与3 之间的有向边是成对出现且方向相反；因为有的点有自环，有的点没有自环，故不是自反的，也不是反自反的；因为$\langle2,1\rangle\in R$，$\langle1,3\rangle\in R$，若是传递关系，必有$\langle2,3\rangle\in R$。然而结点2 没有一条指向结点3 的有向边，故不是传递的；因为$\langle2,1\rangle\in R$且$\langle1,2\rangle\in R$，但 $1\neq2$，故不是反对称的。  

图$G_{2}$的关系是反自反的，因为每个顶点都没有自环；是反对称的，因为两条边都是单向边；是传递的，因为不存在顶点$a,b,c\in\{1,\!2,\!3\}$，使得$a$ 到$b$ 有边，$b$ 到$c$ 有边，但$a$ 到$c$没有边。同理可知，图$G_{3}$的关系是自反的、反对称的，但不是传递的。  

【例题5.36】设$A=\{1,\!2,\!3,\!4,\!6,\!12\}$，$A$上的整除关系记为$R$，则$R$ 是自反的、对称的、反自反的、反对称的、传递的吗？画出$A$中关系$R$ 的关系图。  

【解】关系$R$ 是$A$ 中的关系，所以它的关系图如图5-17 所示。  

从图5-17 容易看出，$R$ 是自反、反对称和传递的，不是反自反的，也不是对称的。

 容易验证，一般正整数集合中整除关系都具有自反性、反对称性、传递性，而不具有反自反性和对称性。  

![](images/07c476a48acc49fc9a2d94a1e04c6a443647580d4bfef64d9a38e460e4c0ed2d.jpg)  

【例题5-37】设集合$\cdot A=\{1,\!2,\!3,\!4,\!5\}$，$R$ 是$A$ 中的关系，定义为：$R=\{\langle1,1\rangle$,〈1,2〉,〈1,3〉,〈1,4〉, 〈1,5〉, 〈2,2〉, 〈2,3〉,〈2,4〉,〈2,5〉, 〈3,3〉, 〈3,4〉,〈3,5〉, 〈4,4〉, 〈4,5〉,〈5,5〉}。试写出$R$ 的关系矩阵$M_{R}$，画出关系图，并根据关系矩阵和关系图的特点判断$R$ 的基本性质。  

【解】$R$ 的关系矩阵$\textstyle M_{R}$如下：  
$$
M_{R}=\left(\begin{array}{c c c c c}{{1}}&{{1}}&{{1}}&{{1}}&{{1}}\\ {{0}}&{{1}}&{{1}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{0}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{0}}&{{0}}&{{1}}\end{array}\right)
$$
关系图如图5-18 所示。下面根据关系矩阵和关系图判定R 的基本性质：  

(1 ) $\forall a\in A$，显然有$\langle a,a\rangle\in R$，或${M_{R}}$的主对角线元素皆为1，或关系图中每个顶点都有闭路，故R 是自反关系。因R 是自反关系，故不是反自反关系。  

(2 ) 因为$\langle1,\!2\rangle\in R$，但$\langle2,1\rangle\not\in R$，或$M_{R}$不是对称矩阵，或关系图中不是每对顶点之间都有成对出现的方向相反的边，故R 不是对称关系。$\forall a,b\in A$，如果$\langle a,b\rangle\in R$，且$a\neq b$，则$\langle b,a\rangle\not\in R$，或$M_{R}$的主对角线对称位置元素最多只有一个值为1，或关系图中每对顶点都没有成对有向边，故R 是反对称关系。  

不难验证$\forall a,b,c\in A$，若$\langle a,b\rangle\in R$且$\langle b,c\rangle\in R$，则$\langle a,c\rangle\in R$，或关系图中$\forall a,b,c\in A$，如果$a$到$b$有有向边，$b$到$c$有有向边，则$a$到$c$必有有向边，故R 是传递关系。 

## § 5.4 关系的性质闭包  

自反性、对称性和传递性是关系的重要性质，在对很多关系问题的求解过程中都需要用到这些性质。然而，并不是所有二元关系都具备这些性质。在关系模型求解时必须用到但现有关系不具备这些性质的时候，通常需要做一些变通，采用适当方法对现有关系进行尽可能小的调整或改变，使其具有所需的性质。给关系加上适当的性质闭包就是一种常用的变通方法，在很多场合都有着成功的应用。本节着重介绍这种加闭包的方法，具体包括关系闭包的基本概念、构造方法和基本性质。  

### 5.4.1  关系闭包的概念  

首先，我们考察关系的自反闭包。假设$R$ 是集合$A$ 上的二元关系，如果$R$ 不满足自反性，就说明集合$A$ 中存在某个元素$a.$,使得$\langle a,a\rangle\not\in R$，此时可以将关系R 进行调整或修改，避免这种情况的发生。具体地说，就是将序偶$\langle a,a\rangle$纳入到关系$R$ 由此产生一个新的关系$R^{\prime}$。一般地，如果对于$A$ 中的每个元素${x}$，都将$\langle x,x\rangle$纳入到关系$R$，由此产生新的关系$R^{\prime}$必然满足自反性。事实上，关系$R^{\prime}$是对关系$R$ 的一种扩充，使得扩充后的关系能够满足自反性。若能证明这种扩充是满足扩充目的最小扩充，则$R^{\prime}$就是关系$R$ 的自反闭包。  

可同理考察对称闭包。假设$R$ 是集合$A$ 上的二元关系，如果$R$ 不满足对称性，就说明集合$A$ 中存在两个元素$a$和$b$使得$\langle a,b\rangle\in R$，但$\langle b,a\rangle\not\in R$。此时，只需将$\langle b,a\rangle$纳入$R$ 中就可避免这种情况发生。因此，可以对$R$ 进行适当扩充构成其对称闭包。  

可类似考虑传递闭包的基本思想，不再赘述。下面给出这三个闭包的具体定义：  

【定义5.22】设$R$ 是集合$A$ 上的关系，若存在$A$ 上的另一个关系$R^{\prime}$，满足：  

（1）$R^{\prime}$是自反的（对称的、或传递的）  

（2）对$A$ 上任何自反（对称的、或传递）关系$R^{\prime\prime}$，如果$R\subseteq R^{\prime\prime}$，那么$R^{\prime}\subseteq R^{\prime\prime}$，则称${R^{\prime}}$为$R$的自反闭包（对称闭包或传递闭包），记为$r(R)(s(R)$或$t(R))$。  

下面定理给出了自反闭包和传递闭包的构造方法：  

【定理5.12】设$R$ 是非空集合$A$ 上的关系，则有：

 $r(R)=R\cup R^{0};\,\,\,s(R)=R\cup R^{-1}$  

【证明】这里只证明$r(R)=R\cup R^{0}$。读者可类似证明$s(R)=R\cup R^{-1}$  

由 $R^{0}=I_{A}$ 且 $I_{A}\subseteq R\cup I_{A}$ ，知 $R\cup I_{A}$ 或 $R\cup R^{0}$ 满足自反性。下面进一步证明 $R\cup R^{0}$ 是满足 扩充目的的最小关系。假设$R^{\prime\prime}$是$A$ 上任一包含$R$的自反关系，即有$R\subseteq R^{\prime\prime}$且$I_{A}\subseteq R^{\prime\prime}$。则任取$\langle x,y\rangle\in R\cup I_{A}$，显然有$\langle x,y\rangle\in R^{\prime\prime}$。故有$R\cup I_{A}\subseteq R^{\prime\prime}$，即$R\cup R^{0}\subseteq R^{\prime\prime}$。证毕！  

【例题5.38】设$A=\{1,\!2,\!3\}$，$R=\{\langle1,1\rangle$, 〈1,2〉,〈1,3〉,〈2,1〉}是$A$ 上的关系，试求$R$ 的自反闭包和对称闭包。  

【解】在$R$ 中添加上〈2,2〉和〈3, 3〉后得到的新关系就是$R$的自反闭包，即有：  
$$
r(R)=\{\langle1,1\rangle,\langle1,2\rangle,\langle1,3\rangle,\langle2,1\rangle,\langle2,2\rangle,\langle3,3\rangle\}
$$
类似地，有：$s(R)=\{\langle1,1\rangle$,〈1,2〉, 〈1,3〉, 〈2,1〉,〈3,1〉}

 下面定理给出了使用关系矩阵构造自反闭包和对称闭包的具体方法：  

【定理5.19】设$R$ 是非空集合$A$ 上的关系，$R$、$r(R)$、$s(R)$的关系矩阵分别是$M$、$M_{r}$、$M_{s}$，则有：$M_{r}=M\vee M^{0}$；$\begin{array}{r l}{M_{s}=}&{{}M\vee M^{T}}\end{array}$。其中$M^{0}$为单位矩阵，$M^{T}$为$M$的转置矩阵。  

【证明】与定理5.12 的证明类似，在此从略。  

【例题5.39】设集合$A=\{1,\!2,\!3,\!4\}$，$R=\{\langle1,2\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,4\rangle\}$$A$上的一个二元关系，试分别用集合运算法和矩阵法构造$r(R)$和$s(R)$。  

【解】使用集合运算法构造：  

$r(R)=R\cup R^{0}=\{\langle1,2\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,4\rangle\}\cup\{\langle1,1\rangle,\langle2,2\rangle,\langle3,3\rangle,\langle4,4\rangle\}$ $=\{\langle1,1\rangle,\langle1,2\rangle,\langle2,1\rangle,\langle2,2\rangle,\langle2,3\rangle,\langle3,3\rangle,\langle3,4\rangle,\langle4,4\rangle\}$ $\begin{array}{c}{{s(R)=R\cup R^{-1}=\{\langle1,2\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,4\rangle\}\cup\{\langle1,2\rangle,\langle2,1\rangle,\langle3,2\rangle,\langle4,3\rangle\}}}\\ {{=\{\langle1,2\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,2\rangle,\langle3,4\rangle,\langle4,3\rangle,\langle2,1\rangle,\langle3,2\rangle,\langle2,3\rangle,\langle3,4\rangle\}}}\end{array}$  

使用关系矩阵求解：  
$$
M_{r}=M\lor M^{0}={\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {1}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{0}&{0}\end{array}\right)}\lor{\left(\begin{array}{l l l l}{1}&{0}&{0}&{0}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\end{array}\right)}={\left(\begin{array}{l l l l}{1}&{1}&{0}&{0}\\ {1}&{1}&{1}&{0}\\ {0}&{0}&{1}&{1}\\ {0}&{0}&{0}&{1}\end{array}\right)}
$$

$$
\begin{array}{c c l}{M_{s}=}&{M\lor M^{T}=\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {1}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{0}&{0}\end{array}\right)\lor\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {1}&{0}&{0}&{0}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{0}\end{array}\right)=\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {1}&{0}&{1}&{0}\\ {0}&{1}&{0}&{0}\\ {0}&{0}&{1}&{0}\end{array}\right)}\end{array}
$$
解毕！  

【例题5.40】设集合$A=\{1,\!2,\!3,\!4\}$，$R$ 是$A$ 上的关系，且有：$R=\{\langle1,2\rangle,\langle2,2\rangle,\langle3,4\rangle\}$。试画出$R$ 的关系图，并根据关系图求出$r(R)$，$s(R)$和$t(R)$。  

【解】${R}$ 的关系图如图5-19 所示。从关系图上看，如果每个结点都有自环，那么该关系就具有自反性。故可在$R$ 的关系图的结点1，3 和4 处添加自环，即得到$|r(R)$的关系图，如图5-20 所示，故有：$\begin{array}{r}{r(R)=\{\langle1,2\rangle,\langle2,2\rangle,\langle2,3\rangle,\langle3,4\rangle,\langle1,1\rangle,\langle3,3\rangle,\langle4,4\rangle\}_{\circ}}\end{array}$。  

如果关系图的任何一对结点之间要么有方向相反的两条边，要么没有边，那么该关系的关系就具有对称性。故可在$R$ 的关系图中添加2 到1、3 到2 和4 到3 的有向边，即得到$s(R)$的关系图，如图5-20 所示，故有：$s(R)=\{\langle1,2\rangle,$,〈2,2〉,〈2,3〉, 〈3,4〉, 〈2,1〉,〈3,2〉,〈4,3〉}  

![](images/4cec1baa96fbafcfd2216cd381d9912ef23389dadcfe40fd062876be0362c609.jpg)  
图5-20 例题5.40 中$s(R)$的关系图  

如果关系图的任何三个结点$x,y,z$之间，若从$x$到𝑦有一条边且从𝑦到𝑧有一条边，那么必然存在一条从$x$到$z$的边，那么该关系就具有传递性。因此，在R 的关系图中添加1 到3、1到4 和2 到4 的有向边，即得到$t(R)$的关系图，如图5-20 所示，故有：  
$$
\begin{array}{r l}{t(R)}&{=\{\langle1,2\rangle,\langle2,2\rangle,\langle2,3\rangle,\langle3,4\rangle,\langle1,3\rangle,\langle1,4\rangle,\langle2,4\rangle\}}\end{array}
$$
解毕！  

由上述例题可得利用关系图求关系$R$ 闭包的方法：  

（1）检查$R$ 的关系图，在没有自环的结点处加上自环，可得$r(R)$的关系图；  

（2）检查$R$ 的关系图，将每条单向边全部改成双向边，可得$s(R)$的关系图；  

（3）检查$R$ 的关系图，从每个结点出发，找到其终点，如果该结点到其终点没有边相连，就加上此边，由此可得$t(R)$的关系图。  

### 5.4.2 传递闭包的构造  

自反闭包和对称闭包的构造比较简单，一般通过枚举的方法就可以得到解决。然而，传递闭包的构造比自反闭包和对称闭包要困难一些，需要一些技巧。因此，本小节对传递闭包概念做进一步深入理解并由此给出传递闭包构造方法和技巧。  

假设𝐴是任一给定的有限非空集合，$R$ 是$A$ 上的一个二元关系，$t(R)$是$R$ 的传递闭包，显然有${\boldsymbol{R}}\subseteq\ t({\boldsymbol{R}})$。现对于任意$\langle x,z\rangle\in R^{2}$或$\langle x,z\rangle\in R\circ R$，由$R\circ R$的定义知必存在$A$ 中某个元素$y$，使得$\langle x,y\rangle\in R$且$\langle y,z\rangle\in R$，那么根据关系$t(R)$的传递性，必有$\langle x,z\rangle\in t(R)$。故有：$R^{2}\subseteq\ t(R)$，即$R^{2}$也是$t(R)$的一个子集合。  

类似地，对于任意$\langle x,z\rangle\in R^{3}$或$\langle x,z\rangle\in R^{2}\circ R$，则必存在$A$ 中某元素$y$，使得$\langle x,y\rangle\in R^{2}$且$\langle y,z\rangle\in R$，从而有$\langle x,z\rangle\in t(R)$，故有$R^{3}\subseteq\ t(R)$。以此类推，可知，对于任意自然数$k$，必有$R^{k}\subseteq\ t(R)$。故有：  
$$
R\ \cup R^{2}\cup R^{3}\cup\cdots\cup R^{k}\cup\cdots\subseteq\ t(R)\quad\text{(5-15)}
$$
根据传递闭包$t(R)$的定义，$t(R)$是包含$ R$的传递性关系中最小的集合，要证明：  
$$
t(R)\ \,\subseteq\,R\,\cup R^{2}\cup R^{3}\cup\cdots\cup R^{k}\cup\cdots
$$
只需证明 $R\ \cup R^{2}\cup R^{3}\cup\cdots\cup R^{k}\cup\cdots$ 满足传递性即可。任取两个序偶 $\langle x,y\rangle$ 和 $\langle y,z\rangle$ ，满足：  
$$
\langle x,y\rangle\in R\ \cup R^{2}\cup R^{3}\cup\cdots\cup R^{k}\cup\cdots;\ \ \langle y,z\rangle\in R\ \cup R^{2}\cup R^{3}\cup\cdots\cup R^{k}\cup\cdots
$$
则分别存在自然数$t,s$，使得$\langle x,y\rangle\in R^{t}$且$\langle y,z\rangle\in R^{s}$，则根据关系复合运算的定义，有：$\langle x,z\rangle\in R^{t}\circ R^{s}$，即有：$\langle x,z\rangle\in R^{t+s}$。故有：$\langle x,z\rangle\in\!\!R\,\cup\!R^{2}\cup\!R^{3}\cup\cdots\cup\!R^{k}\cup\cdots_{\circ}$。即有：  
$$
t(R)\ \,\subseteq\,R\,\cup R^{2}\cup R^{3}\cup\cdots\cup R^{k}\cup\cdots\quad\text{(5-16)}
$$
经过以上分析，可得到如果关于传递闭包构造定理：  

【定理5.13】设$R$ 是非空集合$A$ 上的关系，$t(R)$是$R$ 的传递闭包，$M$和$M_{t}$分别为$R$ 和$t(R)$的关系矩阵，则有：  
$$
t(R)=\,R\,\cup R^{2}\cup R^{3}\cup\cdots\quad\text{(5-17)}
$$

$$
M_{t}=M\lor M^{2}\lor M^{3}\lor\cdots\quad\text{(5-18)}
$$
【证明】类似于以上分析，在此从略。  

由上述定理可知，对于$t(R)$中的任一序偶$\langle x,y\rangle$，必有某个自然数$k$，使得$\langle x,y\rangle\in R^{k}$。根据$R^{k}$的定义，也就是说关系$R$中必然存在如下${k}$个序偶：  
$$
\langle x,a_{1}\rangle,\langle a_{1},a_{2}\rangle,\cdots,\langle a_{k-1},y\rangle
$$
从𝑅的关系图上看，这$k$个序偶组成了一个以$,x,a_{1},a_{2},\cdots,a_{k-1},y$为结点的链路。如果不考虑重复结点的话，$R$的关系图中最长链路也只有$|A|$个结点。也就是说，$R$方幂的次数超过$|A|$的话，一定会出现重复或循环，故有：  
$$
t(R)=\,R\,\cup R^{2}\cup R^{3}\cup\cdots\cup R^{n};\,\,\,M_{t}=M\lor M^{2}\lor M^{3}\lor\cdots\lor M^{n}
$$
其中$n$为不超过$|A|$的某个自然数。  

【例题5.41】设集合$A=\{1,\!2,\!3,\!4\}$，$R=\{\langle1,2\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,4\rangle\}\,\,\,$$A$上的一个二元关系，试分别用集合运算法和矩阵法构造$t(R)$。  

【解】通过集合运算求解：  
$$
R=\{\langle1,2\rangle,\langle2,1\rangle,\langle2,3\rangle,\langle3,4\rangle\};\,\,\,R^{2}=\{\langle1,1\rangle,\langle1,3\rangle,\langle2,2\rangle,\langle2,4\rangle\}
$$

$$
R^{3}=\{\langle1,2\rangle,\langle1,4\rangle,\langle2,1\rangle,\langle2,3\rangle\};\;\;R^{4}=\{\langle1,1\rangle,\langle1,3\rangle,\langle2,2\rangle,\langle2,4\rangle\}=R^{2}
$$

故有：$\begin{array}{c l c l}{t(R)=}&{R\cup R^{2}\cup R^{3}\cup R^{4}=\{\langle1,1\rangle,\langle1,2\rangle,\langle1,3\rangle,\langle1,4\rangle,\langle2,1\rangle,\langle2,2\rangle,\langle2,3\rangle,\langle2,4\rangle,\langle3,4\rangle\}_{\circ}}\end{array}$

通过关系矩阵求解：  
$$
M_{t}=M\lor M^{2}\lor M^{3}\lor M^{4}=M\lor M^{2}\lor M^{3}
$$

$$
=\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}\\ {1}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{0}&{0}\end{array}\right)+\left(\begin{array}{l l l l}{1}&{0}&{1}&{0}\\ {0}&{1}&{0}&{1}\\ {0}&{0}&{0}&{0}\\ {0}&{0}&{0}&{0}\end{array}\right)+\left(\begin{array}{l l l l}{0}&{1}&{0}&{1}\\ {1}&{0}&{1}&{0}\\ {0}&{0}&{0}&{0}\\ {0}&{0}&{0}&{0}\end{array}\right)=\left(\begin{array}{l l l l}{1}&{1}&{1}&{1}\\ {1}&{1}&{1}&{1}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{0}&{0}\end{array}\right)
$$
解毕！  

通过前面的例题可以看出，使用集合运算法计算传递闭包比较繁琐晦涩，非常容易出错，使用矩阵计算则涉及计算量很大的方幂计算。为了更加方便地构造关系的传递闭包，下面介绍一个比较高效传递闭包构造算法，即著名的沃舍尔算法。  

假设$R$ 是非空集合$A$ 上的二元关系，$t(R)$是$R$ 的传递闭包，$G$ 是$R$ 的关系图。从前面分析可知，在传递闭包$t(R)$的关系图中，若从结点$x$到结点$y$有一条边，当且仅当在$R$的关系图$G$ 中存在一条从结点$x$到结点$y$且边数大于或等于1 的链路，即在图$G$ 可以从结点$x$连通到结点$y$。因此，关于$R$的传递闭包$t(R)$实际上就是$R$的关系图$G$ 的连通关系$R^{*}$，即有：  

$R^{*}=\{\langle x,y\rangle|$在图$G$中存在一条从结点结点$x$到结点𝑦有向链路}  

现考虑 $n+1$ 个矩阵序列 $M_{0},M_{1},\cdots,M_{n}$ ，将矩阵 ${M}_{k}$ 的第 $𝑖 $行第$ 𝑗 $列的元素记为 $M_{k}[i,j]$ 。对 于$k=0,1,\cdots n$，$M_{k}[i,j]=1$当且仅当在$R$的关系图$G$ 中存在一条结点$x_{i}$到结点$x_{j}$的一条链路，并且这条链路除两个端点之外的中间结点只能经过集合$\{x_{1},x_{2},\cdots,x_{k}\}$中的结点。显然，$M_{0}$就是$R$ 的关系矩阵，而$M_{n}$就是$R$ 的传递闭包$t(R)$的关系矩阵。沃舍尔算法的核心思想就是采用递推的方法从$M_{0}$逐步计算出$M_{n}$，据此给出$t(R)$的高效构造算法。  

假设$M_{k}$已经计算完成，那么如何从$M_{k}$计算出$M_{k+1}$呢？所谓计算出$M_{k+1}$，其实就是对每组$i,j$，确定$M_{k+1}[i,j]$是否为1。根据$M_{k+1}$的定义，$M_{k+1}[i,j]=1$当且仅当在$R$的关系图$G$中存在一条结点$x_{i}$到结点$x_{j}$的一条链路，并且这条链路除两个端点之外的中间结点只能经过集合$\{x_{1},x_{2},\cdots,x_{k},x_{k+1}\}$中的结点。这种链路只有两种可能性：  

第一种是只经过$\{x_{1},x_{2},\cdots,x_{k}\}$中的结点，此时$M_{k}[i,j]=1$  

第二种可能是链路经过了结点$x_{k+1}$，此时显然仅考虑只经过结点$x_{k+1}$一次的情形，因为如果经过两次$x_{k+1}$则必然形成一个回路，将该回路删除即可。将该链路分成如下两段，即：从结点$x_{i}$到结点$x_{k+1}$，以及从结点$x_{k+1}$到结点$x_{j}$。故有$M_{k}[i,k+1]{=}1$ 且$M_{k}[k+1,j]{=}1$。  

综上所述，可由下列公式从$M_{k}$计算出$M_{k+1}$  
$$
M_{k+1}[i,j]=M_{k}[i,j]\vee M_{k}[i,k+1]\wedge M_{k}[k+1,j]\quad\text{(5-19)}
$$
具体地说，对于$k=0,1,2,\cdots,n-1$，从$M_{k}$构造$M_{k+1}$的具体过程如下：  

(1)$ M_{k}[i,j]=s_{i j},\,\,\,M_{k+1}[i,j]=t_{i j}$ 

（2）将$M_{k}$中的所有值为1 元素复制到$M_{k+1}$中相应位置，即若$s_{i j}=1$，则$t_{i j}=1$  ;

（3）对于所有$i,j=1,2,\cdots,n$，若$t_{i j}=0$，则当$s_{i k+1}=s_{k+1j}=1$时，令$t_{i j}=1$ 。 

【例题5.42】设集合$A=\{a,b,c,\mathtt{d}\}$，$R=\{\langle a,b\rangle,\langle a,c\rangle,\langle b,c\rangle,\langle c,d\rangle,\langle d,c\rangle\}$是 $A$上的一个二元关系，试分别用矩阵法和沃舍尔算法构造$R$的传递闭包$t(R)$矩阵  

【解】令$M$是$R$的关系矩阵，$M_{t}$是 $t(R)$的关系矩阵，由矩阵法得：  
$$
M_{t}=M\vee M^{2}\vee M^{3}\vee M^{4}
$$

$$
\begin{array}{r l}{\mathbf{\Lambda}}&{=\left(\begin{array}{l l l l}{0}&{1}&{1}&{0}\\ {0}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{1}&{0}\end{array}\right)\lor\left(\begin{array}{l l l l}{0}&{0}&{1}&{1}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\end{array}\right)\lor\left(\begin{array}{l l l l}{0}&{0}&{1}&{1}\\ {0}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{1}&{0}\end{array}\right)\lor\left(\begin{array}{l l l l}{0}&{0}&{1}&{1}\\ {0}&{0}&{0}&{1}\\ {0}&{0}&{1}&{0}\\ {0}&{0}&{0}&{1}\end{array}\right)}\\ &{\qquad=\left(\begin{array}{l l l l}{0}&{1}&{1}&{1}\\ {0}&{0}&{1}&{1}\\ {0}&{0}&{1}&{1}\\ {0}&{0}&{1}&{1}\end{array}\right)}\end{array}
$$
由沃舍尔算法，得：  
$$
\begin{array}{l l}{{M_{0}\!\!=\!\!\left(\begin{array}{l l l l}{{0}}&{{1}}&{{1}}&{{0}}\\ {{0}}&{{0}}&{{1}}&{{0}}\\ {{0}}&{{0}}&{{0}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{0}}\end{array}\right)\!;\;M_{1}\!\!=\!\!\left(\begin{array}{l l l l}{{0}}&{{1}}&{{1}}&{{0}}\\ {{0}}&{{0}}&{{1}}&{{0}}\\ {{0}}&{{0}}&{{0}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{0}}\end{array}\right)\!;\;M_{2}\!\!=\!\!\left(\begin{array}{l l l l}{{0}}&{{1}}&{{1}}&{{0}}\\ {{0}}&{{0}}&{{1}}&{{0}}\\ {{0}}&{{0}}&{{0}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{0}}\end{array}\right)\!;}}\\ {{M_{3}\!\!=\!\!\left(\begin{array}{l l l l}{{0}}&{{1}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{0}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{1}}\end{array}\right)\!;\;M_{4}\!\!=\!\!\left(\begin{array}{l l l l}{{0}}&{{1}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{1}}\\ {{0}}&{{0}}&{{1}}&{{1}}\end{array}\right)}}\end{array}
$$
$M_{4}$ 即为所求。  

从上述例题可以看出，矩阵法和沃舍尔算法得到的结果完全相同。不难看出，沃舍尔算法的计算复杂度为$0(n^{3})$，显然比矩阵法的计算效率高很多。  

### 5.4.3  关系闭包的性质  

下面讨论关系闭包的一些基本性质：  

【定理5.14】若$R$ 是$A$ 上二元关系，则有：  

（1）$R$ 是自反的，当且仅当$r(R)=R$

（2）$R$ 是对称的，当且仅当$s(R)=R$；

（3）$R$ 是传递的，当且仅当$t(R)=R$。  

【证明】（1）必要性：显然有$R\subseteq r(R)$，又因$R$ 是包含了$R$ 的自反关系，根据自反闭包定义有$r\;\left(R\right)\;\subseteq R$，从而得到$r(R)=R$。充分性显然成立。（2）（3）的证明同（1）。  

【定理5.15】若$R$ 是$A$ 上二元关系，则有：  

（1）$R$ 是自反的，则$s(R)$和$t(R)$也是自反的；

（2）$R$ 是对称的，则$r(R)$和$t(R)$也是对称的；

（3）$R$ 是传递的，则$r(R)$也是传递的。  

【证明】只证（2），其余的证明与（2）类似，读者可自己给出证明。  

假设$R$ 是$A$ 上的对称关系，则有：$R=R^{-1}$。又由于${I_{A}}={{I_{A}}^{-1}}$，故有： $r(R)^{-1}=(R\cup R^{0})^{-1}=(R\cup I_{A})^{-1}=R^{-1}\cup{I_{A}}^{-1}=\ R\cup I_{A}=r(R)$  

故$r(R)$是对称关系。  

为证明$t(R)$是对称关系，首先证明对于任意自然数$_n$，$R$的$n$次方幂$\textstyle R^{n}$也是对称关系。使用数学归纳法证明：  

当$n=1$ 时，$R^{1}=~\ R$，故$R^{1}$是对称的。现假设当$n=k$时，$R^{k}$是对称关系，则对于任意$\langle x,y\rangle\in R^{k+1}$，有$\langle x,y\rangle\in R^{k}\circ R$。故必存在元素$w\in A$，使得$\langle x,w\rangle\in R^{k}$且$\langle w,y\rangle\in R$。根据$R$和$R^{k}$的对称性知。必有$\langle w,x\rangle\in R^{k}$且$\langle y,w\rangle\in R$。因此，$\langle y,x\rangle\in R\circ R^{k}{=}\ R^{k+1}$。故$R^{k+1}$是对称关系。根据归纳法原理，对于任意自然数$ n$， $R^{n}$是对称关系。  

对于任意$\langle x,y\rangle\in t(R)$，则必存在某个自然数$m$，使得$\langle x,y\rangle\in R^{m}$，由$R^{m}$的对称性知，$\langle y,x\rangle\in R^{m}$，故有$\langle y,x\rangle\in t(R)$。因此，$t(R)$是对称关系。

说明：上述定理讨论了关系性质和闭包运算之间的联系；  

（1）如果关系$R$ 是具有自反性，那么经过闭包运算之后得到的关系仍然具有自反性；

（2）如果关系$R$ 是具有对称性，那么经过闭包运算之后得到的关系仍然具有对称性；  

（3）但是对于具有传递性的关系不是如此，其自反闭包仍然具有传递性，而其对称闭包则不一一定具有传递性。例如，假设$A=\{1,\!2,\!3\}$, 则$R=\{\langle1,\!2\rangle\}$是𝐴上的传递关系，此时有$s(R)=\{\langle1,\!2\rangle,\langle2,\!1\rangle\}$。显然$s(R)$不具有传递性。 

下面定理给出了关系的闭包与集合运算之间的关系：  

【定理5.16】设$A$ 是一个非空有限集合，$R$和$𝑆$均为$A$ 上二元关系，则有：  

(1）若 $R\subseteq S$ ，则有： $r(R)\subseteq r(S);\,\,\,s(R)\subseteq s(S);\,\,\,t(R)\subseteq t(S)$ 。   (2)$r(R\cup S)=r(R)\cup r(S);\quad s(R\cup S)=s(R)\cup s(S);\quad t(R)\cup t(S)\subseteq t(R\cup S)\,。$  

【证明】 （ 1 ）由 $r(R)=\ R\cup I_{A}$ ； $s(S)=\ S\cup I_{A}$ 知，若 $R\subseteq S$ ，则有 $r(R)\subseteq r(S)$   。可类似 证明其余两个式子 $s(R)\subseteq s(S);\,\,\,t(R)\subseteq t(S)$。  

（2）$r(R\cup S)=R\cup S\cup I_{A}=(R\cup I_{A})\cup(S\cup I_{A})=r(R)\cup r(S);$ $s(R\cup S)=(R\cup S)\cup(R\cup S)^{-1}=R\cup S\cup R^{-1}\cup S^{-1}=~s(R)\cup s(S);$   

  由于$R\subseteq R\cup S$，$S\subseteq R\cup S$，故有：$t(R)\subseteq\ t(R\cup S)$，$t(S)\subseteq\ t(R\cup S)$，故有：$t(R)\cup t(S)\subseteq t(R\cup S)$  

证毕！  

对于非空集合$A$ 上的二元关系$𝑅$，由于其自反闭包$r(R)$、对称闭包$s(R)$和传递闭包$t(R)$仍然是$A$ 上的二元关系，因此可以对这些闭包进一步做不同的闭包，例如在自反闭包$r(R)$的基础上再做对称闭包或传递闭包、在对称闭包$s(R)$的基础上再做自反包或传递闭包、在传递闭包$t(R)$的基础上再做自反包或对称闭包等，由此可以得到多重闭包。下面定理给出了关于这些多重闭包的基本性质：  

【定理5.17】设$A$ 是一个含有${n}$个元素的非空集合，$R$ 是$A$ 上二元关系，则有： $(1)r s(R)=s r(R);~~~(2)r t(R)=t r(R);~~(3)~s t(R)\subseteq t s(R)$ 

【证明】（1）$rs(R)=r(R\cup R^{-1})=(R\cup R^{-1})\cup I_A=R\cup R^{-1}\cup I_A; {\text{而:}}$

$\begin{gathered}
sr(R)=(R\cup I_{A})\cup(R\cup I_{A})^{-1}=R\cup I_{A}\cup R^{-1}\cup I_{A}^{-1} \\
=R\cup R^{-1}\cup I_{A} \\
\text{故有:}rs(R)= sr(R)。 \\\end{gathered}$

(2) $tr(R)= t(R\cup I_A)=(R\cup I_A)\cup(R\cup I_A)^2\cup(R\cup I_A)^3\cup\cdots\cup(R\cup I_A)^n$

$\begin{gathered}=(R\cup I_{A})\cup(R^{2}\cup R\cup I_{A})\cup(R^{3}\cup R^{2}\cup R\cup I_{A})\cup\cdots \\
\cup(\quad R^n\cup\cdots\cup R^2\cup R\cup I_A) \\
= R \cup R^{2}\cup R^{3}\cup\cdots\cup R^{n}\cup I_{A}=r( R \cup R^{2}\cup R^{3}\cup\cdots R^{n}) \\
=rt(R) \\
\text{故有:}rt(R)= tr(R)。 
\end{gathered}$
(3) 根据闭包的定义有$R\subseteq s(R)$，则根据闭包的性质知：$t(R)\subseteq t s(R)$；$s t(R)\subseteq s t s(R)。$由于$t s(R)$为对称关系，故有$t s(R)=s t s(R)$，即有$s t(R)\subseteq s t s(R)=t s(R)$。证毕！ 

注意，上述定理结论(3)中$\subseteq$不能用$=$替代。例如，令$A=\{1,\!2,\!3\}$, $R=\{\langle1,\!2\rangle\}$是𝐴上的二元关系，则${s t(R)=\{\langle1,2\rangle,\langle2,1\rangle\}}$，而$ts(R)=\{\langle1,2\rangle,\langle2,1\rangle,\langle1,1\rangle,\langle2,2\rangle\}$，$s t(R)\neq t s(R)$。  

## § 5.5 关系模型的应用  

在计算机中专门用于存储与管理数据的系统称为数据库管理系统，而存储与管理数据的基本特征的抽象表示称为数据模型。一般来讲，数据模型都可以用数学形式表示，常用的有图的形式、关系形式及逻辑形式等。其中基于关系代数与关系演算的关系数据模型是计算机科学的重大理论成果，它对数据库的发展起着关键性与基础性的作用。关系代数模型运用了关系及关系运算，实现数据库中数据结构的描述，数据操作、操作优化及规范化的表示；关系演算模型运用了谓词逻辑理论，以实现数据库中数据结构的表示、数据操作及查询优化，并通过谓词推理获取查询结果。由关系代数而建立起了关系数据库，由关系演算而建立起了知识库与演绎数据库，开创了数据库学科研究的重大方向。几十年来，基于关系数据模型的关系型数据库系统一直是主流数据库系统。  

### 5.5.1 关系代数模型  

关系代数模型由IBM 公司E.F.Codd 于1970 年提出，并最终于1976 年研制出具有实用价值的关系模型数据库系统system R。此项成果首次实现了以理论带动系统的重要突破，从此以后关系模型数据库系统是数据库中最具优势的数据模型。  

关系数据模型是一种以二维表的方式表示数据的多元关系结构以及相关的关系操作。二维表又称表，它由表框架及表元组两部分组成。表框架由表名及若干个命名属性列构成。表中每行数据称为元组。元组由若干个分量组成，其每个分量对应表框架中的一个属性值，一个表框架可以储存若干个元组，它们构成了一个完整的二维表。例如，表5-2 和表5-3 分别为4 元关系𝑅和𝑆的二维表。

表5-2 关系𝑅的二维表    

![](images/1bedfc7c88000b4cf5a1542d888887ac793b5a954f111138c9a373b25e404611.jpg)  


表5-3 关系S的二维表 
![](images/1a8eb6a738768389cb850c5f08a9fb36d42702a5e326c1cc16a02917285ec49a.jpg)  

建立在二维表上的数据操作，包括查询、删除、插入及修改等操作。查询操作可分解成三个定位与一个操作，即表的列指定、表的行选择、两张表的合并、选择操作。删除操作的基本操作单位是元组，其功能是将指定表内的指定元组删除。它也分为定位与操作两部分，其中定位部分即是行选择，定位后即执行删除操作。插入操作的功能是在指定表中插入一至多个元组。入操作无须定位，仅对指定表执行（插入）操作即可。改操作是在表中修改指定元组的数据.它可以分解为两个操作，即先进行删除操作再进行插入操作。  

由以上分析可知，关系数据模型中的基本操作共有六种，三种定位操作与三种执行操作，即：表的列指定、表的行选择、两表的合并、选择操作、删除操作、插入操作。二维表上的六种基本操作可对应关系的五种运算，因为选择操作不涉及逻辑运算，可在关系代数中忽略。其中一些操作可以关系的集合运算与复合运算实现。具体地说：二维表的数据操作插入可用关系集合并运算实现、数据删除操作可用关系集合差运算实现、两表合并可用关系集合的笛卡尔积运算实现、多表查询运算可用关系的复合运算实现。  

例如，若将表所示关系𝑅插入表所示关系𝑆的全部数据，则如表5-4 所示，使用关系的集合并运算即可完成该项操作。  

![](images/e8307e7e667a7c55af17e1fb2237de2afa5ae8d2f96c1f87db8ab79373e5f29a.jpg)  
表5-4 关系表中数据插入操作  

再如，表5-5 和5-6 为某计算机学院的课程信息表，其中Cno、Cname、Cpno、Ccredit分别表示课程编号、名称、先修课程编号和学分。若要查询表中每门课程的先修课程的先修课程，则可通过对该表所示关系进行复合运算得到表5-7。  

表5-5 课程信息表           表5-6 课程信息表               表5-7 关系表的复合  

![](images/583cda9271250a95bd1e8b2bda00f43e42da09a7fd406c4096803ced0e575304.jpg)  

关系代数在数据库系统中具体应用可参阅数据库专业教材，不再赘述。  

### 5.5.2 关系演算模型  

关系演算作为一种数学模型也产生于二十世纪70 年代，该模型以关系理论为基础并在关系理论中引入谓词推理机制，将推理与查询融为一体，从而实现关系数据库与知识库的一体化，主要用于对操作的优化，有效提高查询效率。目前，在大数据环境下，希望能够从海量数据中总结或发现一些有价值的规律或知识，这就是一直比较热门的大数据知识发现或者数据挖掘的研究课题。关系演算作为一个具备谓词推理机制的数据模型，能够的完成知识表示与推理，实现关系数据库系统与知识库系统有效整合。因此，关系演算无论在理论还是在应用方面都具有非常重要的价值。  

对于任意给定的一个二维表，可用一个多元谓词对其进行表示。其中谓词中个体变元即是表的属性，而表中的元组就是使该谓词为真的赋值，不在表中元组则是使该谓词为假的赋值。例如，对于表5-8 所示的学生基本信息表，其中表中属性sno、sn、sd、 sa 分别表示学生对象的学号、姓名、系别和年龄信息。可用谓词S（sno，sn，sd，sa）对该表进行表示，表中元组（07001，张曼英，CS，19）、（07002，丁一明，CS，20）、（07003，王爱国，CS，18）、（07004，李强，CS，18）是该谓词公式全部成真赋值，也就是说不在表中的元组均为该谓词成假赋值。  

表5-8 学生基本信息表
![](images/6776047d5bf30473704fe88f7b291d196fd0ffae2639cdc0fd808869c2e3b6f4.jpg)  

可用谓词公司演算实现关系表的数据操作。具体地说，可用谓词公式的析取运算实现关系表中数据的插入操作、谓词公式的合取运算实现关系表中数据的删除操作、可用谓词公式的推理实现查询操作的优化，等等。例如，若需在表中插入数据（07005，史今强，MA，21），则首先需构建一个新谓词$S^{\prime}$(sno，sn，sd，sa)，该谓词成真赋值为需插入元组，然后通过谓词公式的析取运算实现对数据（07005，史今强，MA，21）的插入操作：  
$$
S\big(\mathrm{{sno},\ \ s n,\ \ s d,\ \ s a}\big)\vee S^{\prime}(\mathrm{{sno},\ \ s n,\ \ s d,\ \ s a})
$$
若需在表中删除元组（07001 ，张曼英，CS，19 ），则首先需构建一个新谓词S′(sno，sn，sd，sa)，该谓词成真赋值为需删除元组，通过谓词公式的合取运算实现对数据（07001，张曼英，CS，19）的插入操作：  
$$
\mathrm{S}\big(\mathrm{sno},\ \mathrm{sn},\ \mathrm{sd},\ \mathrm{sa}\big)\wedge\neg S^{\prime}(\mathrm{sno},\ \mathrm{sn},\ \mathrm{sd},\ \mathrm{sa})
$$
若需在表中查询年龄大于18 岁的学生姓名，则可用如下谓词蕴涵式实现：  
$$
\exists\mathrm{sno}\exists\mathrm{sd}\exists\mathrm{sa}(\mathrm{S}\big(\mathrm{sno},~\mathrm{sn},~\mathrm{sd},~\mathrm{sa}\big)\land(\mathrm{sa}>18))\rightarrow\mathrm{S}^{\prime}(\mathrm{sn})
$$
其中前件表示查询操作要求，后件$S^{\prime}(\mathrm{sn})$则表示查询结果。关系演算在数据库及知识库系统中具体应用可参阅数据库专业教材，不再赘述。  

## § 5.6 习 题 <abd> 

1.已知集合$A=\{a,b\}$，$B=\{1,\!2,\!3\}$，求：  
$$
\mathrm{A\timesB,\;\;B\times A,\;\;A\times A,\;\;B\times B,\;\;(A\times B)\cap(B\times A)}
$$
2.  设A是$\mathsf{n}$ 元集合，证明：（1）A上有$2^{n}$个一元关系；（2）A上有$2^{n^{2}}$个二元关系。  

3.设$\mathrm{A}=\{1,\!2,\!4,\!6\}$，试列出下列关系R,  
$$
\mathrm{R}=\{\langle x,y\rangle|x,y\in A\Lambda x+y\neq2\};\;\;(\mathrm{\scriptsize~(~2~)~}\mathrm{~R}=\{\langle x,y\rangle|x,y\in A\Lambda|x-y|=1\};
$$
$\mathsf{R}=\Big\{\langle x,y\rangle\Big|x,y\in A\Lambda\frac{x}{y}\in A\Big\};$；（4）$\mathsf{R}=\left\{\langle x,y\rangle\big|x,y\in A\Lambda y\right\}$为素数}  

4. $R_{i}$是集合$\cdot X$上二元关系，对$\forall x\in X$定义集合$R_{i}(x)=\{y|x R_{i}y\}$，显然$R_{i}(x)\subseteq X$.如果$\mathrm{X=}$$\{-4,-3,-2,-1,0,1,2,3,4\}$，且令：  
$$
R_{1}=\{\langle x,y\rangle|x,y\in X\Lambda x<y\};\ \ \ \ R_{2}=\{\langle x,y\rangle|x,y\in X\Lambda y-1<x<y+2\}
$$
求 $R_{1}(0)\,,\,\,\,R_{1}(1)\,,\,\,\,R_{2}(0)\,,\,\,\,R_{2}(-1)\,.$  

5. 设$\mathbf{A}=\{0,\!1,\!2,\!3,\!4,\!5\}$，$B=\{1,\!2,\!3\}$，用列举法描述下列关系，求出关系图及关系矩阵。  

$R_{1}=\{\langle x,y\rangle|x\in A\cap B\land y\in A\cap B\};\;\;(\,2\,)\;\;R_{2}=\{\langle x,y\rangle|x\in A\land y\in B\land x=y^{2}\};$ （3）$R_{3}=\{\langle x,y\rangle|x\in A\Lambda y\in A\land x+y=5\}$； $R_{4}=\{\langle x,y\rangle|x\in A\land y\in A\land\exists k(x=k\cdot y\land k\in N\land k<2)\}.$  

6.设$A=\{1,\!2,\!3,\!4,\!5,\!6\}$，定义𝐴上二元关系$R=\{\langle x,y\rangle|(x-y)^{2}\in A\}$$S=\big\{\langle x,y\rangle\big|y$是$x$倍数}$T=\big\{\langle x,y\rangle\big|x\big|y$是素数}.写出$R,S,T$ 的元素，并画出$R,S,T$的关系图。  

7. 设$H=\{a,b,c\}$是3 个不同姓的同班同学的集合，  

（1）给出$H$上全域关系、空关系、恒等关系的含义解释； （2）确定$H$上的一个关系，指出该关系的定义域、值域和域。  

8.图5-21 是$A=\{1,\!2,\!3,\!4,\!5,\!6\}$上关系$R$的关系图，依据该图写出R的元素及关系矩阵。  

![](images/eeb2cd62eb27954d00a142b4288c6eb079d966dbc9da66cc39e12a85fc8312e4.jpg)  
图5-21 第8 题图  

9. 设 $A=\{\langle1,\!2\rangle,\langle2,\!4\rangle,\langle3,\!3\rangle\}$ ， $B=\{\langle1,3\rangle,\langle2,4\rangle,\langle4,2\rangle\}$ ，求 $A\cap B$ ， $A\cup B$ ， dom𝐴 ， dom𝐵 ran𝐴，ran𝐵，$\operatorname{dom}(A\cup B)$，ran(𝐴∩𝐵)，$A\circ B$。  

10. 设$\mathcal{R}_{1}=\{\langle0,1\rangle,\langle1,2\rangle,\langle3,4\rangle\}$，求$R_{2}$使得$\cdot R_{1}\circ R_{2}=\{\langle1,3\rangle,\langle1,4\rangle,\langle3,3\rangle\}.$且$\{R_{2}\}$最小。一般地，若给定$R_{1}$和$R_{1}\circ R_{2}$，则$R_{2}$能被确定吗？使得$|R_{2}|$最小的$R_{2}$能确定吗？ 11.设$N=\{0,1,2,\cdots\}$,关系$S=\{\langle x,x^{2}\rangle|x\in N\}$和$T=\{\langle x,2x\rangle|x\in N\}$,求$R\cup S$与$R\cap S$。 12.设$A=\{1,\!2,\!3,\!4\},\,R$和$S$都是𝐴上二元关系：$R=\{\langle1,2\rangle,\langle3,4\rangle,\langle2,2\rangle\},\mathrm{A}=\{\langle4,2\rangle,\langle2,3\rangle,\langle3,1\rangle\}.$试求$R\circ S$, $S\circ R$, $R\circ(\ S\circ R)$, $(\mathrm{\boldmath~}R\circ S)\circ R,R^{2},$$S^{2}$, $R^{3}$的关系矩阵，并分别画出关系图。13.设A是整数集合，确定下列合成关系$R\circ S$：  
$$
R=\{\langle x,y\rangle|x,y\in A\land y=2x-1\};\,\ S=\{\langle x,y\rangle|x,y\in A\land y=x+3\};
$$
$R=\{\langle x,y\rangle|x,y\in A\land y=x-4\};\;\;S=\{\langle x,y\rangle|x,y\in A\land y=x^{2}+3x+1\};$ $R=\{\langle x,y\rangle|x,y\in A\land y=2^{x}\};\,\ S=\{\langle x,y\rangle|x,y\in A\land x=2^{y}\};$ $R=\{\langle x,y\rangle|x,y\in A\land y=2^{x}\};\,\ S=\{\langle x,y\rangle|x,y\in A\land y=x^{2}\};$ $R=\{\langle x,y\rangle|x,y\in A\land y=x-7\};\;\;S=\{\langle x,y\rangle|x,y\in A\land y=x^{2}+x+1\};$ $R=\{\langle x,y\rangle|x,y\in A\land x y\leq100\};\,\,\,S=\{\langle x,y\rangle|x,y\in A\land x y\leq5\}.$ 14. 设$A=\{0,1,2,3\}$，$R$和𝑆是𝐴上的二元关系，$R=\big\{\langle i,j\rangle\big|(j=i+1)$或$(j=i/2)$； $S=\{\langle i,j\rangle|(i=j+2)\}.

$  

（1）用关系矩阵求$R\circ S$；（2）用关系图求$S\circ R$；（3）用任意方法求$R\circ S\circ R,R^{3},S^{3}

$  

15.集合 $A=\{a,b,c,d,e,f,g,h\}$上关系$R$的关系图如图5-22 所示，求最小正整数$m$和$n,$满足 $m<n$ 且 $R^{m}=R^{n}$ 。  

![](images/fa239e0013bda9ded803cf5a2e6aff292e389c3ab26d166423ee0f7d3776568b.jpg)  
图5-22 第16 题图  

16. 设 $A=\{1,\!2,\!3,\!4\}$ ,  $M_{R}={\left(\begin{array}{l l l}{0}&{0}&{0}\\ {0}&{0}&{0}\\ {1}&{1}&{0}\\ {0}&{0}&{1}\end{array}\right)},$ 求 $M_{R^{n}}$ ,     $n\in N

$  

17. 确定以下二元关系是否满足自反性、反自反性、对称性、反对称性、非对称性、传递性：  

（1） {(2,2), (2,3), (2,4), (3,2), (3,3), (3,4)} ； （2） {(1,1),(1,2),(2,1),(2,2),(3,3),(4,4)}  

 （3）{(2,4), (4,2)}；（4）{(1,2),(2,3),(3,4)} 

（5） {(1,1), (2,2), (3,3), (4,4)} ； （6） {(1,3),(1,4),(2,3),(2,4),(3,1),(3,4)}  

18.确定下列整数集合上关系$R$是否为自反、反自反、对称、反对称、非对称：  

（1）$x\neq y$；（2）$x y\ge1$；（3）$x=y+1$或$x=y-1$；（4）$x\equiv y({\bmod{7}})

$  

（5）$x$是𝑦的倍数；（6）$x$与𝑦或者都是负的，或者都是非负的；（7）$x=y^{2}$；（8）$x\geq y^{2}$。

19.设集合$A=\{1,\!2,\!3,\!4,\!6,\!12\}$上的整除关系记为$R$，求逆关系$R^{-1}$及$R$的关系矩阵，说明逆关系$R^{-1}$的属性。  

20.设$\cdot A=\{a,b,c\}$,以下分别给出一个$P(A)$上的二元关系，确定它们哪些是自反的、反自反的、对称的、反对称的、非对称的、传递的。  

（1）$x$和𝑦是一个真子集，$R_{1}=\{(x,y)|x\subset y,x,y\in P(A)\}.

$（2）$x$与𝑦不相交，$R_{2}=\{(x,y)|x\cap y=\emptyset,x,y\in P(A)\}.$。 $x\cup y=A,\ \ R_{3}=\{(x,y)|x\cup y=A,x,y\in P(A)\}.

$  

21.设$\therefore A=\{a,b,c\}$,请分别给出集合𝐴中的关系$R$使它具有下列性质之一：  

（1）既是对称又是反对称；（2）既不是对称又不是反对称； 

（3）既是自反又是传递；（4）既不是自反又不是传递。  

22.设$\cdot R$、𝑆是A 中的两个二元关系，  

（1）若$R$、$S$是自反的，试证：$R\cup S,$, $R\cap S$也是自反的； 

（2）若𝑅、$S$是对称的、传递的，试证： $R\cap S$也是对称的、传递的.𝑅∪S亦是吗？为什么？  

23.设集合$|A|=3$,试计算𝐴上具有对称性和反对称性的关系的个数。  

24.设𝑅、$S$是集合𝐴上的关系，试证明或否定以下论断：  

（1）若$R$、$S$是自反的，则$R\circ S$是自反的； 

（2）若$R$、$S$是反自反的，则$R\circ S$是反自反的； 

（3）若$R$、$S$是对称的，则$R\circ S$是对称的；  

（4）若$R$、$S$是反对称的，则$R\circ S$是反对称的； 

（5）若$R$、$S$是传递的，则$R\circ S$是传递的。 

25. 设$A=\{1,\!2,\!3,\!4\}$上的二元关系 $R=\{(1,\!2)$,(2,1),(3,1),(4,3)}： 

（1）说明$R$不传递；（2）求$R$的自反闭包、对称闭包和传递闭包。 

26.设$A=\{a,b,c,d,e\}$, $A$中关系$R$定义为$R=\{\langle a,b\rangle,\langle b,c\rangle,\langle c,d\rangle,\langle d,e\rangle\}$,试求${\mathfrak{t}}(R)

$27.找出图5-23 中每个关系的自反、对称和传递闭包。  

![](images/80b3e5714866c0dd97bef0e6c7e075037850b7abf623e092cdae327c50c3a8bf.jpg)  

28.设$\cdot R$是$A=\{1,\!2,\!3,\!4\}$上的二元关系，其关系矩阵是$\begin{array}{r}{\boldsymbol{\cdot}M_{R}=\left(\begin{array}{l l l l}{0}&{1}&{0}&{0}&{0}\\ {1}&{0}&{1}&{0}&{0}\\ {0}&{0}&{0}&{1}&{0}\\ {0}&{1}&{0}&{0}&{1}\end{array}\right)\!,}\end{array}$  

试求：（1）$M_{r(R)}$；（2）$M_{s(R)}$；（3）$M_{R^{2}}$、$M_{R^{3}}$、$M_{R^{4}}$和$M_{t(R)}

$  

29.设${\bf\nabla}^{\perp}R_{1}$和$R_{2}$是集合𝐴中的两个二元关系,且$R_{1}\supseteq R_{2}$.试证：  
$$
\operatorname{r}(R_{1})\supseteq\operatorname{r}(R_{2});{\mathrm{~\bf~(~2~)~}}\boldsymbol{s}(R_{1})\supseteq\operatorname{s}(R_{2});{\mathrm{~\bf~(~3~)~}}\operatorname{t}(R_{1})\supseteq\operatorname{t}(R_{2})\,\mathrm{{\bf~(~2~)~}}\,\operatorname{\bf~(~3~)~}
$$

30.令${\bf\nabla}^{\cdot}R_{1}$和$R_{2}$是集合$\cdot A$中的两个二元关系，证明以下命题：（1）$\mathrm{r}(R_{1}\cup R_{2})=\mathrm{r}(R_{1})\cup\mathrm{r}(R_{2})$$\mathrm{s}(R_{1}\cup R_{2})=\mathrm{s}(R_{1})\cup\mathrm{s}(R_{2});~\mathrm{(\,3\,)}~\mathrm{t}(R_{1}\cup R_{2})\supseteq\mathrm{t}(R_{1})\cup\mathrm{t}(R_{2})\,\mathrm{.}

$  

31.设$\cdot R$是集合$A$上的关系，证明或否定下述论断。  

（1）若$R$是自反的，则$s(R)$, ${\mathfrak{t}}(R)$是自反的；（2）若$R$是对称的，则$\mathbf{r}(R)$, ${\mathfrak{t}}(R)$是对称的； 

（3）若$R$是传递的，则$\mathbf{r}(R)$, $s(R)$是传递的；（4）若$R$是反对称的，则 ${\mathfrak{t}}(R)$是反对称的。  