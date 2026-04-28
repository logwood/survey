Chapter 2 defines the embodied interfaces and constraints of manipulation systems; 
Chapter 3 reinterprets datasets as executable, temporally structured traces of embodied behavior; 
Chapter 4 then asks how such traces can be generated, composed, and scaled automatically.

Embodiment Foundations of Robotic arms: System Architecture
Data Ecosystem for Robotic arms: Data Support
Learning Paradigms for Robotic arms: Methodological Frameworks


The sensing stack plays a major role in whether contact-rich control can remain closed loop. Eye-in-hand vision resolves object geometry before contact, but it provides only indirect information about force, slip, and local deformation once contact occurs. 
Tactile sensing fills this gap: vision-based tactile sensors such as GelSight~\cite{zhao2023gelsightsveltehumanfingershaped} and DIGIT convert contact geometry into images, while force- and vibration-sensitive sensors such as BioTac provide signals for slip detection and contact regulation. 
In practice, visuo-tactile integration matters most in insertion, re-grasping, and fragile-object handling, where task-relevant feedback comes primarily from contact state.


Having examined the physical and software architecture of robotic arms, we now turn to the data ecosystem that supports learning, adaptation, and scaling in embodied manipulation beyond the datasets used for training.
In practice, progress depends equally on how manipulation data is collected, refined, and scaled across tasks, scenes, and embodiments. 
This chapter therefore moves beyond embodied datasets to examine the broader data support structure, beginning with dataset regimes in Section~\ref{sec:eai_datasets}, followed by data acquisition in Section~\ref{sec:data_acquisition}, data refinement in Section~\ref{sec:data_refinement}, and finally the large-scale pipelines that integrate these processes in Section~\ref{sec:data_factories_robotic_arms}.
Together, these elements provide a structured view of the support system summarized in Fig.~\ref{fig:data_support}.


The previous subsection distinguished datasets by the support they provide, but these support regimes are not equally easy to produce. In real-world collection, observation, contact, and execution remain tightly coupled to hardware and environment, so the resulting data often mixes several forms of support at once. 
Simulation provides a more decoupled setting, making it easier to construct and analyze different kinds of data support in a controlled way. 
Automatic data generation further expands these supports through synthetic scenes, demonstrations, and rollouts. 
This section therefore examines three acquisition routes: real-world collection, simulation ecosystems, and automatic data generation.


The key distinction in embodied data acquisition is therefore not only where data comes from, but how tightly its production is coupled to the embodied system, since this determines what form of \(\mathcal{D}\) can be generated reliably and what level of knowledge support \(\mathcal{K}\) it can sustain.


Compared with real-world collection, simulation ecosystem offers a more controllable route for constructing \(\mathcal{D}\). 
Because environment structure, sensing, action interfaces, and embodiment variation can be adjusted more deliberately, current ecosystems differ not only in their physics engines, but also in the kinds of embodied data support they most readily provide. 
MuJoCo is strongest for contact-stable, controller-oriented interaction, SAPIEN for articulated objects and part-level semantics, and NVIDIA Isaac for large-scale multimodal synthesis and broader embodiment coverage. 
Table~\ref{tab:sim_classification} summarizes these design tendencies, while specialized platforms remain useful for narrower task families and physical regimes.

Data refinement通过四种方式提升数据质量：数据增强、数据过滤、数据标注和数据合成，对应的是四种


你现在真正缺的，不是单独给 learning 下一个孤立定义，而是先把 \mathcal{K} 正式定义出来。因为在 survey.tex 到 survey.tex 里，你已经在用 \mathcal{D}_i \rightarrow \mathcal{K}_i 这条线了，但 \mathcal{K} 还没有被真正说清。这样到了 survey.tex 到 survey.tex，learning 就只能被写成“把 data 变成 capability”，这就有点空。

更稳的关系应该是：

\mathcal{D}：embodied execution 的 structured record
\mathcal{K}：从 \mathcal{D} 中获得的 execution-relevant knowledge support
learning：把 \mathcal{D} 转化为 \mathcal{K} 的过程
planning / policy：\mathcal{K} 的两种主要实现形式
所以，如果要严格对齐前文，我建议你把 learning 定义成：

Learning is the process by which a robotic manipulation system transforms data support \mathcal{D} into execution-relevant knowledge support \mathcal{K} under embodiment and control constraints.

这里最关键的是 execution-relevant knowledge support。因为它能同时罩住：

cognitive planning 产生的 code / task plan / spatial representation / predictive rollout
policy learning 产生的 observation-to-action mapping
这比“learning is mapping observations to actions”更宽，也比“learning converts data into capability”更严谨。

如果再把 \mathcal{K} 说清楚，我会这样定义：

\mathcal{K} denotes the execution-relevant knowledge a system can extract from \mathcal{D} and organize for planning or control.

这样你前面的三层就顺了：

\mathcal{K}_1：local interaction knowledge
\mathcal{K}_2：task-structured knowledge
\mathcal{K}_3：transferable cross-embodiment knowledge
然后 Chapter 4 就不再是“learning paradigms”凭空冒出来，而是：

data chapter: what support \mathcal{D} is available
learning chapter: how that support becomes \mathcal{K}
integration chapter: how different forms of \mathcal{K} are coupled into a system
如果你要落成英文正文，我建议直接用这段：


| ID | Sub-direction                                     |        推荐 K | 判断                                                                                    |
| -- | ------------------------------------------------- | ----------: | ------------------------------------------------------------------------------------- |
| P1 | Percept.-Action Regr.                             | **K1 > K2** | 最典型的是 skill-level imitation，直接从观测回归动作；也能扩到 task-level，但主战场还是 skill 数据。                |
| P1 | Temporal Chunking                                 | **K2 > K1** | chunking 往往服务于更长时域、更复杂任务分布，所以比纯 skill BC 更偏 task-level；但仍可由 skill 数据训练。               |
| P1 | Recovery & Transfer                               | **K2 > K1** | 这类方法强调 goal/plan transfer、cross-task 或 cross-embodiment 泛化，天然更需要 task-level 结构。       |
| P2 | Uniform & Spatial Discr.                          | **K2 > K3** | 固定离散 bins / voxel 化动作空间，首先在多任务 task-scale 上成立；扩到更大 generalist/foundation 也合理，但不是最原生。  |
| P2 | Learned Quantization                              | **K2 > K1** | codebook / latent discrete action 主要依赖 task-scale 的多样动作分布，通常不需要 foundation 级别数据才成立。   |
| P2 | Prompted LM Tokens                                | **K3 > K2** | 一旦进入 prompt-conditioned token/action-language 统一建模，foundation-style 多模态预训练支撑更强。       |
| P2 | Autoregr. Generalists                             | **K3 > K2** | “generalist” 本身就说明更偏 foundation/task-general 数据组织，而不是 skill-only。                     |
| P3 | Diffusion Policy Learning / Diffusion Foundations | **K1 > K2** | diffusion policy 最早、最稳的落点仍是 skill/task manipulation；但从原型范式看，先由高质量 skill 数据支撑最自然。      |
| P3 | 3D Geometric Enhanc.                              | **K1 > K2** | 3D point-cloud / geometry-aware diffusion 通常强依赖 skill-level、接触级、操作级数据；可扩到 task 但不是核心。 |
| P3 | Flow & Acceleration                               | **K1 > K2** | 这是对 diffusion-style policy 的加速/替代，一般继承其数据生态，首先还是 skill-centric。                       |
| P3 | Generalist Scaling                                | **K3 > K2** | 这一行就是 foundation/generalist scaling，本质上由大规模多任务/跨域数据支撑。                                |


| ID | Sub-direction                  |        推荐 K | 判断                                                                                              |
| -- | ------------------------------ | ----------: | ----------------------------------------------------------------------------------------------- |
| B1 | Probabilistic Alignment        | **K2 > K1** | 语言目标与 skill API 对齐，通常要有 task-level 指令-技能对应关系；可退化到 skill 库检索。                                    |
| B1 | Program Synthesis              | **K2 > K1** | code/program 生成大多面向 task completion，而不是单一 skill；但底层仍依赖 skill primitives。                        |
| B1 | Reward Synthesis               | **K2 > K1** | language-to-reward 更像 task specification，再交给 RL/optimizer；主支撑仍是 task-level。                     |
| B1 | Structured Control Flow        | **K2 > K1** | BT / XML / program flow 的意义主要在 task composition，不是单技能本体。                                        |
| B2 | Formal Solvers                 | **K2 > K1** | symbolic task plan + classical planner，典型 task-level。                                           |
| B2 | Semantic Search                | **K2 > K1** | 从语义检索 sub-task sequence，本质是 task decomposition。                                                 |
| B2 | State-Aware Planning           | **K2 > K1** | 这类方法强调 replanning / feedback-aware task progression，天然更偏 task-level。                            |
| B3 | Explicit Grounding             | **K3 > K2** | 一旦是大模型式 grounded multimodal reasoning，foundation-scale multimodal pretraining 的支撑会更强。           |
| B3 | Implicit Grounding             | **K3 > K2** | CoT trace / latent grounding 同样更依赖 foundation-style multimodal reasoning能力。                     |
| B4 | Physical Constraint            | **K1 > K2** | contact、SE(3)、grasp pose 这类约束首先来自 skill-level interaction。                                      |
| B4 | 2D Affordance                  | **K1 > K2** | heatmap/mask/affordance 本质是 action-relevant intermediate abstraction，最原生地由 skill-level 操作数据支撑。  |
| B4 | 3D Neural Fields               | **K1 > K2** | object-centric / scene-centric 3D representations 多服务于具体 manipulation skill grounding。          |
| B4 | Constraint Reasoning           | **K2 > K1** | 这行虽然用几何/value map/keypoints，但通常是为 task-level sequencing/planning 服务，所以比前几行更偏 K2。                |
| B5 | Future Video Prediction        | **K2 > K3** | 未来视频预测先在 embodied task trajectories 上最直接成立；再往 foundation video world model 扩。                   |
| B5 | Latent World Simulation        | **K3 > K2** | latent world model / JEPA / large-scale simulation 更自然对应 foundation-scale pretraining。          |
| B5 | Physics-Constrained Prediction | **K2 > K1** | 物理一致的 trajectory/dynamics prediction 常服务于 planner/MPC，通常需要 task-level rollout 结构；比纯 skill 稍高一层。 |

B1 methods are unified by their production of executable task specifications, such as code, rewards, or structured control flow, and are therefore organized around task-level structure, and they are therefore primarily supported by \(\mathcal{K}_2\).

B2 methods are unified by task decomposition, symbolic planning, and replanning, and likewise center on task-level structure, making \(\mathcal{K}_2\) their primary source of support.

Within B3, explicit grounding remains organized around task-conditioned scene understanding and is primarily supported by \(\mathcal{K}_2\), whereas implicit grounding draws more heavily on foundation-scale multimodal priors and is thus better supported by \(\mathcal{K}_3\).

Within B4, local interaction grounding is grounded in contact, geometry, and affordance structure, and therefore relies primarily on \(\mathcal{K}_1\), whereas higher-level constraint reasoning is more closely tied to task-level constraint use and is better supported by \(\mathcal{K}_2\).

Within B5, task-conditioned future prediction remains centered on embodied task trajectories and is primarily supported by \(\mathcal{K}_2\), whereas larger latent world simulation draws more heavily on broad predictive priors and is more naturally supported by \(\mathcal{K}_3\).

Within P1, reactive local control is grounded in local interaction and therefore relies primarily on \(\mathcal{K}_1\), whereas task-conditioned, chunked, and recovery-aware policies are more structured by task-level execution and are better supported by \(\mathcal{K}_2\).

Within P2, task-scale discrete action generation remains organized around task-level action structure and is primarily supported by \(\mathcal{K}_2\), whereas multimodal and generalist token policies draw more heavily on large-scale priors and are thus better supported by \(\mathcal{K}_3\).

Within P3, local generative control is grounded in continuous interaction and therefore relies primarily on \(\mathcal{K}_1\), whereas large-scale generalist generative policies depend more on heterogeneous pretraining and are correspondingly better supported by \(\mathcal{K}_3\).


Here, \(\mathcal{K}_1\), \(\mathcal{K}_2\), and \(\mathcal{K}_3\) denote levels of knowledge support that a paradigm primarily requires and organizes, rather than categories to which the paradigm itself belongs.

B1 methods are unified by their production of executable task specifications, such as code, rewards, or structured control flow. Because these methods must organize task-level structure into executable intermediate forms, they primarily require \(\mathcal{K}_2\) as their knowledge support.

B2 methods are unified by task decomposition, symbolic planning, and replanning. Since they depend on the organization of long-horizon task structure and subtask relations, they likewise primarily require \(\mathcal{K}_2\).

Within B3, explicit grounding remains centered on task-conditioned scene understanding and therefore primarily depends on \(\mathcal{K}_2\). By contrast, implicit grounding more often requires \(\mathcal{K}_3\) when it must organize transferable multimodal structure beyond a single task configuration.

Within B4, local interaction grounding is centered on contact, geometry, and affordance structure, and therefore primarily requires \(\mathcal{K}_1\). Higher-level constraint reasoning, however, depends more strongly on task-level constraint structure and thus more directly requires \(\mathcal{K}_2\).

Within B5, task-conditioned future prediction remains organized around embodied task trajectories and their temporal evolution, and therefore primarily requires \(\mathcal{K}_2\). Broader latent world simulation increasingly requires \(\mathcal{K}_3\) when it is used to organize transferable predictive structure across embodiments or environments.

Within P1, reactive local control is grounded in local interaction and therefore primarily depends on \(\mathcal{K}_1\). Task-conditioned, chunked, and recovery-aware policies, by contrast, rely more on task-level execution structure and accordingly require \(\mathcal{K}_2\) more strongly.

Within P2, task-scale discrete action generation remains organized around task-level action structure and therefore primarily requires \(\mathcal{K}_2\). Multimodal and generalist token policies increasingly require \(\mathcal{K}_3\) when they must organize transferable action structure across heterogeneous embodiments.

Within P3, local generative control is grounded in continuous interaction and therefore primarily requires \(\mathcal{K}_1\). Larger-scale generalist generative policies, however, require \(\mathcal{K}_3\) to the extent that they are used to capture transferable action regularities across embodiments, rather than merely benefiting from larger-scale pretraining.


\(\mathcal{K}_1\) is the level of support that makes local interaction learnable, grounding capability in immediate contact, geometry, and short-horizon control.

\(\mathcal{K}_2\) is the level of support that makes task structure learnable, enabling local interactions to be composed into temporally extended execution.

\(\mathcal{K}_3\) is the level of support that makes cross-embodiment transfer learnable, by exposing the shared structure required for generalization beyond a single embodiment.

Embodied manipulation is learned within a feasible space already shaped by embodiment, structured recorded data, and carried forward by knowledge support.


In this section, \(\mathcal{D}\) remains the immediate object of learning: a structured record of embodied execution from which the system learns. What learning acquires from this object is the knowledge support \(\mathcal{K}\) induced by the data ecosystem. Different learning paradigms should therefore not be understood as learning different objects or defining independent knowledge categories. Rather, they differ in how the same underlying support is internalized, organized, and made operational under embodiment constraints. This is why \(\mathcal{K}\) serves as the underlying organizing logic of the chapter, while the taxonomy itself is presented through two major learning paths, cognitive planning and policy learning, and their corresponding sub-directions.


The object available to learning remains \(\mathcal{D}\), whereas \(\mathcal{K}\) denotes the knowledge support induced by that object. What varies across learning paradigms is therefore not the ultimate learning object itself, but the way in which this support is internalized, organized, and externalized under embodiment constraints. In this sense, \(\mathcal{K}\) provides the underlying logic of the taxonomy, while B and P describe its two principal learning paths.


Embodied learning is internalization, organization, and expression of \(\mathcal{K}\) support within a feasible space already constrained by embodiment foundations.

Embodied manipulation is learned within a feasible space already shaped by embodiment foundations, reflected in \(\mathcal{D}\), and inherited by \(\mathcal{K}\).



对，这正好反过来解释了为什么你的 taxonomy 很难分干净，而且这不是你分类能力不够，而是对象本身就不干净。

更准确地说，你的 taxonomy 分不干净，至少说明了三件事：

第一，类别之间不是天然互斥的。
很多方法不是落在单一范畴里，而是同时混合了多个设计维度：表示、规划、控制、接口、适配机制。你在分类时看到的“重叠”，往往不是 taxonomy 的失误，而是方法本身就是混成的。

第二，同一个标签下面的方法并不功能等价。
也就是说，名字一样，不代表它们在 grounding、executability、control coupling、deployment role 上是同一种东西。这样一来，按“名义类别”分类就必然会漏掉真正重要的差异。

第三，决定方法形态的主轴不是单一原理，而是 trade-off 和 deployment context。
当设计选择主要由任务结构、平台条件、实时性要求、可执行性约束共同决定时，taxonomy 就很难像纯理论分类那样切出清晰边界。因为边界本身就在被具体条件不断改写。

所以你可以把这个判断说得更锋利一点：

The difficulty of drawing a clean taxonomy is itself symptomatic of the field: the relevant categories are neither functionally uniform nor compositionally stable, because system design is shaped less by a single organizing principle than by layered trade-offs across tasks, platforms, and deployment conditions.

中文压缩一下就是：

taxonomy 分不干净，本身就是问题结构的一部分。它说明这个领域的方法类别既不功能齐整，也不组合稳定，其边界会随着任务、平台和部署约束的变化而变形。

这其实是个很强的论点，因为它把“分类不够整齐”从一个写作缺陷，转成了一个诊断信号：

不是 taxonomy 失败了，而是 taxonomy 的模糊性暴露了该领域尚未形成稳定、可分解、可收敛的方法结构。

如果你愿意，你这里甚至可以顺手落一句很漂亮的话：

In this sense, the taxonomy does not fail despite the field’s complexity; it becomes informative precisely where clean separation breaks down.

这句的意思是：

taxonomy 的价值，不是在于硬分干净，而是在于它在哪些地方分不干净，恰恰揭示了领域真正的结构张力。


一、流水线的起点不是 D，而是 embodiment

这篇一开始就说，physical embodiment 和 software framework 一起定义了机器人系统可实现 perception、action、coordination 的条件；更具体地说，end effector 决定 contact space，sensor 决定 observation space，arm/platform 决定 execution structure，而 software/control stack 决定这些能力如何在 runtime 被组织和执行。最后作者明确说：这些 physical and computational constraints shape system execution and define the data requirements for learning。

这一步很重要，因为它说明：

D 不是凭空出现的数据集，D 是 embodiment constraints 被记录下来的形式。

也就是说，
机器人能看到什么、摸到什么、如何动作、哪些动作稳定可复现、哪些状态能被观测——这些都先由 embodiment 决定，然后才进入数据。

所以如果写成最前面的链条，就是：

Embodiment / software stack
→ 决定 observation space / contact space / execution structure
→ 决定什么样的 embodied execution 可以被记录
→ 才有 D。

二、D 到底是什么：不是“数据集”，而是 embodied execution 的结构化记录

作者对 D 的定义非常关键。文中明确说：

𝐷
D 是 a structured record of embodied execution generated as the robot interacts with the world。
更具体地，它包括：

motion sequences
sensory observations
contact events
state transitions。

这四项其实就是作者整篇最重要的“数据构成论”。

所以 D 不是普通意义上的训练样本，而是：

机器人在具身约束下与世界发生耦合时，留下来的四种核心痕迹。

这意味着后面所有 learning，本质上都在利用这四类支撑：

motion sequences：动作怎么展开
sensory observations：过程看到了什么
contact events：接触怎么发生、怎么变化
state transitions：任务状态如何被改变。
三、D 不是单层的，作者把它分成 D1 / D2 / D3

作者接着说，embodied datasets 不是平的，而是在逐步扩大“support for learning”。于是把 D 写成分层演化：

𝐷
1
D
1
	​

：skill-level datasets，编码 local interaction dynamics
𝐷
2
D
2
	​

：task-level datasets，编码 skills 如何被组织成 temporally extended behaviors
𝐷
3
D
3
	​

：foundation-level datasets，编码 cross-embodiment variation needed for transfer at scale。

这是整篇里 D 和 K 开始联动的地方，因为作者紧接着说：

each tier enlarges the available data support and thereby expands the effective knowledge support 
𝐾
K available to the system.

也就是说：

D1 不只是“小数据”，而是支持局部交互知识
D2 不只是“长轨迹”，而是支持任务结构知识
D3 不只是“多机器人大规模数据”，而是支持跨 embodiment 的可迁移知识。
四、K 到底是什么：不是显式知识库，而是“knowledge support”

这里最容易误解。
K 不是作者说的某个独立模块，也不是显式 symbolic knowledge base。

它更像是：

系统从 D 中可以获得并组织起来、用来支撑操控能力的知识基础。

作者在 learning section 里明确说：

learning paradigms take 
𝐷
D as the central object
from 
𝐷
D, the knowledge support 
𝐾
K is acquired and organized
\mathcal K}_1 supports local interaction
\mathcal K}_2 supports task structure over time
\mathcal K}_3 supports transferable structure across embodiments。

所以 K 最准确的理解不是“知识内容本身”，而是：

可被学习系统提炼出来、并足以支撑某一级操控能力的结构化知识支持。

于是：

K1 对应 local interaction competence
K2 对应 long-horizon task organization
K3 对应 transfer/generalization across embodiments。

换句话说，D 是“被记录下来的 embodied experience”，K 是“从这些 experience 中可形成的 support hierarchy”。

五、B 和 P 到底是什么：它们不是 K 的结果，而是 K 的两种组织路径

这是整篇最关键、也最容易被说错的地方。

很多人会顺手把它理解成：

先有 D，再得到 K，然后再做 B 和 P。

但作者写得更精确：
B 和 P 是 acquiring and organizing K 的两类 learning paradigms。

也就是说：

B（cognitive planning）：更偏从 sensory observations + state transitions 中获取和组织 K，用来形成 intermediate artifacts and action specification
P（policy learning）：更偏从 contact events + motion sequences 中获取和组织 K，用来形成 executable motor behavior through action representations。

这句话非常重要，因为它说明：

B 和 P 不是两个成品模块，而是两种不同的“知识组织机制”。

5.1 B：从 D 中抽取“中间结构”

作者把 B 叫做 cognitive planning，并细分成 B1–B5。
它们的共同点是：不直接等于动作，而是产生某种 intermediate artifact。

B1：semantic logic / code generation
输出 code、reward、skill ranking 这类可执行语义规格
B2：long-horizon task decomposition
输出 sub-task sequence / symbolic task plan
B3：grounded multimodal reasoning
输出 grounded scene-conditioned task representation
B4：geometric grounding / spatial intelligence
输出 contact region、pose、affordance map、3D field 这类空间表示
B5：generative dynamics / physical imagination
输出 imagined futures / predicted consequences，用来评估行动。

所以 B 的功能不是“直接控制”，而是：

把 D 中的 observation/state-transition 支撑组织成某种足以指导执行的中间表示。

这也是为什么文中说 B1/B2/B5 更强调 state transitions，而 B3/B4 更强调 sensory observations。

5.2 P：从 D 中抽取“可执行动作机制”

作者把 P 叫做 policy learning，并按 action representation 分成 P1–P3。

P1：explicit continuous
直接回归 continuous action vectors
P2：discrete action
把动作 token 化，做 autoregressive generation
P3：iterative generative
用 diffusion / flow matching 建模完整 action distribution。

P 的共同点是：

它更接近“从 perception 到 motor command”的执行环节。

所以它更强调 D 里的：

contact events
motion sequences。

也就是说：

B 更像把 K 组织成“怎么想、怎么表征、怎么中介”；
P 更像把 K 组织成“怎么做、怎么出动作、怎么闭环执行”。

六、从 B/P 到 integration：文章真正关心的是两条路怎么接起来

作者接下来明确说：

To learn from the full structured record of D, a practical and widely adopted solution is to integrate cognitive planning and policy learning within a complete manipulation learning paradigm.

这句话说明：

仅有 B 不够，因为它往往停在中间 artifact
仅有 P 也不够，因为它难以覆盖高层 reasoning
所以完整系统需要把两者耦合起来。

于是 integration 被分成三类：

Type I：Unified End-to-End

一个 shared backbone 同时吸收 reasoning 和 action generation。
典型配对是 B3 + P2/P3，对应 K3 级的数据支持。

Type II：Hierarchical

把 slow planning 和 fast execution 分开。
显式层级多见 B1/B2 + P1/P2；隐式层级多见 B2/B3 + P2/P3。

Type III：Shared World Representation

让 planning 和 policy 共同消费一个 shared state。
如果 shared state 是 spatial 的，就偏 B4 + P1/P2/P3；
如果 shared state 是 predictive world model，就偏 B5 + P3。

所以从流水线看，这里发生的是：

D 提供的多种支撑 → 被 B / P 分别组织 → 再在 integration 层被耦合成系统架构。

七、deployment 不是尾声，而是 B/P 系统真正进入现实的第二次加工

deployment 这一章特别重要，因为它说明：

B/P integration 之后，系统还没有真正完成。

作者把 deployment 写成三阶段：

S1 Offline Pre-deployment

把 learned system 从训练状态改造成能上真实机器人之前的状态：
包括 offline RL at scale、cross-embodiment transfer、sim-to-real alignment、compression。

S2 Online Physical Alignment

系统上到真实硬件后，还要适应 real contact、friction、noise、OOD objects。
这里发生的是 post-training improvement、real-world fine-tuning、contact-rich refinement。

S3 Inference-Time Execution

真正运行时，要解决 latency、quantization、decoding acceleration、runtime robustness、failure recovery。

所以 deployment 在这篇文里不是“工程细节”，而是：

K 经过 B/P 组织后，要变成真实 embodied capability，还必须经历第二轮系统加工。

八、evaluation 如何回头检查整条流水线

作者自己给了一个非常明确的回看方式：

Execution Quality：检查 B 和 P 能否把 D 诱导出的 K 组织成成功的 embodied task execution
Data Efficiency & Quality：检查 D 是否足够 efficient / informative，能够诱导 useful K
Generalization & Transfer：检查从 D 学到、经 B/P 组织的 K，在 embodiment 变化和 distribution shift 下是否仍然 robust
Deployment Cost：检查由 B/P 从 D-induced K 产生的 embodied capability，是否能在 deployment pipeline 中高效执行。

这一步很关键，因为 evaluation 不是只测 policy，而是在四个角度回查整条链：

D 好不好？
K 够不够？
B/P 组织得对不对？
deployment 后还能不能跑？

九、把整条流水线压成一句真正完整的话

这篇文章里的完整流水线，其实应该写成：

Embodiment 与 software stack 先定义 observation/contact/execution constraints；
这些 constraints 被记录成 D（motion sequences, sensory observations, contact events, state transitions）；
不同层级的 D（D1/D2/D3）扩展出不同层级的 knowledge support K（K1/K2/K3）；
B 和 P 不是 K 之后的附属模块，而是从 D 中获取并组织 K 的两类学习路径——B 更生成中间 planning artifacts，P 更生成 executable motor behavior；
integration 把 B/P 耦合成完整系统；
deployment 再把这个系统加工成可在真实机器人上运行的能力；
evaluation 最后从 execution、data、generalization、deployment cost 四个角度回查这条链是否成立。

十、这条流水线里最深的 insight

如果只留一个最重要的 insight，我会留这个：

这篇文章真正想做的，不是给机器人方法分类，而是把“操控智能”重新表述成一条由 embodied constraints 驱动的数据—知识—组织—部署流水线。

因此：

D 不是资源，是 embodied execution 的记录
K 不是显式知识库，是由 D 支撑出来的能力层级
B/P 不是并列模型种类，而是两种获取和组织 K 的路径
integration / deployment / evaluation 则是在检查这些路径能否真正拼成并支撑现实系统。

这才是这篇文章最硬的骨架。


B1 is closest to the semantic interface of MLLMs, producing executable semantic specifications such as skill rankings, programs, reward functions, and behavior trees.
A first form is skill-level alignment.
SayCan~\cite{brohan2023can} grounds abstract language goals by scoring primitive skills according to both semantic relevance and execution feasibility, but its output remains a ranked selection over predefined skills rather than a compositional execution program.
Program synthesis makes the semantic specification more explicit.
CaP~\cite{liang2022code} generates executable Python from natural language, while ProgPrompt~\cite{singh2022progprompt} embeds precondition assertions into the prompt structure to enforce logical constraints.
Demo2Code~\cite{wang2023demo2code} extends this direction beyond language-only input by translating visual demonstrations into symbolic code.
A parallel form specifies objectives rather than control programs.
Tan et al.~\cite{tan2023l2r} synthesize programmatic reward functions that decouple semantic task specification from continuous trajectory optimization.
Text2Touch~\cite{field2025text2touch} extends reward synthesis to tactile dexterous manipulation by using LLMs to design reward functions over tactile and proprioceptive signals.
Structured control flow provides another executable specification.
LLM-BT~\cite{zhou2024llmbt} generates behavior trees that can be dynamically updated under environmental changes, while LLM-as-BT~\cite{ao2025llmbt} generates modular behavior trees that support reactive switching and error recovery.
Overall, B1 methods formulate task structure as executable semantic specifications.
They mainly require \(\mathcal{K}_2\), because their outputs are organized around task semantics, skill preconditions, objectives, and control logic rather than local sensorimotor dynamics.


Type~II models separate slower reasoning from faster execution, and their key distinction lies in how the reasoning--execution interface is represented.
One paradigm exposes this interface explicitly through intermediate structures such as language motions, reasoning traces, symbolic bridges, or coarse paths.
RT-H~\cite{belkhale2024rth} introduces language motions as an intermediate layer between high-level instructions and low-level actions.
CoT-VLA~\cite{zhao2025cotvla} and ThinkAct~\cite{huang2025thinkact} expose intermediate reasoning steps, RoBridge~\cite{zhang2025robridge} places a symbolic bridge between a cognitive planner and a learned policy, and HAMSTER~\cite{li2025hamster} predicts a coarse 2D path to guide low-level 3D manipulation.

The other paradigm keeps the hierarchy more implicit, separating reasoning and execution at the architectural or latent level rather than through a fully exposed symbolic interface.
FiS-VLA~\cite{chen2025fis} couples a slower semantic branch with a real-time execution branch, while Hi Robot~\cite{shi2025hirobot} adopts a hierarchical 
design for open-ended instruction following and user feedback during execution.



Because semantic grounding and action generation are integrated into the same unified backbone, the model needs to process heterogeneous information. This makes it difficult for the shared backbone to learn representations that support both semantic understanding and precise action generation.