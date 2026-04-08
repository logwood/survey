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