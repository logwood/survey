
1. 主线已经确定：不是方法细节，而是 D → K → Learning Paradigms

你这章最重要的不是去穷举各种方法定义，而是把整套具身学习讲成一条清楚的链条：

𝐷
𝑖
D
i
	​

：数据生态 / dataset tier

𝐾
𝑖
K
i
	​

：由数据生态所支撑的 effective knowledge support

Learning paradigms：处理 
𝐷
D、内化 
𝐾
K、并把它显化为能力的模型形式

所以真正的主语始终是：

系统如何从 
𝐷
D 中获得并内化 
𝐾
K。

而不是：

某个具体 encoder

某个 tokenization

某个 diffusion / flow

某个 output abstraction

这些都只是 means, not ends。

2. K 的定义现在非常清楚了

你给出的定义比我们一开始讨论的更严格：

𝐷
𝑖
D
i
	​

 是数据层级

𝐾
𝑖
K
i
	​

 不是简单的数据标签，而是
由该数据层级所诱导出的 effective knowledge support

也就是说：

𝐷
1
→
𝐾
1
D
1
	​

→K
1
	​


𝐷
2
→
𝐾
2
D
2
	​

→K
2
	​


𝐷
3
→
𝐾
3
D
3
	​

→K
3
	​


所以 K 不是方法类别，也不是表格里的某个附属标签，而是：

学习系统在该层级数据下真正可获得的知识支持层级。

这也解释了为什么：

K 不该塞进 Sub-direction

K 应该保持为一条干净的底层支持轴

3. K1 / K2 / K3 的真正功能含义已经想通了
𝐾
1
K
1
	​


核心是 local interaction support

支撑局部接触、几何关系、短时控制

对应 skill-level learning

让系统学会“在这里怎么动、怎么接触、怎么执行局部操作”

金句可以是：

𝐾
1
K
1
	​

 supports learning at the level of local interaction.

𝐾
2
K
2
	​


核心是 task-structure support

支撑 skill composition

支撑 temporally extended execution

让系统学会“这些局部交互怎么串起来形成任务”

金句可以是：

𝐾
2
K
2
	​

 supports learning at the level of temporally extended task execution.

𝐾
3
K
3
	​


这是你后来最关键的顿悟点。

它不是“更大一点的数据”而已，而是：

使能力能够稳定跨 embodiment 迁移的那一级 support

也就是说：

如果目标机械臂不在已有 embodiment 范围里

但系统仍要稳定地产生该机械臂的能力

那它真正缺的不是技巧，而是 
𝐾
3
K
3
	​

-level support

所以 K3 的必要性最清楚地体现在：

当系统需要超出单一 embodiment 的局部/任务数据覆盖范围，仍维持稳定能力时。

金句可以是：

𝐾
3
K
3
	​

 supports learning at the level of cross-embodiment transferable capability.

或者更强一点：

The necessity of 
𝐾
3
K
3
	​

 becomes most evident when stable capability must transfer beyond the embodiment space directly represented in local interaction or task-level data.

4. B / P 的角色已经明确
B = Brain / Cognitive Planning

负责把 semantic intent 变成 structured planning artifacts

输出的是中间抽象：

code

reward

task plan

affordance map

constraint

future prediction

latent world state

所以 B 的本质不是直接输出 motor command，而是：

给 action 提供可执行的中间组织形式。

P = Policy / Embodied Cerebellum

负责把观测映射成动作

输出的是 action 本身，或 action tokens/chunks/denoised actions 等低层控制变量

所以 P 的本质是：

把已知 support 直接参数化为可执行控制。

5. affordance 的归属：更适合放在 B，不是 P

这点我们也想清楚了。

如果一个方法输出的是：

heatmap

mask

SE(3) pose proposal

value map

keypoints

grasp candidates

spatial constraint

然后还要经过：

grasp planner

motion planner

trajectory optimization

skill API

才能变成实际电机命令，

那它在你的 taxonomy 里更像 Brain，不是 Policy。

所以可以明确立场：

affordance-oriented methods belong to B because they produce action-relevant intermediate abstractions rather than motor commands themselves.

6. 为什么 B / P 表里要保留 K，但不把 K 塞进 sub-direction

我们后来达成的共识是：

B/P 是功能范式

Sub-direction 是技术路线

K 是这些路线主要依赖的 knowledge support 层级

所以 K 更像是：

orthogonal support axis

不是 sub-direction 的组成部分。

把 K 塞进 sub-direction 会有两个坏处：

技术路线和知识层级混在一起

taxonomy 失去干净性

所以最好的写法不是：

Task-level Program Synthesis

K3 Grounding

Skill-level Diffusion

而是：

保留原 sub-direction

再用一句总结说明它主要由哪一级 K 支撑

7. 不是所有类都需要硬配单一 K；有些类更适合写“内部关键分化”

这个 insight 也很重要。

对于内部相对一致的类，可以直接写共同特点和主 K：

B1

B2

P2

例如：

B1 primarily supported by 
𝐾
2
K
2
	​


B2 primarily supported by 
𝐾
2
K
2
	​


P2 mainly task-scale, thus 
𝐾
2
K
2
	​

, unless扩到generalist才更接近 
𝐾
3
K
3
	​


但对于内部确实有明显分化的类，不适合硬压一个 K，而更适合解释分化点：

B3

B4

B5

P1

P3

即：

B3：explicit vs implicit grounding

B4：local interaction grounding vs higher-level constraint reasoning

B5：task-conditioned future prediction vs latent world simulation

P1：local reactive control vs task-conditioned/chunked/recovery-aware policy

P3：local generative control vs generalist generative learning

这个写法比“每一小项生硬绑定一个 K”更成熟。

8. 你真正的理论立场：paradigm 的 object 始终是 K

这是我们后来最核心的本体论收束。

不是说：

learning paradigm 把 K “转化”成能力

而是说：

K 本来就作为可学习对象存在；learning paradigm 只是通过特定模型形式，把 K 的某些部分显化、组织并读出。

所以：

Sub-direction

Output Abstraction

Modeling

Execution Gap

各种 representation / parameterization

都不是独立知识本体，

而是：

𝐾
K 的底层支持结构在不同模型形式中的外显方式。

所以最适合你的表述不是：

they introduce independent knowledge categories

而是：

they are paradigm-level manifestations of the underlying support structure of 
𝐾
K.

9. architecture 的作用：不是创造 K，而是显化 K

这个也定下来了。

架构不是知识本体，它的作用是：

读出 K

组织 K

参数化 K

显化 K

把 K 变成可调用的 planning/action interface

所以更准确地说：

Architecture does not define the existence of knowledge support; it defines the form through which that support is exposed and used.

10. exogenous priors 不是重点，不要让它抢主线

这个我们最后也收住了。

你一开始纠结：

exogenous priors 算不算 learning paradigm

backbone 算不算外源知识

接入模型后还算不算模型的一部分

最后其实都变成了次要问题。

因为你的主线不是：

prior 哲学

backbone 定义

外源/内源元区分

而是：

大多数能力差异首先来自 
𝐾
K 提供了什么支持；learning paradigm 决定模型如何去内化、组织、参数化这些支持。

所以对 exogenous priors 的最稳处理方式是：

轻轻承认它们存在

但不作为主分类轴展开

只在必要时说明某些 paradigms 会带入额外先验

一句最合适的边界说明是：

Our focus here is on the endogenous support induced by 
𝐾
K, rather than on auxiliary exogenous priors that some models may additionally incorporate.

11. 具身本体（embodiment）的位置：不是主语，而是 constraint

这个补充也很关键。

你后来意识到：

learning object 不是 embodiment 本身

但 embodiment 绝对不能忽略

更准确的定位是：

Embodiment defines the feasible space within which learned support can be realized.

也就是：

𝐾
K 决定能学到什么

paradigm 决定怎么学、怎么显化

embodiment 决定最终什么是 physically realizable

所以一句最适合内部记忆的话是：

K decides what can be learned, paradigm decides how it is learned, and embodiment decides what is physically realizable.

12. 数据空间与能力边界：能超出样本，不能稳定超出本体

这个 insight 也非常好。

我们后来讲清楚了：

数据本身采样自某个具身可行空间

所以 
𝐾
K 也被限制在这个空间里

学习可以：

插值

组合

局部外推

但不能从根本上超出具身本体定义的 feasible space

一句最好的总结是：

Learning may generalize within the feasible embodiment space, but cannot fundamentally transcend it.

或者更短：

It may exceed samples, but not embodiment.

13. 为什么 K3 在这里不可替代

这个是整个讨论里最重要的顿悟。

你提出的问题是：

一个从来没有某个机械臂相关 support 的模型，能不能稳定地产生这个机械臂的稳定能力？

最后我们得到的答案是：

如果没有该机械臂相关数据

没有跨 embodiment 抽象

没有足够的共享结构支撑

那它就不能稳定地产生这个机械臂的能力。

而这恰恰说明：

K3 的功能，不是简单的“foundation scale”，而是支撑跨 embodiment 稳定能力。

这让 K3 从一个抽象层级，变成了一个功能上不可替代的支撑级别。

14. 你最后真正确定下来的总原则

把刚才所有 insight 压成一句话，其实就是：

What varies across learning paradigms is not the ultimate learning object, which remains the knowledge support 
𝐾
K induced by data, but the model-level means by which that support is internalized, organized, and expressed under embodiment constraints.

中文可以写成：

不同 learning paradigms 真正变化的，并不是最终学习对象；最终学习对象始终是由数据所诱导的知识支持 
𝐾
K。变化的是模型在具身约束下如何将这种支持内化、组织并显化出来。

15. 你现在可以放心忽略的“废话区”

这些不是主线，可以在正文里轻轻带过，不必深究：

exogenous priors 到底算不算 paradigm

architectural parameterization 是否包含 backbone

外源知识接进模型后还算不算外源

某个 encoder 具体算 representation 还是 prior

因为这些都已经被降级为：

实现层或边界层问题，而不是主叙事。
