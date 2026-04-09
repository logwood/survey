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

B1 methods are unified by their production of executable task specifications, such as code, rewards, or structured control flow, and are therefore organized around task-level structure, with \(\mathcal{K}_2\) providing their primary support.

B2 methods are unified by task decomposition, symbolic planning, and replanning, and likewise center on task-level structure, making \(\mathcal{K}_2\) their primary source of support.

Within B3, explicit grounding remains organized around task-conditioned scene understanding and is primarily supported by \(\mathcal{K}_2\), whereas implicit grounding draws more heavily on foundation-scale multimodal priors and is thus better supported by \(\mathcal{K}_3\).

Within B4, local interaction grounding is grounded in contact, geometry, and affordance structure, and therefore relies primarily on \(\mathcal{K}_1\), whereas higher-level constraint reasoning is more closely tied to task-level constraint use and is better supported by \(\mathcal{K}_2\).

Within B5, task-conditioned future prediction remains centered on embodied task trajectories and is primarily supported by \(\mathcal{K}_2\), whereas larger latent world simulation draws more heavily on broad predictive priors and is more naturally supported by \(\mathcal{K}_3\).

Within P1, reactive local control is grounded in local interaction and therefore relies primarily on \(\mathcal{K}_1\), whereas task-conditioned, chunked, and recovery-aware policies are more structured by task-level execution and are better supported by \(\mathcal{K}_2\).

Within P2, task-scale discrete action generation remains organized around task-level action structure and is primarily supported by \(\mathcal{K}_2\), whereas multimodal and generalist token policies draw more heavily on large-scale priors and are thus better supported by \(\mathcal{K}_3\).

Within P3, local generative control is grounded in continuous interaction and therefore relies primarily on \(\mathcal{K}_1\), whereas large-scale generalist generative policies depend more on heterogeneous pretraining and are correspondingly better supported by \(\mathcal{K}_3\).


In our view, the object of learning remains the knowledge support encoded in the data ecosystem. 
The paradigm-level distinctions introduced below are derived from the underlying support structure of \(\mathcal{K}\) and become explicit through different architectural parameterizations. 
In embodied manipulation, this is especially clear for robotic arms, where most capability is induced from the support already present in the data, except when additional priors are injected through exogenous parameterizations.

The data ecosystem discussed in Section~\ref{sec:embodiment_dataset} provides \(\mathcal{D}\), a structured record of embodied execution containing sensory observations, sequences of motion, state transitions, and contact events. The present section examines how different learning paradigms use these records to acquire the knowledge support needed for manipulation.


\(\mathcal{K}_1\) is the level of support that makes local interaction learnable, grounding capability in immediate contact, geometry, and short-horizon control.

\(\mathcal{K}_2\) is the level of support that makes task structure learnable, enabling local interactions to be composed into temporally extended execution.

\(\mathcal{K}_3\) is the level of support that makes cross-embodiment transfer learnable, by exposing the shared structure required for generalization beyond a single embodiment.

Embodied manipulation is learned within a feasible space already shaped by embodiment, structured recorded data, and carried forward by knowledge support.
