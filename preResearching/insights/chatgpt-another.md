# ChatGPT Chat Log

为我找一些综述种的Principles and Preliminaries，这个一定要有吗？

---

我先帮你查两件事：一是哪些综述确实用了 “Principles and Preliminaries” 这类章节名，二是它在综述里是不是硬性必需。

---

我已经找到不少真实综述里用了 “Preliminaries / Background and Preliminaries / mathematical preliminaries” 这类章节名。接下来我补一条更关键的依据：有没有哪个规范要求综述必须写这一节。

---

不一定要有。

综述并没有一个统一硬性规定，要求必须单独设一个叫 “Principles and Preliminaries” 的章节。像 MDPI 的作者模板就明确说，review papers 的结构更灵活；FEBS 的写作建议也只是把综述的宽框架概括为 引言 + 主体部分 + 总结/展望，子标题应按内容需要来定。
MDPI
+1

但它很常见，尤其是在技术综述里。比如：

A Survey on Prompting Techniques in LLMs 明确有 “II. PRELIMINARIES”；
arXiv

A Survey of Financial AI 说明第 2 节用于建立 mathematical preliminaries and notations；
arXiv

A Survey of Mamba 也说会先回顾基础知识 as preliminaries；
arXiv
+1

一篇 embodied AI 综述同样直接设置了 “2 PRELIMINARIES”。
arXiv

所以更准确地说：

要不要有这一节，取决于你的综述是否需要先“垫一层共同背景”。
通常在下面几种情况下，建议保留：

后文要用很多符号、定义、任务设定；

读者不一定都是本领域专家；

你要先统一 taxonomy、problem setup、evaluation protocol。

如果你的综述本身比较短、读者就是领域内同行、基础概念很少，那么这部分完全可以并进 Introduction，或者改成更自然的标题，比如：

Background

Preliminaries

Background and Preliminaries

Problem Setup and Notation

Foundations / Fundamentals

另外，“Principles and Preliminaries” 这个标题本身并不是固定模板。我查到的真实综述里，更常见的是 Preliminaries / Background and Preliminaries / Mathematical Preliminaries，而不是非得写成这个组合。这个结论是基于上面的实际论文样例做的归纳。
arXiv
+2
arXiv
+2

你如果是在写一篇综述，我的建议是：

偏理论/方法型综述：保留，通常很有帮助；

偏应用盘点型综述：可弱化，甚至合并到引言；

标题优先用 Background and Preliminaries，一般比 Principles and Preliminaries 更自然。

把你的目录贴给我，我可以直接帮你判断这节该不该留，以及该叫什么更合适。

---

3727640.pdf
PDF
为我讲讲这篇综述

---

可以。这篇综述的核心价值，不只是“列举了有哪些后门/木马攻击”，而是把 Trojan attacks（也可理解为 DNN backdoor / 木马攻击）按模型全生命周期重写了一遍：训练阶段、后训练阶段、推理/部署阶段分别怎么攻击；这些攻击和 poisoning、adversarial example、bit-flip 三类经典攻击是什么关系；以及现有防御到底能防到什么程度。作者还强调，这篇文章的重点比很多旧综述更偏向 countermeasures（检测与消除） 及其实用效果。

3727640

如果我用一句话概括：
这是一篇“以生命周期为主线、以防御为重点”的 Trojan 攻击综述。 它认为 DNN 在安全关键场景里之所以容易遭受 Trojan 威胁，一方面来自模型规模大、冗余高、可解释性差，另一方面来自开放数据集、第三方预训练模型、MLaaS 平台这些外部生态；而 Trojan 攻击之所以特别危险，是因为它隐蔽、持久，而且能在特定触发条件下精确地让模型做错事。

3727640

这篇文章的第一个重要贡献，是它把 Trojan 攻击放进了一个很清楚的三阶段框架里。作者把攻击分成：
训练阶段的 Trojan，多数通过 数据投毒 把 trigger 学进模型；
后训练阶段的 Trojan，多数通过 微调模型或修改参数/结构 建立 trigger 和内部神经元/权重的联系；
推理/部署阶段的 Trojan，则主要依赖 bit-flipping，也就是所谓 Bit-Trojan。这也是这篇综述标题里 “from Life-Cycle Perspective” 最实质的内容。

3727640

 

3727640

第二个重要贡献，是作者没有把 “Trojan attack” 当成一个孤立概念，而是专门解释了它和三类相关攻击的关系：
poisoning attack 给了 Trojan 在训练阶段的基本思路；
adversarial example attack 给了 Trojan 更隐蔽的 trigger 设计方法；
bit-flip attack 则让 Trojan 能在推理阶段落地，形成更隐蔽的 Bit-Trojan。这个关系梳理得很好，因为它解释了为什么很多 Trojan 技术看起来像“杂交物种”。

3727640

第三个重要贡献，是它的分类做得比较细。训练阶段里，作者把数据投毒型 Trojan 又细分成 sticky trigger 和 optimized trigger；优化型 trigger 下面又分成随机扰动、像素级编码、风格迁移/样本重构等路线；同时还区分了 label-inconsistent 和 label-consistent 两种攻击范式。后训练阶段则分成 模型结构型 和 模型参数型；推理阶段重点就是 Bit-Trojan，并且介绍了它的典型两步框架：先生成 trigger，再搜索要翻转的目标 bit。

3727640

这篇综述还挺有价值的一点，是它没有只停留在传统 CNN/CV 语境。作者往外扩展到了 ViT、SNN、NLP、transfer learning、model distillation、GNN、知识产权保护/水印 等方向。比如它提到 ViT 的强注意力机制会更容易聚焦 trigger，因此可能更脆弱；也提到 SNN 在对抗样本上可能更稳健，但对 Trojan 并不一定更安全，甚至可能更脆弱。这个部分说明作者是在努力把 Trojan 问题从“CV 里的局部问题”提升成“更广义的模型安全问题”。

3727640

防御部分是这篇文章最值得读的地方。作者把防御拆成两大块：
一块是 Trojan detection，即怎么发现数据集或模型被动了手脚；
另一块是 Trojan elimination，即发现之后怎么去除。
检测又按数据、模型参数/结构、输出三类来分；消除又分成数据预处理、重训练、微调、知识蒸馏、unlearning、mode connectivity、pruning 等路线。这个框架很适合拿来当你自己写 related work 或 survey 的骨架。

3727640

 

3727640

作者对现有防御的判断并不乐观。它明确指出：
现有方法对 code poisoning-based Trojan 和 Bit-Trojan 的防御仍然比较薄弱；
在消除方法里，retraining 和 fine-tuning 仍然是最有效的主流路线，但 fine-tuning 会遇到 样本太少时无效 和 catastrophic forgetting 两个典型问题；
另外，许多现有方法仍然缺少真正到 神经元级/权重级解释 的能力。也就是说，今天很多防御是“能测出不对劲”，但离“知道哪里坏了、为什么坏、怎样最低代价修复”还有距离。

3727640

 

3727640

如果你问我，这篇综述最强的地方是什么，我会说有三个。
第一，结构特别清楚，非常适合入门和搭框架。
第二，防御部分覆盖得比很多旧综述更完整。
第三，它确实把 Trojan 攻击放进了更大的安全脉络里，而不是只堆论文。

3727640

 

3727640

它的局限也很明显。作者自己就承认，虽然文章会涉及 NLP、GNN、SNN 等其他方向，但 主要关注点还是 CV 任务；另外，很多结论更像“结构性归纳”和“方法地图”，而不是严格统一基准下的定量比较。换句话说，这篇文章更适合回答“这个领域长什么样”，不太适合直接回答“哪种方法绝对最好”。

3727640

 

3727640

你前面问过 “Principles and Preliminaries 这一节是不是一定要有”，这篇文章其实就是一个很好的例子。它的第 2 节不是空话，而是在做四件事：
定义技术术语；
说明 Trojan 的本质是“通过权重变化让模型对特定 trigger 高响应”；
给出高风险场景/威胁模型；
解释它和 poisoning、adversarial example、bit-flip 的关系。
所以这里的 “Principles and Preliminaries” 不是模板式摆设，而是为后面的 taxonomy 和 defenses 搭共同语境。

3727640

 

3727640

如果你是为了读论文、写综述或开题，我会这样用这篇文章：先读引言和 Figure 1，把生命周期框架吃透；再读 Section 2，把术语、威胁模型和与相关攻击的关系理顺；然后重点看 Section 3.5 的比较和 Section 4 的防御分类；最后看未来方向，因为作者明确提到今后的重点会落在 code poisoning、DyNN、模型可解释性、更系统的主动防御平台，以及针对 Bit-Trojan 的软硬件协同防御。

3727640

 

3727640

你要是愿意，我下一步可以直接继续帮你做两种事里的一个：
一是把这篇综述按“论文汇报”格式给你整理成 5 分钟中文讲稿；
二是专门把它的 Section 2: Principles and Preliminaries 拆开细讲。

---

survey.pdf
PDF
这篇讲了什么呢？

---

这篇主要是在讲：

机器人手臂的 embodied manipulation（具身操作）这个方向，到底应该怎么系统地理解。
它不是单纯按“某个模型家族”来综述，而是把整个问题拆成四个互相耦合的层面：硬件具身/系统架构、数据生态、学习范式、评测体系。作者认为，只有把这四部分放在一起看，才能真正解释为什么一个操作系统能不能学得会、迁得动、落得下去。

survey

 

survey

更具体地说，这篇综述有三个核心贡献。
第一，它提出了一个分层的数据视角，把 manipulation 数据分成 skill-level、task-level、foundation-level 三层，并讨论这些数据是怎么采集、合成、清洗和流水线化生产的。第二，它把学习过程拆成 cognitive planning 和 policy learning 两条路径，也就是“高层认知规划”和“低层动作策略”。第三，它把 embodied manipulation 看成一个系统级设计问题，分析 embodiment、data、learning、deployment、evaluation 是怎么相互制约的。

survey

你可以把它理解成这样：

1. 它先讲“机器人本体长什么样”

第 2 节先从 physical embodiment 讲起：末端执行器、固定基座、双臂、移动机械臂、类人平台，这些硬件差异会直接决定机器人能感知什么、能控制什么、能执行什么。作者还强调，接触丰富操作里，视觉不够，触觉/力觉很重要。例如插入、重抓取、脆弱物体处理，很多关键信息其实来自接触状态。

survey

它还补了一层软件栈：内核层、通信层、系统层。也就是说，具身智能不是只有模型，底层实时性、ROS 2/DDS、零拷贝数据流、边云协同这些工程因素，也会反过来影响 manipulation 是否能稳定运行。

survey

2. 然后讲“数据怎么支撑操作学习”

这篇文章非常重视数据，不像很多综述只按模型分类。作者认为 manipulation 的核心瓶颈之一就是：什么数据可用、这些数据怎么来、质量怎么样、能不能跨 embodiment 复用。

survey

它把数据分成三层：

Skill-level datasets：偏局部技能，比如抓取、推、铰接物体开合、装配。这里能看到数据从 2D grasp rectangle，发展到 6-DoF grasp、灵巧手抓取，以及非抓取操作。

survey

Task-level datasets：偏指令驱动和长时程轨迹，比如从 BC-Z、RT-1 到 DROID，逐渐提升语言监督、场景多样性和标定质量。

survey

Foundation-level datasets：偏跨平台聚合，比如 OXE、ARIO、AgiBot World，目标是支撑跨机器人、跨模态、跨任务迁移。

survey

接着它还系统讨论了数据从哪来：
真实世界采集、仿真生态（MuJoCo / SAPIEN / Isaac 等）、自动数据生成、数据增强、失败恢复数据、数据筛选与重加权，以及大规模数据 pipeline。第 3 节其实不只是“列数据集”，而是在讲机器人数据生产体系。

survey

3. 核心部分是“学习范式怎么分”

第 4 节是整篇最核心的地方。作者把学习分成两部分：

Cognitive planning（embodied brain）
负责把高层任务意图变成可以执行的中间表示。它分成五类：

语义逻辑/代码生成

长时程任务分解

grounded multimodal representation

几何 grounding 与空间智能

generative dynamics / physical imagination

也就是从“直接产出代码/奖励/行为树”，到“分解子任务”，再到“输出 affordance、SE(3) 位姿、3D 表征、未来动态预测”等不同规划接口。

survey

Policy learning（embodied cerebellum）
负责把观测变成动作。作者把策略分成三类：

P1 显式连续动作策略：一次前向直接回归连续动作，快，但容易平均化；

P2 离散动作策略：把动作 token 化，自回归生成，表达力更强，但推理延迟更高；

P3 迭代生成策略：扩散/流匹配这类方法，分布建模能力最强，但计算也最重。

survey

这部分的价值在于，它不是简单说“VLA、RL、Diffusion 各有什么论文”，而是告诉你：不同方法本质上在用不同的动作表示和不同的中间规划接口。这比按模型名字分更有解释力。

survey

4. 它还讲了“系统怎么集成、怎么部署”

作者继续往下拆，分析 planning 和 policy 怎么组合成完整系统。它分成三类 integration model：

Type I：统一端到端 foundation model

Type II：分层/模块化推理系统

Type III：基于空间表征或 world model 的共享世界状态系统 

survey

然后又讲 deployment pipeline，分成三阶段：

offline pre-deployment

online physical alignment

inference-time execution

也就是说，模型不是训练完就完了，还要考虑 sim-to-real、跨 embodiment 对齐、压缩、量化、在线适配、边缘部署等现实问题。

survey

5. 最后讲“怎么评测，以及现在还卡在哪里”

第 5 节把评测分成四个面向：

task execution quality

data efficiency & quality

generalization & transfer

energy / efficiency evaluation

作者特别指出，现有评测虽然越来越细，但还是不够统一，很多 benchmark 仍然偏单臂桌面场景，真实世界复现实验也很难标准化。

survey

第 6 节则总结了六类开放问题：

Embodiment：传感模态仍然窄，跨平台差异很大；

Data：高质量真实数据少，异构数据难对齐；

Learning：没有统一最优范式，不同设计取舍复杂；

Deployment：预部署、在线适配、推理执行三阶段目标常常互相冲突；

Evaluation：现有 benchmark 对真实能力覆盖不够；

Trustworthiness：高层模型和低层控制都存在鲁棒性与安全性问题。

survey

 

survey

 

survey

所以如果用一句更凝练的话概括，这篇综述想表达的是：

机器人操作能力不是“换个更大的模型”就能解决的，它本质上是一个由 embodiment、data、learning、deployment、evaluation 共同决定的系统问题。 文章最后也明确说，具身操作不能只按模型家族来理解，而要看这些层之间的依赖关系。

survey

如果你是为了读论文或写 related work，这篇最值得你抓住的是这条主线：

硬件具身 → 数据生态 → 学习范式 → 集成与部署 → 评测与可信性

这比单纯背一串 VLA / diffusion / world model 的论文更有用。

你要的话，我下一条可以直接帮你做一个更适合汇报的版本：
“3分钟讲清这篇综述”。

---

你认为这两篇哪个主线更清晰

---

我主观上会选 第一篇（Trojan Attacks and Countermeasures…）主线更清晰。

3727640

原因很简单：

第一篇从标题开始就把主线钉死了：from Life-Cycle Perspective。它基本就是沿着一条单轴往下走：
Trojan attack 是什么 → 在训练/后训练/推理三个生命周期阶段怎么发生 → 对应有哪些防御 → 还有哪些挑战。
这个组织方式非常直，读者很容易抓住“作者到底想讲什么”。而且文中也明确写了：Section 2 讲 principles and preliminaries，Section 3 讲不同生命周期阶段的 Trojan taxonomy，Section 4 讲 countermeasures，Section 5 讲 challenges and future directions。这个线性推进感很强。

3727640

相比之下，第二篇 Embodied Manipulation for Robotic Arms 更像一篇框架型、系统型综述。它不是围绕一个单主轴展开，而是同时铺四条线：
system architecture、data ecosystem、learning paradigms、evaluation。
作者自己也强调，它想把 manipulation intelligence 放在四个维度下统一理解，并进一步拆成数据三层、学习双路径、三类集成架构、四类评测轴。这样做很全面，但天然会让“单一主线感”弱一些。

survey

所以如果你的标准是：

读起来一条线很顺

章节之间推进关系非常明确

适合拿来学“综述主线怎么立”

那第一篇更清晰。

3727640

但如果你的标准是：

想搭一个大框架

想把 embodiment、data、learning、deployment、evaluation 全串起来

更重视系统全景而不是单主轴叙事

那第二篇其实更强，只是它的主线不是“单线推进”，而是“多维框架展开”。

survey

我会这样下结论：

第一篇胜在“主线清楚”；第二篇胜在“框架完整”。
如果你现在是在学“综述怎么写得更像一篇有主线的 survey”，我更建议你参考第一篇。
如果你是在搭自己论文的总框架，第二篇更有启发。

3727640

 

survey

你要的话，我可以下一条直接帮你把这两篇的主线结构并排拆开，告诉你哪种写法更适合你现在这篇。

---

那哪篇说明更清晰

---

如果说的是 “概念有没有讲明白、读起来是不是更顺”，我还是会选 第一篇 Trojan 那篇。它一上来就把目标讲得很直白：按 training / post-training / inference 三个生命周期阶段来讲 Trojan attack，同时补上与 poisoning、adversarial examples、bit-flip 的关系，再系统讲 countermeasures。随后它马上进入 Principles and Preliminaries，先定义 Trojan information、clean model、trigger、poisoned sample 这些关键术语，再按阶段解释 Trojan injection 是怎么发生的。这个解释路径很线性，也很适合读者建立基本概念。

3727640

 

3727640

第二篇 Embodied Manipulation 不是不清楚，而是它更像一篇框架型综述。它自己就说要同时从四个维度组织内容：三层数据体系、认知规划/策略学习双路径、三类集成架构、四类评测轴；后面又把 planning 拆成 B1–B5，把 policy learning 拆成 P1–P3。这样做很系统，但读者需要同时跟住很多坐标轴，所以“说明感”会比第一篇弱一点，尤其对第一次读这个方向的人来说。

survey

 

3727640

 

survey

所以我的判断是：

说明更清晰：第一篇。
框架更大、更系统：第二篇。

如果你现在在学“综述里怎么把一个概念讲清楚”，更值得模仿第一篇。
如果你在学“怎么搭一个覆盖 embodiment–data–learning–deployment–evaluation 的大框架”，第二篇更值得参考。

---

哪篇工作量更大

---

我会倾向于说：第二篇《Embodied Manipulation for Robotic Arms》工作量更大。 

survey

理由不是它页数更长。两篇其实篇幅接近：第一篇是 37 pages，第二篇是 35 pages，单看页数分不出明显差距。

3727640

 

survey

我之所以更偏第二篇，是因为它的覆盖面和组织成本更高。它同时要梳理：

硬件具身与软件栈，

数据生态（数据集、采集、合成、精炼、pipeline），

学习范式（cognitive planning、policy learning、integration、deployment），

评测体系，

最后再收束到 open challenges。
这类综述不是只做一个主题纵深，而是在多个维度上同时搭框架，资料收集、分类设计、术语统一、表格整理的工作量通常更大。

survey

第一篇 Trojan 那篇的工作量也不小，而且它在单一主题深挖上很扎实：要把 Trojan attack 按生命周期重构，还要讲清和 poisoning / adversarial example / bit-flip 的关系，再系统总结 detection 和 elimination。这个是聚焦型重整，深度很强。

3727640

所以更准确地说：

按“调研广度、材料整合、框架搭建”的外显工作量看：第二篇更大。 

survey

按“围绕一个核心安全问题做深度重构和防御分析”的专题难度看：第一篇也非常重。 

3727640

我的最终判断还是：
第二篇更像“大工程型综述”，第一篇更像“深挖型综述”。
如果只问“哪篇工作量更大”，我投第二篇。

---

哪篇语句构词更成熟？

---

如果你说的是 英文写作里的“语句组织 + 用词成熟度”，我会选 第二篇《Embodied Manipulation for Robotic Arms》更成熟一些。

survey

我的判断依据主要有三点。

第一，第二篇的抽象层级控制得更稳。
它的摘要一开始就把领域背景、问题张力、文章框架和贡献范围压缩得很自然，比如连续用了 “broadened the design space”、“analyze embodiment, data, learning, integration, and evaluation together”、“recurring design pressures” 这类表达，既是学术英语里很成熟的概括句法，也没有明显的堆词感。后面的贡献段落也用非常整齐的并列句展开，读起来像是经过较多打磨的 journal prose。

survey

第二，第二篇的段落推进更像成熟综述写法。
例如引言后半段，它先指出已有综述的不足，再提出自己的组织框架，接着用 “This survey therefore organizes…”、“Contributions:”、“Structure of the Paper:” 依次推进，过渡非常顺；到正文里也能看到很多很成熟的 topic sentence，比如 “The action space of a robotic system is constrained by its hardware embodiment.”、“Together, hardware embodiment and the software stack define…”，这种句子既准又稳。

survey

第三，第一篇更清楚直接，但语言上略偏“能说明白”而不是“很老练”。
Trojan 那篇的优点是非常直给，主线推进也更线性；但从英语表达到“成熟度”来看，它有一些更明显的模板化和重复感，比如摘要和引言里连续使用 “On the one hand… On the other hand…”、“This article presents…”、“Furthermore…” 这类较常规的连接方式。它的术语定义部分很清楚，但也更像技术说明文，语言张力和节奏感不如第二篇自然。

3727640

所以我会给你一个更细的结论：

如果比“写得成熟、学术英语更老练”：第二篇更强。

survey

如果比“讲得直白、主线更容易跟”：第一篇更强。

3727640

换句话说：

第一篇胜在清楚，第二篇胜在文气和笔法。

你如果是在学英文综述写作，我会建议：

学 第一篇 的主线组织；

学 第二篇 的句式和用词控制。

---

第一篇文章的4.2.2 讲了什么

---

第一篇的 4.2.2 讲的是 Model Weight-based Elimination，也就是：
从模型权重层面去消除 Trojan 信息，核心做法主要是 retraining（重训练） 和 fine-tuning（微调）。作者把它看成“在模型层面修恶意权重”，而不是像 4.2.1 那样只在输入端做预处理。

3727640

它先讲 retraining。
作者认为，重训练是一种比较直接而且通用的方式：用 clean data 重新训练 Trojaned model，让原来藏在恶意权重里的 Trojan information 在训练过程中被压制。文中还强调，虽然它看起来像从头训练，但通常不需要那么多样本，因此收敛会更快、成本也低于完全重训。

3727640

然后它介绍了一个重训练增强方案 MESA。
这个方法不会直接盲目重训，而是先去估计 trigger distribution，再做模型恢复。它通过多个 sub-model 去逼近未知触发器分布，把随机噪声当成潜在 trigger 输入到 Trojaned model 和 sub-model 中，再根据输出和 trigger 的熵来更新生成器和子模型。最后，对识别出的目标类分别训练多个 sub-model，做重训练去除 Trojan，再从中挑效果最好的模型。

3727640

接着它讲 fine-tuning。
作者说，重训练虽然有效，但时间和算力开销大，所以可以只对一小部分权重做微调，而且只用少量 clean data。文中举的例子是：Ji 等人的方法不是微调整个模型，而是只微调 convolutional layers，希望用干净样本把和 Trojan 相关的风险压下去。

3727640

再往下，4.2.2 还讲了一种更“定点修复”的 fine-tuning 思路。
Zhao 等人的方法先找出误分类样本中的关键区域，再构造 companion sample，通过差分特征分析定位导致错误输出的特征，也就是 trigger pattern；接着计算哪些神经元对这些特征贡献最大，把它们识别成 error-inducing neurons。最后对这些神经元做两种处理：
一种是 neuron flipping，直接把符号反转，破坏错误输出；
另一种是 neuron fine-tuning，用额外训练样本去调这些神经元，阻断 Trojan 传播。

3727640

 

3727640

但作者并没有把 fine-tuning 说得很乐观，而是明确指出它有两个典型问题：
第一是 Ineffectiveness，也就是当 clean dataset 太小时，微调常常不够有效；而且 Trojaned model 本来就已经把目标攻击学得很稳了，所以少量 clean sample 很难真正破坏 Trojan functionality。
第二是 Catastrophic Forgetting，因为微调依赖的数据太少，容易在修 Trojan 的同时损伤模型原本能力。

3727640

正因为有这两个问题，4.2.2 后半段又顺势引出三类改进路线：
knowledge distillation、mode connectivity、unlearning。

其中 knowledge distillation 分两类：
一类是 data-based KD，先从 Trojaned model 中筛出正确分类的 clean sample，蒸馏出新模型；也有工作先用蒸馏模型和 Trojaned model 联合过滤 latent poisoned samples，再在清洗后的数据上 fine-tune，以避开前面提到的两个问题。
另一类是 feature map / attention-based KD，例如 NAD、ARGD 这种，通过对齐 teacher 和 student 的 attention/feature 关系，让 student 更接近 clean model。

Mode connectivity 的思路是：
把一个经过 clean sample 微调的模型和另一个 Trojaned model 通过低损失路径连接起来，在保持两者相似性的同时，逐步把其中的 malicious weights 消掉。文中把它描述成一种也能对抗错误注入和规避攻击的消除方式。

3727640

Unlearning 则更像“反向抹除”。
一类方法先恢复 trigger pattern，再用基于 gradient ascent 的 unlearning 去擦除 Trojaned information；另一类则把 Trojan elimination 直接形式化成与攻击优化目标相反的 minimax 问题，本质上把“注入 Trojan”的过程反着做一遍。

3727640

所以你可以把 4.2.2 总结成一句话：

它讨论的是：如何不靠输入端处理，而是直接在模型权重层面对 Trojan 动手，主要手段是重训练和微调；但由于微调会遇到“效果不足”和“灾难性遗忘”，于是又发展出蒸馏、模式连通、反学习这些更高级的权重级消除方法。

你要的话，我下一条可以直接把 4.2.2 的逻辑结构画成一个很清楚的中文树状图。

---

case study是吧，挑一个典型？

---

对，有一点这个意思，但更准确地说：

4.2.2 不是“单个 case study”，而是“按一条技术路线，挑几个代表性方法来讲”。

3727640

这一小节的写法其实是：

先给出一个总类目
Model Weight-based Elimination，也就是“从模型权重层面清除 Trojan”。

3727640

然后在这个总类目下面，选几种典型路线来展开：

Retraining：重新用 clean data 压制恶意权重；

MESA：先估计 trigger distribution，再做恢复；

Fine-tuning：只调一部分权重，降低成本；

再进一步引出 knowledge distillation / mode connectivity / unlearning 这些改进办法。

3727640

所以它更像是：

总论点 → 典型方案 A → 典型方案 B → 该路线的问题 → 后续改进方案

而不是那种传统意义上“拿一篇论文当 case study 从头讲到尾”。

你要是借鉴这种写法，可以这样理解：

小节标题定一条主线，比如“weight-based elimination”

正文里挑 2 到 4 个最有代表性的方法

每个方法只讲它的核心机制，不必把所有论文平铺

最后再总结这条路线的共性问题和演化方向

所以你说“挑一个典型”，可以，但我会建议你稍微扩成：

挑一个主代表 + 再带两个后续变体，

这样会比只讲一个 case 更像综述写法，也更接近这篇 4.2.2 的组织方式。

3727640

你要的话，我可以直接把 4.2.2 的写法模板 给你抽出来，变成你自己综述里能直接套的段落骨架。

---

为什么另一篇文章的小节内容似乎也没有那么多那么长，但是篇幅似乎跟这个比也差不特别多

---

对，因为篇幅不是只由“小节正文有多长”决定的。

你看到第二篇有些小节单独拿出来不算特别长，但它整体页数还是接近第一篇，主要是因为它的“占页方式”不一样。最主要有四个原因。

第一，第二篇是多维框架型综述，横向铺得很开。
它不是沿一条主线往下讲，而是同时展开 system architecture、data ecosystem、learning paradigms、evaluation 四大块；作者还明确把内容再细分成 三层数据体系、planning/policy 双路径、三类 integration model、三阶段 deployment、四类 evaluation。这种写法的特点就是：每个子节未必写得很深，但子节数量多、覆盖面广、转换成本高，总页数自然会上去。

survey

 

survey

第二，第二篇吃了很多“表格页”和“框架图页”。
你可以直接看到它有不少大块版面被 taxonomy figure 和综述型表格占掉了。比如：

第 3 页整块是总 taxonomy 图；

survey

第 5 页有完整的三层软件架构表；

survey

第 7、8、9、10 页连续出现大表：skill-level datasets、task-level datasets、foundation-level datasets、simulation infrastructures；

survey

 

survey

第 16、18、19、20、21、23 页附近又有 learning taxonomy、policy taxonomy、integration patterns、deployment bottlenecks、evaluation metrics 等表格。

survey

 

survey

 

survey

也就是说，第二篇很多篇幅不是“某个小节正文特别长”，而是被大图、大表、分类框架占据了。

第三，第二篇每个小节都在做“定义 + 分类 + 举例 + 比较”。
例如它在数据部分，不只是说“有哪些数据集”，而是先提出三层数据 regime，再分别列代表性数据集、采集方式、仿真生态、数据增强、数据 pipeline；在学习部分，也不是直接罗列模型，而是先定义 cognitive planning 与 policy learning，再把 planning 拆成 B1–B5，把 policy learning 拆成 P1–P3，再继续讲 integration 和 deployment。这样的写法会让单个自然段看起来不长，但每个子节都有自己的结构负担。

survey

 

survey

 

survey

第四，第一篇和第二篇的“页数来源”其实不一样。
第一篇更像“深挖型综述”，主轴很集中：lifecycle 下的 attack taxonomy + defense，它的页数更多来自围绕同一主题做纵深展开。文中也明确说，Section 2 是 principles and preliminaries，Section 3 是按生命周期的 attack taxonomy，Section 4 是 countermeasures，Section 5 是 challenges。

3727640

 

3727640


第二篇则更像“系统工程型综述”，它的页数更多来自框架铺陈、横向并列、表格化整理。所以你会感觉“单个小节好像没写很长”，但总页数并不小。

survey

再加一个很直观的事实：两篇本来页数就接近，第一篇是 37 pages，第二篇是 35 pages。差距其实只有 2 页，本来就不算大。

3727640

 

survey

所以一句话总结：

第一篇的篇幅主要来自“围绕一条主线深入讲”；第二篇的篇幅主要来自“框架广、子类多、图表密”。
你看起来觉得第二篇“小节不长”，是因为它把很多信息压进了分类图、对比表、taxonomy 和结构过渡里，而不是全部写成连续长段落。

如果你在想怎么写自己的综述，这里其实有个很有用的判断标准：
长篇幅不一定靠长段落，也可以靠“框架密度”。

---

你认为他们各自的做法是合理的吗？有更优的办法吗？

---

我觉得 两篇的做法都合理，只是它们在解决不同类型的综述问题，所以“最优结构”也不一样。

第一篇 Trojan 那篇的做法是合理的。
它从一开始就把文章目标限定为 life-cycle perspective：训练、后训练、推理/部署三个阶段；随后再按这个顺序展开 attack taxonomy，最后统一讲 detection / elimination，再讨论 challenges。也就是说，它的主轴不是“模型家族”，而是“攻击发生在生命周期的哪一段”。对 Trojan 这种安全问题，这个主轴天然成立，因为不同阶段的攻击入口、威胁模型、触发条件和防御手段都不一样，文章自己也明确按这个顺序组织了 Section 2–5。

3727640

 

3727640

而且这条主线不是装饰性的。它后面真的把不同阶段的攻击优缺点分开比较：训练阶段更通用，后训练和推理阶段更隐蔽但更依赖高权限；防御部分也按 detection / elimination 两步来收束，并进一步比较不同方法在各阶段的有效性与局限。也就是说，它的目录和它的比较表是互相支撑的，不是“标题写生命周期，正文却按论文堆”。

3727640

 

3727640

 

3727640

但第一篇也不是最优到不能改。
我觉得它最大的可优化点是：attack 和 defense 被切成了两个大块。读者读完 Section 3 记住的是训练/后训练/推理三阶段攻击，到了 Section 4 又要重新切换到 detection/elimination 两种防御逻辑。这样会有一点“先按时间轴讲问题，再按功能轴讲解决方案”的坐标切换。对初学者来说，容易在脑子里做两次重组。

3727640

 

3727640

所以如果我要改第一篇，我会用一个嵌套式版本：
每个生命周期阶段下面固定回答四个问题：
“攻击面是什么 → 代表性方法有哪些 → 当前防御能防到什么程度 → 这一阶段还有什么空白”。
然后最后再单独放一个 cross-stage 的总比较表。这样会比“先全讲攻击、再全讲防御”更贴近读者的阅读路径。

第二篇 Embodied Manipulation 那篇的做法也合理。
因为它自己就在引言里说了，现有综述常按 model family 去组织，但这会掩盖 manipulation 里真正重要的差别，比如 planning artifact、action representation、system integration；所以它故意把文章重组为 data regimes、cognitive planning、policy learning、integration architectures，并把 embodiment、deployment、evaluation 一起拉进来。这个动机本身是成立的。

survey

它后面的结构也严格执行了这个设计：
Section 2 讲 embodiment 和 software infrastructure；
Section 3 讲数据生态，从 dataset 到 acquisition、refinement、pipeline；
Section 4 讲 planning、policy、integration、deployment；
Section 5 讲 evaluation；
Section 6 讲 open challenges。

survey

更关键的是，它并不是乱铺四条线，而是在文章内部反复强调一条系统论逻辑：hardware embodiment 和 software stack 定义了系统约束，这些约束又决定了需要什么数据；数据再支撑 learning；learning 再落到 deployment 和 evaluation。第 3 页的总 taxonomy 图和第 6 页从“system architecture”过渡到“data ecosystem”的文字，其实都在强化这种“约束向下传导”的关系。

survey

 

3727640

但第二篇的问题也很明显：
它同时引入了 四个大维度，再往下拆成 三层数据、双路径学习、三类集成、四类评测，信息架构非常强，但“单一主线”会被削弱。你读它时，脑子里需要同时维护很多坐标轴。它很适合搭全景图，不一定最适合第一次入门。

survey

 

survey

所以如果我要改第二篇，我会让它更“单主线化”一点。最自然的办法是把整篇改写成：

Embodiment constraints → Data regime → Learning design → Deployment trade-off → Evaluation

也就是把它现在隐含的因果链，直接提升为显式主轴。
这样一来，data / planning / policy / integration / evaluation 仍然都能保留，但它们不再是并列大块，而是围绕一个核心问题展开：
机器人身体和接口的差异，如何一步步传导成数据需求、学习选择、部署代价和评测标准。

所以我的判断是：

第一篇的结构，对它那个题目是合理而且高效的。
因为 Trojan 本来就是一个适合按生命周期和防御链条来组织的专题。

3727640

第二篇的结构，对它那个题目也是合理的。
因为 embodied manipulation 本来就是系统级问题，单靠“按模型家族分类”确实不够。

survey

但如果问“有没有更优办法”，我的答案是：

第一篇最优改法：用“按阶段嵌套 attack–defense–gap”的写法，减少坐标切换。

第二篇最优改法：保留多维框架，但把“embodiment constraints 向下传导”变成唯一显式主线，弱化平行并列感。

一句话总结：

第一篇更像“纵向专题综述”的优解，第二篇更像“横向系统综述”的强解；真要更优，应该把第一篇做得更局部闭环，把第二篇做得更单线驱动。

你要的话，我可以下一条直接给你写一个 “两篇综述结构的改写方案对照表”。

---

看起来你认为第二篇的优化空间更大

---

对，从“结构还能怎么再收紧”这个角度看，我确实认为第二篇的优化空间更大一些。第二篇一开始就主动把问题铺成多维框架：数据分层、planning/policy 双路径、integration architectures、evaluation，再加上 embodiment 和 deployment 一起讨论；这当然很完整，但也意味着它天然更容易出现“框架很强、单线感稍弱”的情况。

survey

 

survey

不过这不是说第二篇写得差，而是说它的目标更难。它想解决的不是单一专题，而是一个系统级问题，所以目录本身就是并列展开的：Section 2 讲 embodiment 和软件栈，Section 3 讲数据生态，Section 4 讲 learning / integration / deployment，Section 5 再讲 evaluation。这样的组织法信息量大、覆盖全，但也更依赖作者把这些块之间的因果关系讲得非常显。

survey

 

survey

第一篇则相反，它的题目和结构几乎是天然贴合的。作者明确把文章锚定在 life-cycle perspective：训练、后训练、推理三个阶段；接着按这个轴展开 Trojan taxonomy，再统一讲 detection / elimination 和 practical effectiveness。这个组织方式和问题本身高度同构，所以结构上的“松动空间”更小。

3727640

 

3727640

所以更准确地说：

第一篇像是“已经比较接近它这个题目的结构优解”。

第二篇不是不合理，而是因为它承担了更多并行维度，所以更有进一步压缩成单主线的空间。

3727640

 

survey

我会把这个“优化空间”具体理解成两点：

第一，第二篇可以把现在隐含的主线再显式一点。
它其实已经有一条潜在线索：embodiment 约束 → 数据需求 → learning design → deployment trade-off → evaluation。这条线在文中是存在的，但目前更多是“框架之间的关联”，还不是完全压过并列目录的唯一主轴。

survey

第二，第二篇可以进一步减少“分类的分类”。
比如它在 learning 部分继续拆成 B1–B5、P1–P3，再接 integration 和 deployment，这在学术上很完整，但阅读上会提高坐标切换成本。也正因为如此，它在后面自己总结 open challenges 时，又不得不回到 embodiment、data、learning、deployment、evaluation、trustworthiness 六个大面向重新收束。这个现象本身就说明：它的内容非常丰富，但收束难度也更高。

survey

 

survey

所以我的最终判断是：

是的，我认为第二篇的优化空间更大。
但这是一种“高上限但更难收”的大框架优化空间，不是“结构不行”。
第一篇更像已经收紧的专题综述，第二篇更像还可以继续压缩主线的系统综述。

---

你能再找找其他的这两种风格的综述吗？

---

可以。我按你刚才那个标准来分：

第一类：专题主线型
围绕一个核心问题一路往下讲，常见结构是“定义/边界 → taxonomy → 代表方法 → 局限/挑战”。

第二类：系统框架型
不是只抓一个问题，而是把多个维度一起搭起来，常见结构是“数据/模型/系统/评测/部署”并行展开。

下面这些我觉得都比较像。

1）更像第一篇那种“专题主线型”的综述

1. Interactive Imitation Learning in Robotics: A Survey
这篇很像“围绕一个窄主题做纵深重构”的写法。它的对象就是 Interactive Imitation Learning (IIL)，摘要里先说明 IIL 是什么、为什么重要，然后强调这篇综述的任务是把这个方向的 terminology、structure、applicability 统一起来；目录也明显是围绕这个单主题推进的，比如 theoretical background、interaction modalities、behavior representations、interfaces、benchmarks、research challenges。这个“单主题持续推进”的味道很像你说的第一篇。 
CRIS
+1

2. Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning
这篇也偏“主线型”。它抓住的是 safe learning in robotics 这个中心问题，摘要里明确说要统一 control theory 和 reinforcement learning 两边的语言与框架，然后依次讨论 learning-based control、safe/robust RL、formal certification，再收束到 benchmarks 和 open challenges。它不是四处铺开，而是始终围绕“机器人学习怎么保证安全”这条线。 
Annual Reviews

3. A Survey of Active Learning for Natural Language Processing
这篇虽然不在机器人或安全领域，但写法很典型：先锁定 AL for NLP 这个单问题，再往下拆成 query strategies、structured prediction、annotation cost、starting/stopping AL、future directions。它的摘要里就明确说，目标是给出 NLP-specific 的 AL 综述，而不是泛泛谈 active learning。这个也是很标准的“专题型综述”写法。 
arXiv

4. Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations
如果你想找一个更贴近 Trojan 那篇安全写法的例子，这篇很值得看。NIST 这份报告明确按 ML method types、lifecycle stages of attack、attacker goals/capabilities、mitigations、open challenges 来搭 taxonomy，本质上也是围绕一个核心问题——AML——来做统一术语、攻击分类和缓解路线梳理。它比一般 survey 更像“标准化综述/框架报告”，但结构气质非常接近第一篇。 
NIST Computer Security Resource Center
+1

2）更像第二篇那种“系统框架型”的综述

1. Foundation Models in Robotics: Applications, Challenges, and the Future
这篇很像第二篇。它不是只讲某一种模型，而是从 robot autonomy stack 的多个部分切入：perception、decision-making、control，再统一讨论 data scarcity、safety、uncertainty、real-time execution 等挑战。也就是说，它天然是“多维系统视角”，而不是“单轴主题视角”。 
Sage Journals

2. Human Motion Trajectory Prediction: A Survey
这篇也偏框架型。摘要和引言都说得很清楚：它一方面按 motion modeling approaches 分类，另一方面又按 contextual cues 分类，同时还专门讲 datasets、performance metrics、open challenges。也就是说，它不是单线往下讲，而是多个维度交叉组织，这一点很像第二篇。 
arXiv
+1

3. Video Question Answering: Datasets, Algorithms and Challenges
标题就已经很“第二类”了：datasets + algorithms + challenges。摘要里也明确先分数据集，再分技术路线，再抽 common insights，最后讲 research trends。它是典型的“把任务、数据、算法、趋势一起搭成框架”的综述，而不是只抓一个单点问题做深挖。 
arXiv
+1

4. Embodied AI with Foundation Models for Mobile Service Robots: A Systematic Review
这篇和你第二篇在气质上最接近。它把 foundation models 放进 mobile service robotics 这个系统场景里，围绕 自然语言到动作、multimodal perception、uncertainty、real-time deployment 四个核心挑战组织内容，再往下接 real-world applications、ethics、societal/HRI、physical design。这就是很标准的“系统全景图式综述”。 
MDPI

如果你是想“对照着学写法”

我会这样建议：

想学第一篇那种写法，优先看这两篇：

Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations：最接近安全问题里的“taxonomy + mitigation + lifecycle”写法。 
NIST Computer Security Resource Center
+1

Interactive Imitation Learning in Robotics: A Survey：单主题、纵深推进感很强。 
CRIS
+1

想学第二篇那种写法，优先看这两篇：

Foundation Models in Robotics: Applications, Challenges, and the Future：最像“从系统栈拆开讲”。 
Sage Journals

Embodied AI with Foundation Models for Mobile Service Robots: A Systematic Review：最像“把任务、能力、部署、伦理一起纳入”。 
MDPI

我自己的判断是：

第一类最像的关键词：single-topic, taxonomy, attacks/mitigations, design choices, challenges。 
CRIS
+1

第二类最像的关键词：datasets, architectures, applications, deployment, evaluation, challenges。 
Sage Journals
+2
MDPI
+2

你要的话，我可以下一条直接把这些文献再筛成一个更实用的版本：“最值得精读的 2+2 篇，并告诉你各自该学什么”。

---

你看看这两篇文章对于优缺点以及可以体现作者性的地方的对比

---

可以。我把“作者性”理解为：作者在选题、结构、分类方式、表达习惯和价值取向上，最能暴露其写作人格的部分。按这个标准看，这两篇的差别其实很鲜明。第一篇把自己定义为一篇 life-cycle perspective 的 Trojan 安全综述，强调训练、后训练、推理三个阶段，并且把重点放在 countermeasures 和实际防御效果上；第二篇则明确反对只按 model family 组织 manipulation 综述，而是主动提出一个四维框架：数据分层、planning/policy 双路径、integration architectures、evaluation axes，并把 embodiment、deployment 一起纳入。光看作者在引言里如何定义自己的文章，气质就已经很不同了。

3727640

 

survey

先说优点对比。

第一篇的优点，是“专题抓得很牢，推进很直”。它从摘要到引言都反复强调同一件事：Trojan attack 要按生命周期理解，而且要把它与 poisoning、adversarial examples、bit-flip 的关系讲清，再把防御放进来做 practical effectiveness 的比较。正文结构也严格执行这个承诺：先 principles and preliminaries，再 lifecycle taxonomy，再 detection/elimination 与 effectiveness，最后 challenges。对读者来说，进入门槛低，逻辑路径单一，读完后会很容易记住主轴。

3727640

第二篇的优点，是“框架搭得更大、更系统”。它不是只讲某类模型，而是把 robotic manipulation 视为一个 coupled design problem：embodiment 会影响数据接口和控制接口，数据 regime 又影响 learning 和 integration，deployment 与 evaluation 也必须联动考察。它在引言里就把这种系统论立场讲得很明白，后面又用 Fig. 1、Fig. 3 等总图把 system architecture、data ecosystem、architectural paradigms、evaluation 串起来，这种能力很强。

survey

再说缺点对比。

第一篇的缺点，不是写得乱，而是“太稳了，所以有点保守”。它的结构高效，但也比较传统：先 attack，再 defense，再 challenges。这样做的代价是，读者脑中要完成一次坐标切换——第 3 节按生命周期理解攻击，第 4 节又按 detection/elimination 理解防御。文章自己在后面也需要再用表格把不同 detection/elimination 方法的 advantage / disadvantage 以及 black-box/white-box、runtime feasibility、不同 stage effectiveness 重新收束，说明前面的两条轴线并不是天然重合的。

3727640

 

3727640

另外，第一篇虽然也提到 ViT、SNN、NLP 等扩展方向，但文中明确说 主要还是聚焦 CV 里的 Trojan attacks，因为这部分“most rapidly evolving and mature”。这使它的专题性更强，但也让它的外延略收。

3727640

第二篇的缺点，则恰好来自它的雄心：维度太多。它一上来就同时引入四个大维度，再往下拆成三层数据、五类 cognitive planning、三类 policy learning、三类 integration、三阶段 deployment、四类 evaluation。这个框架很强，但阅读负担也会明显上升。你可以从总 taxonomy 图直接看出这一点：这篇不是单主线推到底，而是多条并行坐标一起展开。对已经熟悉领域的人，这很有价值；对第一次读的人，容易觉得“信息很满，但需要自己再二次整理”。

survey

还有一个更细的缺点是：第二篇虽然不断强调“coupled design problem”，但真正的阅读体验仍然更像 并列式大框架，而不是一条完全压住其他维度的单主线。作者在第 6 节又把挑战重新收束为 embodiment、data、learning、deployment、evaluation、trustworthiness 六类，这恰恰说明文章很完整，但收束难度也更高。

survey

下面说你最关心的：哪些地方最能体现作者性。

第一篇最显作者性的地方，我觉得有四个。

第一，它很强烈地表现出一种安全研究者的“威胁面—攻击面—防御面”思维。文章不是只列攻击论文，而是先定义 technical terms，再 formalize Trojan injection 的本质，再列高风险场景和 threat models。这说明作者很在意“攻击成立的条件是什么”，而不仅是“谁做过什么方法”。

3727640

第二，它很明显偏好专题重构。作者不是按数据投毒/后门种类随手分类，而是刻意重写为 training / post-training / inference 三阶段，并且在摘要里强调这是 “the first comprehensive survey … from a life-cycle perspective”。这说明作者有很强的“重排领域叙事”的意识。

3727640

第三，它体现出作者对防御有效性和实用性的执念。引言明确说，相比旧综述，它更关注 countermeasures 及其 practical effectiveness；后面还专门做 advantage/disadvantage 比较表，并讨论哪些方法对 code poisoning 或 Bit-Trojan 无效。也就是说，作者不满足于“整理攻击谱系”，而是更在意“这些防御到底在现实里管不管用”。这很有作者立场。

3727640

 

3727640

第四，它的语言里有一种规范化、说明文式的气质。比如大段 technical terms、scenario definition、method comparison，这类写法说明作者倾向于把复杂问题拆成可以定义、比较、评估的部件。这种“安全+规范化”的写法就是它最强的作者性之一。

3727640

第二篇最显作者性的地方，也有四个。

第一，它有很强的框架建构欲。作者在引言里直接批评按 model family 组织 manipulation 综述会遮蔽 planning artifacts、action representations、system integration 的关键差别，然后主动提出自己的组织方式。这不是单纯写综述，而是在“争夺解释权”：作者要告诉读者，这个领域应该怎么被组织才更合理。这非常有作者性。

survey

第二，它有鲜明的系统工程视角。文章并不把操作学习当成“感知模型+控制模型”的堆叠，而是始终在强调 embodiment、software stack、data acquisition、data refinement、pipeline、deployment、evaluation 的耦合关系。比如第 2 节从硬件具身讲到实时软件栈，第 3 节马上顺着“系统约束定义数据需求”往下推进，这种推导方式很说明作者的系统论偏好。

survey

第三，它特别爱用层级 taxonomy 和接口分解。三层 dataset、B1–B5 的 planning、P1–P3 的 policy、Type I/II/III 的 integration，这些都不是被动总结，而是主动构造出来的分析框架。作者像是在说：这个领域太散了，我先把它做成一张工程地图。你从 Fig. 1、Fig. 3，以及后面 learning paradigms 的图文组织，都能看出来这点。

survey

第四，第二篇的“作者性”还体现在写作姿态更成熟、更抽象。它很少停留在“某模型做了什么”，而更喜欢写“what this component makes practical”“what trade-off it entails”“how these components jointly shape system design”。这种句法习惯说明作者更在意抽象层面的结构关系，而不是单条方法描述。这个气质和第一篇的“技术定义+威胁建模+防御效果”很不一样。

survey

如果把两篇放在一起，我会给你一个更简洁的结论：

第一篇的作者性，更像“安全研究者 + 专题整理者”：
喜欢定义边界、列 threat model、做 attack-defense 对照、关注实用防御效果。

3727640

 

3727640

第二篇的作者性，更像“系统搭框架的人 + 领域解释者”：
喜欢重写领域坐标系、强调耦合关系、构造多层 taxonomy，把 manipulation 解释成一个系统设计问题。

survey

所以如果你问我哪篇“更能看出作者是谁在写”，我反而会说：

第一篇的作者性更体现在问题意识和评价立场上；

第二篇的作者性更体现在框架能力和组织方式上。

一句话压缩：

第一篇像“会打磨专题的人”写的，第二篇像“会搭学科地图的人”写的。

你要的话，我下一条可以直接帮你把这个结论变成一个更适合写在你论文笔记里的版本：
“两篇综述的优缺点—作者性—可借鉴点”三栏式对照。

---

你认为并列式大框架是个很要命的文图吗？

---

你认为并列式大框架是个很要命的问题吗？

---

不算致命问题，但它是个高风险问题。

更准确地说，并列式大框架本身不是错；错的是：
只有框架，没有主导问题；只有分类，没有推导关系。

第二篇这种写法之所以成立，是因为作者不是随便并列几个板块，而是明确提出：manipulation 应该被看成一个 coupled design problem，要把 embodiment、data、learning、integration、deployment、evaluation 一起看。也就是说，它至少试图给这些并列块一个总的解释逻辑。

survey

所以我会这样判断：

并列式大框架不致命，在两种情况下反而是合理的。

第一种，是你的对象本来就是系统级问题。
像第二篇这种 robotic manipulation 综述，如果只按某一条单轴讲，很容易漏掉真正重要的约束传递关系。作者自己就说，现有综述按 model family 组织会遮蔽 planning artifacts、action representations、system integration 的关键差异，所以它才改成多维框架。这个动机是合理的。

survey

第二种，是你能让这些并列块之间有反复回钩的因果链。
第二篇其实一直在暗示这条链：embodiment 约束系统执行 → 系统约束定义数据需求 → 数据支撑 learning → learning 决定 deployment 和 evaluation 的方式。第 2 节末尾就有一句很关键的话：硬件 embodiment 和 software stack 定义了 learned policy 所处的物理与计算约束，而这又塑造了学习所需的数据。说明作者不是简单拼盘。

survey

但它也确实有风险，而且风险不小。

它真正“要命”的时候，通常是下面这种情况：
读者看完整篇，只记住“有很多板块”，却说不出作者到底想证明什么。
也就是说，框架变成了目录管理工具，而不是论证工具。

第二篇离这个风险并不远，因为它同时铺开了 system architecture、data ecosystem、learning paradigms、evaluation metrics，还进一步拆成三层数据、B1–B5、P1–P3、Type I/II/III、三阶段 deployment。这个信息架构很强，但也意味着读者需要一直维护很多坐标轴。

survey

所以我的态度是：

并列式大框架不是“很要命”，但它比单主线写法更考验作者。
单主线综述的问题常常是“会不会太窄”；
并列式综述的问题则是“会不会散、会不会像手册、会不会失去中心论点”。

如果拿你前面那两篇来比：

第一篇的结构风险更低，因为它天然有生命周期主轴；

3727640

第二篇的结构上限更高，但更依赖作者把“并列板块之间的关系”讲出来。

survey

所以我的最终结论是：

不是致命伤，但属于“处理不好就会伤到整篇文章核心说服力”的问题。
它不是不能用，而是必须满足三个条件才稳：

有一个压住全篇的总问题；

各板块之间不是并排摆放，而是能相互解释；

结尾能把这些维度重新收束成一条清楚结论。

第二篇已经做到了一部分，所以我会说它是有风险但可接受，不是“犯了大错”。
只是相比第一篇，它更需要额外的结构打磨。

---

Embodied Intelligence: A Synergy of Morphology, Action,
Perception and Learning

---

这篇我看了下，它不太像第一篇 Trojan 那种“单问题主线型”综述，也不完全像你第二篇那种“系统工程型大框架”综述；
我会把它归成：

“概念统摄型 / 理念框架型综述”，而且偏第二类，但比第二篇更收束一些。

Pasted text

原因很明确。

它在引言里先说，现有 embodied intelligence 综述大致有两类：
一类沿着经典 embodied intelligence 理论线走，另一类更偏最近的机器学习、计算机视觉、基础模型进展；然后作者明确提出，这篇文章要把 embodied intelligence 理解成 morphology、action、perception、learning 四者的 synergy，重点讨论这四个部分之间的连接，并给出一个统一框架。

Pasted text

这说明它的主轴不是：

某一个专题问题，

也不是像你那篇 manipulation survey 那样把系统拆成 data / learning / deployment / evaluation 多层工程模块，

而是一个更高层的核心观念：

“具身智能到底由哪几个基本成分构成，它们之间如何耦合。” 

Pasted text

而且它的文章组织也印证了这一点：
作者说全文是

Section 2：brief history

Section 3：proposed architecture of embodied intelligence

Section 4：research frontiers。

Pasted text

这三个部分其实非常说明风格：

history：先给理论脉络；

architecture：再给统一框架；

frontiers：最后讲前沿与方向。

这不是第一篇那种“定义—taxonomy—defense—challenge”的专题推进法；
也不是第二篇那种“system architecture—data ecosystem—learning paradigms—evaluation”的系统分层法；
它更像是在做一件事：

先立一个大的解释框架，再用这个框架去收编已有研究。 

Pasted text

所以如果你问我它更接近哪种风格，我会这样排：

第一篇 Trojan：专题主线型
这篇 Embodied Intelligence: A Synergy...：概念框架型
第二篇 Embodied Manipulation...：系统工程型框架综述。

Pasted text

 

survey

再说得更细一点：

这篇的优点会是：

站位高；

容易形成作者自己的“解释权”；

适合做领域级概念整理。

Pasted text

它的风险也很明显：

容易偏“理念正确、框架宏大”，但不一定像第一篇那样主线锋利；

也不一定像第二篇那样在 data / deployment / evaluation 上落得很细。
因为它的重心明显是在统一 embodied intelligence 的概念骨架，不是在做一个特别细的系统拆解。

Pasted text

所以我的一句话判断是：

这篇更像“高层理论综述”，不是“问题驱动综述”，也不是“工程系统综述”。
如果你拿它跟前面两篇比，它最突出的特点不是“清楚”或者“铺得全”，而是**“概念统摄力强”**。

Pasted text

如果你愿意，我下一条可以直接帮你把这三篇排成一个表：
专题主线型 vs 概念框架型 vs 系统工程型。

---

那种最吃香?

---

要分开说：

就“更容易被接受”来说：专题主线型最稳。
审稿和编辑通常最看重 review 是否 范围清楚、结构顺、讨论准确且有批判性，而不是某种固定模板。Springer Nature 的审稿指导就明确把 review 的评价重点放在 timeliness、breadth and accuracy、structure and flow、future research avenues 上；Nature Reviews 也强调高质量综述要 timely、objective、balanced、forward-thinking、easy to read。这套标准下，主线清楚的专题综述最不容易失控。
Springer Nature
+1

就“更容易显得高级、影响力更大”来说：概念框架型 / 系统框架型上限更高。
但前提是，你不只是“搭了很多并列板块”，而是真的提出了一个能重组领域理解的框架。Springer 的 conceptual article 方法论里把 theory synthesis、typology、model 这类文章单独拿出来，核心就是它们要提供 新的更高层视角，而不只是盘点文献。最近一篇给综述投稿的编辑建议也直说了：很多 review 虽然形式完整，但因为 按模板堆砌、缺少 conceptual/theoretical contribution，会更容易被 desk reject。
Springer
+1

所以真要给你一个排序，我会这么排：

最稳、最通用：专题主线型
适合大多数综述投稿，尤其你还在建立自己的写作控制力时。

最吃香、但门槛最高：专题主线 + 你自己的框架提升
这其实是最优解：不是纯“列论文”，也不是纯“大拼盘”，而是
一个清楚的问题主线 + 一层作者自己的概念重组/比较框架。
这最符合编辑部对“review 不只是总结，还要教会读者新东西”的期待。
Nature
+2
Springer
+2

最危险：纯并列式大框架
如果没有一个压住全篇的中心问题，这类文章最容易变成“信息很多，但贡献不够聚焦”。审稿标准并不奖励“板块多”，而是奖励“结构有逻辑、判断有提升”。
Springer Nature
+1

所以落到你前面那几种风格：

只选一种最稳的：专题主线型

只选一种上限最高的：概念/系统框架型，但必须真的有框架创新

综合来看最吃香的写法：
第一篇那种清楚主线，外加第二篇那种框架意识，但不要把框架铺得太散

一句话压缩：

审稿最喜欢的，不是“哪种风格”，而是“有清晰边界的主线综述，同时还能给出作者自己的更高层解释框架”。

你要的话，我可以直接把这个结论改写成一个更实用的版本：
“如果你自己要写综述，目录该怎么选”。

---

你分析一下Trojan那篇文章的详细结构

---

可以。我把这篇 Trojan Attacks and Countermeasures on Deep Neural Networks from Life-Cycle Perspective: A Review 的结构，按“表层目录 + 深层推进逻辑 + 每节功能”给你拆开。整体上，它不是普通的“列文献综述”，而是一个很典型的 单主线专题综述：
先定义问题 → 再按生命周期分类攻击 → 再按防御流程分类防御 → 最后做效果比较与研究展望。 这条主线从摘要、引言到正文都很一致。

3727640

 

3727640

一、最外层的大结构

这篇文章的外层结构可以概括成 6 个部分：

1 Introduction
2 Principles and Preliminaries
3 Trojan Attacks against Deep Neural Networks
4 Countermeasures against Trojan Attacks
5 Challenges and Future Research Directions
6 Conclusion 

3727640

 

3727640

不过有一个小细节值得注意：
引言里作者在介绍文章组织时，写的是 “Section 2… Section 3… Section 4… Finally, Section 5 discusses…”；但正文后面实际上还有 Section 6 Conclusion。也就是说，引言里的“文章结构预告”没有把 Conclusion 单独算进去。这不影响理解，但如果你在学写综述，这就是一个可注意的小地方。

3727640

 

3727640

二、这篇文章真正的“骨架主线”

它真正的骨架不是“攻击方法很多，所以分类”，而是：

主线 1：按生命周期组织 Trojan attack

training stage

post-training stage

inference / deployment stage

这是全文最核心的结构轴。作者在引言里就明确说，这篇综述的独特之处是 from a life-cycle perspective，并用 Figure 1 说明不同阶段的攻击入口与高风险场景。

3727640

主线 2：按防御流程组织 countermeasure

detection

elimination

comparison of practical effectiveness

也就是说，第 3 节在回答“攻击怎么发生”，第 4 节在回答“发现后怎么防”。

3727640

所以这篇文章其实是两层结构叠在一起：

上半篇：攻击 taxonomy
下半篇：防御 taxonomy

这也是它读起来很清楚的原因。

三、逐节细拆
1. Introduction：不是铺背景，而是在“立题”

这一节做了四件事：

1）先说为什么 Trojan 值得单独综述

作者先从 DNN 的安全关键应用讲起，再指出 Trojan attack 的特别之处：
它高隐蔽、高危害、可跨模型生命周期持续存在。

3727640

2）提出全文的核心视角：lifecycle

作者强调 Trojan 不是只发生在训练阶段，而是贯穿：

训练阶段：数据投毒

后训练阶段：对开源模型做 Trojan injection

推理/部署阶段：bit-flip 等方式注入 Trojan

Figure 1 本质上是在把“生命周期”可视化。

3727640

3）交代本文相对已有综述的贡献

引言里说得很清楚，这篇比旧综述更强调：

lifecycle 视角

与 poisoning / adversarial example / bit-flip 的关系

countermeasures

practical effectiveness 

3727640

4）预告后文结构

它在这里就把第 2 节、第 3 节、第 4 节、第 5 节各自的任务讲清了。
所以 Introduction 在这篇文章里更像“立题 + 定骨架”，不是简单背景综述。

3727640

2. Principles and Preliminaries：给后文建统一语言

这一节的作用是：
先把后面所有分类和比较所需的公共概念搭起来。

它下面有 4 个子部分：

2.1 Technical Terms

定义核心术语：

Trojan information

clean model

Trojaned model

trigger pattern

clean sample

poisoned sample

这一步很关键，因为作者后面要把各种方法统一到“trigger—sample—weight—model behavior”这组语言上。

3727640

2.2 Principles of Trojan Attacks

这是本节最“理论化”的部分。
作者把 DNN 写成函数组合，再把 Trojan 的本质抽象成：

通过修改权重，让模型对特定 trigger 高响应。

然后进一步把不同阶段的 Trojan injection 写成不同形式：

训练阶段：靠 poisoned data 学进去

后训练阶段：靠 trigger + activation + fine-tuning 建联

推理阶段：靠 bit-flipping 修改量化权重

也就是说，这一小节的功能不是证明复杂数学，而是告诉你：

各种 Trojan attack 表面不同，本质都是“改模型，让 trigger 与目标行为形成强耦合”。 

3727640

2.3 High-risk Scenarios and Threat Models

这一节建立 S1–S4 场景：

S1：开源数据平台

S2：第三方模型市场

S3：智能服务平台

S4：代码仓库与依赖库

这一步很重要，因为后文第 3 节在讲每类攻击时，会不断回指这些 threat model。
也就是说，第 2.3 节起到了“攻击分类的环境锚点”作用。

3727640

2.4 Related Areas of Trojan Attacks

这是个很聪明的过渡节。
作者没有立刻进入 Trojan taxonomy，而是先把 Trojan 与三类相邻攻击连起来：

poisoning attack

adversarial example attack

bit-flip attack

其作用是两层：

说明 Trojan 不是孤立概念；

为后文很多 trigger optimization / Bit-Trojan 方法埋理论来源。

3727640

所以第 2 节的本质不是“背景补充”，而是：
先统一定义、统一威胁模型、统一相邻概念边界。

3. Trojan Attacks against Deep Neural Networks：全文主体之一，按生命周期分攻击

这一节是文章的攻击篇。结构非常规整：

3.1 Trojan Attack at Training Stage

这是第一层生命周期攻击，下面又分成两类：

3.1.1 Data Poisoning-based Trojan Attacks

这里作者重点从两个维度讲：

A. 按 trigger pattern 分

sticky trigger

optimized trigger

random perturbation

pixel-level encoding

transformation

B. 按 label selection 分

label-inconsistent

label-consistent

这说明作者在训练阶段不是简单按论文罗列，而是抓住两个关键设计变量：
trigger 怎么做、label 怎么配。 

3727640

3.1.2 Code Poisoning-based Trojan Attacks

这个子节相当于训练阶段里的“非常规分支”。
它不再通过数据，而是通过代码仓库 / 依赖库污染，也对应前面的 S4 场景。

3727640

所以 3.1 的内部逻辑是：

训练阶段 Trojan = 数据投毒主流 + 代码投毒特例

3.2 Trojan Attack at Post-training Stage

这一节对应“模型已经有了，再去做 Trojan 注入”。

它分两类：

3.2.1 Model Structure-based Trojan Attacks

核心是：
改结构，比如加额外神经元或恶意连接。
这个方向方法不多，因为结构变化更容易被检测。

3727640

3.2.2 Model Parameter-based Trojan Attacks

核心是：
不改结构，改参数或激活行为。
这里又分：

activation-based

weight-based

也就是说，3.2 的内部逻辑是：

后训练 Trojan = 结构级注入 + 参数级注入

这跟训练阶段的“按 trigger/label 分类”不同，说明作者每一阶段都在找最自然的分类变量。

3727640

3.3 Trojan Attack at Inference Stage

这里讲的是部署后 Trojan，主角就是 Bit-Trojan。
作者先介绍基础攻击框架，再拆出三个改进方向：

3.3.1 Improvement in Implementability

聚焦于：
怎么让 bit-flip 更可实施、翻更少 bit。

3.3.2 Improvement in Optimization Objective

聚焦于：
怎么改目标函数，让攻击更高效、翻 bit 更少。

3.3.3 Other Interesting Improvements

聚焦于：
evasiveness、generalizability、攻击目标的其他扩展。

也就是说，3.3 不是按“类型”拆，而是按 Bit-Trojan 研究逐步优化的三个方向 来讲。这个写法有点像一个“小专题中的专题”。

3727640

3.4 Exploration in State-of-the-art Model Structures and Research Fields

这一节相当于“把主线往外扩”。

3.4.1 Advanced Model Structures

比如：

ViT

SNN

3.4.2 Research Fields

比如：

NLP

transfer learning

model distillation

GNN / relationship modeling

watermark / IP protection

这一节的作用不是改变主线，而是说明：

前面的生命周期框架虽然主要针对 CV-DNN，但可以往新模型和其他领域迁移。 

3727640

3.5 Comparison of Different Trojan Attacks

这是第 3 节的收束。
作者在这里用图表和 Table 1 把不同 stage 的 Trojan attack 做统一对比：

threat model

key idea

advantage

disadvantage

这一步很关键，因为前面 3.1–3.4 已经讲得很散了，这里把全节重新压回生命周期主轴上。

3727640

所以第 3 节其实是：

先按 stage 展开

再按 stage 内部最自然的分类变量细分

最后统一对比收束

这是这篇文章最工整的地方之一。

4. Countermeasures against Trojan Attacks：全文主体之二，按防御流程分

这一节是防御篇。
和第 3 节按 lifecycle 不同，这一节改成了按 defense workflow 组织：

4.1 Detection

4.2 Elimination

4.3 Comparison

也就是“先发现，再清除，再比较效果”。

3727640

4.1 Trojan Detection

作者把检测分成三大模块，再加一个补充模块：

4.1.1 Data-based Detection

核心方法：

anomaly detection

trigger inversion

4.1.2 Model Parameter-based Detection

核心是分析：

activation

weights

gradients / parameter statistics

4.1.3 Model Structure-based Detection

核心是：

critical neuron analysis

code auditing

4.1.4 Output-based Detection

核心是：

output distribution

outputs + representation 联合分析

4.1.5 Other Detection Methods

作为收尾，把难以放进前三类的方法归进去。

3727640

所以 4.1 的结构本质上是：

数据入口 → 模型内部 → 输出端 → 杂项补充

这个分类方式很像“从外到内再到输出”的检测视角。

4.2 Trojan Elimination

这一节回答：检测到以后，怎么去除。

它有 3 个子部分：

4.2.1 Input Data-based Mitigation

不直接改模型，而是处理输入：

trigger removal

trigger renovation

trigger destruction

它本质上是“数据侧缓解”。

3727640

4.2.2 Model Weight-based Elimination

这是你前面问过的重点部分。
它从模型权重层面下手，主线是：

retraining

fine-tuning
然后继续扩展到：

knowledge distillation

mode connectivity

unlearning

这部分其实是在讲：
如何通过重训/微调/逆向消除，让恶意权重失效。 

3727640

4.2.3 Model Structure-based Elimination

这一节讲的是 pruning，包括：

neuron pruning

weight pruning

它的特点是直接从结构上把 Trojan 相关神经元或权重剪掉。

3727640

所以 4.2 的结构是：

数据侧缓解 → 权重侧消除 → 结构侧剪除

和 4.1 一样，也是在做从浅到深的处理层级。

4.3 Comparison of Countermeasures

这里是防御篇的总收束。
作者做了两类比较：

Table 2：不同 detection / elimination 方法各自的优缺点

Table 3（文中提到）：从黑盒/白盒、runtime feasibility、是否需要 poisoned data、对不同阶段 Trojan 的实际效果来比较

而且这里不只是总结，还明确指出几个结论：

除输入数据类防御外，多数方法需要白盒访问

现有方法对 code poisoning 和 Bit-Trojan 效果弱

retraining / fine-tuning 虽有效，但成本和局限都明显 

3727640

 

3727640

所以第 4 节不是简单“防御方法综述”，而是一个完整的防御流程：
发现 → 去除 → 比较哪些真有用。

5. Challenges and Future Research Directions

这一节是问题清单 + 研究路线图。
它先列当前主要挑战，例如：

攻击往往要求较高访问权限

跨模型结构迁移性差

DyNN 研究不足

countermeasure 缺少 neuron / weight-level insight

optimized trigger 太隐蔽

Bit-Trojan 防御弱

然后再给未来方向，比如：

code poisoning 值得继续深挖

建 Trojan generation platform

研究 DyNN 安全性

深化 interpretability

做完整的 proactive defense system

开发专门对付 Bit-Trojan 的硬件方案 

3727640

 

3727640

这一节的作用很明确：
把前面 attack 和 defense 两篇内容重新压成“还没解决的关键矛盾”。

6. Conclusion

结论没有引入新东西，而是把全文的四个动作再复述一遍：

重构 Trojan 与 poisoning / AEA / BFA 的关系

总结不同阶段的 Trojan attacks

总结 countermeasures

比较防御 practical effectiveness

提出 limitations 与 future directions 

3727640

这是一种非常标准的 ACM survey 收尾方式：
回顾结构贡献，而不是只重复背景。

四、如果再抽象一层，这篇的“详细结构逻辑”其实是这样

你可以把全文理解成一个 4 步推进：

第一步：先建立公共语言

对应第 2 节。
解决“后面讲这么多方法，到底在同一个什么框架里比较”。

第二步：按生命周期分类攻击

对应第 3 节。
解决“Trojan 在哪里发生、各阶段有什么代表性技术路线”。

第三步：按防御流程分类防御

对应第 4 节。
解决“发现以后怎么处理，哪些方法真有效”。

第四步：把整个领域的短板显式列出

对应第 5 节、第 6 节。
解决“现状哪儿不够、下一步应该往哪儿走”。

五、这篇结构为什么会显得特别清楚

我觉得有三个原因。

1）它始终只有一个总问题

不是“深度学习安全很复杂”，而是：
Trojan attacks across the model lifecycle。

3727640

2）每一层分类都只用一个最自然的变量

大层：按 lifecycle

防御层：按 detection / elimination

训练阶段内部：按 trigger 和 label

后训练阶段内部：按 structure / parameter

推理阶段内部：按 Bit-Trojan 的优化方向

所以虽然层级多，但不乱。

3）每个大节最后都有“收束动作”

3.5 比较不同 Trojan attack

4.3 比较不同 countermeasure

5 总结挑战

6 总结全文

这让文章不会一路散掉。

六、如果你是想“借鉴它来写综述”，最该学的是这个模板

你完全可以把它抽象成一个通用写法：

Section 1：立题 + 贡献 + 结构预告
Section 2：概念、边界、威胁模型、相关概念关系
Section 3：核心对象的 taxonomy（按主轴分类）
Section 4：应对方案 taxonomy（按处理流程分类）
Section 5：比较、局限、未来方向
Section 6：总结

这其实就是它的详细结构精髓。

如果你愿意，我下一条可以继续帮你做一件更实用的事：
把这篇文章的结构直接改写成一个“你自己的综述目录模板”。

---

你分析一下第二篇文章的详细结构

---

可以，这篇第二篇文章的结构，和前面那篇 Trojan survey 很不一样。
如果说第一篇是**“围绕一个安全问题沿主线推进”，那这篇 Embodied Manipulation for Robotic Arms: Embodiment, Data, Learning, and Evaluation 更像一篇系统框架型综述**：它不是按某一种模型家族来排，也不是按单一问题链条来排，而是把“机器人操作智能”拆成几个彼此耦合的维度，再把这些维度重新拼成一个完整系统。作者自己在摘要和引言里就说得很清楚：全文围绕四个维度组织——embodiment、data、learning/integration、evaluation，并且强调不要只按 VLA、RL 这种模型标签来理解 manipulation。

survey

一、先给你一句总判断

这篇文章的详细结构，本质上是一个 “从系统约束到系统能力，再到系统评估”的分层框架：

硬件/软件 embodiment 约束
→ 数据生态
→ 学习范式
→ 集成与部署
→ 评价体系
→ 开放挑战与未来方向。 

survey

所以它表面看是 2、3、4、5、6、7 六七个大节，实际上深层逻辑是一条很强的“因果式工程链”：

机器人身体和软件栈决定能做什么；

这些约束决定需要什么数据；

数据再决定什么学习范式可行；

学习范式如何集成，决定部署方式；

部署后的系统，再由评价体系来闭环检验。 

survey

二、最外层目录结构

这篇文章的显式目录是：

1 Introduction
2 System Architecture of Robotic Arms
3 Data Ecosystem of Robotic Arms
4 Learning Paradigms of Robotic Arms
5 System Evaluation of Robotic Arms
6 Open Challenges and Future Directions
7 Conclusion 

survey

这里有个很值得注意的小细节：
引言里写的是“Section 5 synthesizes evaluation methodologies, and Section 6 concludes with open challenges and future directions”，但正文实际上还有 Section 7 Conclusion。也就是说，它在引言的结构预告里，把“挑战与未来方向”当成收尾，但正式成文时又额外保留了一个标准的 Conclusion。这个现象和你前面那篇文章有点类似：结构预告略简化，正文层级更完整。 

survey

三、这篇文章真正的“骨架”是什么

它的骨架不是“操作学习有哪些模型”，而是 Figure 1 里那套总 taxonomy。
Figure 1 几乎就是全文的总目录图，它把全文拆成四大块：

System Architecture of Robotic Arms

Data Ecosystem of Robotic Arms

Architectural/Learning Paradigms of Robotic Arms

System Evaluation of Robotic Arms 

survey

这四大块不是并列罗列，而是有明显连接关系：

Section 2 先定义机器人的物理与软件约束；

Section 3 再说明在这些约束下，数据如何生产、扩展、清洗、流水线化；

Section 4 再看这些数据如何被转成 planning、policy、integration 和 deployment；

Section 5 最后从执行质量、数据效率、泛化、能耗四个维度评估整个系统。 

survey

所以它不是“线性单问题综述”，而是“四层系统结构综述”。

四、逐节细拆
1. Introduction：不是单纯背景，而是在“换一种综述坐标系”

引言做了四件事。

1）先说明 manipulation 为什么是 embodied intelligence 的核心问题

文章从 embodied intelligence 的定义讲起，强调 robotic manipulation 的难点在于：

contact dynamics

force exchange

high-DoF kinematics

fine-grained object perception

所以机械臂操作是 embodied intelligence 的典型载体。

survey

2）指出现有综述的问题：按模型家族分类不够

作者明确批评了一种常见综述写法：
只按 VLA、RL、foundation models 之类分类，会遮蔽真正重要的差异，比如：

planning artifact 不同

action representation 不同

system integration 不同

data regime 不同 

survey

也就是说，这篇文章一开始就在“改坐标系”。

3）提出自己的组织方法

作者说，他们要围绕以下几个轴来组织领域：

data regimes

cognitive planning

policy learning

integration architectures

并且考察不同 embodiment，包括 stationary、bimanual、mobile、humanoid。

survey

4）给出三项贡献

引言把贡献说得很清楚：

建立 layered taxonomy of embodied datasets，并分析数据生产生态；

区分 cognitive planning 和 policy learning，并分析它们的整合与部署权衡；

把 embodied manipulation 看成一个耦合设计问题，分析 embodiment、data、learning、deployment、evaluation 的相互作用。 

survey

所以引言的功能不是“铺文献”，而是：
把这篇综述从“模型综述”重新定义成“系统设计综述”。

2. System Architecture of Robotic Arms：先立“约束层”

这一节是全文的起点。
作者的逻辑很明确：在讲数据和学习之前，先问一个更底层的问题——

机器人身体和软件栈，到底给学习系统施加了什么边界？ 

survey

它分两大部分：

2.1 Physical Embodiment

又分三层：

2.1.1 End Effectors and Contact Sensing

这里讲接触界面与接触感知：

parallel-jaw / adaptive grippers

dexterous hands

soft hands

eye-in-hand vision

tactile sensing

也就是说，这一节关心的是：
你是怎么和世界发生接触的，以及接触后你能感知到什么。 

survey

2.1.2 Fixed-base Platforms

这里把平台分成：

single-arm

bimanual fixed-base

重点不是列机器人，而是说明控制瓶颈如何变化：

单臂偏向局部控制；

双臂转向多接触点协调、内力调节、闭链约束。 

survey

2.1.3 Mobile and Whole-body Platforms

这里讲：

wheeled mobile manipulators

legged manipulators

humanoids

这一层的关键词是 coupling：
当机械臂不再固定时，manipulation 就和 navigation、balance、whole-body coordination 耦合起来。

survey

所以 2.1 本质上是在做一个三层 embodiment 分析：

接触层 → 机械臂平台层 → 全身/移动层

2.2 Software Framework

这部分把“软件侧约束”接上来。

2.2.1 Modern Robotics Middleware and Operating Systems

作者把软件栈组织成三层：

L0 Kernel Layer

L1 Transport Layer

L2 System Layer

并用 Table 1 去对应：

实时内核

ROS2 / dataflow 通信

robot-edge-cloud-fleet orchestration 

survey

这个写法很有意思，因为它不是泛泛讲软件框架，而是直接把 manipulation 软件栈拆成一个“控制时序—数据传输—系统编排”的层级。

2.2.2 Low-level Motion Planning and Control

这里进一步落到执行层：

operational/joint-space mapping

nonlinear dynamics compensation

constraints

MPC / WBC

impedance control

这部分的功能是告诉你：
高层再聪明，最后都必须落到低层运动控制和实时执行上。

survey

这一节结尾特别重要

作者明确写道：
hardware embodiment 和 software stack 一起定义了 learned policy 的 physical and computational constraints；这些约束进一步 shape data requirements for learning。 

survey

这句话其实就是全文从第 2 节过渡到第 3 节的总铰链。

3. Data Ecosystem of Robotic Arms：从“数据集”升级到“数据生态”

这一节是全文最有辨识度的部分之一。
作者没有只写 datasets，而是写 data ecosystem。也就是说，他们想讨论的不是“有哪些数据集”，而是：

数据如何被分层、收集、生成、修正、整合成流水线。 

survey

这一节分成四个部分：

3.1 Embodied Datasets

这里先建立三层 dataset taxonomy：

3.1.1 Skill-level Datasets

关注局部技能、局部 interaction dynamics。
比如 grasping、pushing、articulation、assembly。

survey

3.1.2 Task-level Datasets

把孤立 primitive 扩展成 instruction-aligned trajectories。
也就是从“动作片段”走向“任务轨迹”。

survey

3.1.3 Foundation-level Datasets

进一步走向跨平台、跨 embodiment、跨模态的大规模统一数据。
关键词是：

cross-robot aggregation

standardization

multimodal consistency

transfer at scale 

survey

这里作者还给了一个很概括性的表达：

Kᵢ ≈ Kᵢ₋₁ ⊕ Dᵢ

意思是每一层数据都在上一层的知识状态上加上新的数据支持。
这让 3.1 不只是“列举数据集”，而是有一个明确的层级扩张逻辑。

survey

3.2 Data Acquisition

讲“数据怎么来”，分三路：

3.2.1 Real-world Data Gathering

真实世界采集：

teleoperation

distributed collection

human-hand / egocentric capture

robot-free demonstration then retargeting 

survey

3.2.2 Simulation Data Ecosystems

仿真生态，作者重点不是按软件名单罗列，而是按“数据偏向”解释三大生态：

MuJoCo 偏 contact-stable / controller-oriented dynamics

SAPIEN 偏 articulated-object / part semantics

Isaac 偏 scalable GPU-parallel synthesis 

survey

3.2.3 Automatic Data Generation

自动生成再分三种：

scene generation

demonstration synthesis

world-model rollouts

这说明作者把“自动生成”看成比仿真更上层的一种 data production 机制。

survey

3.3 Data Refinement

这是这篇文章比普通数据综述更细的地方。
作者认为数据问题不只是采集，还包括 refinement，并且分成四类：

3.3.1 Visual and Viewpoint Augmentation

扩大感知分布。

survey

3.3.2 Physically Grounded Augmentation

保证增强后的轨迹依然满足运动学、碰撞、接触约束。

survey

3.3.3 Correction and Recovery Augmentation

补上 expert-only datasets 里缺少的失败恢复数据。

survey

3.3.4 Data Curation and Verification

做过滤、重加权、价值评估。

survey

所以 3.3 实际上在回答一个很工程的问题：
当数据规模上来以后，瓶颈从“有没有”变成“好不好”。

3.4 Data Pipeline

这一小节是第 3 节的收束。
作者强调 acquisition、synthesis、refinement 正在被整合成 end-to-end production systems，把数据生产当成一个工程栈。

survey

所以第 3 节不是静态数据综述，而是一条完整链条：

dataset regimes → acquisition → refinement → pipeline

这是这篇文章非常清晰的一个结构亮点。

4. Learning Paradigms of Robotic Arms：全文的核心主体

这一节是文章最大、最复杂，也是最有“作者自创框架感”的部分。
它不是简单分 model families，而是先把学习系统拆成两半：

Cognitive Planning = embodied brain

Policy Learning = embodied cerebellum

然后再讨论它们如何集成，以及如何部署。

survey

所以第 4 节内部其实是：

4.1 规划脑
4.2 控制小脑
4.3 二者如何拼接
4.4 拼完后如何上机器

4.1 Cognitive Planning: The Embodied Brain

作者把 planning 按“给执行层产出什么 artifact”分成五类 B1–B5：

4.1.1 Semantic Logic and Code Generation（B1）

产出 code、reward function、skill ranking、behavior tree 这类语义级可执行规格。
特点是离语义接口最近，但离物理世界最远。

survey

4.1.2 Long-Horizon Task Decomposition（B2）

把长任务拆成 sub-task sequence 或 formal plan。
这是典型的任务结构层。

survey

4.1.3 Grounded Multimodal Representation（B3）

把 task intent 接到当前 embodied scene 上，形成 scene-conditioned task representation。
这是语义与场景结合的中间层。

survey

4.1.4 Geometric Grounding and Spatial Intelligence（B4）

输出 spatial representations：

contact region

SE(3) pose

affordance map

neural field

也就是把 planning 进一步物理化。

survey

4.1.5 Generative Dynamics and Physical Imagination（B5）

输出对未来状态/观测/动力学的预测，用 imagined rollout 评估候选动作。
这是最靠近“物理想象”的 planning。

survey

这一小节的深层逻辑

B1 到 B5 不是平行枚举，而是一条**“从语义到物理”的 grounding 递进链**：

语义规格 → 任务结构 → 场景化表征 → 空间化表征 → 动力学预测

这也是为什么 Figure 5 特别重要：它把五种 planning mode 当作不同物理 grounding 水平上的路线。

survey

4.2 Policy Learning: The Embodied Cerebellum

这里作者不按 BC/RL/VLA 分，而是按 action representation 分三类：

4.2.1 Explicit Continuous Policies（P1）

单步连续回归，快，但表达力有限。

survey

4.2.2 Discrete Action Policies（P2）

把动作 token 化，用 autoregressive 方式生成。
好处是能建模 multimodal action distribution，问题是量化误差和解码延迟。

survey

4.2.3 Iterative Generative Policies（P3）

用 diffusion / flow matching 等多步生成完整动作分布。
表达力最强，但推理最重。

survey

这一小节的深层逻辑

Figure 6 很关键，它把三类 policy 放到一个二维比较里：

一边是 distribution expressivity

一边是 computational complexity

所以 4.2 的本质不是 taxonomy 本身，而是一个核心 trade-off：

动作分布表达力 vs 推理效率。 

survey

4.3 Integration Models

这里进入第 4 节最“架构设计”的部分：
前面 4.1 和 4.2 分开讲，现在问——

planning 和 policy 到底怎么组合成完整 manipulation system？

作者分三类：

4.3.1 Type I: Unified End-to-End Foundation Models

共享 backbone，把 perception、reasoning、action generation 尽量装进一个统一模型。

survey

4.3.2 Type II: Hierarchical & Modular Reasoning Models

把 slow reasoning 和 fast execution 分层分模块。
作者还进一步指出这里面有：

explicit hierarchy

implicit hierarchy 

survey

4.3.3 Type III: Spatial Grounding & Predictive World Models

维护一个 shared world representation，让 planning 和 policy 都消费它。
这里又包含：

spatial grounding

predictive world models 

survey

这一节特别成熟的地方

作者没有只分类，还给每类都写了一个“中心矛盾”：

Type I：统一虽强，但高层 reasoning 和实时控制是否真能放进一个 loop？

Type II：分层虽合理，但 planner-controller interface 成为瓶颈；显式层级可能过硬，隐式层级可能过黑箱。

Type III：共享 world representation 很强，但如果 representation 不准或过时，整个系统都会被误导，而且训练/部署代价大。 

survey

这说明 4.3 不是“列架构”，而是在做 architecture-level critique。

4.4 Deployment Pipeline

前面还主要是“学什么、怎么拼”，这里开始问：

学出来的系统，怎么真正部署到物理机器人上？

作者把 deployment 分三阶段：

4.4.1 Stage 1: Offline Pre-deployment

关注：

sim-to-real

cross-embodiment transfer

compression / making models practical 

survey

4.4.2 Stage 2: Online Physical Alignment

部署后再对齐真实世界：

friction

sensing noise

contact-rich adaptation

RL fine-tuning

world-model-guided adaptation 

survey

4.4.3 Stage 3: Inference-Time Execution

关注实时执行时的：

quantization

decoding acceleration

runtime robustness

failure detection & recovery 

survey

这部分结构很像工程流水线

而且作者明确说三阶段 analytically distinct，但 practically tightly coupled。
也就是说这不是简单时间顺序，而是一个互相制约的部署闭环。

survey

所以第 4 节整体上是：

brain → cerebellum → architecture → deployment

这是这篇文章最有原创组织感的一段。

5. System Evaluation of Robotic Arms：用四个评价轴闭环

这一节的开头写得很清楚：
前面 2–4 节已经讲了 embodiment、data、learning、deployment，这一节是来 close that loop 的。

survey

它从四个维度评价系统：

5.1 Task Execution Quality Evaluation

看任务完成质量。
从 binary success 扩展到：

task progression

smoothness

coordination 等。

survey

5.2 Data Efficiency and Quality Evaluation

看 demonstrations 到 capability 的转化效率。
包括：

coverage

contribution

downstream utility

AULC 等。

survey

5.3 Generalization and Transfer Evaluation

看：

human preference

OOD robustness

sim-to-real proxy validity

world model as evaluator 

survey

5.4 Energy and Efficiency Evaluation

看部署成本：

latency

compute

memory

hardware load

energy consumption 

survey

这一节的深层逻辑

不是单纯“评价指标综述”，而是把系统评价重新拆成四个互补轴：

执行质量
数据效率
泛化迁移
部署效率

这四个轴，正好反过来对应前文的系统组成。
所以第 5 节是很标准的“反向闭环”。

6. Open Challenges and Future Directions：不是泛泛展望，而是按系统维度逐项开账

这一节很工整，直接按六个维度列挑战：

6.1 Embodiment

6.2 Data

6.3 Learning

6.4 Deployment

6.5 Evaluation

6.6 Trustworthiness

6.7 Emerging Directions 

survey

你会发现，这六项基本上就是把前文四大模块再细分后重新开账：

embodiment 对应第 2 节；

data 对应第 3 节；

learning / deployment 对应第 4 节；

evaluation 对应第 5 节；

trustworthiness 是跨层问题；

emerging directions 则是把未来趋势单独拎出来。

survey

这说明第 6 节不是附加内容，而是对整篇 taxonomy 的“问题映射”。

7. Conclusion：把四阶段框架重新压缩回一句话

结论部分非常标准，也很克制。
作者说，这篇综述把 learned manipulation intelligence 组织成四个 interdependent stages：

hardware embodiment

data ecosystem

learning paradigm

evaluation

并强调：
embodied manipulation 不能只通过 model families 来理解。 

survey

这句话其实就是全文的总论断。

五、如果再抽象一层，这篇文章的“详细结构逻辑”是怎样的

我觉得它其实是一个 两层嵌套结构。

第一层：四大系统维度

system architecture

data ecosystem

learning paradigms

evaluation 

survey

第二层：每个维度内部再做层级化分解

比如：

architecture：physical + software

data：datasets + acquisition + refinement + pipeline

learning：planning + policy + integration + deployment

evaluation：execution + data efficiency + transfer + efficiency 

survey

所以它的详细结构非常“模块化”，但不是松散并列，而是有一条贯穿全篇的转换链：

constraints → data support → learning conversion → system integration/deployment → evaluation closure

六、这篇文章和第一篇 Trojan 综述在结构上最大的不同

这个你如果要做比较，非常值得讲。

第一篇 Trojan survey

是单问题主线型：

先定义 Trojan

再按生命周期讲攻击

再按检测/消除讲防御

最后讲挑战与展望

它的主线非常像“一个问题的完整生命周期”。

第二篇 manipulation survey

是系统分层型：

先讲系统约束

再讲数据生态

再讲学习与集成

再讲评价

最后讲挑战

它不是围绕某个单点问题，而是围绕“一个完整 embodied manipulation 系统”来展开。 

survey

所以如果你要一句话概括：

第一篇是 problem-centered survey。
第二篇是 system-centered survey。

七、这篇文章最值得学的结构写法

如果你是想借它来写综述，我觉得最值得学的是三点。

1）先立系统层级，再填文献

这篇不是先搜一堆 paper 再分类，而是先构建：

embodiment

data

learning

evaluation

然后把文献放进去。这样结构特别稳。

survey

2）每个大节都有“内部微结构”

比如：

第 3 节是 datasets/acquisition/refinement/pipeline

第 4 节是 planning/policy/integration/deployment

第 5 节是四个评价轴

所以每节不是一堆小论文堆起来，而是有自己的内在组织逻辑。

survey

3）它特别善于用图表充当结构骨架

Figure 1：总 taxonomy

Figure 3：data support

Figure 4：learning paradigms 总览

Figure 5：planning 五范式

Figure 6：policy 三范式比较

Table 1–11：几乎把每一节的分类骨架都固化了 

survey

也就是说，这篇文章的结构不仅写在标题里，还写进了图表系统里。

八、最后给你一个最简洁的“结构地图”

你可以把这篇文章压成下面这个图式来记：

Section 1：为什么不能只按模型家族看 manipulation
Section 2：机器人身体和软件栈给学习施加什么约束
Section 3：这些约束下，数据如何分层、采集、生成、修正、流水线化
Section 4：数据如何被转化为 planning、policy、integration、deployment 能力
Section 5：系统最终该如何评价
Section 6：这些层面各自还卡在哪些关键瓶颈
Section 7：回到总论——manipulation 是一个耦合系统问题 

survey

如果你愿意，我下一条可以继续帮你做一个更有用的版本：
把这第二篇文章和第一篇 Trojan 文章的结构并排对照成一个表。

---

你认为那篇文章的内容密度大?

---

如果你说的是 第二篇《Embodied Manipulation for Robotic Arms》，我会说：

整体内容密度是大的，而且偏“大框架压缩型”的密度。

更具体一点，它的“密”主要体现在三层。

第一层是 结构密度大。
作者不是只讲一个问题，而是同时铺开 system architecture、data ecosystem、learning paradigms、evaluation 四大块；摘要和引言里又明确把它进一步压成 三层数据体系、planning/policy 双路径、三类 integration、四类 evaluation axes。这意味着读者一开始就要同时处理很多坐标轴，所以主观上会觉得“信息很满”。

survey

 

survey

第二层是 taxonomy 密度大。
你看它几乎每个大节都不是单纯讲 prose，而是在建分类系统：
第 3 节把数据拆成 embodied datasets / acquisition / refinement / pipelines；第 4 节把 learning 拆成 cognitive planning / policy learning / integration / deployment，其中 planning 还细分成 B1–B5，policy 再细分成 P1–P3。这种写法会让每页承载的“框架节点数”非常高。

survey

 

survey

第三层是 图表压缩密度大。
这篇不是靠长段落取胜，而是靠大图、大表把很多信息压进页面。Figure 1 直接把全文的系统架构、数据生态、learning、deployment、evaluation 全部串在一张图里；Figure 3 又把数据支持体系压成一张 pipeline 图；Table 6、Table 7 分别把 planning 和 policy taxonomy 高度压缩成对照表。也就是说，它的密度很大一部分来自 “信息压缩率高”，不是来自每段都写得特别长。

survey

 

survey

 

survey

 

survey

但我会再补一句：

它是“广度密度大”，不完全是“单点深度密度大”。

也就是说，它对每个局部问题未必都像 Trojan 那篇那样深挖到很细；它更像是在用有限篇幅，把一个大系统的多个层面尽量装进去。比如第 4 节会把 planning、policy、integration、deployment 连着讲，但每一种具体方法通常只点核心机制和代表工作，不会展开成很长的机理分析。

survey

 

survey

所以我的结论是：

第二篇的内容密度确实大，且是“框架型高密度”。
不是那种“每个点都讲得特别深”的密，而是
层级多、分类多、图表多、每页压的信息量大。

如果和第一篇比，我会这样说：

第一篇：单主题纵深密度更强

第二篇：系统框架广度密度更强

你现在会觉得第二篇“读起来满”，这个判断是对的。

---

我说这两篇哪篇内容密度大，你理解错了

---

对，我刚才理解成“第二篇自身密不密”了。
你现在问的是：这两篇相比，哪篇内容密度更大。

我的判断是：

如果按通常说的“单位页里有多少连续的实质分析、机制解释、比较判断”，第一篇 Trojan 那篇内容密度更大。 

3727640

 

survey

原因主要有三个。

第一，第一篇更聚焦，浪费更少。
它几乎全篇都在围绕一个单问题推进：Trojan attack 在训练、后训练、推理三个阶段怎么发生，和 poisoning / adversarial examples / bit-flip 是什么关系，检测和消除怎么做，以及现有防御到底哪里无效。这个主轴非常集中，所以每往后翻一页，基本都还是在同一个问题上继续压深。摘要和引言也明确说，它的重点是 lifecycle taxonomy、countermeasures 和 practical effectiveness。

3727640

 

3727640

第二，第一篇“连续论证段落”更多。
它在前面先定义术语，再给 Trojan injection 的统一形式化表达，再讲 threat models，然后按 stage 展开攻击，再按 detection / elimination 展开防御，最后还有 effectiveness comparison。你会发现它很多页都是长段的机制解释和方法比较，不只是列结构。像第 2 节就已经在做 technical terms、principles、scenarios 的连续建模；第 4 节又直接进入 countermeasures 与优缺点比较。

3727640

 

3727640

第三，第二篇更像“框架摊开”，不是“单点压深”。
第二篇当然信息量也很大，但它的信息更分散在大框架里：system architecture、data ecosystem、learning paradigms、evaluation 四大块，再往下拆成三层数据、B1–B5、P1–P3、integration、deployment 等。它很多页的篇幅被 taxonomy 图、总览图、表格、数据集盘点占掉了，这种写法更偏“广度覆盖”和“框架组织”，不完全等于“单位页连续论证更密”。

survey

 

survey

 

survey

所以更准确地说：

第一篇：纵深密度更高
更像“每一页都在继续压一个核心问题”。 

3727640

第二篇：框架密度更高
更像“每一页都在往大地图里塞新模块”。 

survey

 

survey

如果你非要我只选一个“内容密度更大”的，我会选：

第一篇 Trojan 那篇。

因为第二篇虽然也很满，但它更多是覆盖面满；
第一篇则是分析链条更紧、更压缩、更少留白。

---

信息量更大呢？

---

如果说的是 “覆盖的信息面、模块数、材料种类、框架层次”，我会改判成：

第二篇的信息量更大。 

survey

因为第二篇装进去的东西明显更多、更杂，也更铺开。它不是只讲一个核心问题，而是同时覆盖：

embodiment / system architecture

data ecosystem

learning paradigms

integration + deployment

evaluation

open challenges 

survey

而且它在每个大块里还继续细分，比如：

数据分成 skill-level / task-level / foundation-level；

learning 分成 cognitive planning / policy learning / integration / deployment；

planning 再拆成 B1–B5；

policy 再拆成 P1–P3；

evaluation 再拆成四个轴。 

survey

相比之下，第一篇虽然也很完整，但它主要还是围绕一个更集中的主题：
Trojan attack 在 DNN 生命周期中的攻击与防御，核心是 training、post-training、inference 三阶段，加上 detection / elimination / challenges。它更像对一个专题做高强度压缩。

3727640

所以你可以这样区分：

内容密度更大：第一篇
因为它更聚焦，单位页里的连续分析更紧。

3727640

信息量更大：第二篇
因为它覆盖的维度更多，装进去的数据集、平台、learning 范式、部署与评测内容也更多。

survey

一句话说就是：

第一篇更“浓”，第二篇更“多”。

---

你这次重新审视，你认为他们的行章逻辑合理吗？他们是否是一个水平的文章?

---

我这次重新收一遍看，结论会更稳一点：

两篇的行章逻辑都合理。
而且我认为它们总体上是一个水平段位的文章，但不是同一种强项。

更具体地说：

1. 先回答“行章逻辑是否合理”
第一篇 Trojan：非常合理，而且是“高闭环”的合理

它从摘要到引言就把中心问题钉死了：
这篇要用 life-cycle perspective 重组 Trojan attack，把问题放到 training / post-training / inference 三个阶段里看，同时再补上和 poisoning、adversarial examples、bit-flip 的关系，以及对应的 countermeasures 和 practical effectiveness。

3727640

它后面也确实严格执行这个承诺：
引言先说明 Trojan 贯穿模型生命周期，随后明确说 Section 2 讲 principles and preliminaries，Section 3 按生命周期讲 Trojan taxonomy，Section 4 讲 detection 和 elimination，Section 5 讲 challenges。

3727640


而且第 2 节不是空铺背景，它先定义 Trojan information、trigger、poisoned sample 等术语，再把 Trojan injection 在训练、后训练、推理三个阶段分别形式化。也就是说，它的“预备知识”直接服务于后面的三阶段 taxonomy。

3727640

 

3727640

所以第一篇的结构不是“目录好看”，而是主张、章节、分类变量三者一致。
这是很成熟的行章逻辑。

第二篇 Manipulation：也合理，但属于“系统分层型合理”

第二篇的引言明确说，很多综述主要按 model family 组织领域，但这样会遮蔽 manipulation 里更关键的差异，比如 planning artifacts、action representations、system integration；因此它故意改成按 data regimes、cognitive planning、policy learning、integration architectures 来组织，并把 embodiment、deployment、evaluation 一起纳入。

survey

后面的章节安排也和这个动机对得上：

Section 2 讲 physical embodiment + software infrastructure

Section 3 讲 data ecosystem

Section 4 讲 cognitive planning / policy learning / integration / deployment

Section 5 讲 evaluation。

survey

更重要的是，它不是生硬并列。第 2 节结尾明确写出一个关键过渡：
hardware embodiment 和 software stack 定义了 learned policy 所处的 physical and computational constraints，这些约束进一步 shape 了 learning 所需的数据。
然后第 3 节顺势转入 data ecosystem。

survey

这说明第二篇虽然是大框架，但不是散架的拼盘。它的深层逻辑其实是：

约束层（embodiment / software） → 数据支持层 → 学习与集成层 → 评测闭环层。 

survey

所以我的判断不是“第二篇结构有问题”，而是：

它的结构逻辑是合理的，只是比第一篇更吃读者的抽象能力。

2. 再回答“他们是否是一个水平的文章”
我的判断：总体是一个水平段位，但不是同一种优秀

如果你说的是“是不是明显一篇高、一篇低”，我的答案是：

不是。它们是同一档次的综述，只是各自擅长的维度不同。

第一篇更强的地方

第一篇的强项是：

主线集中

内部闭环强

论证推进紧

专题收束力强

它的阅读体验像一个高聚焦专题综述：
从 lifecycle 出发，把攻击、防御、局限收成一条完整问题链。尤其作者明确说，相比已有综述，它更重视 countermeasures 和 practical effectiveness，这让文章不仅“会分类”，而且“会判断”。

3727640

 

3727640

所以第一篇是那种结构纪律性特别强的文章。

第二篇更强的地方

第二篇的强项是：

系统视野更大

框架建构能力更强

跨层级组织难度更高

信息容量更高

它不仅要处理 embodiment、data、learning、evaluation 这四大层，还在内部继续做三层 datasets、planning/policy 分解、integration type、deployment stages 的嵌套结构。Figure 1 基本就是一整张“领域地图”。

survey


第 3 节又不是只列数据集，而是把数据写成 datasets → acquisition → refinement → pipeline 的生产体系。

survey

所以第二篇是那种框架野心和搭桥能力很强的文章。

3. 但如果非要细分“谁更稳、谁更险”

我会这样说：

第一篇：更稳

因为它的问题边界清楚，主线单一，分类变量也始终比较克制。
换句话说，它更接近“这类题目的一种近乎最优结构解”。

第二篇：上限高，但更险

因为它承担的是一个系统级大题目。
作者自己也承认这是一个 coupled design problem，并且在第 6 节又重新按 embodiment、data、learning、deployment、evaluation、trustworthiness 六个方向开账。

survey


这说明它不是没有控制住，而是它本来就比第一篇更难写，也更容易出现“维度很多、收束更难”的风险。

所以如果只论“结构稳健性”，我还是会把第一篇排前一点。
但如果论“框架野心”和“系统化程度”，第二篇一点不低。

4. 我的最终结论

一句话说：

两篇的行章逻辑都合理。
它们是同一水平段位的文章，但不是同一种写法。

更具体压缩成一句就是：

第一篇：同水平里更偏“专题深挖型优等生”

第二篇：同水平里更偏“系统框架型优等生”

如果你逼我做一个学术写作上的排序，我会这样排：

结构完成度与稳定性：第一篇略占优。
框架雄心与系统覆盖力：第二篇略占优。

所以不是“谁高谁低”，而是：

一个赢在收束，一个赢在展开。

你要是愿意，我下一条可以直接把它们做成一个特别清楚的对照表：
主线、结构、信息量、内容密度、作者性、风险点、可借鉴点 七栏并排。

---

其实第二个文章还是初稿

---

那这个信息很关键。
如果第二篇还是初稿，我会调整前面的判断：

它们的“研究野心”可以是一个水平，
但当前稿件完成度不是一个水平。

第一篇 Trojan 那篇是已经完成度很高的综述：主线从引言就钉在 life-cycle perspective，后面按 principles/preliminaries → lifecycle attacks → countermeasures → challenges 往下推，闭环很完整。

3727640

第二篇则明显更像框架先行的初稿。它的顶层设计其实已经很清楚：引言明确说不想按 model family 组织，而要按 embodiment、data、planning/policy、integration、evaluation 来重构领域；后面目录也确实照这个框架在搭。

survey


但初稿常见的问题，它身上也很像有：

顶层框架强，局部收束还没完全打磨好

大图大表先搭好了，段落之间的过渡和“为什么现在讲这个”还不够紧

有些部分更像“把版图铺开”，还没完全压成成熟的论证链

所以如果第二篇是初稿，那我会这么改口：

1. 对第二篇的很多“问题”，不能直接当成结构缺陷

比如我前面说它有“并列式大框架”的风险。
现在更准确的说法应该是：

它的框架方向是对的，但目前还停留在“框架已立，论证还可继续压实”的阶段。

这和“框架本身不合理”不是一回事。

2. 现在不适合拿它和第一篇比“成熟度”

因为第一篇看起来是成熟发表稿，第二篇如果还是初稿，那：

语言成熟度

段落收束

小节平衡

主线显化程度

这些本来就不该直接硬比。

3. 但可以比“潜力”和“骨架”

如果只看骨架，我还是会说第二篇的设计是有潜力的。
尤其第 2 节末尾那句过渡很关键：hardware embodiment 和 software stack 定义了 learned policy 的约束，而这些约束进一步 shape 数据需求，这说明作者其实已经意识到整篇应该沿着一条“约束传导链”来走。

survey

所以现在更公平的结论应该是：

第一篇：成熟稿，结构完成度高，收束已经做好

第二篇：初稿，顶层框架有想法，但还在把“框架”变成“成稿”的过程中

一句话说：

第一篇赢在成稿质量，第二篇可能赢在框架野心。
如果第二篇后续认真改，未必会输；但就“眼下这版稿子”来看，确实不能和第一篇按同一完成度标准硬比。

你要的话，我可以直接按“这是初稿”这个前提，帮你判断第二篇最该改的 3 个结构点。

---

你来判断一下

---

我来给一个直接判断：

结论

按“当前稿件质量”看：第一篇明显更成熟。
按“框架潜力”看：第二篇不低，但现在还没打磨到第一篇那个完成度。

所以如果你让我现在拍板，我会说：

现在这两个文本，不算一个完成度水平。
第一篇是成熟成稿，第二篇还是有想法的初稿。

为什么我这样判断
1）第一篇已经是“结构—内容—收束”三位一体

第一篇从一开始就把主轴钉死在 life-cycle perspective：
训练、后训练、推理三个阶段；然后对应地展开 Trojan taxonomy，再进入 countermeasures，最后收束到 challenges 和 conclusion。引言里对各节功能的预告，和正文实际展开基本一致。

3727640

而且第 2 节不是虚铺背景，它先定义 technical terms，再解释 Trojan injection 的统一原理和 threat model，为后面 3、4 节的分类直接服务。也就是说，这篇文章不是“先搭目录再塞内容”，而是每一节都在给下一节铺路。

3727640

2）第二篇的顶层框架是对的，但还更像“架子先立起来了”

第二篇的引言其实很有想法。它明确反对只按 model family 组织 manipulation 综述，而要改成按 embodiment、data、cognitive planning、policy learning、integration、evaluation 这些更底层的组织变量来写，这个判断本身是成立的。

survey

而且它的章节安排也确实对应这个想法：

Section 2 讲 embodiment 和 software infrastructure

Section 3 讲 data ecosystem

Section 4 讲 learning / integration / deployment

Section 5 讲 evaluation。

survey

问题不在于框架错，而在于：
现在更像“框架正确，但论证压缩度还不够”的初稿状态。

我认为第二篇现在最像哪种状态

我会把它定义成：

“高潜力的大框架初稿”

它已经有三样好东西：

第一，有清楚的总野心。
它不是普通资料综述，而是在争取一种新的解释方式：把 manipulation 看成一个 coupled design problem。

survey

第二，有系统性的章节链。
第 2 节末尾那句过渡很关键：
hardware embodiment 和 software stack 定义了 physical / computational constraints，而这些约束又 shape learning 所需的数据。这个过渡说明作者其实已经意识到，全篇应该沿着“约束向下传导”的逻辑走。

survey

第三，图表骨架已经成型。
总 taxonomy 图、data support 图、learning paradigms 图，都说明作者不是没有结构，而是结构已经先搭起来了。

survey

但它还缺两步：

把并列板块之间的关系讲得更“必然”

把每一节收束成更明确的判断，而不只是完整覆盖

所以我的最终判断是
如果按“现在拿出去比”

第一篇赢。

因为第一篇已经是完整成稿：
主线稳定、论证收紧、结构闭环、阅读成本低。

3727640

如果按“潜力和上限”

第二篇不输。

因为第二篇的框架野心更大，系统视角也更强；只是初稿阶段，这种文章本来就更难写，也更需要后期打磨。

survey

一句话拍板

我的判断：第一篇现在是成熟稿，第二篇现在是有框架优势但尚未收紧的初稿。
所以当前不在同一完成度水平，但第二篇有机会通过结构打磨追上来。

你要的话，我下一条我可以直接按“初稿修订”的标准，给第二篇列出最该优先改的 3 个结构问题。

---

问你怎么改，没让你继续比了

---

对，你说得对。那我就直接回答 第二篇初稿怎么改，不继续比。

我会抓 3 个一级问题 + 1 个可直接落地的新目录。

一、先说我认为最该改的 3 个问题
1）主线不够显，框架先于论证

这篇引言已经把野心说清了：不想按 model family 讲，而要围绕 embodiment、data、planning/policy、integration、evaluation 来组织，还把 manipulation 定义成一个 coupled design problem。这一步方向是对的。

survey

问题在于，正文现在更像是把这几个块都铺开了，但**“为什么这一块自然导向下一块”** 还没有被反复钉死。
虽然第 2 节末尾已经写出一个很关键的过渡——hardware embodiment 和 software stack 定义物理/计算约束，这些约束又 shape 了 learning 所需的数据——但这条线后面没有成为每节都反复回扣的唯一主轴。

survey

2）第 4 节分类过密，读者负担太高

你现在第 4 节一下子引入：

cognitive planning

policy learning

integration models

deployment pipeline

其中 planning 又拆成 B1–B5，policy 又拆成 P1–P3。作者自己也承认，这些 planning 范式其实是“parallel routes”，是不同物理 grounding 程度下的并行路线。

survey

 

survey

这会导致一个初稿很常见的问题：
分类很完整，但读者读完不一定立刻抓住“最重要的那条判断”。

3）数据部分很强，但还没完全变成“服务主线”的数据部分

第 3 节本身是好的，尤其是你把 data 写成：
datasets → acquisition → refinement → pipeline，这比“列数据集”高一个层次。

survey

 

survey

但现在它还有点像一个“很完整的数据生态综述块”，而不是完全被主线驱动的内容块。
你其实已经有一句非常好的桥句：what data enables effective learning under such constraints。

survey


下一步要做的是：让读者感到第 3 节不是“第二大块”，而是第 2 节约束自然推出来的结果。

二、我建议的改法：不要推翻框架，要把它“压成一条链”

你现在最不该做的，是把全文重写成第一篇 Trojan 那种单专题结构。
因为你的题目本来就是系统级题目，四块大框架是合理的。

survey

你该做的是：

把全文从“并列四大块”

改成读者能明显感觉到的这条链：

Embodiment constraints
→ Data requirements and production
→ Learning choices and integration
→ Deployment trade-offs
→ Evaluation criteria

这条链其实已经在文中隐含存在了：

第 2 节讲约束；

survey

第 3 节开头承接“在这些约束下需要什么数据”；

survey

第 4 节开头承接“数据如何转成 manipulation capability”；

survey

第 5 节开头说它是来 close that loop 的。

survey

所以不是重搭，而是把已有暗线显化成明线。

三、最实用的改法：每个大节开头都加一句“本节在主线中的作用”

你现在最需要补的，不是更多文献，而是章节功能句。

我建议你在每个大节开头都用一句非常硬的句子，把它钉进主线里：

Section 2 开头

现在已经有：

The action space of a robotic system is constrained by its hardware embodiment.
这句很好。

survey

但你可以再加一句更强的总领句，比如：

We begin from embodiment because hardware and software interfaces define the feasible control, sensing, and timing constraints under which all subsequent data collection and learning must operate.

这样读者马上知道：这是“约束层”。

Section 3 开头

你已经写了：

The next question, therefore, is what data enables effective learning under such constraints… 

survey

这句其实很好。建议把它再往前提、更显眼，甚至变成第 3 节第一段的最后一句或小节总领句。
因为它就是全文最好的承接句之一。

Section 4 开头

你现在写的是：

The data ecosystem discussed in Section 3 provides the raw material for learning… 

survey

这句对，但还可以更强一点。
建议改成：

Given the constraints of embodiment and the resulting data regimes, the next question is how manipulation capability is assembled: what should be planned, what should be learned as policy, how these two are integrated, and what deployment burdens each design incurs.

这样第 4 节就不是“learning 大块”，而是主线的“能力构建层”。

Section 5 开头

你已经写了它是来 close that loop 的，这很好。

survey


建议把“四个评价维度为什么正好对应前文四类设计后果”再说得更明显，而不只是列 evaluation families。

四、第 4 节我建议你“减分类，不减内容”

这是最关键的手术点。

现在的问题

B1–B5 和 P1–P3 都有学理价值，但对初稿来说，分类密度偏高。
尤其 B1–B5 这套，如果读者没有完全进入你的坐标系，会觉得：

“好像分得很细，但这些分法之间的一级逻辑是什么？”

我的建议

你可以保留 B1–B5、P1–P3，但把正文显式改成“先粗后细”：

先粗分两层

Planning outputs become progressively more physically grounded.
然后只先讲三档：

semantic / symbolic outputs

grounded spatial outputs

predictive / imaginative outputs

接着再说：

Within this broad progression, we further distinguish five representative planning paradigms (B1–B5)...

这样 B1–B5 就变成二级细分，而不是读者一上来就得吃下的一级框架。
你现在其实已经有这个思路，因为你自己写了这些 planning 范式是从高层 semantic competence 逐渐转向 physically grounded representations。

survey

P1–P3 也一样

先把总判断说死：

P1：快，但 mode-averaging

P2：离散化后表达力更强，但有 quantization 和 decoding latency

P3：分布建模最强，但推理最重。

survey

然后再放代表方法。
这样 Table 7 和 Figure 6 就是在支持你的总判断，而不是代替总判断。

survey

五、第 3 节的具体改法：少一点“盘点感”，多一点“决策感”

你第 3 节素材很好，但要再往前走一步：

现在像什么

“我们有三层数据、三种 acquisition、四种 refinement、pipeline。”

你应该让它更像什么

“不同 embodiment 和 deployment 目标，会推着系统走向不同的数据 regime；因此数据的核心问题不是规模本身，而是可用性、对齐、物理真实性和跨 embodiment 可迁移性。”

你第 6 节其实已经把这些问题说出来了：

真实数据少且昂贵；

heterogeneous data 难对齐；

simulation / synthetic 仍受物理真实性限制；

failures、recoveries、contact-rich transitions、cross-embodiment adaptation 尤其缺。

survey

 

survey

所以我建议你反过来改：
让第 3 节每个子部分都更明确地服务于第 6 节最后提出的问题。

最简单的办法是，在 3.1–3.4 每节末尾各加一个两三句的小结：

这一层解决了什么

没解决什么

它为什么会把系统推向某类 learning/integration choice

这样第 3 节就不只是 data review，而是 data-driven design review。

六、我建议你直接改目录显示方式，而不是大改目录内容

内容上不用推翻，目录显示方式要改得更像主线。

我建议的目录写法

你现在的目录可以保留，但每个一级节标题前面都明确它在系统链条里的角色：

2. Embodiment Constraints: Physical Platforms and Software Interfaces
3. Data Support Under Embodiment Constraints
4. From Data to Manipulation Capability: Planning, Policy, Integration, and Deployment
5. Closing the Loop: Evaluation of Manipulation Systems
6. Open Bottlenecks Across the Stack

这样读者仅看目录，就已经感到全文不是并列块，而是一条链。

七、如果只允许改 3 个地方，我建议你优先改这 3 个
第一优先：重写引言最后两段

把“本文结构”那段，从目录预告改成主线预告。
不要只是：

Section 2 does…

Section 3 does…

Section 4 does…

而要写成：

Section 2 defines the embodiment and system constraints

Section 3 shows how these constraints determine data needs and production regimes

Section 4 analyzes how data is converted into capability through planning, policy, and system integration

Section 5 evaluates the resulting systems along execution, transfer, and deployment axes

这一步收益最大。

survey

第二优先：压缩第 4 节的一级分类压力

把 B1–B5 和 P1–P3 先放到“粗分类后的二级细分”里讲。
这样你不会损失学术完整性，但阅读阻力会明显下降。

survey

第三优先：给第 3 节和第 4 节每个大子块补“小结句”

每节末尾都回答一句：
这一层设计会把系统推向什么后续选择？
这样你的大框架就会更像论证，不像手册。

八、我直接给你一句最短判断

这篇不用推翻重写。
它最需要的不是换框架，而是把现有框架从“分类图”压成“因果链”。

如果你愿意，我下一条可以直接替你做两件很实用的事里的一个：
一是把引言最后两段帮你重写成“主线更强”的版本；二是把第 4 节目录帮你压缩成更顺的层级。

---

分类密，但是第四章表格是是挂在衔接在一起的呀，你可以去看看?小结句?怎么个小结句，引言确实不太行

---

对，你这个提醒是对的。我前面对第 4 章说得有点重了，应该修正。

先纠正一点：第 4 章的表格和正文，其实是挂住了的

不是“表格孤零零地摆着”。

你看第 4 章开头先把 learning stack 分成两部分：
4.1 cognitive planning 和 4.2 policy learning，再说 4.3 integration 和 4.4 deployment，而且明确写了 Figure 4 是这一章的总组织图。

survey

接着 4.1 开头不是直接扔 Table 6，而是先解释为什么要分 B1–B5：因为 planning 的关键在于“输出给执行层的是什么 artifact”，并且这五类代表了从高层语义能力逐渐走向更强物理 grounding 的路线；然后才说 Table 6 summarizes 这些 paradigm-level properties。这个衔接其实是成立的。

survey

4.2 也是一样。它先解释为什么 policy 要按 action representation 分成 P1/P2/P3，再点出核心 trade-off 是 action expressiveness vs inference efficiency，然后才让 Table 7 去压缩这套比较。这个也不是“先有表后有文”，而是“文先定比较轴，表再做压缩”。

survey

 

survey

所以更准确地说：

第 4 章的问题不在“表格没挂住正文”，而在“挂住了，但挂得还可以更顺、更省认知负担”。

我现在对第 4 章的判断
第 4 章本身是成立的

因为它有一条很清楚的内部链条：

Figure 4 先给总图：planning → policy → integration → deployment。

survey

4.1 再细分 planning 的五种产物形态，Table 6 做总结。

survey

 

survey

4.2 再细分 policy 的三种 action representation，Table 7 做总结。

survey

 

survey

这个结构不是散的。

但它还是有一个“初稿感”

这个初稿感主要在于：

它已经有分类—图表—总结轴了，但“读者如何一路跟下来”的提示还不够多。

也就是说，不是逻辑断，而是阅读引导还不够强。

你问“小结句怎么个小结句”，我具体说一下

我说的不是那种很空的“综上所述”。
而是那种把这一小段为什么存在、它和下一段什么关系、作者真正判断是什么，一句话钉死的句子。

这种小结句有三种用途
1）收束一组分类，不让它变成纯罗列

比如 4.1 讲完 B1–B5 后，可以补一句类似：

Taken together, B1–B5 differ mainly in how far semantic competence is pushed toward physically executable representations: from code and symbolic structure to spatial constraints and predictive dynamics.

这类句子做的事不是总结文献，而是把 B1–B5 的一级逻辑 再钉一次。
因为你现在虽然在 4.1 开头已经说了这五类是从高层 semantic competence 走向 increasingly physically grounded representations，但后面讲着讲着读者可能会被具体方法带走。

survey

2）给下一小节搭桥

比如 4.1 结束、4.2 开头之间，其实就很适合有一句桥句：

If cognitive planning determines what form of execution-relevant specification is produced, the next question is how that specification is converted into motor commands, which leads directly to policy learning.

这样从 brain 转到 cerebellum 会更自然。
现在 4.2 虽然直接开门见山也能看懂，但多这一句，章节“咬合感”会更强。

survey

3）把表格从“信息块”变成“判断块”

比如在 Table 7 前后，不只是说“Table 7 summarizes…”，还可以多一句：

Across these three policy families, the core design trade-off is consistent: richer action distributions generally improve expressiveness but increase decoding or refinement cost.

这样读者看表时，脑子里已经有一个“该看什么”的判断坐标。

survey

我建议你具体加哪几类“小结句”
A. 在 4.1 结尾加一个总收束句

因为 4.1 是 B1–B5，信息量最大，最需要收。
可写成这种风格：

Overall, the five planning paradigms can be understood as different answers to the same question: what intermediate representation should connect high-level intent to low-level execution.

这句话的作用是：
把 B1–B5 从“五种方法桶”重新收束成“一个核心问题的五种答案”。

B. 在 4.2 结尾加一个总收束句

因为 P1/P2/P3 虽然已经有 Figure 6 和 Table 7，但还可以更明确地告诉读者这三类的总判断是什么。
例如：

In essence, P1, P2, and P3 occupy different points on the same frontier between inference efficiency and distributional expressiveness, and later integration and deployment choices largely inherit this trade-off.

这句能自然挂到 4.3 和 4.4。
因为 integration 和 deployment 的很多差别，本质上都在消化这个 trade-off。

survey

 

survey

C. 在 3.4 → 4 开头之间再强化一句桥句

这一句你其实已经有了一个不错版本：

The data ecosystem discussed in Section 3 provides the raw material for learning... 

survey

我建议改得更硬一点，比如：

Once the data support stack is in place, the central question becomes not how to collect experience, but how to convert it into manipulation capability through planning, action generation, system integration, and deployment.

这样第 4 章会更像“顺着前面推出来”，不是新开一大块。

你说“引言确实不太行”，这个我同意

我现在最明确的判断就是：

这篇最需要改的，不是第 4 章的表格，而是引言最后那两段。

因为现在引言已经有三个好东西：

提出已有综述按 model family 组织的不足；

survey

提出自己的组织方式；

survey

提出三条贡献。

survey

但它还缺一个最关键的动作：

把全文压成一条“为什么会自然走到下一节”的链。

现在 “Structure of the Paper” 那段还是偏目录式：

Section 2 reviews...

Section 3 examines...

Section 4 analyzes...

Section 5 synthesizes... 

survey

这对初稿来说很常见，但确实不够强。

我建议你怎么改引言最后这段

不是简单列目录，而是改成这种“主线版目录”：

We begin with embodiment and software infrastructure, because they define the sensing, control, and timing constraints under which manipulation systems must operate.
We then turn to the data ecosystem, asking what kinds of data are required under these constraints and how such data is collected, synthesized, refined, and scaled.
On this basis, we analyze how manipulation capability is constructed through cognitive planning, policy learning, and their integration into deployable systems.
Finally, we evaluate these systems along execution, transfer, and efficiency axes, before discussing the remaining bottlenecks across embodiment, data, learning, deployment, and trustworthiness.

这段的作用就是把全文从“目录并列”改成“因果推进”。

我现在给你的最终修正意见
你是对的：

第 4 章不是主要问题。

它的图表和正文其实是接住了的。

survey

 

survey

我现在更准确的建议是：

先改引言最后两段，把目录预告改成主线预告。

survey

在 4.1 和 4.2 末尾各加一个总收束句，把分类变成判断。

在 3.4→4、4.2→4.3、4.4→5 这几个地方补桥句，增强“咬合感”。

一句话说：

这篇不是“第四章分类太密所以有问题”，而是“引言没把主线钉死，导致第四章的好结构没被提前预告和放大”。

你要的话，我下一条直接给你两样现成的东西之一：
一个是 引言最后两段的重写版，另一个是 4.1、4.2 末尾的小结句成稿版。

---

理论上来说需要一个case study，这个还是好搞，直接用agibot讲清楚所有

---

理论上来说需要一个case study，这个还是好搞，直接用agibot讲清楚所有

---

可以，而且我觉得 这是个对的改法。
但我会把你的想法稍微收一下：

不是“用 AgiBot 讲清楚所有东西”，而是“用 AgiBot 做一个贯穿全篇的 cross-stage case，把你这篇文章的主线落地”。

这样就很强。

为什么我觉得可行：
这篇文章自己的总论点就是，manipulation 要从 hardware embodiment、data ecosystem、learning paradigm、evaluation 四个相互依赖的阶段来理解，而不是只按 model family 讲。

survey


引言也明确说，它想把 embodied manipulation 当成一个 coupled design problem，去分析 embodiment、data、learning、deployment、evaluation 如何共同塑造系统设计与实际表现。

survey

所以，理论上加一个 case study 是很顺的，因为 case study 正好能把“耦合关系”具体化。

为什么 AgiBot 合适

AgiBot 在你这篇文里已经不是边缘例子了，而是出现在两个很关键的位置：

一是 foundation-level dataset。文中把 AgiBot World 放进 foundation-level tier，说它把这一层推进到了 foundation-scale humanoid and dual-arm manipulation，提供了 100+ robots、100+ real-world scenarios、1M+ trajectories，而且在表里还标成了 B/H（双臂/类人）、RGB/D/F、language supervision、whole-body action、pipeline-level alignment。这说明它天然能承接你文章里“cross-embodiment + large-scale + multimodal”的那条线。

survey

 

survey

二是 data pipeline。文中又把 AgiBot World Colosseo 放到 3.4，专门说它把 fleet-scale humanoid collection 和 simulator-based augmentation 耦合起来，让真实数据流和合成数据流互相支撑。这个位置非常适合当 case study，因为它刚好对应你全文想强调的“data production 不是静态数据集，而是工程栈”。

survey

所以如果你问“有没有一个案例能把这篇文章的系统主线串起来”，
AgiBot 确实是个很自然的选择。

但要注意一个关键点

AgiBot 最适合讲清楚的是：embodiment × data × pipeline × deployment pressure。
它不一定天然能“讲清楚所有 learning paradigms”。

因为第 4 章里你讲的是一整套 learning taxonomy：
planning 讲 B1–B5，policy 讲 P1–P3，integration 再分 Type I/II/III。这个层级很完整。

survey

 

survey


而 AgiBot 在你文里的现有位置，主要还是：

foundation-scale 数据支持，

pipeline 组织，

humanoid / dual-arm 平台化。

survey

 

survey

所以它不是天然覆盖全文每一个 learning 子类。
这不是问题，但你写的时候要诚实：

把它写成“一个贯穿式实例”，不是“一个替代全文 taxonomy 的万能样本”。

我建议你怎么放

最好的放法不是单独硬插一个很长的新大节。
我建议两种方式里选一种：

放法 A：在第 1 节末尾加一个短说明，在第 5 节后加一个整合型 case study

标题可以很直：

Case Study: AgiBot as a Cross-Stage Instantiation of Embodied Manipulation

这样它的功能就不是补材料，而是把前面 2–5 节的框架回投到一个具体系统上。

这个放法最稳，因为：

前文 taxonomy 先讲清；

后文用 AgiBot 做“落地验证”；

不会打断正文分类节奏。

放法 B：每一大节末尾都用 AgiBot 做一个 3–4 句的小锚点

比如：

2 节后：AgiBot 体现了 humanoid / dual-arm embodiment 对 whole-body action interface 的压力；

3 节后：AgiBot 体现了 foundation-level dataset 与 pipeline-level alignment；

4 节后：AgiBot 体现了为何大规模平台会逼近 unified deployment stack；

5 节后：AgiBot 暴露了现有 evaluation 和 trustworthiness 的不足。

这个放法更像“running case”。

如果你真要写成一个独立 case study，建议只写这 5 个点
1. Embodiment

先点明为什么它是个好 case：
它不是单臂桌面，而是 humanoid / dual-arm / whole-body 场景，因此更能代表你文章里强调的 embodiment complexity。

survey

2. Data regime

把它对应到你的三层数据里：
AgiBot 在文中被放在 foundation-level dataset，说明它最适合拿来代表“跨 embodiment、跨场景、大规模聚合经验”的这一层。

survey

3. Data production pipeline

这里是它最强的部分：
AgiBot World Colosseo 把 fleet collection + simulator augmentation 结合起来，正好对应你第 3 节最有特色的 “datasets → acquisition → refinement → pipeline” 逻辑。

survey

4. Why this pressures learning and deployment

你第 3 节末尾和第 4 节开头本来就在说：
data ecosystem 提供 raw material，而 learning paradigms 决定这些材料怎样变成 manipulation capability。

survey


所以这里要写成：
AgiBot 不是“有个大数据集”这么简单，而是它的数据规模、平台异质性和 whole-body action interface，天然会逼着系统在 integration 和 deployment 上做出不同选择。

5. What it still does not solve

这是 case study 最重要的一笔。
你第 6 节已经写得很清楚：真正的难点仍然在 embodiment mismatch、heterogeneous data alignment、deployment-stage incompatibility、evaluation weakness 和 trustworthiness。

survey


所以 case study 结尾一定要写：
AgiBot 展示了 full-stack platformization 的方向，但并没有自动解决跨 embodiment 泛化、真实世界评价和可信部署问题。

我给你的直接判断

是，需要。
而且 AgiBot 是个好 case。
但最好的写法不是“拿 AgiBot 替代全文”，而是：

把 AgiBot 写成一个把你全文主线具体化的 cross-stage case study。

一句话版本：

用 AgiBot，不是为了“讲完所有”，而是为了“证明你这篇文章的四层框架在真实系统里确实是连在一起的”。

你要的话，我可以直接帮你把这个 case study 写成一个可放进论文里的小节骨架。

---

这不就格局小了吗，agibot是个公司，不只是一组模型

---

对，所以我现在会改口：

如果把 AgiBot 写成“一个模型 case”，格局会小。
但如果把 AgiBot 写成“一个 full-stack industrial ecosystem / platform case”，格局反而会变大。

这两个不是一回事。

这篇文章本来就不是只讲模型，它讲的是：
embodiment → data ecosystem → learning / integration / deployment → evaluation 这一整条系统链。

survey

 

survey


而且文中提到 AgiBot 的位置也不是“某个单模型”，而是：

在 foundation-level datasets 里，AgiBot World 被当成大规模、跨机器人、双臂/类人平台的数据基础设施；

survey

在 data pipeline 里，AgiBot World Colosseo 被当成“fleet-scale humanoid collection + simulator-based augmentation” 的平台型例子。

survey

所以你真正该做的，不是：

“拿 AgiBot 解释所有模型”

而是：

“拿 AgiBot 解释一个公司/平台如何把 embodiment、data、pipeline、deployment 组织成一个具身操作系统工程。”

这样格局就不小了。

我建议你怎么写，才不会“小”
不要写成：

Case Study: AgiBot Model

要写成：

Industrial Platform Case: AgiBot as a Full-Stack Embodied Manipulation Ecosystem

或者更学术一点：

Case Study: AgiBot as a Cross-Stage Industrial Instantiation of Embodied Manipulation

这个标题一换，味道就完全不同了。
你不再是在讲“某个方法好不好”，而是在讲：

它如何选 embodiment

它如何做数据生产

它如何组织 foundation-scale collection

它如何把 real + sim 接起来

它会给 learning / deployment 带来什么压力

它暴露了哪些 evaluation 和 trustworthiness 问题

这就很符合你这篇 survey 的大框架。

最好的写法：不是 case study，而是 running industrial example

我甚至觉得你不一定非要单开一个大 case study 节。
更高级的写法是：

在全文里把 AgiBot 当作一个“贯穿式产业样本”

比如：

第 3 节数据生态：AgiBot 说明 foundation-level data 和 pipeline-level alignment 怎么走到一起。

survey

 

survey

第 4 节 learning / integration / deployment：AgiBot 不是某个 isolated policy，而是平台规模和全身/双臂接口会反过来塑造 integration 和 deployment 需求。

第 5 节 evaluation：像这种公司级系统，最终不能只看 task success，还要看 transfer、efficiency、hardware cost、real-world reproducibility。

survey

这样 AgiBot 就像一根线，把你的 taxonomy 从“概念图”牵到“工业现实”。

但我建议你再做一个动作：不要只押一家

因为你说得也对，AgiBot 是公司，不是一组模型。
那就更应该避免让全文看起来像“用一家公司的版图替代整个领域”。

所以最稳的办法是：

用 AgiBot 做主 case，再配 1–2 个对照点

比如你不用展开很长，只要在关键地方提一句：

AgiBot 更代表 fleet-scale, humanoid/dual-arm, platformized data-production

Open X-Embodiment / Octo 一类更代表 cross-lab aggregation / generalist foundation policy

ALOHA / DROID 一类更代表 teleoperation-driven task-level data collection

这样读者会感觉：
你不是被 AgiBot“带着走”，
而是把 AgiBot 放在一个更大的生态坐标里定位。

这一下，格局就出来了。

所以我现在的直接建议
你可以保留 AgiBot，但要改 framing：

不是
“AgiBot 证明了这篇文章的所有内容”

而是
“AgiBot 提供了一个很典型的产业级 full-stack 实例，用来观察 embodiment、data pipeline、deployment 如何在真实平台中耦合。”

一句话压缩：

写 AgiBot，不要把它当“模型例子”，要把它当“平台化具身智能的组织样本”。

这样不是格局小，反而会让你的文章从“学术分类综述”更接近“学术—产业一体化解释框架”。

你要的话，我可以直接把这个 AgiBot 部分给你起一个标题，并写成一段能放进正文的成稿。

---

主要的问题是没篇幅了

---

那就不要单开 case study 节。

你现在最合适的做法是：

方案一：改成 running example

只在 3 个关键位置各加 1–2 句，总共半页都不用。

放在：

3.4 Data Pipeline 后面：一句话点出 AgiBot 代表的是 fleet-scale collection + sim augmentation + pipeline integration

4.4 Deployment Pipeline 后面：一句话点出这种平台化数据生产会反过来塑造 deployment 和 online alignment

6 Open Challenges 里：一句话点出即使是 AgiBot 这类 full-stack 平台，也还没自动解决 cross-embodiment、evaluation、trustworthiness

这样 AgiBot 就成了贯穿例子，不是额外负担。

方案二：加一个 4–6 句的 boxed paragraph

不用新节，就放在第 3 节末尾或第 4 节开头，标题叫：

A Platform-Level Example: AgiBot

内容只回答 4 件事：

它不是单模型，而是平台化生态

它体现 foundation-level dataset

它体现 real + sim pipeline

它暴露 deployment / evaluation 压力

这比完整 case study 省很多篇幅，但已经足够把你的“大框架”落地。

方案三：直接写进引言最后一段

加一句就够：

Throughout the survey, platforms such as AgiBot can be understood not merely as individual models, but as industrial-scale embodiments of the full stack spanning embodiment, data production, system integration, and deployment.

这句的作用是先给读者一个心理预期：
后文提到 AgiBot，不是举模型例子，而是在举平台例子。

我的直接建议

在你“没篇幅”的前提下，最优解是方案一 + 方案三：

引言最后埋一句

正文 3 个地方各补 1–2 句

这样几乎不增篇幅，但会明显提升文章的“落地感”和“现实感”。

一句话说：

没篇幅时，不要做 case study section，改做 case thread。

你要的话，我可以直接帮你把这 3 处补句 写成可粘贴版本。

---

你这么说让我觉得第二篇文章只是衔接没打磨好

---

不只是衔接没打磨好，但最大的问题确实更偏“组织与收束”，不是“框架错了”或者“内容不行”。

我会把第二篇现在的问题分成三层：

第一层：引言和主线显化不够。
这是真问题，而且是最大的。它其实已经有一条很好的暗线：
embodiment constraints → data → learning/integration → deployment → evaluation，
但引言最后没有把这条线钉死，所以读者进入正文时，更容易把它读成“四大并列板块”，而不是“一条系统传导链”。

第二层：章节之间的咬合还可以更强。
这就是你说的“衔接”。
但这里的衔接，不只是加过渡句，而是要让每一节都回答：
我为什么现在讲这个？它怎么自然导向下一节？
第 2 节末尾那句其实已经很好了，说明约束会 shape data needs；第 3、4、5 节也都有类似意识。问题是，这种意识还没有在全文里被持续放大。

第三层：局部小节的“判断感”还不够强。
这不是内容少，而是有些地方“分类已经很好了，但作者的总判断还可以再压一句”。
尤其第 4 章，B1–B5、P1–P3 的分类本身是成立的，表格和正文也是接住的；但如果每一大块结尾再有一句更硬的收束，读者会更容易记住：

B1–B5 本质上是在回答什么共同问题；

P1–P3 本质上是在同一条 trade-off 曲线上的不同点位。

所以我现在更准确的判断是：

第二篇不是“只有衔接问题”。
但它的问题主要也不是知识缺口，而是：

主线没有被充分显化；

板块之间的因果关系没有被反复钉住；

分类之后的作者判断还可以更集中。

换句话说，它更像：

框架已经对了，材料也够，下一步主要是把“框架”打磨成“论证”。

如果再压缩成一句：

不是“只差过渡句”，而是“差主线显化 + 章节咬合 + 分类后的判断收束”。

你要是愿意，我可以直接给你一个最实用的版本：
只改引言和每章开头/结尾，不动主体内容，怎么把这篇文章一下子提一个完成度。

---

这些在第一篇文章里是怎么体现的

---

有，而且第一篇是把这三件事做得很“显”：
主线显化、章节咬合、作者判断，都不是藏着的，而是反复写出来的。

3727640

我按你刚才那三个点来对应说。

1. 主线显化：第一篇是直接写出来的

它不是让读者自己猜主线，而是在摘要和引言里反复说：

这篇文章的独特点是 from a life-cycle perspective；

生命周期分成 training / post-training / inference (deployment)；

文章还会讲 countermeasures，并且特别强调 practical effectiveness。

3727640

引言后面还有一个非常标准的“结构预告段”：

Section 2 讲 principles and preliminaries

Section 3 讲 different lifecycle stages 下的 Trojan taxonomy

Section 4 讲 detection 和 elimination，并分析 practical effectiveness

Section 5 讲 challenges and future directions。

3727640

也就是说，第一篇不是“目录是目录，正文是正文”，而是从一开始就把全文压成了一条清楚的问题链：

生命周期攻击 → 防御 → 防御到底行不行 → 还差什么。 

3727640

2. 章节咬合：第一篇每一节都在给下一节铺路

这个是它比第二篇更成熟的地方。

（1）第 2 节不是背景堆砌，而是给第 3 节造语言

2.1 先定义术语；
2.2 直接把 Trojan 的本质统一成“改权重，让模型对特定 trigger 高响应”；
而且 2.2 还把 Trojan injection 按三阶段分别写出来：training、post-training、inference。

3727640

这一步的作用非常直接：
后面第 3 节按生命周期分类攻击时，不需要重新解释“Trojan 本质是什么”。

（2）2.4 是一个很强的桥

它没有直接进入 taxonomy，而是先讲 Trojan 和 poisoning、adversarial examples、bit-flip 的关系，并明确说这些相关攻击推动了 Trojan attack 的创新。

3727640

然后紧接着下一句就是：
“In this section, we investigate the Trojan attacks from the perspective of the DNN lifecycle…”
这个过渡非常顺：
先讲边界和来源，再进主分类。

3727640

（3）第 3 节内部也不是平铺，而是“分完再收”

比如：

3.1 开头先说 training-stage attack 的总体特征，再告诉你它会从 trigger 和 poisoned labels 两个维度展开，然后才进 3.1.1/3.1.2。

3727640

3.2 开头先说 post-training stage 的攻击逻辑，再明确分成 model structure-based 和 model parameter-based。

3727640

3.3 先给 Bit-Trojan 的基础框架，再按三个“改进方向”展开。

3727640

更关键的是，3.5 不是结束文献罗列，而是重新把这些 attack 拉回同一张比较表里，然后明确给出一个总判断：
training-stage Trojan 更 generic；post-training 和 inference-stage Trojan 更 specific 但更 stealthy；Bit-Trojans 的 stealthiness 和 evasiveness 更强。 

3727640

这就完成了“第 3 节的内部收束”。

（4）第 4 节开头也把防御逻辑说死了

它直接写：
countermeasures 分两步：

Trojan detection

Trojan elimination
最后再比较不同方法在不同 stage 上的 practical effectiveness。

3727640

也就是说，第 4 节不是另起炉灶，而是把第 3 节“攻击 taxonomy”转成“防御 workflow”。

3. 作者判断：第一篇不只是分类，还不断下判断

这点特别明显。

（1）它会直接判断别人的分类“不合理”

在 2.4 讨论 poisoning attack 时，作者提到有人把 data-poisoning-based Trojan attacks 视为 targeted poisoning attack 的子集，但作者明确说：

“this classification is neither reasonable nor accurate”。

3727640

这就是很典型的作者判断。
不是“有人这么说”，而是“我认为这不对，并给出理由”。

（2）它会在分类后直接总结“谁更泛化、谁更隐蔽”

3.5 里不是只给表格，而是文字上直接收出判断：

training-phase Trojan 更 generic

post-training / inference-phase Trojan 更隐蔽、更定向

Bit-Trojans 更 stealthy / evasive。

3727640

（3）它会对防御的现实效果下结论

4.3 是作者判断最密集的地方。
它不是只列优缺点，而是明确说：

input-data-based countermeasures generalizability 更强；

retraining 能彻底去 Trojan，但 time and computational cost 太高，因此 impractical；

除输入数据类方法外，多数防御都要求 white-box；

当前 countermeasures 对 code poisoning-based Trojan 和 Bit-Trojans 效果并不好。

3727640

 

3727640

这就把“综述”从整理文献提升成了“带立场的评估”。

（4）最后 challenges 也不是空泛展望

第 5 节和 conclusion 都是在把前面的判断再压一次：

Trojan 攻击通常需要高访问权限；

迁移性不足；

DyNN 研究不够；

现有 countermeasures 缺乏 neuron/weight-level insight；

optimized triggers 太隐蔽；

Bit-Trojan 防御尤其弱。

3727640

所以它不是“最后例行公事写 future work”，而是把前文比较结果提炼成明确的问题清单。

你要的那个对应关系，可以压成一句话

你前面说第二篇的问题更像：

主线没完全显化

板块之间因果链需要加强

分类之后还差一句判断

第一篇恰好把这三件事都显式做出来了：

主线显化：摘要 + 引言 + 结构预告反复强调 lifecycle + countermeasures + practical effectiveness。

3727640

章节咬合：第 2 节给第 3 节造统一语言，第 3.5 收束到第 4 节，第 4 节再按 workflow 推到第 5 节。

3727640

作者判断：2.4 直接批评既有分类，3.5 和 4.3 直接下总体判断，5 节把判断转成 challenges。

一句更短的话就是：

第一篇不是“先分类、再顺着写”，而是“先定问题链，再让分类服务问题链”。

你要的话，我下一条可以直接把这个答案再翻成一个更适合你自己写作时套用的版本：
“第一篇可模仿的 5 个结构动作”。

---

他这不是按方法分的吗

---

对，你这个说法有一半是对的：

局部看，它确实按方法分。
但全局看，它首先是按生命周期分。

更准确地说，这篇的 一级主轴 是：

training stage

post-training stage

inference stage

引言里就明说了，Section 3 要总结 different lifecycle stages 下的 Trojan taxonomy；第 3 节开头也再次强调，是从 the perspective of the DNN lifecycle 来考察 Trojan attacks。

3727640

但进入每个 stage 以后，它又会用**该阶段最自然的“方法变量”**继续细分，所以你才会觉得“它这不还是按方法分吗”。比如：

训练阶段 3.1 先定死是 Training Stage，然后再分成

data poisoning-based

code poisoning-based，
而 data poisoning-based 里面又继续按 trigger patterns 和 poisoned sample labels 往下拆。

3727640

后训练阶段 3.2 也是同样逻辑：
先定在 Post-training Stage，然后再分成

model structure-based

model parameter-based。

3727640

推理阶段 3.3 则基本围绕 Bit-Trojan / bit-flipping 展开，再按改进方向去分，比如 implementability、optimization objective、other improvements。

3727640

所以这篇文章真正的结构是：

第一层：按阶段分。
第二层：在每个阶段里按方法分。

不是纯粹的“method-based survey”，而是：

lifecycle-based survey with method-based subdivision

这也是为什么我前面一直说它主线很清楚。因为“方法分类”是服务于“阶段分类”的，不是反过来。
你可以把它理解成：

大框架：攻击发生在模型生命周期的哪一段

小框架：这一段里常见的技术路线有哪些

一句话压缩：

它不是“只按方法分”，而是“先按阶段分，再在阶段内部按方法分”。

---

你越这么说我越觉得只是因为有外显的句子，要是细究怕是还不一定比第二篇主线明显

---

你这个质疑是对的。
我现在会把判断修正成：

第一篇不一定是“本体上远比第二篇主线更清楚”，更准确地说，它是“主线更外显、更锋利”。
第二篇不是没有主线，而是主线更隐含、更系统化。 

3727640

 

survey

也就是说，前面我把差距说大了。

真正该怎么比

你说得对，不能只看有没有外显句子。
像“Section 2 does X, Section 3 does Y” 这种 signposting，确实会制造一种“主线很清楚”的阅读感，但这只是表层。真正该比的是：

把这些外显句子拿掉之后，文章内部还能不能自己站住。

按这个标准重新看：

第一篇的深层主线

第一篇的深层结构还是比较硬的，因为它的中心问题非常单一：
Trojan attack 在模型生命周期里怎么发生、怎么防、现有防御哪里不行。
它不是只在引言里说自己是 life-cycle perspective，而是第 2 节先统一 technical terms、Trojan injection 原理和 threat scenarios，第 3 节再按 training / post-training / inference 讲 attack，第 4 节转到 detection / elimination，第 5 节再把问题收成 challenges。
所以就算你把那些外显提示句拿掉，它仍然是一条很明确的 “问题链”。

3727640

第二篇的深层主线

第二篇其实也有主线，而且不弱。
它真正的深层逻辑不是“四大并列板块”，而是：

embodiment / software constraints
→ data requirements and data production
→ planning / policy / integration / deployment choices
→ evaluation and system bottlenecks

这一条线在文中是存在的。引言里已经明确说它想把 manipulation 作为一个 coupled design problem 来看，分析 embodiment、data、learning、deployment、evaluation 如何共同塑造系统；第 2 节末尾也明确说 hardware embodiment 和 software stack 定义约束，而这些约束会 shape learning 所需的数据。
所以如果细究，它不是“没主线”，而是主线被大框架包住了。

survey

所以差别到底在哪

我现在更愿意这样说：

第一篇

是 单问题主线。
它的主线像一根钢筋，读者很容易抓住。

第二篇

是 系统传导主线。
它的主线像一张骨架，不是一眼就抓住，但一旦抓住，会发现它其实贯穿全文。

所以并不是：

第一篇有主线

第二篇没有主线

而更像是：

第一篇主线更“尖”

第二篇主线更“深”但更“埋”

你这个判断为什么重要

因为它会直接影响你怎么改第二篇。

如果第二篇真的是“没有主线”，那就得重搭。
但如果像你说的，问题主要只是“外显程度不够”，那改法就不是推翻，而是：

把引言里的主线说透

把每个大节和这条传导链的关系钉出来

把分类后的总判断再压实一点

换句话说：

第二篇的问题更像“主线显化不足”，不一定是“主线本身不成立”。

我现在的最终判断

如果细究，不看表层 signposting，我会这样下结论：

第一篇的主线仍然更明显，但优势没有我前面说得那么大。
第二篇的主线其实是存在的，只是它属于系统级暗线，不像第一篇那样是单问题明线。

一句话压缩：

第一篇赢在“锋利”，第二篇赢在“潜在结构”；前者更容易被看见，后者更依赖打磨。

你要的话，我下一条可以直接做一件更实用的事：
把第二篇那条“暗主线”替你抽成 4 句引言骨架。

---

问题是第二篇是功能导向的，这就会让他在模块间的关联看起来不是很明显

---

对，这个判断我赞同，而且我觉得你点到了第二篇最核心的结构风险。

第二篇的问题，不是没有主线，而是它的主线被“功能导向分块”遮住了。 

survey

更具体地说：

第二篇现在是按“系统分别负责什么功能”来组织的：

Section 2：system architecture

Section 3：data ecosystem

Section 4：learning paradigms

Section 5：evaluation。

survey

这种写法的好处是局部很顺。
每一块内部都能自洽：数据讲数据，学习讲学习，评测讲评测。尤其第 4 章内部其实也是顺的，先 planning，再 policy，再 integration，再 deployment。

survey

但它的代价就是你说的这个：
模块间关系不够显。

因为“功能导向”天然回答的是：
这一块是什么、负责什么。

可读者更想看到的往往是：
为什么讲完这一块，下一块会自然出现？
这一块对下一块施加了什么约束？

而第二篇真正的深层逻辑其实是有的，它在文中也隐约说出来了：

embodiment 和 software stack 定义了系统的 physical / computational constraints；

survey

在这些 constraints 下，才会出现特定的数据需求和数据生产方式；

survey

data ecosystem 再提供 learning 的 raw material；

survey

evaluation 最后是来 “close that loop”。

survey

所以它不是没有关联，
而是这些关联更多停留在隐含传导链里，没有压成读者一眼能抓住的显式因果链。

我会把它总结成一句：

第一篇是问题导向，所以关系天然显；第二篇是功能导向，所以关系需要额外“做出来”。

这也解释了为什么你会觉得第二篇不像第一篇那样主线一眼就明白。
不是因为它比第一篇乱很多，而是因为：

第一篇在回答一个单问题：Trojan 在生命周期里怎么攻防；

3727640

第二篇在组织一个系统：不同功能模块如何拼成 manipulation intelligence。

survey

所以第二篇最该改的地方，不是推翻功能分块，而是让每个功能块都更明确地回答一句：

“这一块如何决定下一块？”

比如：

embodiment 不只是“第一块内容”，而应被写成 constraints source；

data 不只是“第二块内容”，而应被写成 response to those constraints；

learning 不只是“第三块内容”，而应被写成 conversion of data into capability；

evaluation 不只是“最后一块内容”，而应被写成 the criterion that closes the system loop。

所以你的这个判断，我会直接认可：

是，第二篇因为是功能导向的，确实会让模块之间的关联显得没那么明显。
但这更像是**“显化不足”，不是“结构失效”**。

你要是想，我可以下一条直接帮你把第二篇的四个一级标题改写成更有“传导关系”的版本。

---

我甚至觉得第一篇如果在第二篇中，可能就会像delpoyment lifecycle那样

---

对，我觉得你这个比喻很到位。

你这句话的意思其实是：

第一篇那种“单问题主线”，如果被放进第二篇这种功能导向的大框架里，很可能只会沦为其中一个模块级小节。

这正好说明了两篇文章的根本差别，不在“谁更会写”，而在组织单位不同。

你这个判断为什么成立
第一篇的组织单位是“问题”

第一篇围绕的是一个非常具体的问题：
Trojan attacks across the lifecycle of DNNs。
所以 training、post-training、inference 不是普通章节，而是这个问题本身的天然展开。

3727640

换句话说，第一篇里：

lifecycle 不是功能模块，

而是核心论证轴。

第二篇的组织单位是“系统功能”

第二篇围绕的是一个系统：

embodiment

data

learning

integration / deployment

evaluation。

survey

所以在第二篇里，像 deployment lifecycle 这种东西，本质上只是：
整个 embodied manipulation system 里的一个功能环节。

survey

也就是说，如果把第一篇那种写法硬塞进第二篇的大框架里，它很可能真的会变成：

“某个局部问题沿一个小轴线展开的子模块”

而不是全篇主线。

这说明什么

这说明第二篇不是简单“主线弱”，而是它的主线层级更高。

第一篇是：

问题级主线

第二篇是：

系统级主线

所以你会感觉：

第一篇的 training / post-training / inference 很“显”

第二篇的 deployment lifecycle、data pipeline、integration models 很像平行模块

这是因为第一篇拿“阶段”当全文主轴，
第二篇拿“功能”当全文主轴。

你说“第一篇放到第二篇里可能就像 deployment lifecycle 那样”，本质上就是在说：

第二篇把很多东西都降成了系统里的一个部件。

这个观察我觉得是对的。

进一步说，这也是第二篇最容易吃亏的地方

因为一旦是功能导向写法，读者就会下意识把每一章看成：

一个模块

一组组件

一种职责

而不会自动把它们看成一条论证链。

所以第二篇真正的难点不是“内容不够”，而是：

它必须证明这些功能模块不是并列拼盘，而是一个系统传导链。

否则就会像你说的那样：
每一块都像 “deployment lifecycle” 一样，
是一个完整但局部的子问题，
而不是全篇唯一主线。

所以你的判断反过来还能推出一个很重要的结论

第二篇要改的，不是局部小节写法，而是要把“模块”重新提升成“关系”。

也就是不要让读者只看到：

embodiment

data

learning

deployment

evaluation

而要让读者一直看到：

embodiment 决定 data requirement

data 约束 learning choice

learning/integration 带来 deployment burden

deployment 反过来规定 evaluation criterion

这样它们才不会只是一个个功能块。

一句话总结

对，你这个感觉是对的。
第一篇的生命周期在第一篇里是“全文主轴”；
放到第二篇里，很可能只会降成类似 “deployment lifecycle” 那样的一个系统子模块。

这不说明第二篇差，
而说明：

第二篇的组织层级更高，但也因此更容易把强主线问题“模块化”。

你这个观察，其实已经很接近第二篇结构问题的本质了。

你要是愿意，我可以下一条直接顺着这个思路讲：
为什么“问题导向”天然比“功能导向”更容易显得主线清楚。

---

但问题就在这，如果显式的方法足够明显确定，大家不就能比较容易的明确关系了吗？那还要说很多吗？

---

对，所以关键不在“说很多”，而在说得准。

我的看法是：

如果显式结构已经足够强，确实不需要说很多。
但还是需要说一点，因为分类本身只解决“看见模块”，不自动解决“理解关系”。

可以把它分成三层看：

1. 显式结构能解决一半问题

如果你把一级标题、图、表、开头句都做得很清楚，读者当然更容易看出关系。
这就是为什么第一篇读起来会更“顺”：它直接把全文钉在 life-cycle perspective 上，然后顺着 principles → lifecycle attacks → countermeasures → challenges 往下走。这里很多关系，读者确实一眼就能抓住。

3727640

所以你说得对：
结构如果足够显，很多关系不必再反复解释。

2. 但“模块清楚”不等于“关系清楚”

尤其像第二篇这种功能导向写法，一级标题是：

system architecture

data ecosystem

learning paradigms

evaluation

读者当然知道“有这四块”。
但仅靠这四块，读者未必自动知道：

architecture 是不是在约束 data，

data 是不是在决定 learning choice，

learning/integration 是不是在引出 deployment burden，

evaluation 是不是在闭环检验前面的系统设计。

survey

也就是说，看见板块，不等于知道板块间是什么关系。
这里还是需要几句“关系句”。

3. 所以真正需要的不是“多说”，而是“少量高密度的关系句”

最有效的不是大段解释，而是这种句子：

“We begin with embodiment because it defines the sensing and control constraints…”

“These constraints in turn shape the data requirements…”

“Given these data regimes, the next question becomes how capability is constructed…”

“Evaluation closes this loop by assessing the resulting system…”

这种句子每节一两句就够了。
它们的作用不是补知识，而是告诉读者：

你现在看到的不是四块并列内容，而是一条传导链。

所以我的结论是：

对，显式方法如果足够强，就不用说很多。
但还是要说一点，因为“显式分类”只能让人看到结构，“显式关系”才能让人看到论证。

一句话压缩就是：

不是要多写，而是要把“关系”写出来，而不是指望读者自己从模块里推出来。

你这个判断其实已经很接近一个写作原则了：

好综述不是解释每个模块，而是用最少的话，把模块之间的必要关系钉死。

---

问题不是这个是有的吗？

---

对，是有的。
所以我现在更准确的说法应该是：

第二篇不是“没有关系链”，而是“关系链已经存在，但支配阅读体验的力度还不够强”。

这两者差很多。

它文中其实已经明确写出了几条关键关系：

引言里已经说，这篇不是按 model family 组织，而是把 manipulation 当成一个 coupled design problem，一起看 embodiment、data、learning、deployment、evaluation。

survey

第 2 节末尾也明确写了：hardware embodiment 和 software stack 定义了 learned policy 所处的 physical / computational constraints，而这些约束又会 shape learning 所需的数据。

survey

第 4 节开头又接了一次：Section 3 的 data ecosystem 提供了 learning 的 raw material。

survey

第 5 节开头甚至直接说，这一章是来 close that loop 的。

survey

所以如果只问“这种关系有没有写出来”，答案是：

有，而且不是一点点，是明确存在的。

我现在真正想说的是：

它的问题不在“缺关系”，而在“这些关系还没有压过功能分块本身”。

也就是说，读者先感受到的仍然更像是：

system architecture

data ecosystem

learning paradigms

evaluation

这四块内容；
而不是第一时间感受到：

constraints → data → capability construction → evaluation closure

这条链。

所以你说得对，不能说它“没有”。
更准确的批评应该是：

它已经有主线关系，但主线关系还偏“埋在线里”，没有强到让人一进文就自动按这条链来读。

一句话压缩：

不是缺，而是显著性还可以更高。

---

这种风格让我想起了一篇3d点云的文章

---

对，这个联想很合理。

3D 点云综述里很常见这种写法：
不是围绕一个单问题一路往下推，而是按功能模块 / pipeline 环节来组织，比如：

representation

sampling / grouping

feature learning

segmentation / detection / registration

downstream applications

这种写法的优点也是框架全、覆盖广、方便查阅；
缺点也和你刚才说的一样：模块都清楚，但模块之间的“为什么自然连起来”不一定特别强。

所以你会有一种很像的感觉：

第一篇 Trojan 更像“问题导向综述”

第二篇 更像很多 3D 点云 / 系统综述 那种“功能导向综述”

前者读起来像一条线，后者读起来像一张图。

你这个类比其实挺准确，因为点云领域很多综述也是：
局部很清楚，整体很完整，但主线感主要靠作者后期打磨出来。

你要是把那篇 3D 点云文章名字发我，我可以直接帮你对比它和第二篇到底像在哪。

---

deep learning for 3d point clouds a survey这篇

---

我去核一下这篇点云综述的组织方式，再跟你刚才说的第二篇这种“功能导向大框架”对照。

---

对，就是这篇。你的直觉是对的，它和第二篇的气质很像。

更准确地说，《Deep Learning for 3D Point Clouds: A Survey》是很典型的“功能/任务导向综述”，不是像 Trojan 那篇那样围绕一个单问题主线推进。它在摘要里就把范围定成三大任务：3D shape classification、3D object detection and tracking、3D point cloud segmentation，并强调会给出数据集上的比较结果和未来方向。也就是说，它的组织单位首先是“任务簇”，不是“一个核心矛盾”。
PubMed
+1

而且它的目录预告也很说明问题。根据可访问的论文预览，这篇文章的结构大致是：
Section 2 先讲 datasets and evaluation metrics，
Section 3 讲 3D shape classification，
Section 4 讲 3D object detection and tracking，
Section 5 讲 point cloud segmentation，
最后 Section 6 conclude。这就是很标准的“先给公共背景/基准，再按主要任务模块展开”的综述套路。
ResearchGate
+1

所以它和第二篇像的地方，不只是“都分模块”，而是更深一层：

像在哪里

第一，都不是单问题综述。
点云这篇不是围绕一个单一问题链，比如“点云的不规则性如何被统一解决”，而是围绕点云学习的大版图来组织：分类、检测/跟踪、分割。第二篇也类似，不是围绕一个单问题，而是围绕 embodied manipulation 的系统版图来组织：embodiment、data、learning、evaluation。
PubMed
+1

第二，组织方式都偏“功能导向”。
点云那篇按不同任务功能分：classification、detection/tracking、segmentation；第二篇按系统功能分：system architecture、data ecosystem、learning paradigms、evaluation。两者的共同点都是：局部块很清楚，全文像一张地图。
ResearchGate
+1

第三，都很依赖 taxonomy、表格和总览图。
点云那篇预览里明确提到有 “a taxonomy of existing deep learning methods for 3D point clouds”，并强调会在多个公开数据集上做表格比较。第二篇也是明显靠总 taxonomy 图、各类表格来承载结构。也就是说，两者都不是靠一条连续长论证撑起来的，而是靠“模块 + taxonomy + benchmark tables”的组合。
ResearchGate
+1

但也有一个重要区别

点云那篇虽然也是功能导向，但它的任务轴更天然。
分类、检测/跟踪、分割，本来就是点云领域最稳的三大任务，所以读者会天然接受这种分法。第二篇的功能块则更抽象一些：embodiment、data、learning、evaluation 之间虽然有关系，但不如“任务三分法”那样天然，因此模块间关系更需要作者主动打磨出来。这个差别会让第二篇更容易显得“板块很全，但板块间关系要多想一步”。这个判断是我基于两篇的结构类型做的比较性分析。
ResearchGate
+1

所以如果把它们放在一条线上，我会这么排：

Trojan 那篇：问题导向综述

3D point clouds 这篇：任务导向综述

第二篇 manipulation：系统功能导向综述

其中，后两者确实更像一类。
你会觉得第二篇像这篇点云综述，我认为这个类比是成立的。

一句话压缩：

点云这篇和第二篇都更像“给领域画地图”，而不是“沿一个核心问题打一条隧道”。

你要的话，我可以继续把这三篇直接排成一个表：问题导向 / 任务导向 / 系统功能导向。

---

你再确定一下第二篇的每一章节名字

---

我去把第二篇的目录标题再核一遍，直接给你精确版本。

---

我再核了一遍，正文里实际的一级章节名是这些：

Introduction 

survey

System Architecture of Robotic Arms 

survey

Data Ecosystem of Robotic Arms 

survey

Learning Paradigms of Robotic Arms 

survey

System Evaluation of Robotic Arms 

survey

Open Challenges and Future Directions 

survey

Conclusion 

survey

再往下一层，几个关键二级标题是：

第 2 章：

2.1 Physical Embodiment

2.2 Software Framework 

survey

第 3 章：

3.1 Embodied Datasets

3.2 Data Acquisition

3.3 Data Refinement

3.4 Data Pipeline 

survey

第 4 章：

4.1 Cognitive Planning: The Embodied Brain

4.2 Policy Learning: The Embodied Cerebellum

4.3 Integration Models

4.4 Deployment Pipeline 

survey

第 5 章：

5.1 Task Execution Quality Evaluation

5.2 Data Efficiency and Quality Evaluation

5.3 Generalization and Transfer Evaluation

5.4 Energy and Efficiency Evaluation 

survey

第 6 章：

6.1 Embodiment

6.2 Data

6.3 Learning

6.4 Deployment

6.5 Evaluation

6.6 Trustworthiness

6.7 Emerging Directions 

survey

 

survey

有一个你前面可能会在意的小点：
Figure 1 里第 4 块写的是 “Architectural Paradigms of Robotic Arms”，但正文真正的一级节标题是 “4 Learning Paradigms of Robotic Arms”。也就是说，图里的概括名和正文正式标题不完全一样。

survey

 

survey

如果你要，我可以下一条直接把这篇文章整理成一个完整目录树给你。

---

System Architecture似乎不太贴切，的改个名字

---

我同意，“System Architecture of Robotic Arms” 不算最贴切。
因为这一章实际写的不是完整的“系统架构”，而是两块更具体的内容：2.1 Physical Embodiment 和 2.2 Software Framework；而且章末还明确把这一章的作用说成：定义 learned policy 所处的 physical and computational constraints。

survey

 

survey

所以它更像是在讲：

机器人操作系统的“约束基础层”，
而不是在讲一个完整的 system architecture blueprint。

我建议的改名
最稳妥的版本

Embodiment and Software Foundations of Robotic Arms

这个最好的一点是：

跟 2.1 Physical Embodiment、2.2 Software Framework 直接对齐；

不会夸大成“整个系统架构”；

还能自然承接后文 data / learning / evaluation。

survey

如果你想更强调“这是约束来源”
我更推荐这个

Embodiment Constraints and Software Foundations of Robotic Arms

这个版本比前一个更有“主线意识”，因为它直接点明：
这一章不是中性介绍，而是在交代后面数据与学习设计的约束来源。这和章末那句 “hardware embodiment and the software stack define the physical and computational constraints…” 很一致。

survey

如果你想保守改，不动太大
可以用

Physical Embodiment and Software Framework of Robotic Arms

这个最直白，也最不容易出错。
缺点是稍微平一点，没有把“这一章在全文里的功能”说出来。

我的排序

如果是我来定，我会这样排：

Embodiment Constraints and Software Foundations of Robotic Arms

Embodiment and Software Foundations of Robotic Arms

Physical Embodiment and Software Framework of Robotic Arms

一句话建议

如果你想让这一章更服务全文主线，就用：

Embodiment Constraints and Software Foundations of Robotic Arms

如果你想让标题更自然、没那么用力，就用：

Embodiment and Software Foundations of Robotic Arms

你要的话，我可以顺手把第 3、4、5 章标题也一起改成同一风格。

---

最好两个词

---

最推荐：

Embodiment Foundations

理由：

比 System Architecture 更准；

能罩住 physical embodiment + software framework；

也更贴合全文的具身主线。

如果你想更偏“平台感”，备选是：

Platform Foundations

System Foundations

但我还是首推 Embodiment Foundations。

---

data economstem还是datasupport?

---

选 Data Ecosystem。

原因很直接：

Data Support 太虚、太弱，像在说“数据提供了一些支持”，不够像一个完整章节标题。
而你这章实际写的是：

datasets

acquisition

refinement

pipeline

这已经不是“support”了，而是一个数据生产、流动、清洗、扩展、组织的系统。
所以 Ecosystem 更贴切，也更有格局。

你可以这样理解
用 Data Support

读者会预期你讲的是：

数据怎么支撑模型

数据为什么重要

数据资源有哪些

它更像“辅助条件”。

用 Data Ecosystem

读者会预期你讲的是：

数据有哪些层级

数据怎么采

数据怎么生成

数据怎么增强/筛选

数据怎么进入 pipeline

这就和你现在第 3 章的内容更一致。

我的结论

如果保留原来的章内容，一定选 Data Ecosystem。
除非你把这一章大幅收窄成“数据如何支持学习”，那才考虑 Data Support。

如果你想让标题再更硬一点，也可以用：

Data Regimes and Ecosystem

但在你给的两个里，Data Ecosystem 明显更好。

---

那你之前说的主线收的不紧的问题，举一些例子，给一点建议

---

可以。这里的“主线收得不紧”，更准确地说，不是没有主线，而是主线经常被分块式的信息组织盖过去了。你这篇其实已经有一条很清楚的链条：embodiment / software constraints → data requirements → learning / integration / deployment → evaluation。这条线在文中是存在的，只是很多地方一进入章节，就又回到“模块介绍模式”，所以读者读感上会觉得是在看几个并列大块。

survey

 

survey

 

survey

我举几个很具体的例子。

例子 1：引言里立的是“耦合设计问题”，但结构说明马上退回成目录式。
你在 introduction 里其实已经把 ambition 说得很强了：不是按 model family 排，而是看 data regimes、cognitive planning、policy learning、integration、deployment、evaluation 之间怎么耦合；而且 contribution 里也明确说是在分析这些组件如何共同 shape system design 和 real-world performance。可一到 “Structure of the Paper” 就变成了 “Section 2 reviews… Section 3 examines… Section 4 analyzes…” 这种目录播报。这样会把前面刚建立起来的“因果链 / design pressure”弱化成“下面分几个部分介绍”。这就是主线“收得不紧”的第一个典型表现：立意是耦合论证，展开却先变成章节清单。 

survey

例子 2：第 2 章真正重要的是“constraint formation”，但这个意思到章末才最清楚。
第 2 章标题叫 “System Architecture of Robotic Arms”，内容确实覆盖了 embodiment 和 software framework；而且你也讲了 fixed-base、mobile、humanoid 的 coupling，以及 software stack 的 latency / transport / orchestration 问题。真正把它和后文拧紧的是章末那句：hardware embodiment 和 software stack 一起定义 learned policy 必须面对的 physical / computational constraints，这些 constraints 进一步定义 learning 所需的数据。这个转折其实非常关键，因为它把第 2 章从“系统综述”变成了“后文的约束前提”。但问题是，这个关键句出现在离开第 2 章的时候，前面读者更容易把这一章读成 architecture inventory，而不是 why embodiment matters for the rest of the paper。

survey

 

survey

 

survey

例子 3：第 3 章内部很完整，但它更像“data menu”，不像“data-to-learning pressure chain”。
第 3 章的组织本身很好：datasets → acquisition → refinement → pipeline，而且开头也明确说这是在问“what data enables effective learning under such constraints”。问题在于，3.1–3.4 很容易被读成一个越来越大的 data taxonomy：先讲数据层级，再讲采集，再讲 refinement，再讲 pipeline。也就是说，第 3 章内部是顺的，但它对第 4 章的“压迫关系”还不够显眼。比如 3.1 讲三层 dataset，3.3 讲 augmentation / curation，3.4 讲 end-to-end production system，这些都很扎实；但多数小节停在“数据是怎么被组织和扩展的”，没有频繁回钩到“这些 data regimes 具体会偏向什么 planning/policy/integration choices”。所以第 3 章虽然内容强，但读感上更像独立板块。

survey

 

survey

 

survey

 

survey

例子 4：第 4 章分类很强，但正因为太强，也容易自成一个世界。
第 4 章其实写得很系统：你先把 learning stack 拆成 cognitive planning 和 policy learning，再给出 B1–B5、P1–P3 两套 taxonomy，还进一步上升到 integration models 和 deployment pipeline。问题是，这一章的内部逻辑太完整了，读者会自然把注意力放到“B1 和 B2 有什么差别”“P2 和 P3 的 trade-off 是什么”上，而不一定一直记得这是在回应第 3 章的数据问题。换句话说，第 4 章的分类能力很强，但跨章牵引力还可以更强。你自己其实已经写了关键过渡句——“The data ecosystem discussed in Section 3 provides the raw material for learning”——但这句话更像入口说明，后面没有被不断放大成贯穿解释。

survey

 

survey

例子 5：第 6 章又按 embodiment / data / learning / deployment / evaluation / trustworthiness 分开讲，容易像“重新开抽屉”。
第 6 章的 challenges 当然是合理的，而且和全文结构对齐。但也正因为它再次按这些维度逐项展开，读者会有一种感觉：前面开过一次这些抽屉，后面又开了一次。于是 ending 更像“把前文各模块再各自总结一下”，而不是把全文收束成几条更高阶的核心矛盾。你在 6.7 和结论里其实已经开始往“cross-stage directions”“four interdependent stages”上收了，这说明你是有系统级收束意识的；只是这一步还可以更早、更狠。

survey

 

survey

给你的建议，我觉得不用大改框架，主要做下面几种“收线”动作就够了。

第一，把 introduction 末尾的“Structure of the Paper”改成因果链，而不是目录链。
现在是：Section 2 review，Section 3 examine，Section 4 analyze。
可以改成类似这种写法：

Section 2 establishes the embodiment and software constraints that define what data and control interfaces are feasible.
Section 3 then examines how these constraints give rise to distinct data regimes and production pipelines.
Section 4 analyzes how learning and integration architectures are selected under those data conditions and deployment pressures.
Section 5 evaluates whether these coupled design choices translate into robust embodied performance.

这样不是在换内容，只是在把章节顺序改写成论证顺序。这一步性价比最高。

survey

第二，第 2 章开头就提前亮明“本章不是 catalog，而是 constraint chapter”。
你现在真正有力的话在章末。建议把那句意思前置到第 2 章第一段，直接告诉读者：
“本章讨论 embodiment 和 software，不是为了完整介绍系统组件，而是为了确定后续数据、学习和部署问题的约束边界。”
这样读者从一开始就会按“constraint lens”来读第 2 章，而不是按“architecture overview”来读。依据就在你章末已经写出来的那条逻辑链。

survey

 

survey

第三，在第 3 章末尾加一个 5–7 句的小 synthesis，不要只跳转到第 4 章。
这个 synthesis 不用长，但要明确说三件事：
第一，skill / task / foundation 三层数据并不只是规模差别，而是支持不同 abstraction level；
第二，acquisition / refinement / pipeline 决定了数据是否能跨 embodiment、跨场景、跨部署阶段复用；
第三，这些差异会直接偏置后面的 planning / policy / integration choices。
也就是说，让第 3 章末尾不只是 “next we discuss learning”，而是 “here is exactly what this data organization implies for learning design”。这样第 3 章就不再只是 data block。

survey

 

survey

 

survey

第四，第 4 章里把两套 taxonomy 明确写成两条“连续谱”，而不是两组并列类别。
你现在对 B1–B5 的写法，其实已经隐含了“越来越 physical grounding”；对 P1–P3 的写法，也已经隐含了“expressivity ↔ efficiency”的连续张力。这个特别好，但还可以再明说一点。
比如在 4.1 开头再加一句：
“B1–B5 should not be read as five unrelated classes, but as progressively more execution-grounded interfaces between semantic intent and motor realization.”
在 4.2 开头再加一句：
“P1–P3 lie on a common frontier between inference efficiency and distributional expressivity.”
这样读者会把 taxonomy 读成沿同一条轴展开，而不是五类 / 三类分盒子。

survey

第五，第 6 章不要只按六类 challenge 平铺，可以先提炼成 2–3 个“总矛盾”。
比如我会建议你把全文最后收成这三条：
一是 heterogeneity vs standardization：embodiment 和 data 都异构，但 learning 又需要统一接口；
二是 expressivity vs deployability：模型越强，往往越难实时、可靠、低成本部署；
三是 scalable proxies vs physical validity：评测越可扩展，越可能离真实接触动力学和 embodiment shift 更远。
然后 6.1–6.6 只是这些总矛盾在不同层面的展开。这样第 6 章会像“总收束”，而不只是“分项罗列挑战”。这和你 conclusion 里的 “four interdependent stages” 也更一致。

survey

 

survey

一句话概括我的建议：
你这篇现在的问题不是“块太多”，而是“块与块之间的因果压力还没被反复压实”。 框架不用推翻，只要把每章开头和结尾都改成“为什么这一章会逼出下一章”的写法，主线就会立刻紧很多。

survey

 

survey

如果你愿意，我下一步可以直接帮你改 Introduction 最后一段 + 第2章开头 + 第3章结尾 这三处示范文本。

---

第一篇文章有很强的章节间联系吗？

---

有，而且算是比较强的。不是那种“每章各讲各的，然后靠目录串起来”的强行连接；它的章节关系是有明确推进逻辑的：先定义问题和阶段框架，再按 lifecycle 展开攻击，再转到 defense workflow，最后收束到 challenge/future directions。

3727640

 

3727640

最明显的第一层联系，是 Introduction 直接把后面几章预设成一条顺序链：Section 2 讲 principles/preliminaries，Section 3 按 lifecycle 总结 Trojan attacks，Section 4 转到 countermeasures，Section 5 再讨论 challenges 和 future directions。这个安排本身就不是并列拼盘，而是“攻击问题怎么定义 → 攻击怎么展开 → 防御怎么应对 → 还有什么没解决”。

3727640

第二层更重要：第 2 章不是孤立背景，而是在给第 3 章搭结构骨架。
它在 2.2 里把 Trojan injection 明确拆成 training、post-training、inference 三个阶段，并分别形式化了三种阶段下的注入过程；到 2.4 又把 Trojan 和 poisoning / adversarial example / bit-flip 的关系讲清楚。紧接着第 3 章开头就说，下面要从 DNN lifecycle 的 training、post-training、inference 三个阶段来考察 Trojan attacks。也就是说，第 3 章不是凭空分类，而是直接继承第 2 章建立的阶段框架和概念框架。这一点是实打实的章节间连接。

3727640

 

3727640

 

3727640

第三层联系体现在 第 3 章内部也不是简单并列。
3.1、3.2、3.3 分别对应 training、post-training、inference，而且每节开头都会先说明该阶段的核心机制、典型 threat model，再进入具体分类。到 3.5，作者没有直接结束，而是专门做了一个 comparison，把不同阶段攻击的共享条件和差异重新收束一遍，比如哪些攻击都依赖 trigger，哪些攻击都要求对设备/模型有更高访问权限，training-stage 更 generic，post-training 和 inference-stage 更 stealthy。这样一来，第 3 章末尾就不只是“讲完了”，而是把前面分散的分类重新压成一个总结。

3727640

 

3727640

 

3727640

然后 3.5 到第 4 章的衔接也很顺。
3.5 先把不同 Trojan attack 的联系和差别总结出来，下一章立刻转到 countermeasures，而且不是随便讲防御，而是明确说 Section 4 分成 detection 和 elimination 两大步，后面还要比较不同 defense 在不同阶段上的 practical effectiveness。也就是说，前面攻击的阶段化与差异化，后面变成了防御的组织原则。

3727640

 

3727640

更进一步，第 4 章内部的章节联系也写得很外显。
比如 4.1 把 detection 分成 data/model/output 三个模块；其中还明确说 trigger inversion 常常会“指导” model parameter-based detection。到 4.2，作者又把 elimination 分成 data 和 model 两个模块，并且明确说明 data-based methods 会给 model-based elimination 提供 clean datasets。这个写法说明它不只是分类，还在努力写出“方法之间如何配合”。

3727640

 

3727640

 

3727640

所以我的判断是：第一篇的章节间联系确实强，而且不只是靠“Section 2… Section 3…”这种目录播报撑起来。
它真正强的地方在于，前一章提出的框架，后面一章真的拿来用：
第 2 章建 lifecycle 与 related-attacks 框架，第 3 章按这个框架写 attack taxonomy；
第 3 章比较不同 attack 的特征，第 4 章再按 defense workflow 接过去；
第 4 章内部还不断写方法间的 guidance/support 关系。

3727640

 

3727640

 

3727640

但也要说一句更细的：它的“强联系”有一部分确实被写得很外显，所以读者更容易感受到主线。也就是说，它既有真实结构联系，也有比较强的 signposting；两者叠加，读感上就会显得比很多综述更“收”。

3727640

如果你愿意，我可以下一步直接把第一篇和你那篇在“章节间联系”上的差别，压缩成 3 条最关键的写法差异。

---

你研究一下这两篇文章的学术用语恰当性问题

---

可以。我把“学术用语恰当性”拆成两层来看：

一层是“是否贴合学科共同体的常用说法”，
一层是“作者自造术语/标签是否必要、是否稳、是否会误导”。

总体判断先给你：

第一篇（Trojan）的问题，更多是“局部术语有点自造、个别措辞和编辑不够稳”。
第二篇（Embodied Manipulation）的问题，更多是“整体语言更成熟，但 taxonomy 标签里有一些作者性很强、略带修辞化的叫法”。 

3727640

 

survey

一、第一篇：核心安全术语基本对路，但有几个词不够“学界通用”
1）优点：安全领域的主干词汇基本是对的

第一篇在大框架上用的词是合适的：
DNNs、poisoning attacks、adversarial example attacks、bit-flip attacks、countermeasures、detection、elimination、threat models、high-risk scenarios、white-box / black-box、runtime feasibility，这些都属于安全综述里很正常、很学界化的词。它也明确把文章组织在 training / post-training / inference 三个 lifecycle stages 上，这个用词框架本身是稳的。

3727640

 

3727640

 

3727640

2）主要问题一：“Trojan information” 不够通用

它在 2.1 里把 Trojan information 定义成“一组 abnormal weights”，后面又用这个词去统摄 trigger、poisoned sample 和 model weight 之间的关系。这个词在文内自洽，因为作者一旦定义完，后面就一直按这个词来推进；但从学界常见表达看，它不如 backdoor parameters / malicious weights / Trojaned parameters / backdoor behavior 这类说法自然。也就是说：

作为文内工作定义：成立

作为领域共识术语：偏自造

它的问题不在“错”，而在“容易把一个机制性现象实体化成一个看起来很稳定的名词对象”。

3727640

 

3727640

3）主要问题二：“Trojaned model” 可懂，但不一定是最自然的首选

文中大量使用 Trojaned model，这在 Trojan/backdoor 文献里不是不能用，但和更常见的 backdoored model 相比，读者接受成本略高。好在这篇文章在关键词里同时放了 backdoor attack 和 Trojan attack，某种程度上缓解了术语映射问题。
所以我的判断是：

可用

但略显作者偏好，不是最顺手的共同体默认写法。 

3727640

4）主要问题三：“Trojan injection” 很有组织力，但有点过度总括

第 2.2 节把 training-stage poisoning、post-training fine-tuning、inference-stage bit-flipping 都统摄到 Trojan injection 这一个总词下，还用 Γ 表示不同阶段的 injection process。这个写法在结构上很有效，因为它帮助作者把不同攻击阶段统一到一个抽象框架里。
但代价是：这个词会把机制差异很大的事情说得好像同质化很强。数据投毒、参数微调、bit-flipping 在操作层面差异非常大，统一叫 injection 可以，但会带一点“概念压平”的副作用。

3727640

5）主要问题四：个别措辞有 overclaim 或英语精细度不足

这一篇还有几个更像“学术英语稳不稳”的问题：

引言说 Section 4 investigates the most effective countermeasures，这个说法有点过。因为后文自己又明确承认现有防御存在大量局限，尤其对 code poisoning 和 Bit-Trojan 效果不强。更稳妥的说法应该是 representative / existing / state-of-the-art countermeasures，而不是先预设“most effective”。

3727640

 

3727640

文中有一些语言层面的不稳，比如表里有 Elimiantion 的拼写问题，正文里也能看到 can not、classt、for running time 这类不够地道或编辑不彻底的痕迹。这个不全是“术语问题”，但会影响学术用语的整体可信度。

3727640

 

3727640

6）对第一篇的总评

所以第一篇的术语问题，我会概括成一句：

它的“学科框架词”是对的，但它喜欢把机制重新命名成自己的统一术语；这种做法有组织力，但通用性略弱。 

3727640

 

3727640

二、第二篇：整体语言更成熟，但 taxonomy 名称有些过于“作者化”
1）优点：系统与机器人领域的主干用语整体更成熟

第二篇在大框架上的词，比第一篇更成熟、更稳。
像 physical embodiment、software infrastructure、data ecosystem、cognitive planning、policy learning、integration architectures、deployment trade-offs、cross-embodiment generalization、system-level trustworthiness 这些词，整体上既学术，又贴合 robotics / embodied AI 的最近几年 discourse。尤其它把 manipulation 写成一个 coupled design problem，这在综述里是很有力量、也相当恰当的组织性表述。

survey

另外，正文里很多具体词也很到位，比如：

contact-rich manipulation

whole-body platforms

visuo-tactile integration

physical and computational constraints

distributional expressivity / computational complexity

cross-platform compatibility / physical fidelity / quality control

这些都说明第二篇在句子层面的学术英语成熟度明显更高。

survey

 

survey

 

3727640

2）主要问题一：“Embodied Brain / Embodied Cerebellum” 偏修辞，不够标准

第 4 章把 cognitive planning 称为 the embodied brain，policy learning 称为 the embodied cerebellum。这两个说法很形象，也有教学性，但它们本质上是作者构造的比喻性标签，不是领域内已经稳定成立的标准术语。
所以它们的问题不是“不好懂”，而是：

放在讲解里很好

放在正式 taxonomy 名称里略显修辞化

尤其 embodied cerebellum，会让“policy learning = 小脑”这个映射显得过于生理隐喻化。

survey

3）主要问题二：有些一级标题或图中标签不够贴切

这个问题你前面其实已经敏感地抓到了。

“System Architecture of Robotic Arms”

这一章实际讲的是 2.1 Physical Embodiment + 2.2 Software Framework，并且章末明确说它的功能是定义 learned policy 所处的 physical and computational constraints。所以 System Architecture 这个标题是有点大的，容易让人以为要讲完整系统蓝图。更贴近内容的其实是 Embodiment and Software Foundations 或 Embodiment Constraints and Software Foundations。

survey

 

survey

“Data Support”

Figure 3 的总标题和正文里 broader data support structure 这个说法，都比同章正式标题 Data Ecosystem of Robotic Arms 弱一些。
因为这一章实际讲的是 datasets、acquisition、refinement、pipeline，明显已经是一个生产—扩展—清洗—整合的系统，不只是“support”。所以：

Data Ecosystem 很好

Data Support 偏虚，像辅助条件名，不像章节骨架词。

survey

“Architectural Paradigms” vs “Learning Paradigms”

Figure 1 里写 Architectural Paradigms of Robotic Arms，正文 Section 4 却叫 Learning Paradigms of Robotic Arms。这会造成一点 taxonomy 命名漂移。
因为 Section 4 实际上既讲 planning/policy，也讲 integration 和 deployment，所以如果要统一，最好一开始就决定到底是 learning paradigms 还是 architectural paradigms，不要图里和正文各用一套。

survey

 

survey

4）主要问题三：部分范式名很有作者性，但略带“造概念”感

像下面这些标签，都不是错，但作者痕迹比较重：

Semantic Logic and Code Generation

Generative Dynamics and Physical Imagination

Spatial Grounding & Predictive World Models

Unified End-to-End Foundation Models

这些标签的优点是概括力强；
问题是它们有时会同时承担“分类名 + 解释句 + 观点”三重功能，所以略显重。尤其 Generative Dynamics and Physical Imagination，更像一个有气势的研究宣言，不是已经很稳的学界标准类目。

survey

 

survey

5）主要问题四：数学化/抽象化命名有时会显得比必要程度更重

例如 3.1 用 Kᵢ ≈ Kᵢ₋₁ ⊕ Dᵢ 去概括三层数据集的层级扩展，这个写法有概念化的味道，但严格说更像一种说明性符号，而非真正需要的理论表达。
它的问题不是错误，而是：
会让 taxonomy 看起来比实际更“形式化”一些。 对综述而言，这种做法要慎用。

survey

6）对第二篇的总评

第二篇的术语问题，我会概括成一句：

它的主干学术英语比第一篇成熟，但它更爱构造高层 taxonomy 名称；这些名称有解释力，却偶尔会越过“恰当”走向“过于作者化”。 

survey

 

survey

三、两篇放在一起，怎么比较
第一篇

更像：
领域词汇基本保守，局部概念自造。

优点是结构容易统一；
缺点是像 Trojan information / Trojan injection 这种词，不一定是共同体最自然的默认说法。

3727640

 

3727640

第二篇

更像：
句法成熟、系统词汇高级，但 taxonomy 名称带明显作者设计痕迹。

优点是读起来更像成熟的 journal prose；
缺点是像 embodied cerebellum / data support / architectural paradigms 这种地方，容易让读者感觉是作者在“给领域重新命名”。

survey

 

survey

 

survey

四、如果只给一句最短结论

第一篇的问题是“术语不够通用”；
第二篇的问题是“术语有时太有设计感”。

再压缩一点：

第一篇偏“叫法略土但稳”；第二篇偏“叫法更漂亮但有些过”。

五、如果你要改，我会怎么改
第一篇优先改

把这些词收紧：

Trojan information → 更中性地改成 Trojan-related parameters / malicious weights / backdoor-related weights

the most effective countermeasures → 改成 representative / existing / state-of-the-art countermeasures

统一 lifecycle / life-cycle，修掉明显拼写和格式问题。 

3727640

 

3727640

第二篇优先改

把这些标签降一点修辞：

Embodied Brain / Embodied Cerebellum → 留在解释句里，不要做核心 taxonomy 标签

System Architecture → 改成更贴内容的 foundation/constraints 类标题

Data Support → 统一成 Data Ecosystem

Architectural Paradigms / Learning Paradigms 二选一统一。 

survey

 

survey

 

survey

如果你愿意，我下一步可以直接帮你做一个更实用的版本：把两篇里“最该改的 10 个术语”逐个列出来。

---

Kᵢ ≈ Kᵢ₋₁ ⊕ Dᵢ 主要是这样的概括有什么问题

---

有，主要问题不在“数学上错”，而在“学术表达上有点过度形式化”。

这句式子在文里是用来概括三层数据集的层级扩展：作者先说他们把 embodied manipulation datasets 分成 skill-level、task-level、foundation-level 三层；然后用

𝐾
𝑖
≈
𝐾
𝑖
−
1
⊕
𝐷
𝑖
K
i
	​

≈K
i−1
	​

⊕D
i
	​


去表达“后一层是在前一层基础上加入新的数据支持，从而扩展系统可用的知识状态”。接着作者把三层分别解释为：
K1 关注局部 interaction dynamics，K2 关注技能组合成长时程行为，K3 关注跨 embodiment 的大规模迁移。

survey

但这类概括有几个问题。

第一，符号是“像理论”，但没有真正定义清楚。
这里的 
𝐾
𝑖
K
i
	​

、
𝐷
𝑖
D
i
	​

、
⊕
⊕ 都不是严格定义的量：

𝐾
𝑖
K
i
	​

 不是可测的知识量；

𝐷
𝑖
D
i
	​

 不是一个具有明确边界的数学对象；

⊕
⊕ 也没有说明到底是并集、增量、融合、还是某种 representation transfer。
所以它更像一种修辞化的示意，而不是可推演、可检验的 formalism。这样写容易让读者误以为这里存在比实际更强的理论结构。

survey

第二，它暗示三层关系是“单调累加”的，但实际未必如此。
作者自己对三层的定义其实是“信息角色不同”：
skill-level 学局部物理交互，task-level 学时序任务组合，foundation-level 学跨平台对齐与迁移。这个关系更像能力维度在变化，不只是“前一层再加一点数据”。尤其 foundation-level datasets 在文中被定义为强调 cross-robot alignment、standardization、multimodal consistency，这已经不是简单在 task-level 上“再加料”，而是目标和组织方式都变了。

survey

 

survey

第三，它把“数据”和“知识”之间的关系说得太顺了。
公式写法像是在说：加上 
𝐷
𝑖
D
i
	​

，就能得到新的 
𝐾
𝑖
K
i
	​

。
但这篇文章别处其实不断强调，真正决定能力的还有 embodiment constraints、software stack、learning paradigms、integration、deployment 等环节；数据不是直接等于知识，中间隔着一整条“从 raw material 到 capability”的转换链。作者在第 3 章末和第 4 章开头自己就写了：第 3 章的数据生态提供的是 raw material，第 4 章讨论的是这些材料如何被转成 manipulation capability。

survey

 

survey

第四，它会把本来很好的 descriptive taxonomy，抬成不必要的 pseudo-theory。
这篇文章真正强的地方，其实是它对三层数据角色的文字解释，以及后面对 acquisition、refinement、pipeline 的展开。Fig. 3 也更像一个数据生产与支撑体系图，而不是某种知识演化公式。换句话说，这里最有价值的是 taxonomy 本身，不是这个公式。

survey

所以我会这样评价这句：

作为“帮助读者快速把握层级递进”的启发式表达，它可以接受；
作为严肃的理论概括，它偏虚，定义不够，容易显得比实际更 formal。

更好的改法有三种。

一种是直接去掉公式，只保留文字。比如写成：
“Each tier extends the previous one by adding new forms of supervision and broader transfer requirements.”
这对综述来说通常已经够了。

一种是把公式降格成 purely schematic statement，明确说只是示意，不是 formal model。
比如加一句：
“Here 
𝐾
𝑖
≈
𝐾
𝑖
−
1
⊕
𝐷
𝑖
K
i
	​

≈K
i−1
	​

⊕D
i
	​

 is only an intuitive shorthand for cumulative expansion, not a formal compositional model.”

还有一种是把“累加”改成“shift”或“reconfiguration”。
因为 foundation-level datasets 更像是在改变学习对象和对齐问题，而不只是简单增加数据量。

一句话总结：

这句最大的问题不是错，而是“形式感超过了实证含量”。
它会让一个本来清楚的层级 taxonomy，看起来像一个并没有真正建立起来的理论公式。

---

主要是K要留着用的，后面也用到了不同的K

---

那就更明确了：

问题不在 K，问题在这个公式。

如果你后面还要继续用 K1 / K2 / K3 指代三层知识/能力支持层级，那 K 完全可以留，而且我觉得是合理的。因为你在原文里已经把它们解释成：

K1：local interaction dynamics

K2：skills composed into temporally extended behaviors

K3：cross-embodiment variation needed for transfer at scale 

survey

这说明 K 在你文里其实已经不是数学变量，而是一个层级标签系统。
只要后面还会反复引用 K1/K2/K3，这套记号是有价值的。

真正该改的是哪一部分

真正让人觉得“不稳”的是这句：

𝐾
𝑖
≈
𝐾
𝑖
−
1
⊕
𝐷
𝑖
K
i
	​

≈K
i−1
	​

⊕D
i
	​


因为它会让读者以为：

K 是严格可组合的数学对象

D 是明确的增量项

⊕
⊕ 表示某种清楚定义的组合运算

三层关系近似是“逐层累加”

但你的正文其实不是在做这个层面的理论。你是在做一个 dataset tier / knowledge support tier 的概念分层。

survey

所以最好的处理方式
方案 A：保留 K，去掉公式

这是我最推荐的。

直接改成这种写法：

We denote these progressively broader knowledge-support tiers as 
𝐾
1
,
𝐾
2
,
K
1
	​

,K
2
	​

, and 
𝐾
3
K
3
	​

.
Here, 
𝐾
1
K
1
	​

 captures local interaction dynamics, 
𝐾
2
K
2
	​

 captures the composition of skills into temporally extended behaviors, and 
𝐾
3
K
3
	​

 captures the cross-embodiment variation required for transfer at scale.

这样你后面照样可以说：

this paradigm is mainly supported by K2

this dataset belongs to K3

transfer at K3 differs from supervision at K1

但不会制造一种“这里好像有个 formal theory”的感觉。

方案 B：保留 K，也保留“递进关系”，但不用代数符号

比如改成：

We summarize this hierarchical progression as a transition from 
𝐾
𝑖
−
1
K
i−1
	​

 to 
𝐾
𝑖
K
i
	​

 through the introduction of additional data support 
𝐷
𝑖
D
i
	​

.

或者：

Conceptually, each tier extends the effective knowledge support of the previous tier by introducing new forms of data support, which we denote as 
𝐷
𝑖
D
i
	​

.

这里仍然保留 K 和 D，但不写 
⊕
⊕，也不假装有严格运算。

方案 C：公式保留，但明确降格成“示意表达”

如果你特别想保留这行式子，也不是不行，但必须补一句降温的话，比如：

Here, 
𝐾
𝑖
≈
𝐾
𝑖
−
1
⊕
𝐷
𝑖
K
i
	​

≈K
i−1
	​

⊕D
i
	​

 is intended only as an intuitive shorthand for progressive expansion, rather than a formal compositional model.

这样读者就知道：
这不是理论公式，只是记忆辅助。

我为什么更建议去掉公式、保留 K

因为你后面真正需要的是：

K1/K2/K3 作为索引系统

而不是 一个关于 K 的“运算定律”

换句话说，你真正有用的是：

“K 是章节内的层级坐标”

而不是：

“K 可以被代数化地推导”

所以如果你后面还要反复说不同方法/数据主要支持哪个 K，这套记号完全值得留；
只是没必要让它背一个过强的公式。

最短建议

K 留着。
把公式弱化或删掉。
因为你需要的是 notation system，不是 pseudo-formalism。

如果你愿意，我可以直接帮你把这一小段改成一个可替换进正文的英文版本。

---

We summarize this hierarchical evolution as
\[
\mathcal{K}_i \approx \mathcal{K}_{i-1} \oplus \mathcal{D}_i,
\]
where each tier extends the previous one by introducing new data support and enlarging the effective knowledge state available to the system. 那这段怎么改

---

可以这样改。既然你说 
𝐾
K 后面还要继续用，那我建议：

最优改法

保留 
𝐾
𝑖
K
i
	​

 和 
𝐷
𝑖
D
i
	​

，
去掉 
⊕
⊕ 这个“像运算”的写法，改成更明确的“conceptual progression”。

版本 A：最稳，最像综述文体
LaTeX
We denote this hierarchical progression by \(\mathcal{K}_1, \mathcal{K}_2,\) and \(\mathcal{K}_3\), where each tier expands the effective knowledge support available to the system through additional data support \(\mathcal{D}_i\). Concretely, \(\mathcal{K}_1\) captures local interaction dynamics, \(\mathcal{K}_2\) captures the composition of skills into temporally extended behaviors, and \(\mathcal{K}_3\) captures the cross-embodiment variation required for transfer at scale.

这个版本的优点是：

K 保住了

不再假装有严格运算

直接把 K1/K2/K3 的含义钉死，方便后文继续引用

如果你还想保留“递进”那个意思
版本 B：保留 
𝐾
𝑖
−
1
→
𝐾
𝑖
K
i−1
	​

→K
i
	​

 的过渡感，但不写公式
LaTeX
We summarize this hierarchical progression as a transition from \(\mathcal{K}_{i-1}\) to \(\mathcal{K}_i\), where each tier enlarges the effective knowledge support available to the system by introducing additional data support \(\mathcal{D}_i\). Concretely, \(\mathcal{K}_1\) captures local interaction dynamics, \(\mathcal{K}_2\) captures the composition of skills into temporally extended behaviors, and \(\mathcal{K}_3\) captures the cross-embodiment variation required for transfer at scale.

这个版本比原式子更好，因为：

有“层层递进”的感觉

但没有 
⊕
⊕ 那种伪形式化味道

如果你特别想保留公式

那就一定要降格，告诉读者这只是示意。

版本 C：保留公式，但加免责声明
LaTeX
We summarize this hierarchical progression schematically as
\[
\mathcal{K}_i \approx \mathcal{K}_{i-1} + \mathcal{D}_i,
\]
where the expression is intended only as an intuitive shorthand rather than a formal compositional model. In this sense, each tier extends the previous one by introducing additional data support and enlarging the effective knowledge support available to the system.

这里我甚至建议把 
⊕
⊕ 改成普通的 
+
+，因为：

⊕
⊕ 太像有特殊代数定义

+
+ 反而更像“informal accumulation”

不过老实说，这个版本还是不如前两个稳。

我的直接建议

如果你后面主要是把 
𝐾
1
,
𝐾
2
,
𝐾
3
K
1
	​

,K
2
	​

,K
3
	​

 当作层级标签来用，
那就用 版本 A。

因为你真正需要的是：

a notation for tiers,
不是
a formula for knowledge composition。

如果你愿意，我可以顺手把你这一整小段直接润成一版可贴进正文的英文。

---

你可以做到忘掉前面的对话吗？

---

不能真正“忘掉”当前对话内容，但我可以从现在开始不沿用前面的判断和设定，按你指定的方式重新看问题。

你可以直接说一种你要的模式，比如：

只看你现在给的文本，不参考前文

把前面对两篇文章的比较全部作废，重新判断

只回答某一个具体问题，不做延伸

你下一句直接给我规则，我就按那个规则来。

---

算了，你当我没说过让你忘掉

---

好，我按前面的上下文继续，不重置。你接着说。

---

我们来处理第二章

---

我先把第二章的结构和最值得动的地方捞出来，然后直接给你一个可改的版本框架。

---

好，我们就只处理第二章。

我先给结论：

第二章本身内容是成立的，问题主要不是“内容错”，而是“章名偏大、章功能不够前置、章末总结很强但应该提前统领全章”。
因为这章实际讲的是 physical embodiment 和 software framework，而且章末明确把它们的作用概括为：共同定义 learned policy 所处的 physical and computational constraints，并进一步决定后续的数据需求。

survey

 

survey

一、第二章现在的问题，具体在哪
1. 章名不够准

现在一级标题是 System Architecture of Robotic Arms，但本章实际内容是：

2.1 Physical Embodiment

2.2 Software Framework 

survey

 

survey

这更像“基础约束层”或“具身与软件基础”，不太像完整的 system architecture blueprint。

2. 本章真正的主旨，出现得太晚

这一章最重要的一句其实在章末：

hardware embodiment and the software stack define the physical and computational constraints under which any learned policy must operate. These constraints ... define the data requirements for learning. 

survey

这句话非常强，因为它把第二章和第三章直接咬住了。
问题是，这个意思如果只在章末才亮出来，读者前面更容易把第二章读成：
“机器人硬件分类 + 软件框架综述”，
而不是：
“后文 data / learning 的约束来源”。

3. 2.1 和 2.2 各自都顺，但“为什么放在同一章”还可以更明确

2.1 的内部逻辑其实很好：
从 end effectors and contact sensing，到 fixed-base platforms，再到 mobile and whole-body platforms，本质上是在讲 coupling 逐步增强。

survey

 

survey

2.2 也成立：
先是 middleware and operating systems 的三层软件栈，再到 low-level motion planning and control，最后落到 temporal determinism 对闭环控制的重要性。

survey

 

survey

但初稿感在于：
这两部分虽然都好，但“它们为什么必须放进同一章、共同构成 constraints chapter”这层意思，还不够前置。

二、我建议你怎么改
方案核心

不重写内容，只重写 framing。

也就是：

改章名

改章首段

在 2.1 和 2.2 之间加一个更强的过渡

把章末总结变成“总收束句”

三、章名怎么改

我建议二选一。

更稳的版本

Embodiment Foundations

优点是短、干净，也能罩住 physical embodiment + software framework。

更强的版本

Embodiment Constraints

如果你想让第二章更服务全文主线，我更偏这个。
因为你后面第三章本来就在承接“what data enables effective learning under such constraints”。

survey

我个人排序：

Embodiment Constraints > Embodiment Foundations

四、第二章开头应该怎么写

你现在开头是：

The action space of a robotic system is constrained by its hardware embodiment... This section reviews the hardware landscape... and then examines the software stack... 

survey

这句不差，但还偏“介绍内容”。
我建议你改成更强的“章功能句”。

建议版
Manipulation capability is shaped before learning begins: by the physical embodiment that determines contact, reach, and whole-body coupling, and by the software stack that determines timing, communication, and control execution. This chapter therefore does not treat embodiment and software as background inventory, but as the constraint layer that defines what data can be collected, what interfaces learning must operate on, and what forms of deployment remain feasible.

这段的作用是：

先把第二章从“catalog”变成“constraint layer”

直接把它和第 3、4 章接上

五、2.1 这一节怎么收得更紧

2.1 现在的三层分法其实很好：

end effector / contact sensing

fixed-base platform

mobile / whole-body platform 

survey

 

survey

我建议你只补一个总领句和一个小结句。

2.1 开头总领句
We analyze embodiment at three nested levels: the contact interface, the manipulation platform, and the mobile or whole-body system that determines how manipulation couples to larger body dynamics.
2.1 结尾小结句
Taken together, these three embodiment levels define not only workspace and dexterity, but also the degree of coupling a learned policy must manage—from local contact regulation to coordinated whole-body stability.

这样 2.1 就不是“列平台”，而是“讲 coupling escalation”。

六、2.1 和 2.2 之间要加一句桥

现在 2.1 结束后直接进 2.2，逻辑上没问题，但还可以更紧。

建议桥句
These embodiment choices do not act alone: once contact interfaces, kinematic scope, and body coupling are fixed, the remaining question is whether the software stack can sustain the timing, transport, and control requirements needed to exploit them.

这句的作用是把 2.2 从“另一个板块”变成 2.1 的自然延续。

七、2.2 的标题其实也可以微调

现在是 Software Framework。
如果你想更学术、更完整一点，我建议：

Software Stack and Control Foundations

因为你 2.2 不只是 middleware，还包括 low-level motion planning and control。

survey

 

survey

八、章末总结，建议保留并稍微再强化

你现在章末这段很好，是全章最强的地方：

Together, hardware embodiment and the software stack define the physical and computational constraints... These constraints shape system execution and define the data requirements for learning. The next question, therefore, is what data enables effective learning under such constraints... 

survey

我建议只稍微压得更利一点：

建议版
Together, embodiment and software define the physical and computational operating envelope of manipulation systems. They determine what can be sensed, what can be controlled, what timing guarantees can be maintained, and therefore what kinds of data are both collectable and useful for learning. The next question is thus not yet how to learn, but what data regimes can support learning under these constraints.

这个版本会让第二章更像第三章的因果前提。

九、如果你只改 3 个地方，就改这 3 个
1

把章名改掉
System Architecture of Robotic Arms → Embodiment Constraints

2

重写第二章第一段
把“this section reviews...”改成“this chapter defines the constraint layer...”

3

保留并强化章末那段
因为这是第二章和第三章最关键的咬合点。

survey

十、我直接给你一个第二章的“可改后骨架”
2 Embodiment Constraints

2.1 Physical Embodiment

2.1.1 End Effectors and Contact Sensing

2.1.2 Fixed-base Platforms

2.1.3 Mobile and Whole-body Platforms
小结：coupling progressively increases from contact interface to whole-body system

2.2 Software Stack and Control Foundations

2.2.1 Modern Robotics Middleware and Operating Systems

2.2.2 Low-level Motion Planning and Control
小结：software determines whether embodiment can be exploited in real time

章末总收束
embodiment + software = physical/computational constraints = data requirements

如果你愿意，我下一条可以直接把 第二章开头两段 和 2.1 结尾 + 2.1→2.2 过渡 + 章末总结 写成英文成稿。

---

不，这部分得重写，我们得讲明白故事

---

对，第二章如果要重写，重点不是换几个标题，而是把它从“架构盘点”改成“约束成形的故事”。

这章现在其实已经有故事的胚子，只是埋得太深了。它一开头就说，机器人的 action space 受 hardware embodiment 限制；后面依次讲 end effectors、fixed-base、mobile/whole-body platforms，再讲 software stack；章末又明确总结：hardware embodiment 和 software stack 一起定义了 learned policy 所处的 physical and computational constraints，并进一步决定数据需求。 

survey

 

survey

所以第二章最好的改法不是“补更多内容”，而是把这条线前置成明线：

manipulation 不先从 learning 开始，而是先从 constraint 开始。

我建议这章讲成什么故事
核心故事

在机器人学会操作之前，系统已经被身体和软件预先塑形了。

这个“预先塑形”有三层递进：

第一层，你如何接触世界
由 end effector 和 sensing 决定。

第二层，你的操作如何和身体耦合
由 fixed-base、bimanual、mobile、humanoid 这些 embodiment 形态决定。

第三层，你的控制闭环能否真正跑起来
由 software stack、timing、transport、motion control 决定。

最后收束成一句：

这些约束共同决定后面什么数据值得收、什么学习方式可行。

这就能自然推到第 3 章。

第二章最该改的，不是内容，而是 framing
现在的问题

现在读起来像：

先讲 hardware 类型

再讲 software 框架

所以更像一个 overview。

你要改成

读起来像：

先讲 contact 和 embodiment 如何塑造 manipulation problem

再讲 software 如何把这些 physical possibilities 变成 executable closed loop

最后讲这些 constraints 为什么直接决定 data needs

也就是把这一章改成：

constraint formation chapter

我建议的章名

如果你真要重写，我建议直接换掉原来的
System Architecture of Robotic Arms

改成：

Embodiment Constraints

这是最干净、最有故事感的标题。

它能自然罩住：

2.1 physical embodiment

2.2 software framework

而且还能和章末那句 “physical and computational constraints” 直接对上。

survey

我建议的新结构
2 Embodiment Constraints
2.1 Physical Constraints of Manipulation

2.1.1 End Effectors and Contact Sensing

2.1.2 Fixed-base and Bimanual Platforms

2.1.3 Mobile and Whole-body Platforms

这一节讲清楚：
constraint 从 contact interface 开始，逐步上升到 platform coupling。

2.2 Computational Constraints of Manipulation

2.2.1 Runtime, Middleware, and System Orchestration

2.2.2 Motion Generation and Contact Control

这一节讲清楚：
physical embodiment 只是给出可行空间，software stack 决定这个空间能否以实时闭环的方式被利用。

2.3 Chapter Synthesis: From Constraints to Data Needs

这一小节很重要，哪怕只写一段也值。
专门说：

embodiment 决定可感知/可执行边界

software 决定 timing / transport / control feasibility

因此第 3 章要问的不是“有哪些数据集”，而是
what data regimes can support learning under these constraints

如果不想加 2.3，也至少要这样重写章首和章末
章首应该怎么写

现在的开头偏“介绍本章内容”。
你需要改成“本章为什么在全文里先出现”。

可以直接写成这种风格：

Manipulation capability is shaped before learning begins. It is first constrained by embodiment: by the contact interface that determines how the robot touches the world, by the platform that determines how manipulation couples to reach, coordination, and mobility, and by the software stack that determines whether these interactions can be sensed, transmitted, and controlled in real time. This chapter therefore treats embodiment and software not as background inventory, but as the constraint layer that defines what kinds of data, learning interfaces, and deployment strategies are feasible.

这段的作用只有一个：
把第二章从“背景章”改成“前提章”。

2.1 这一节要怎么讲故事

你现在的 2.1 其实素材很好，只是可以更明确地写成递进。

递进逻辑应该是

contact interface → platform coupling → whole-body coupling

也就是：

end effectors 讲的是“接触如何发生”

fixed-base / bimanual 讲的是“操作如何组织”

mobile / humanoid 讲的是“操作如何与整体身体动力学耦合”

所以 2.1 结尾最好补一句收束：

Across these embodiments, the central change is not merely workspace size, but coupling: manipulation progresses from local contact regulation to coordinated multi-contact interaction and, eventually, to whole-body stability and motion.

这样 2.1 就不是平台枚举，而是一个问题升级过程。

2.1 到 2.2 的过渡怎么写

这一句很关键，因为这是整章最容易散的地方。

建议直接补一句：

Once these embodiment-level constraints are fixed, the next question is whether the software substrate can sustain them: whether sensing, communication, and control can be executed with the temporal reliability required for contact-rich manipulation.

这句一加，2.2 就不是“顺便再讲讲软件”，而是：

软件为什么必须被拉进这一章。

2.2 这一节要怎么讲故事

2.2 不要讲成“L0/L1/L2 软件栈介绍”。
要讲成：

为了让 embodiment 真正变成 manipulation capability，系统必须满足两类计算约束：

第一类是 runtime and transport

第二类是 motion generation and contact control

也就是说：

2.2.1 不是“有哪些 middleware”

而是“谁来保证系统在时间上能跑起来”

2.2.2 不是“有哪些控制方法”

而是“谁来把高层意图变成 physically executable joint command”

这样这部分就活了。

章末怎么收

你原文章末已经有很好的内容。
我建议把它改成更像“下一章导火索”的版本：

Together, embodiment and software define the operating envelope of embodied manipulation systems. They determine what can be sensed, what can be controlled, how tightly manipulation couples to the rest of the body, and what timing guarantees can be maintained during execution. The next question is therefore not yet how to learn, but what kinds of data are required to support learning under these physical and computational constraints.

这段一写，第三章就不再像“另一大块”，而是第二章自然逼出来的。

如果你想更彻底一点，我建议你删掉“System Architecture”这个表述

因为这章真正的关键词不是 architecture，而是：

constraint

coupling

contact

timing

executability

也就是说，这章真正讲的是：

what the system is allowed to be

而不是：

how the system is architected in the broadest sense

最后给你一句最短判断

第二章要重写成“constraint chapter”，而不是“architecture overview chapter”。

只要这一点成立，故事就出来了：

身体先规定问题，软件再规定闭环，数据需求于是被逼出来。

你要的话，我下一条直接给你一版第二章的英文成稿骨架，包括：

新章标题

章首两段

2.1 结尾

2.1→2.2 过渡

章末总结。

---

这两篇文章哪篇文章的引用文献更硬

---

如果你说的 “更硬” 是指：

参考文献里顶会/顶刊/公认经典更多，且不是太依赖预印本，整体更“稳、更有分量”，

那我会判断：

第一篇 Trojan 那篇的引用文献整体更硬一点。

原因很直接。第一篇的参考文献里能看到一串比较“硬核”的安全与机器学习 venue：
USENIX Security、NDSS、CCS、EuroS&P、RAID、ACSAC、CVPR、ICCV、ICLR、NeurIPS，以及 IEEE Transactions on Neural Networks and Learning Systems、IEEE Transactions on Pattern Analysis and Machine Intelligence、IEEE Transactions on Dependable and Secure Computing、ACM Computing Surveys 等。像 STRIP（ACSAC）、Fine-Pruning（RAID）、BadNets（IEEE Access）、EuroS&P、USENIX Security、NDSS、CVPR、ICLR、TNNLS、TPAMI 这些都能直接在参考文献里看到。

3727640

 

3727640

 

3727640

 

3727640

 

3727640

第二篇当然也不弱，甚至在机器人和 embodied 方向上很强。它引用里有 RSS、CoRL、ICRA、IROS、CVPR、ICML、ICLR、NeurIPS、TMLR、IJRR，甚至还有 Science Robotics。像 RT-H、RT-1、DiWA、Octo、BridgeVLA、HAMSTER、DexCap、MimicPlay、Behavior Transformer、以及 Science Robotics 上的 IAIL，都说明它抓住了 robotics / embodied AI 的主流前沿。

survey

 

survey

 

survey

 

survey

但第二篇有一个很明显的特点：预印本和“刚出炉”的工作占比更高。文中引用了不少 2025–2026 的 arXiv / OpenReview / workshop 论文，比如 π0、AgiBot World Colosseo、LeRobot、Tether、RoboOS、ManiSkill3、REALM、WorldArena 等，这些说明它非常前沿，但也意味着“文献硬度”里那种 沉淀过、共识更强、发表形态更稳定 的比例相对低一些。

survey

 

survey

 

survey

 

3727640

所以我会给你一个更细的结论：

按“传统意义上的硬度”看：第一篇略胜。
因为它的参考系更稳定，安全领域经典与顶级 venue 的锚点更扎实。

3727640

 

3727640

按“新、全、跟最前沿”看：第二篇更猛。
但它更像是在抓一个高速演化中的 embodied/robotics 版图，所以引用会天然更依赖最新 preprint 和尚未完全沉淀的工作。

survey

 

survey

一句话压缩：

第一篇参考文献更“硬”，第二篇参考文献更“新”。

---

再看看引用量呢？

---

看了下，按当前能核实到的情况，第一篇的引用量大概率明显高于第二篇。

我先说最稳妥的部分：

第一篇 《Trojan Attacks and Countermeasures on Deep Neural Networks from Life-Cycle Perspective: A Review》 是 2025 年 5 月发表在 ACM Computing Surveys 的综述。
Kudos
+1

我能在公开可访问结果里确认，它已经至少被一篇 2026 年的期刊论文引用：Data poisoning-based backdoor attacks against supervised learning rules of Spiking Neural Networks 的参考文献里明确列出了这篇综述。
ScienceDirect
+1

第二篇 《Embodied Manipulation for Robotic Arms: Embodiment, Data, Learning, and Evaluation》 在你上传的稿子里标的是 J. ACM, Vol. 35, No. 4, Article 111, Publication date: April 2026。

survey

但我这边没有检索到一个可靠、可直接引用的“当前引用次数”页面来给两篇做精确数字对比；对第二篇，我也没查到可验证的已引用记录。这意味着它很可能还是 0 或接近 0，但这一点我只能说是高概率判断，不能当成已核实的精确数。
ResearchGate
+1

所以更谨慎的结论是：

就目前能核实到的引用表现，第一篇领先。
而且这也很正常：它更早发表（2025 vs 2026），主题也更集中，进入引用循环会更快。
Kudos
+1
 

survey

不过我得坦白一点：
我这次没拿到 Google Scholar 或 Semantic Scholar 上两篇都可直接对照的实时 citation count 页面，所以没法负责任地给你报一个“第一篇 X 次、第二篇 Y 次”的精确数字。现在能确定的是：第一篇至少已有外部引用证据；第二篇我暂时没检到可验证的引用证据。

如果你愿意，我可以继续帮你专门按 Google Scholar / Semantic Scholar / OpenAlex 三个口径再深挖一轮，尽量把数字抠出来。

---

我说的是第二篇预印本和“刚出炉”的工作占比更高 ，他们这些引用真的是没有沉淀过的吗？

---

不应一刀切地说 “第二篇引用都没有沉淀”。更准确的说法是：

它的参考文献里“前沿、很新”的比例确实更高，但其中相当一部分已经是正式 venue 的论文；真正“还没沉淀”的，主要是 arXiv-only、workshop、代码库/平台白皮书这类条目。 

survey

 

survey

可以分三层看。

第一层，很多引用其实已经过了同行评审，不算“没沉淀”，只是“很新”。
这篇文献表里有大量正式会议和期刊来源，比如 CoRL、ICRA、RSS、ICML、ICLR、RA-L、Machine Intelligence Research、Journal of Vibration and Control 等：例如 [2]、[23]、[142]、[226] 在 CoRL/PMLR， [3]、[5]、[22]、[141]、[224] 在 ICRA， [14]、[20]、[187]、[193]、[195] 在 RSS， [220]、[225] 在 ICML/PMLR， [9]、[215] 在 RA-L， [223] 在 Machine Intelligence Research， [143] 在 Journal of Vibration and Control。换句话说，这些不是“博客式材料”，而是已经进入该领域主流发表渠道的工作。

survey

 

survey

 

survey

 

survey

第二层，确实有一批引用还处在“前沿但未充分沉淀”的状态。
这在参考文献里也写得很明白：有些条目直接标成 arXiv，如 [6] V-JEPA 2、[15] π0、[147] REALM、[191] RoboChallenge、[192] AoE、[196] DreamZero；有些是 “arXiv preprint” 搭配会议名或 OpenReview 链接，如 [19] AgiBot World Colosseo、[21] LeRobot、[144] What matters in learning from large-scale datasets for robot manipulation、[189] AutoQVLA；还有 workshop/平台类条目，如 [216] CoRL workshop、[184] AIRSPEED 平台链接、[8] Genesis GitHub。严格说，这些就属于“还在形成共识或尚待更多复现/比较”的部分。

survey

 

survey

 

survey

 

survey

第三层，在机器人/具身这个方向，“沉淀”本来就不能只按年份来判断。
这篇综述自己就把研究对象放在 vision-language-action、world models、diffusion policies 这些快速演化的前沿上，并且强调要分析当前的数据生产生态、learning paradigms 和 deployment trade-offs。换句话说，它本来就不是在回顾一个高度稳定的成熟闭环领域，而是在梳理一个正快速变化的技术栈。这样的选题，天然会逼着作者纳入很多 2025–2026 的新工作。

survey

 

survey

所以我会给你一个更精确的判断：

第二篇的问题不是“引用不硬”，而是“引用的新近前沿成分更高，因此稳定性分层更明显”。
也就是：

一部分已经是正式顶会/期刊，只是很新，不该叫“没沉淀”；

另一部分确实还是预印本、workshop、平台或代码资源，属于需要谨慎对待的前沿材料。 

survey

 

survey

再说得更直白一点：

第二篇的参考文献不是“虚”，而是“新得不均匀”。
它里面既有已经进入主流 venue 的新成果，也有明显还在 preprint / platform / benchmark 成长期的条目。和第一篇比，差别不在于“有没有正式文献”，而在于后者的经典安全文献沉淀更足，前者的 frontier tracking 比例更高。

survey

 

survey

如果你愿意，我下一步可以直接帮你把第二篇参考文献分成三类：已沉淀 / 新但正式发表 / 明显前沿预印本。

---

你看看哪些即使是arxiv没有别的参考的文献，他们真的就是没有一点背书吗？

---

不是。arXiv-only 不等于“零背书”。更准确地说，第二篇里这些文献的“背书”分成三档：

第一档是正式发表背书，这个最硬；
第二档是“被作者当成该轴线的代表工作”，这是结构性背书；
第三档是生态/平台/benchmark 背书，不是 venue 背书，但也不是空气。

survey

 

survey

拿几个你关心的、明明是 arXiv，但并非毫无依托的例子说。

像 π0 [15]，参考文献里是 arXiv:2410.24164，但正文不是随手一扔。它被放进 Table 9 的 Type I: Unified End-to-End Foundation Models，而且作者给了明确位置：B4 + P3、3B backbone、跨 6 类 embodiment、real dexterous tasks。也就是说，在这篇综述内部，它承担的是“统一端到端 VLA/flow 模型代表作”的角色，不是边角料。这个背书不是同行评审背书，但确实是综述作者的结构性遴选背书。

survey

 

survey

再比如 GR-2 [24]，也是 arXiv-only，但它同样被放进 Table 9 的 Type III，而且作者明确把它当成“predictive world model / web-scale knowledge”方向的代表系统之一，还给了 “100+ manipulation tasks” 这种评估定位。它不是“只有个 arXiv 链接就被引用”，而是被纳入了作者的体系比较框架。

survey

 

survey

还有一类是 平台/生态型文献。
像 Cosmos [130]、AIRSPEED [184]、RoboOS [160] 这种，有的在参考文献里是 arXiv 或 URL，但正文里它们不是拿来证明一个算法 SOTA，而是拿来支撑“数据生产生态”“系统层 orchestration”“pipeline infrastructure”这些论述。比如 Cosmos 被作者放进自动数据生成/世界模型那条线里，AIRSPEED 被放进数据生产平台，RoboOS 直接进了 Table 1 的 L2 System Layer。这类条目的背书来自于生态位和系统角色，不是传统 paper-acceptance 的那种背书。

survey

 

survey

 

survey

 

survey

再一类是 benchmark / evaluation 型 preprint。
像 REALM [147]、RoboEval [176]、WorldArena [150]、RoboChallenge [191]，虽然不少也是 arXiv-only，但它们在这篇里承担的是评测基准、评测协议、开放挑战的角色。作者不只是把它们列在后面，而是把它们放进 Table 11 和第 5、6 章的评价与 future directions 里，说明这些工作至少已经在该子方向里形成了“议程设置”作用。它们的背书是benchmark legitimacy，不是期刊沉淀。

survey

 

survey

所以你这个问题的核心答案是：

这些 arXiv 文献里，很多并不是“没有一点背书”，而是“背书类型不是正式发表背书”。
它们常见的背书来源有三种：

被综述纳入核心 taxonomy / comparison table

本身是重要数据集、平台、benchmark、pipeline

已经在该前沿方向里形成代表性议题或系统角色 

survey

 

survey

但也要补一句反面的：

这种背书终究弱于正式 venue 背书。
也就是说，不能因为它被放进表格里、被很多人讨论，就把它和 RSS/ICRA/CoRL/ICML/RA-L 的“硬背书”等量齐观。你更该说的是：

第二篇里不少 arXiv 不是“裸奔引用”，而是有结构性或生态性背书；但它们的证据等级，仍然低于正式同行评审发表。 

survey

 

survey

一句话压缩：

不是“没背书”，而是“很多只有圈内位置背书、体系位置背书、平台角色背书，还没完全变成 venue 背书”。

你要的话，我可以下一步直接把第二篇的 arXiv-only 文献分成三类：有强结构性背书 / 有生态背书 / 基本只是前沿信号引用。

---

你要不要查一下pi0  和GR-2这两篇工作

---

我查了，结论很清楚：

π0 和 GR-2 都不是“毫无背书的 arXiv-only”，但两者的背书强度明显不一样。

π0 的背书更硬。
我能直接核到它已经是 RSS 2025 正式论文，RSS 官方程序页列出了论文、作者和 session；同时，Physical Intelligence 在 2025 年 2 月正式开源了 π0 的代码和权重，并说明可在多种机器人平台上做 inference / fine-tuning。除此之外，openpi 公共仓库目前有大约 9.8k–10k+ stars，而且 Hugging Face / LeRobot 也已经把 π0 作为正式支持对象写进文档里。换句话说，π0 不只是有 arXiv，它还有 正式 venue 背书 + 开源实现背书 + 生态采用背书。 
Hugging Face
+3
Robotics: Science and Systems
+3
Physical Intelligence
+3

GR-2 不是没有背书，但背书类型更弱。
我能核到的公开信息是：它有 arXiv 技术报告、项目页、以及 ByteDance Research 团队署名；论文正文里给了比较强的实验结果，比如用 38 million internet video clips 预训练、在 100+ tasks 上报告很高的平均成功率。作者 Tao Kong 的公开主页也把 GR-2 列为 “Tech report, 2024” 的代表项目。也就是说，GR-2 至少有 大厂研究团队背书 + 项目级背书 + 圈内关注度背书，不是“裸奔 paper”。但就我这次查到的公开证据，它还没有像 π0 那样给出一个我能直接核实的正式顶会发表记录，也没有看到同等级的公开代码/权重生态。 
ResearchGate
+2
taokong.org
+2

所以如果把“背书”拆开看，大概是这样：

π0：
正式论文背书很强，RSS 已收；开源和生态背书也很强，openpi 已公开，LeRobot 已适配。 
Hugging Face
+3
Robotics: Science and Systems
+3
Physical Intelligence
+3

GR-2：
有团队、项目和结果层面的背书，但目前公开可核实的主要还是 tech report / arXiv + 项目页 这一档。 
ResearchGate
+2
taokong.org
+2

所以你前面那个判断，我现在会修正成一句更准确的话：

GR-2 不是“没有一点背书”，但 π0 明显已经从“前沿 arXiv 工作”走到了“有正式 venue 和开源生态支撑的代表作”；GR-2 目前更像“有强团队和项目影响力加持的技术报告”。

如果你愿意，我可以下一步把这两个工作按 “venue / 开源 / 生态 / 结果可信度 / 综述里该怎么引用” 五个维度并排拆一下。

---

你认为GR-2这个位置有更好的替代吗？

---

有。
如果你说的是第二篇里 Table 9 / 4.3.3 这个 “Type III: Predictive World Models” 的代表位置，我会把 GR-2 往下放。
在这篇综述自己的表述里，GR-2 被放在 Type III，并被描述为“用 web-scale 预训练做 action-conditioned video prediction”；同一段里作者还并列了 DreamZero 和 DreamVLA，后两者都更直接地被写成“world model / world action model 驱动 manipulation”的例子。换句话说，GR-2 更像“带强世界知识的视频-动作 generalist”，而不是这个槽位里最典型的世界模型代表”。 

survey

我会这样排：

第一选择：DreamZero
如果你要的是“这个位置最像什么”，DreamZero 比 GR-2 更贴。DreamZero 现在直接把自己定义成 World Action Model (WAM)，核心就是联合预测未来世界状态和机器人动作；而且它已经强调了 real-time closed-loop control、cross-embodiment transfer、few-shot embodiment adaptation 这些很符合这篇综述 Type III 关注点的能力。相比之下，GR-2 更像“web-scale video pretraining + downstream robot fine-tuning”的 generative VLA/agent。也就是说，从概念贴合度看，DreamZero 是更强的一号位。 

survey

 
Hugging Face
+1

第二选择：DreamVLA
如果你不想用 2026 太新的 DreamZero，DreamVLA 是更稳的替代。原因不是它更“硬”，而是它在这篇综述自己的文字里就被描述为 “integrates a diffusion-based world model into the manipulation pipeline for planning via imagined trajectories”，这句话和 “predictive world model” 这个槽位几乎是直对直。它比 GR-2 更像你想要放在 Type III 里的“教科书式例子”。不过它目前仍然主要是 arXiv/workshop 传播态，正式发表背书并不比 GR-2 明显更硬。

survey

 
Hugging Face
+1

第三选择：RoboDreamer
如果你最看重的是“文献更硬”，那我反而会考虑 RoboDreamer。它是 ICML 2024 / PMLR 的正式发表工作，publication pedigree 明显强于 GR-2 这种目前仍是 CoRR/arXiv 的条目。问题是，它更自然地属于 B5（Generative Dynamics / Physical Imagination）或 planning-side world-model 代表，未必是 Table 9 里这种“完整 Type III integration model exemplar”的最自然替代。所以它是“更硬”，但不一定是“更贴槽位”。 
HKUST
+1

所以我给你的直接建议是：

想要最贴这个位置：用 DreamZero

想要更稳妥、不过度激进：用 DreamVLA

想要正式发表背书最硬：用 RoboDreamer，但要承认它有一点“换槽位”的问题

一句话总结：

GR-2 不是不能放，但如果你要一个更像“Type III predictive world model 标杆”的代表，DreamZero / DreamVLA 都比它更顺；如果你要更硬的正式论文背书，RoboDreamer 更硬，但类别贴合度稍差。

---

再看看VideoVLA你看看哪个最适合填表

---

我重新看了 VideoVLA 之后，结论会更细一点：

先给结论

如果你问“概念上谁最适合填 Type III / Predictive World Models 这个表格位置”，
我会排成这样：

DreamVLA > VideoVLA > GR-2

如果你问“综述表格里谁最稳、最不容易被审稿人质疑太新”，
我会排成这样：

GR-2 > DreamVLA > VideoVLA

也就是说：

概念贴合度：VideoVLA 比 GR-2 更像“predictive world model”

表格稳定性：GR-2 目前比 VideoVLA 更稳

两者兼顾：DreamVLA 最平衡

为什么这么排
1）GR-2：有代表性，但“世界模型味”没有 VideoVLA 那么纯

在你这篇文章自己的框架里，Type III 下面有两条：

spatial grounding

predictive world models 

survey

而 4.3.3 对 predictive world models 的定义是：
learn forward dynamics from data，然后举了三个例子：

GR-2：action-conditioned video prediction at web scale

DreamZero：jointly models video and action as a World Action Model

DreamVLA：integrates a diffusion-based world model into the manipulation pipeline for planning via imagined trajectories 

survey

从这个表述就能看出来，GR-2 是能放在这里的，但它更像：
web-scale generative VLA / video-language-action generalist，
而不是“最教科书式”的 predictive world model。
它的强项是 38M internet videos、100+ tasks、高泛化，这个很适合当大模型 generalist 代表。
Hugging Face
+1

2）VideoVLA：概念上更贴这个槽位

VideoVLA 的核心表述是：

用 pre-trained video generation models

jointly predicts action sequences and future visual outcomes

通过 imagined futures 来支撑 manipulation generalization

强调 cross-embodiment imitation 和 novel objects/generalization 
Hugging Face
+1

这和你文里 4.1.5 / 4.3.3 那条“generative dynamics and physical imagination / predictive world models”的语义其实更顺。因为它不是单纯“视频预训练后再做机器人控制”，而是明确把：
未来视觉结果 + 动作预测
绑在一起。

所以如果只是问：

谁更像 Type III 里 predictive world model 这个格子本来的意思？

那我会说 VideoVLA 比 GR-2 更贴。
因为 VideoVLA 更直接地把“未来世界状态预测”做成了 action generation 的一部分。
Hugging Face
+1

3）DreamVLA：最平衡

DreamVLA 的描述是：

integrates comprehensive world knowledge forecasting

establishes a perception-prediction-action loop

uses a diffusion-based transformer

real robot + CALVIN 上都有结果 
Hugging Face
+1

它比 GR-2 更“世界模型”，
又比 VideoVLA 少一点“刚出来、太新”的风险。
而且你文里自己已经把它写成：
integrates a diffusion-based world model into the manipulation pipeline for planning via imagined trajectories，
这几乎就是在替它写“为什么应该填这格”的理由。

survey

所以如果你想选一个：

贴槽位

不至于太先锋

跟你现有正文表述最一致

那我会首推 DreamVLA。

如果你的问题是“GR-2 该不该被 VideoVLA 替掉”

我的答案是：

不建议直接替掉，除非你特别想强化“predictive world model”这一条。

因为 GR-2 还有两个你表格里很需要的优点：

优点 A：它更像“web-scale knowledge → robot manipulation”这条线的代表

GR-2 的 38 million video clips / 50 billion tokens / 100+ tasks 这种规模叙事，在表格里很有存在感。它很适合当“world-knowledge-infused generalist robot agent”的代表。
Hugging Face
+1

优点 B：它比 VideoVLA 更有“已被讨论和接受”的感觉

VideoVLA 是 2025 年 12 月 的 arXiv，很新。GR-2 是 2024 年 10 月，虽然也是 CoRR/arXiv，但已经有更长的传播窗口。
Hugging Face
+1

如果你在写综述表格，尤其想少冒险，GR-2 更稳。

我给你的实际建议
方案 1：最稳妥

保留 GR-2，不用 VideoVLA 替换。
然后在正文 4.3.3 里补一句：

More recent methods such as VideoVLA further tighten this predictive coupling by jointly forecasting actions and future visual outcomes with pre-trained video generators. 
Hugging Face
+1

这最保险。

方案 2：如果你想让表格更“概念精准”

把 GR-2 换成 DreamVLA。
这是我最推荐的改法。
因为 DreamVLA 在“predictive world model”这个槽位上：

比 GR-2 更贴

比 VideoVLA 更稳

跟你现有 4.3.3 正文最一致 

survey

 
Hugging Face
+1

方案 3：如果你要“最新最像”

直接用 VideoVLA。
但我只建议在你愿意接受“太新、还没沉淀”的前提下这么做。
因为它现在确实更像 predictive visual world model for action，但在综述表格里会显得比较冒进。
Hugging Face
+1

最终拍板

如果你现在就要我替你选一个“最适合填表”的，我会说：

首选 DreamVLA。
保守选 GR-2。
想更前沿、更概念纯，就选 VideoVLA。

一句话压缩：

GR-2 更稳，VideoVLA 更像，DreamVLA 最平衡。

你要的话，我下一条可以直接帮你把 Table 9 这一行 按你选的工作重写出来。

---

Pointvla如何？

---

PointVLA 可以用，但不适合拿来替 GR-2 那个“predictive world model”位置。

更准确地说：

如果你在填第二篇 Table 9 里 Type III 这一栏，PointVLA 更像是 spatial grounding / 3D grounding 的代表，
不像 predictive world model 的代表。
因为这篇综述自己对 Type III 的拆法就是两条：
一条是 spatial grounding systems，另一条是 predictive world models；前者强调 3D perception / metric grounding / trajectory traces，后者强调从数据里学 forward dynamics、做 imagined trajectories 和 world-model planning。

survey

而 PointVLA 的核心做法是：

给预训练 VLA 注入 point cloud / 3D features

freeze 原本的 action expert

用轻量模块把 3D 表征插进去

强化空间理解、few-shot multi-tasking、real-vs-photo discrimination、height adaptability 等能力
并且它已经被项目页标明为 RA-L 2025 接收。
pointvla.github.io

这说明它的关键词是：

3D world injection / 3D spatial reasoning / point-cloud grounding

不是：

world dynamics prediction / imagined future rollouts / world-model-based planning

所以如果你问我一句最短的判断：

结论

PointVLA 不适合替 GR-2 去填“predictive world model”那个格子。
但它很适合去填 Type III 里“spatial grounding / 3D grounding”那一侧。

它更适合放到哪里

如果按你这篇综述自己的 taxonomy 来看，PointVLA 更像：

方案 A：放在 4.3.3 Type III: Spatial Grounding

因为它本质上是在做：

3D perception injection

metric/spatial grounding enhancement

point-cloud-conditioned action generation

这个方向和你文里已有的 3D-VLA、SpatialVLA、TraceVLA、BridgeVLA 是一类人。你文里这些工作也都是 B4 路线，强调 3D perception、metric 3D structure、trajectory traces、kinematic feasibility，而不是 forward world dynamics。

survey

方案 B：如果你只想在表里加一行

那我会把 PointVLA 放成：

Type III

B4, P?（偏 B4 肯定没问题；P2/P3 要看你怎么界定它接入的 action generator）

模式更偏 Dirc. / grounded control

核心卖点写成 point-cloud grounding into VLA

它和 GR-2 / DreamVLA / VideoVLA 的区别
PointVLA

更像：
给 VLA 补上 3D 世界感知

GR-2

更像：
web-scale video-language-action generalist

DreamVLA / VideoVLA

更像：
用预测未来视觉/世界状态来驱动 action

所以这几个不是同一个槽位竞争：

PointVLA 竞争的是 3D-VLA / SpatialVLA / BridgeVLA

GR-2 / DreamVLA / VideoVLA 竞争的是 predictive world model / imagined rollout 那一格

如果你现在要“填表”，我的建议是
想替换 GR-2 那格

别用 PointVLA。
优先还是：

DreamVLA

或 VideoVLA

或继续留 GR-2

想给 Type III 增加一个更强的 3D grounding 例子

可以用 PointVLA，而且挺合适。
因为它：

有 正式发表背书（RA-L 2025）
pointvla.github.io

有明确的 3D point-cloud injection 方法
pointvla.github.io

和你文里的 spatial grounding 轴高度一致

survey

我给你的直接拍板

PointVLA：好工作，表里能放。
但不该拿它去顶 GR-2 的 predictive world model 槽位。
它最适合填的是 Type III 里偏 B4 的 3D/spatial grounding 位置。

你要的话，我下一条可以直接帮你把 PointVLA 填进 Table 9 的那一行 写出来。

---

那就换成VideoVLA吧，你看看信息全不全

---

可以，VideoVLA 这行信息已经基本够填表了，而且比我刚才担心的“只有 arXiv 摘要”要完整得多。
因为现在至少有两类可用信息源：

论文摘要/纸页：给出方法核心、任务定位、发布时间。
Hugging Face
+1

项目页：给出 backbone、训练数据、仿真/真实评测平台、硬件、任务类型、泛化设置。
videovla-nips2025.github.io

能确定填的部分

如果你要填的是你们现在那种 Table 9 风格，这些字段基本可以落：

Model
VideoVLA

B & P
我建议填 B5, P3。
理由是它明确做 future visual outcomes 预测，而且用的是 multi-modal Diffusion Transformer，很符合你文里 predictive world model / generative dynamics 和 iterative generative policy 这两个槽位。这个判断是基于你们现有 taxonomy 和论文方法描述做的归类。
videovla-nips2025.github.io
+1

Backbone & Params
可以写成：
CogVideoX-based multi-modal Diffusion Transformer
但参数量我现在没看到公开明确数字，所以这一格不要硬写。项目页明确说 backbone 建在 CogVideoX 上，并采用 unified DiT 架构。
videovla-nips2025.github.io

Mode
建议填 Genr.
因为它联合预测动作和未来视觉结果，本质上是生成式控制。
Hugging Face
+1

Hardware
这一行其实挺全：

仿真：Google robot + WidowX in SIMPLER

真实：Realman robot with 7-DoF arm and gripper 
videovla-nips2025.github.io

Primary Data Scale / Data Form
这格可以写成：
OXE + collected Realman dataset
更细一点的话：

in-domain simulation：all models trained on OXE

real-world：all models pre-trained on OXE and then fine-tuned on their collected Realman dataset

skill transfer real-world：combined WidowX dataset + collected dataset 
videovla-nips2025.github.io

Eval: Sim & Real
这个也够写：

Sim: SIMPLER

in-domain on Google/WidowX

novel objects on Google

new skills transfer from WidowX to Google

Real: Realman robot

in-domain tasks

novel objects

cross-embodiment skill transfer from WidowX to Realman 
videovla-nips2025.github.io

还不够稳的部分

有两项我不建议你硬填：

1. 参数量

我这次查到的项目页、纸页、聚合页都没有给出一个我能直接核实的 model size / parameter count。
所以如果你表格这一列必须有数字，VideoVLA 这点不如某些大模型工作好填。
videovla-nips2025.github.io
+2
Hugging Face
+2

2. 正式发表形态

项目页写的是 NeurIPS 2025，这是个很强的信号；但我这次没有去核 conference 官方程序页。
所以如果你表里不写 venue，这没问题；
如果你正文里要说“NeurIPS 2025 paper”，最好后面再补一次官方来源确认。
videovla-nips2025.github.io

我建议你现在就这样填

如果按你们表格的风格，我会写成：

VideoVLA | B5, P3 | CogVideoX-based multi-modal Diffusion Transformer | Genr. | Google+WidowX+Realman | OXE + collected real-world data | Sim: SIMPLER (in-domain / novel objects / skill transfer); Real: Realman (in-domain / novel objects / cross-embodiment skill transfer) 
videovla-nips2025.github.io
+1

最后判断

信息是够的。
唯一明显缺口就是 参数量，以及如果你特别严谨的话，NeurIPS 2025 还值得再补一个官方程序页确认。
但作为表格里的代表工作，已经比“只有摘要的 arXiv 工作”完整很多了。
videovla-nips2025.github.io
+1

你把 Table 9 那一行的格式发我，我可以直接替你填成可贴版本。

---

GR-2~\cite{cheang2024gr2} trains action-conditioned video prediction at web scale 那这句怎么改

---

如果你要把 GR-2 换成 VideoVLA，这句最好别再写成 “at web scale”，因为 VideoVLA 的亮点不是那个，而是 jointly predicting actions and future visual outcomes。

我建议直接改成下面这种：

LaTeX
VideoVLA~\cite{<videovla-bibkey>} jointly predicts action sequences and future visual outcomes using a pre-trained video generator, enabling manipulation policies to be conditioned on imagined future states.

如果你想更贴你们这一段 predictive world models 的语气，可以用这个版本：

LaTeX
VideoVLA~\cite{<videovla-bibkey>} couples action generation with future visual prediction through a pre-trained video generator, providing a more explicit predictive interface between policy learning and imagined world states.

如果你想写得更平一点、和原句长度接近，可以用：

LaTeX
VideoVLA~\cite{<videovla-bibkey>} jointly models robot actions and future visual outcomes, extending visuomotor control with predictive visual imagination.

我个人最推荐第一句，因为它：

信息最完整

学术语气稳

和你们 4.3.3 里 predictive world models / imagined trajectories 那条线最一致

如果你愿意，我可以顺手把 GR-2 / DreamVLA / VideoVLA 那一小段三句并排改顺。

---

算了，换成PointVLA吧

---

可以，但这句要换写法，因为 PointVLA 不是“action-conditioned video prediction at web scale”那一路，它更偏 3D / point-cloud grounding。项目页把它定义成给预训练 VLA 注入 point-cloud representation，并强调 3D world understanding、few-shot multi-tasking 和 real-world manipulation；同时它已标注为 RA-L 2025。(pointvla.github.io
)

我建议你把原句改成这个版本：

LaTeX
PointVLA~\cite{<pointvla-bibkey>} injects point-cloud-based 3D grounding into pre-trained vision-language-action models, improving spatial understanding and real-world manipulation across diverse tasks.

如果你想更贴你们 Type III / spatial grounding 的语气，可以用这个版本：

LaTeX
PointVLA~\cite{<pointvla-bibkey>} augments pre-trained vision-language-action models with point-cloud-based 3D grounding, providing a stronger spatial interface for manipulation in complex real-world settings.

我更推荐第一句，因为更稳、更中性。
但要提醒一句：如果你这里原本是在讲 predictive world models，那换成 PointVLA 会让这一句的类别偏向 spatial grounding，而不是 world modeling。 (pointvla.github.io
)

如果你要，我下一条可以直接把 Table 9 里 PointVLA 那一行 也一起改好。

---

来吧

---

可以，直接给你可贴版本。

如果是替换正文那一句，我建议写成：

LaTeX
PointVLA~\cite{liu2025pointvla} augments pre-trained vision-language-action models with point-cloud-based 3D grounding, providing a stronger spatial interface for manipulation in complex real-world settings.

如果你想写得更平一点：

LaTeX
PointVLA~\cite{liu2025pointvla} injects point-cloud-based 3D grounding into pre-trained vision-language-action models, improving spatial understanding and real-world manipulation across diverse tasks.

如果你还要改 Table 9 这一行，我建议填成这样：

LaTeX
PointVLA~\cite{liu2025pointvla} & B4, P2 & VLA + point-cloud encoder & Dirc. & Diverse real robots & OXE + real-world data & Real: multi-task manipulation; improved 3D grounding and cross-task performance

有个小提醒：
PointVLA 更适合放在 Type III 里偏 spatial grounding / 3D grounding 的位置，不太适合替代 predictive world model 那一格。 这一点和项目页对它“point-cloud-based 3D grounding”的定位是一致的。

如果你把 Table 9 那几行原文贴出来，我可以直接按你整张表的风格统一改好。

---

算了，还是Videovla吧\textbf{GR-2}~\cite{cheang2024gr2} & B5, P3 & CVAE (230M) & Genr. & Franka & 38M Web Vid. & Sim: CALVIN | Real: 100+ manipulation tasks \\

---

我去核一下 VideoVLA 这一行能不能稳当地替进去，重点看 backbone、平台、数据和评测字段。

---

可以，这行基本能稳替。
我建议把原来的 CVAE (230M) 去掉，因为我能核到 VideoVLA 的 CogVideoX-based multi-modal Diffusion Transformer、平台和评测设置，但没看到官方页面给出一个可直接引用的明确参数量；NeurIPS 2025 poster 和项目页都足够支撑它作为正式代表工作放进表里。 
videovla-nips2025.github.io
+1

你可以直接改成这一行：

LaTeX
\textbf{VideoVLA}~\cite{shen2025videovla} & B5, P3 & CogVideoX-based multi-modal DiT & Genr. & Google+WidowX+Realman & OXE + real-world data & Sim: SIMPLER | Real: novel objects \& cross-embodiment skill transfer \\

如果你想把真实机器人写得更具体一点，可以用这个版本：

LaTeX
\textbf{VideoVLA}~\cite{shen2025videovla} & B5, P3 & CogVideoX-based multi-modal DiT & Genr. & Google+WidowX+Realman & OXE + real-world data & Sim: SIMPLER | Real: Realman, novel objects \& cross-embodiment skill transfer \\

我这样填的依据是：

B5, P3：它联合预测动作和未来视觉结果，用的是多模态 diffusion transformer，最贴你们文里的 predictive world model / generative policy 这一格。 
videovla-nips2025.github.io
+1

Backbone：官方项目页写的是把大视频生成模型转成机器人 VLA，基于 CogVideoX 的多模态 DiT。 
videovla-nips2025.github.io
+1

Hardware / Eval：项目页明确有 Google、WidowX、Realman，仿真在 SIMPLER，真实实验强调 novel objects 和 cross-embodiment skill transfer。 
videovla-nips2025.github.io
+1

你这行如果想和表里其他行风格更统一，我建议把 bibkey 统一成你现有 .bib 里的名字，然后把 “real-world data” 细化成你们习惯的写法。

---

他用的CogVideox是多少B的

---

我去核一下 VideoVLA 里用的 CogVideoX 具体是哪一档参数。

---

如果你问的是 VideoVLA 里用的那个 CogVideoX，那我现在查到的是：

用的是 CogVideoX-5B。

能支撑这个结论的依据有两条：

VideoVLA 的公开介绍明确写它的 backbone 是从 CogVideoX-5B 初始化的多模态 Diffusion Transformer。
Emergent Mind

CogVideoX 官方模型页也明确区分了 2B 和 5B 两个版本，其中 CogVideoX-5B 就是 5B 参数版本。
Hugging Face
+1

所以你表格里如果想写完整，可以把这一格写成：

LaTeX
CogVideoX-5B-based multi-modal DiT

或者更直接一点：

LaTeX
CogVideoX-5B

如果你要，我可以顺手把 VideoVLA 那一整行表格按这个参数补齐。

---

OXE + real-world data

加多少

---

我去把 VideoVLA 里真实数据加了多少补清楚，尽量给你能直接填表的量级。

---

加的是 他们自己采的 Realman 真实机器人数据。
我查到一个较明确的数字是：5,824 samples，用于真实机器人微调；同时还有一条训练流程信息说，VideoVLA 在 OXE 上预训练后，再进行 15,000 fine-tuning steps 的真实机器人微调。这里要说明一下：项目页和 OpenReview 页面都明确说是 “our collected dataset using the Realman robot”，但我没有在官方项目页里直接看到样本数；“5,824 samples” 来自对论文的二手技术解读页面。 所以如果你想最保守，表里写 “OXE + collected Realman dataset” 最稳；如果你接受这个二手来源，就可以细化成 “OXE + 5,824 Realman samples”。 
videovla-nips2025.github.io
+2
Emergent Mind
+2

所以你这行里这一格可以有两种写法：

保守版：

LaTeX
OXE + collected Realman dataset

细化版：

LaTeX
OXE + 5,824 Realman samples

如果你愿意更统一一点，整行我建议改成：

LaTeX
\textbf{VideoVLA}~\cite{shen2025videovla} & B5, P3 & CogVideoX-5B-based multi-modal DiT & Genr. & Google+WidowX+Realman & OXE + collected Realman dataset & Sim: SIMPLER | Real: novel objects \& cross-embodiment skill transfer \\

如果你想用带数字的版本，我也可以直接替你换好。

---

novel objects

Real Traj.?还有这个，是多少novel objects？详细点的数据

---

我去把 VideoVLA 的真实数据和 novel objects 设置具体抠出来，尽量给你能直接填表的数。

---

可以，给你一个能直接填表的版本。

Real Traj. 可以写。
更准确地说，VideoVLA 的真实世界部分是：所有模型都先在 OXE 上预训练，再在作者自采的 Realman 机器人数据上微调；项目页明确写了 real-world evaluation 用的是 Realman 7-DoF arm + gripper，且“all models are finetuned on our collected dataset using the Realman robot”。所以如果你表里这一列只是写数据形式，写 Real Traj. 是成立的。
videovla-nips2025.github.io

如果你想把数据规模也写进去，有一个可用但不是官方项目页直接给出的数字：二手技术解读写的是 5,824 samples 的 Realman 自采数据用于微调。这个数字我没有在项目页原文里直接核到，所以建议你分两档写法：

最稳：OXE + collected Realman dataset

想写数字：OXE + 5,824 Realman samples（但最好心里知道这条来自二手解读） 
videovla-nips2025.github.io
+1

novel objects 的数量有两组：

仿真：Google robot 在 SIMPLER 里测 10 个 novel objects；项目页明确说这些物体来自 YCB 和 GSO，且不在 Google robot 的训练数据里。
videovla-nips2025.github.io

真实世界：Realman robot 的 novel-object evaluation 用的是 12 个 finetuning 没见过的新物体；这个“12”我是在 OpenReview PDF 抓到的。
OpenReview

如果你要“详细点的数据”，我建议你在表格或脚注里这样写最稳：

LaTeX
Real Traj.: OXE pretraining + collected Realman dataset (real-world finetuning);
Novel objects: 10 in SIMPLER (Google; from YCB/GSO, unseen in training), 12 in real-world Realman evaluation (unseen during finetuning).

如果你想把这一行直接改好，我建议写成：

LaTeX
\textbf{VideoVLA}~\cite{shen2025videovla} & B5, P3 & CogVideoX-5B-based multi-modal DiT & Genr. & Google+WidowX+Realman & OXE + collected Realman dataset & Sim: SIMPLER (10 novel objects); Real: Realman (12 novel objects, cross-embodiment skill transfer) \\

如果你更想把 “Real Traj.” 单独塞进表格字段，我可以按你整张表的列格式再帮你压一版。

---

Realman (12 novel objects, cross-embodiment skill transfer) 多少个tasks?

---

我去把 VideoVLA 在 Realman 上的真实任务数核清楚，尤其是 novel objects 和 cross-embodiment 这两块各有多少任务。

---

可以更具体地写成这样：

Real: Realman (3 in-domain task families; 12 novel objects; 6 cross-embodiment transfer tasks across 5 unseen skill categories)

依据是：

Realman 的 in-domain evaluation 明确有 3 类任务：

pick-and-place 到不同颜色盘子，

stack cup/bowl，

block-on-block。
VideoVLA

Novel-object evaluation 是 1 个任务模板：
“Pick up the [Novel Object] and place it onto the [Color] plate”，
但实际评了 12 个 novel objects；OpenReview 的 PDF 还列出了这 12 个对象加 3 个 bottle pose variants。
VideoVLA
+1

Cross-embodiment skill transfer 在 Realman 上对应 6 个具体任务列：
Move Block, Move Fruit, Grab Fruit, Topple Bottle, Take Out Block, Wipe Table，
同时正文说明这些任务来自 5 个未在 Realman 上示范过的 skill categories：Move, Grab, Topple, Take Out, Wipe。
OpenReview

所以你表里这格如果想更完整，我建议直接改成：

LaTeX
Real: Realman (3 in-domain task families; 12 novel objects; 6 cross-embodiment transfer tasks)

如果你想把“skill categories”也写进去，可以用这个更学术一点的版本：

LaTeX
Real: Realman (3 in-domain task families; 12 novel objects; 6 cross-embodiment transfer tasks spanning 5 unseen skill categories)

---

Real: 6 unseen tasks?

---

我核一下这个表述能不能更准确地落在表格里。

---

可以，但要更精确一点：

如果你这格专门写 cross-embodiment transfer，那么可以写 Real: 6 unseen tasks。
VideoVLA 的真实世界 cross-embodiment evaluation 确实是让 Realman 去执行训练时只由 WidowX 示范、未在 Realman 上示范过的技能任务。项目页明确说明这一设置，OpenReview 也把它描述为学到“other embodiments' skills”。
VideoVLA
 
OpenReview

但如果你这格是想概括 全部 real-world evaluation，那只写 6 unseen tasks 会太窄，因为真实实验还包括：

3 个 in-domain task families；

novel-object evaluation；

cross-embodiment skill transfer。
VideoVLA

所以我建议二选一：

如果你想突出 transfer：

LaTeX
Real: 6 unseen cross-embodiment tasks

如果你想概括完整一点：

LaTeX
Real: 3 in-domain task families + novel objects + 6 unseen cross-embodiment tasks

我更推荐第二种。

---

