# ChatGPT Chat Log

Pasted text.txt
Document
现在的第二章没有起到约束得作用，写成了overview，你来进行研究修改并能更好的衔接下文

---

我先把这章当成“结构性问题”来处理，不只润色措辞，而是把它从“硬件综述”改成“对后文学习与数据章节施加约束的前置章”。然后我会直接给你一版可替换的 LaTeX。

---

我已经定位到核心问题了：现在这一章的开头把自己定义成了 “reviews the hardware landscape”，图注也写成 “Overview of physical embodiments”，所以读者自然会把它当作 catalog，而不是后文学习问题的约束前提。原文结尾虽然提到 constraints 和 data requirements，但中间各小节没有持续把“约束链条”说穿。

Pasted text

---

你这个判断是对的。现在第二章的问题不在“材料不够”，而在“叙述功能错位”：开头直接说 reviews the hardware landscape，图注也写成 Overview of physical embodiments，于是整章被读成了 taxonomy / catalog；但你真正需要它承担的是：在学习方法、数据构造和系统设计之前，先定义 embodiment 带来的可行性边界与约束传导链条。原文结尾已经想往 data 过渡，但中间各小节没有持续把“硬件/软件选择 → 控制约束 → 数据需求”这条链收紧，所以约束感没有立住。

Pasted text

我建议不要小修小补，而是把第二章改成下面这个逻辑：

不是在回答“机器人有哪些形态”，而是在回答
“不同 embodiment 会分别约束什么，因此后面的 learning/data 章节必须解决什么问题”。

下面这版尽量保留你现有材料、例子、图表和引用，只重写叙述框架。你可以直接替换。

LaTeX
\section{Embodiment Foundations of Robotic Arms}\label{sec:embodiment_hardware}

The feasible behavior of a robotic manipulation policy is bounded before learning begins. 
End-effector geometry determines admissible contact modes, manipulator kinematics determines reachable motions, base configuration determines stability and workspace, and the software stack determines whether perception and control can be closed within the required latency budget. 
Accordingly, this section does not aim to provide a broad overview of robotic hardware and software. Instead, it identifies the embodiment-induced constraints that shape what a policy can represent, what a controller can execute, and what data later chapters must provide.

For robotic arm systems, these constraints recur along four dimensions. 
First, embodiment defines the \emph{contact and action space}: different end effectors expose different grasp primitives, force transmission properties, and controllable degrees of freedom. 
Second, it defines \emph{observability}: the sensing stack determines whether task-relevant state is available before contact, during contact, or only indirectly through delayed proxies. 
Third, it defines \emph{dynamic coupling and stability}: as systems expand from fixed-base arms to mobile or whole-body platforms, manipulation becomes increasingly coupled with base motion, balance, and multi-contact coordination. 
Fourth, it defines \emph{computational and temporal constraints}: the control stack must transport data and execute feedback fast enough for the physical system to remain stable. 
The rest of this section is organized around these constraints rather than around hardware categories alone.

\subsection{Physical Embodiment as a Source of Constraint}

Physical embodiment shapes what a manipulation system can sense, control, and execute, but more importantly it determines \emph{which difficulties are structural rather than algorithmic}. 
As shown in Figure~\ref{fig:embodiment_taxonomy}, robotic arm systems can be analyzed at three levels: the end effector, the manipulator platform, and the mobile or whole-body base. 
These levels should not be read as a taxonomy of hardware options, but as a hierarchy of constraints. 
The end effector fixes the local contact interface and the dimensionality of fine manipulation. 
The fixed-base platform determines reachability, precision, and coordination structure. 
The mobile or whole-body platform enlarges workspace only by introducing stronger coupling among manipulation, locomotion, and stability.

\subsubsection{End Effectors and Contact Sensing}\label{subsec:end_effectors}

End effectors constrain manipulation first by fixing the robot's admissible contact primitives, and second by determining what contact state can be observed once interaction begins. 
Parallel-jaw and adaptive grippers, including common Robotiq 2F/3F-style designs, reduce the manipulation problem to a comparatively low-dimensional grasp-and-place regime. 
Their appeal lies not only in robustness and implementation simplicity, but also in the fact that they narrow the control and learning problem: grasp closure, pose alignment, and force regulation remain relatively structured. 
Dexterous hands such as Shadow Hand and Allegro Hand enlarge the reachable manipulation space, but they do so by increasing action dimensionality, contact combinatorics, inverse-kinematics complexity, and force-distribution ambiguity. 
Soft hands such as RBO Hand~3~\cite{Puhlmann_2022}, Festo BionicSoftHand, and SpiRobs shift part of the burden from explicit force control to passive compliance. 
This improves tolerance to geometric uncertainty, but it also makes state estimation, contact inference, and dynamics identification more difficult.

The sensing stack determines whether these contact-rich behaviors are observable enough to control. 
Eye-in-hand vision resolves geometry before contact, but once interaction starts it provides only indirect evidence about force, slip, and local deformation. 
Tactile sensing fills this observability gap: vision-based tactile sensors such as GelSight~\cite{zhao2023gelsightsveltehumanfingershaped} and DIGIT convert contact geometry into images, while force- and vibration-sensitive sensors such as BioTac expose signals relevant to slip detection and contact regulation. 
This distinction matters because tasks such as insertion, re-grasping, and fragile-object handling are not limited primarily by global object pose estimation; they are limited by whether the controller can observe contact state quickly and reliably enough to close the loop. 
Embodiment therefore directly determines what information the dataset must contain: for some systems RGB observations may be sufficient, whereas for others the critical supervision lies in tactile transients, force signatures, or multimodal synchronization around contact events.

\subsubsection{Fixed-base Platforms}\label{subsec:manipulators}

Fixed-base manipulators constrain manipulation mainly through reachability, precision, and coordination structure. 
Single-arm systems such as Franka Panda, KUKA iiwa, and Kinova Gen3 remain common for contact-rich manipulation because they provide stable control conditions and largely decouple manipulation from mobility. 
This decoupling is not merely a convenience for system integration; it narrows the problem class itself. 
With base stability treated as given, policy design and data collection can focus on arm kinematics, local contact regulation, and end-effector behavior rather than on full-body balance or navigation-induced uncertainty.

Bimanual fixed-base systems, such as dual Franka Panda setups or ABB YuMi, enlarge the task set to handover, folding, assembly, and other coordinated interactions, but they do so by introducing a qualitatively different constraint regime. 
Once two manipulators act on the same object, the system must regulate internal forces, avoid self-collision, and occasionally satisfy closed-chain constraints. 
As a result, the bottleneck shifts from single-end-effector precision to coordination across multiple contact points and multiple kinematic chains. 
This shift has direct consequences for learning: demonstrations and datasets must now capture relative timing, force sharing, object-mediated coupling, and failure modes that do not appear in single-arm settings.

\subsubsection{Mobile and Whole-body Platforms}\label{subsec:mobile_platforms}

Mobile and whole-body embodiments relax workspace constraints only by introducing stronger dynamic coupling. 
Wheeled mobile manipulators such as PR2, TIAGo, and Stretch extend task coverage beyond fixed workcells, but arm motion must now be reconciled with navigation limits, base positioning error, and nontrivial motion-planning dependencies between base and end effector. 
Legged manipulators, for example Spot-based systems or Unitree platforms equipped with arms, intensify this coupling further: when the arm interacts with the environment, contact forces perturb foothold stability, so manipulation competes directly with locomotion and balance.

Humanoids such as Atlas, Figure~02, Optimus, and Unitree G1 combine bipedal balance, whole-body coordination, and often bimanual manipulation within a single control stack. 
In these systems, manipulation is no longer a localized arm-level problem. 
Contact forces, posture regulation, center-of-mass motion, angular momentum, and environment support conditions must all be coordinated together. 
From the perspective of learning, this means that embodiment enlarges task diversity at the cost of substantially increasing state dimensionality, coupling strength, and failure modes. 
What appears as a broader opportunity set at the system level is simultaneously a much tighter requirement on representation, control bandwidth, and data coverage.

\begin{figure}[t]
    \centering
    \includegraphics[width=\linewidth,trim=0cm 4.1cm 0cm 5.9cm,clip]{assets/embodiment.pdf}
    \caption{Embodiment hierarchy as a source of manipulation constraints. The figure organizes robotic manipulation systems by end effectors, sensing, stationary platforms, and mobile platforms. Rather than serving only as a taxonomy, the hierarchy highlights how embodiment choices alter contact primitives, observability, coordination structure, and stability requirements.}
    \Description{A hierarchical diagram showing embodiments for robotic manipulation. End effectors are classified by contact modality (jaw gripper, dexterous hand, soft hand) and sensing (vision, tactile); platforms are divided into stationary (single-arm, bimanual) and mobile (wheeled, quadrupedal, humanoid). The purpose is to illustrate how embodiment choices change constraints on control and learning.}\label{fig:embodiment_taxonomy}
\end{figure}

\subsection{Software Framework as Computational Constraint}

If physical embodiment determines what the robot can in principle do, the software stack determines what it can do reliably in time. 
For embodied manipulation, software is not a neutral implementation layer. 
It defines whether multimodal observations arrive before they become stale, whether feedback can be closed at the control rate, and whether high-level reasoning can be connected to low-level actuation without violating timing and safety constraints. 
We therefore organize the software stack into three tiers, as summarized in Table~\ref{tab:framework_comparison}, with each tier corresponding to a distinct computational bottleneck.

\subsubsection{Modern Robotics Middleware and Operating Systems}\label{subsec:control_middleware}

The Kernel Layer (L0) constrains temporal determinism and low-latency execution. 
Industrial stacks rely on kernels such as VxWorks\footnote{\url{https://www.windriver.com/products/vxworks}} and QNX\footnote{\url{https://blackberry.qnx.com}} for bounded interrupt latency and fault isolation, while Zephyr\footnote{\url{https://zephyrproject.org/}} extends similar guarantees to resource-constrained edge devices. 
At this layer, the key question is not functionality but whether the controller can execute with sufficiently low jitter for high-frequency feedback to remain stable.

The Transport Layer (L1) constrains how perception, policy, and control modules exchange information. 
ROS~2, built on decentralized DDS~\cite{macenski2022robot}, remains the dominant general-purpose middleware because it provides configurable quality-of-service policies for distributed robotic systems. 
However, embodied intelligence increasingly stresses this layer not through simple message passing, but through the movement of high-rate multimodal data streams. 
This is why zero-copy and shared-memory designs such as Dora-rs~\cite{zhang2026dora} become relevant: they reduce the latency and serialization overhead that would otherwise make rich perceptual feedback unusable at control time.

The System Layer (L2) constrains orchestration across robots, edge devices, cloud services, and fleets. 
Systems such as Zenoh-Flow and FogROS2 elevate deployment, routing, and compute offloading into first-class concerns, while RoboOS reflects a more AI-native direction in which high-level multimodal planning is coupled to modular skill execution across heterogeneous embodiments~\cite{baldoni2023zenohflow, ichnowski2022fogros2, wang2025roboos}. 
At this layer, the issue is no longer only whether messages can be exchanged, but whether system-level composition preserves the latency, reliability, and abstraction boundaries required by embodied control.

\begin{table}[t]
\centering
\caption{\textbf{Three-tier software architecture viewed through computational constraints.}
The software stack is organized into three layers. L0 is the Kernel Layer for hard real-time motor control with microsecond-level determinism. L1 is the Transport Layer for high-throughput, low-latency inter-process and inter-device communication. L2 is the System Layer for distributed orchestration across robots, edge devices, cloud resources, and fleets. The table highlights how each layer introduces a different systems bottleneck for embodied intelligence: execution jitter, communication overhead, and deployment-scale orchestration.}\label{tab:framework_comparison}
\renewcommand{\arraystretch}{1.2}
\setlength{\tabcolsep}{3pt}
\scriptsize

% keep the original tabular content unchanged
\begin{tabular}{
  l
  p{0.10\linewidth}
  p{0.15\linewidth}
  p{0.34\linewidth}
  p{0.06\linewidth}
  p{0.12\linewidth}
}
\toprule
\textbf{Framework} &
\textbf{Type} &
\textbf{Core Mechanism} &
\textbf{Key Contribution} &
\textbf{Profile} &
\textbf{Scope} \\
\midrule

\multicolumn{6}{c}{\textbf{L0: Kernel Layer}} \\
\midrule

\textbf{VxWorks} &
Monolithic&
Priority Preemptive &
Deterministic RTOS kernel with priority-based preemptive scheduling, designed for low-latency and low-jitter execution in mission-critical control systems. &
$<$10\,$\mu$s &
Industrial \\

\textbf{QNX} &
Microkernel &
Spatial Isolation &
Microkernel RTOS that isolates drivers and system services in user space, improving fault containment while preserving deterministic scheduling. &
$<$5\,$\mu$s &
Safety-critical \\

\textbf{Zephyr} &
Modular&
Device Tree + SMP &
Modular RTOS with device-tree-based hardware abstraction and SMP support, aimed at resource-constrained robotic and edge platforms. &
$<$20\,$\mu$s &
Robotic Edge \\

\midrule
\multicolumn{6}{c}{\textbf{L1: Transport Layer}} \\
\midrule

\textbf{ROS~2}~\cite{macenski2022robot} &
Decentralized &
DDS (RTPS) &
Decentralized middleware built on DDS/RTPS, providing configurable QoS policies for reliability, deadline, and liveliness in distributed robotic systems. &
1--10\,ms &
General Robotics \\

\textbf{Dora-rs}~\cite{zhang2026dora} &
Dataflow &
Apache Arrow &
Rust-based dataflow runtime using Apache Arrow and shared memory for low-latency, zero-copy exchange across modular robotic processes. &
$<$50\,$\mu$s &
Low-latency AI \\

\midrule
\multicolumn{6}{c}{\textbf{L2: System Layer}} \\
\midrule

\textbf{Zenoh-Flow}~\cite{baldoni2023zenohflow} &
DAG &
Zenoh Protocol &
Communication and query protocol that unifies pub/sub, storage, and distributed computation across devices ranging from embedded nodes to edge and cloud systems. &
Cloud &
Distributed \\

\textbf{FogROS2}~\cite{ichnowski2022fogros2} &
Cloud &
ROS~2 Graph &
ROS 2 extension for hybrid edge-cloud execution, enabling selected components of a robotic graph to be offloaded while retaining local reactive control. &
Hybrid &
Raas \\

\textbf{RoboOS}~\cite{wang2025roboos} &
Agentic &
MLLM + Skill Lib &
Hierarchical system architecture that separates high-level perception and planning from modular low-level skill execution, with support for cross-embodiment and multi-agent coordination. &
Logic &
Multi-Agent \\

\bottomrule
\end{tabular}
\end{table}

\subsubsection{Low-level Motion Planning and Control}

While middleware determines how information moves, the low-level motion generation and control layer determines whether task-space intent can be converted into physically admissible commands under embodiment-specific constraints. 
Its role is to solve several tightly coupled problems simultaneously: mapping between operational and joint space, compensating nonlinear rigid-body dynamics, enforcing joint and collision constraints, and maintaining stability under external contact. 
Optimization-based approaches, particularly model predictive control and whole-body control, are widely adopted because they can encode tracking, feasibility, and safety within a unified constrained optimization problem solved online at the control rate~\cite{schulman2014optimizing}.

In manipulation, contact behavior matters as much as free-space tracking accuracy. 
Impedance control remains a standard mechanism for shaping compliant interaction during assembly, tool use, and human-robot collaboration, because it allows the robot to absorb positional deviations through compliance and tuned stiffness. 
But the effectiveness of MPC, WBC, and impedance control is inseparable from the embodiment and systems stack discussed above: high-dimensional hands demand richer contact regulation, mobile and humanoid platforms require stronger coordination across coupled subsystems, and all of these controllers rely on sufficiently deterministic execution to keep high-frequency feedback stable.

Taken together, embodiment and software define the hypothesis space within which learning operates. 
They determine which actions are available, which state variables are observable, which couplings dominate task execution, and which latency budgets cannot be violated. 
For that reason, the next issue is not simply how much data to collect, but what data must be collected to make these constraints learnable: which modalities must be recorded, which transitions must be covered, and which contact or coordination events must be represented densely enough for robust policy acquisition.

这版修改的关键点有三个：

把章节功能从“分类介绍”改成“约束定义”
原文的问题是每节都在介绍“有什么”，现在改成每节都回答“这会约束什么”。这会让第二章在论文结构里变成方法与数据章节的前提条件，而不是平行综述。

Pasted text

把“约束”显式拆成四条主线
我给你收成了四个 recurring constraints：

contact/action space

observability

dynamic coupling and stability

computational / temporal constraints
这样后面第三章写 data 的时候就能自然对应成：采什么模态、覆盖哪些 interaction regime、同步精度要求多高、哪些 failure modes 必须进数据集。

把结尾过渡从泛泛而谈改成 data-facing question
原文最后一句已经有过渡意图，但还比较抽象。新版明确落到：

which modalities must be recorded

which transitions must be covered

which contact / coordination events must be represented densely enough
这样下文一开头写 data collection / dataset design 就会非常顺。

如果你想让衔接再更狠一点，第三章开头第一段最好直接承接这四种 constraint，而不是重新从 “data is important” 起笔。

---

你翻译一下两段内容（不用翻译表），我看看

---

我先按我刚才改写版本开头的两段来翻。如果你指的是别的两段，我再继续替换。

第一段：

机械臂操作策略的可行行为边界，在学习开始之前就已经被预先限定。末端执行器的几何形态决定了系统可采用的接触方式，机械臂的运动学结构决定了其可达运动范围，底座配置决定了系统的稳定性与工作空间，而软件栈则决定了感知与控制能否在所需的时延预算内闭环运行。因此，本节的目的并不是对机器人软硬件进行宽泛综述，而是识别那些由 embodiment 所引入的约束：这些约束决定了策略能够表达什么、控制器能够执行什么，以及后续章节中的数据必须提供什么。

第二段：

对于机械臂系统而言，这些约束主要沿着四个维度反复出现。首先，embodiment 决定了接触与动作空间：不同类型的末端执行器对应着不同的抓取原语、力传递特性以及可控自由度。其次，它决定了可观测性：传感系统决定了任务相关状态是在接触前、接触中，还是只能通过滞后的间接信号被观测到。第三，它决定了动力学耦合与稳定性：当系统从固定基机械臂扩展到移动平台或全身系统时，操作任务会越来越强地与底盘运动、平衡控制以及多接触协调耦合在一起。第四，它决定了计算与时序约束：控制栈必须以足够低的延迟传输数据并执行反馈控制，系统才能维持稳定。基于此，后文将不再仅仅按照硬件类别展开，而是围绕这些约束来组织分析。

你要的话，我下一条直接把 “Physical Embodiment as a Source of Constraint” 下面的两段也翻出来。

---

翻译一下原文的全文

---

下面是你给的原文全文中文翻译，我按原有 LaTeX 结构保留，方便你直接对照。内容依据你上传的原文整理。

Pasted text

LaTeX
\section{机械臂的具身基础}\label{sec:embodiment_hardware}

机器人系统的动作空间受到其硬件具身形态的约束。
末端执行器的几何形态、机械臂的运动学结构以及底座的移动能力，共同决定了一项策略在物理上能够执行哪些任务。
本节将从末端执行器、固定平台和移动平台三个方面回顾硬件形态，并进一步考察将感知与执行闭环连接起来的软件栈。

\subsection{物理具身}

物理具身在很大程度上决定了一个操作系统能够感知什么、控制什么以及执行什么。
对于机械臂系统而言，这种影响可以分为三个层面来分析，如图~\ref{fig:embodiment_taxonomy} 所示。
末端执行器定义了接触界面。固定基平台决定了系统的可达范围与控制条件。
移动平台或全身平台则在扩展工作空间的同时，增加了操作与整体身体运动之间的耦合。

\subsubsection{末端执行器与接触感知}\label{subsec:end_effectors}

末端执行器决定了机器人如何与外部世界发生接触，而接触感知则决定了一旦接触开始，策略能够观测到什么。
平行夹爪和自适应夹爪——包括常见的 Robotiq 2F/3F 风格设计——在抓取稳健性和实现简洁性比手内灵巧操作更重要的场景中被广泛使用。
诸如 Shadow Hand 和 Allegro Hand 之类的灵巧手扩展了可实现的操作空间，但同时也增加了动作维度，并使接触规划、逆运动学和力分配更加困难。
诸如 RBO Hand~3~\cite{Puhlmann_2022}、Festo BionicSoftHand 和 SpiRobs 之类的软体手，则将部分控制负担从显式力控制转移到机械顺应性本身，从而提高了系统对不确定性的容忍度，但也使状态估计和动力学建模变得更加困难。

传感栈在接触密集型控制是否能够保持闭环方面起着重要作用。
手眼视觉可以在接触前解析物体几何，但一旦接触发生，它只能提供关于力、滑移和局部形变的间接信息。
触觉传感弥补了这一缺口：诸如 GelSight~\cite{zhao2023gelsightsveltehumanfingershaped} 和 DIGIT 这样的视觉式触觉传感器，会将接触几何转换为图像；而诸如 BioTac 这样的力觉与振动敏感传感器，则能够提供用于滑移检测和接触调节的信号。
在实际中，视觉—触觉融合在插接、重抓取和脆弱物体操作等任务中尤为重要，因为这些任务中与任务相关的反馈主要来自接触状态。

\subsubsection{固定基平台}\label{subsec:manipulators}

固定基机械臂仍然是接触密集型操作中的常见平台，因为它们提供了稳定的控制条件，并将操作问题与移动问题分离开来。
诸如 Franka Panda、KUKA iiwa 和 Kinova Gen3 这样的单臂系统，被广泛用于策略基准测试、遥操作以及高精度力控制任务。
它们的实际优势在于，底座稳定性通常是固定的，因此控制问题可以聚焦于机械臂运动学、接触调节以及末端执行器行为。

双臂固定基系统，例如双 Franka Panda 配置或 ABB YuMi，扩展了任务集合，使其能够处理交接、折叠、装配以及其他协同交互任务，但同时也引入了更强的双臂耦合。
一旦两个机械臂同时作用于同一个物体，控制问题就必须考虑内部力调节、碰撞规避以及闭链约束等问题。
与单臂系统相比，这类平台的瓶颈从局部末端执行器控制转移到了跨多个接触点的协调控制。

\subsubsection{移动平台与全身平台}\label{subsec:mobile_platforms}

将机械臂安装到移动底座上可以扩展任务覆盖范围，但同时也会将操作问题与系统级稳定性和运动规划耦合起来。
诸如 PR2、TIAGo 和 Stretch 之类的轮式移动操作平台，将机械臂控制与底座导航结合起来，迫使控制器在底座约束和末端执行器精度之间进行协调。
腿式操作平台，例如搭载机械臂的 Spot 系统或 Unitree 平台，则进一步加强了这种耦合：当机械臂与环境发生交互时，接触力会影响落足稳定性，因此操作会直接与运动和平衡竞争。

诸如 Atlas、Figure~02、Optimus 和 Unitree G1 之类的人形机器人，将双足平衡、全身协调以及通常的双臂操作整合进同一个控制栈中。
在这些系统里，操作已不再是一个局部的机械臂问题：接触力、姿态调节、质心运动以及角动量都必须被统一协调。
随着具身范围从固定基机械臂扩展到移动系统和人形系统，可执行任务的多样性虽然提高了，但接触、运动和稳定性之间的耦合程度也随之增加。

\begin{figure}[t]
    \centering
    \includegraphics[width=\linewidth,trim=0cm 4.1cm 0cm 5.9cm,clip]{assets/embodiment.pdf}
    \caption{机器人操作物理具身形态概览。该图涵盖了末端执行器、传感器、固定平台和移动平台。}
    \Description{一个分层图，用于展示机器人操作中的物理具身形态概览。末端执行器按照接触模态（夹爪、灵巧手、软体手）以及传感方式（视觉、触觉）分类；平台则分为固定式（单臂、双臂）和移动式（轮式、四足、人形）。}\label{fig:embodiment_taxonomy}
\end{figure}

\subsection{软件框架}

\subsubsection{现代机器人中间件与操作系统}\label{subsec:control_middleware}

具身操作系统的软件栈必须支持实时控制、高效数据传输，以及跨异构计算资源与硬件的系统级编排。
我们将这一软件栈组织为三层，如表~\ref{tab:framework_comparison} 所总结的那样。

内核层（L0）关注时间确定性和低延迟控制执行。
工业系统通常依赖 VxWorks\footnote{\url{https://www.windriver.com/products/vxworks}} 和 QNX\footnote{\url{https://blackberry.qnx.com}} 等内核，以获得有界中断延迟和故障隔离能力，而 Zephyr\footnote{\url{https://zephyrproject.org/}} 则将类似保证扩展到了资源受限的边缘设备。
传输层（L1）负责在进程、设备和模型组件之间传递数据，而当前主要依赖 ROS~2，其中去中心化的 DDS 取代了更早的中心化设计~\cite{macenski2022robot}。
对于具身模型而言，当前的压力已不再主要来自基本连通性，而是来自多模态数据传输的成本，这也推动了诸如 Dora-rs~\cite{zhang2026dora} 这样的零拷贝数据流设计的发展。
系统层（L2）则将重点从局部消息传递转向跨机器人、边缘设备、云服务以及机器人集群的编排。
诸如 Zenoh-Flow 和 FogROS2 这样的系统，将部署、路由和计算卸载视为一等问题；而 RoboOS 则代表了一个更近来的 AI-native 方向，即将高层多模态规划与可在异构具身之间复用的技能库相耦合~\cite{baldoni2023zenohflow, ichnowski2022fogros2, wang2025roboos}。

\begin{table}[t]
\centering
\caption{\textbf{面向具身智能的三层软件体系结构。}
该软件栈被组织为三层。L0 是内核层，用于具备微秒级确定性的硬实时电机控制。L1 是传输层，用于高吞吐、低延迟的进程间与设备间通信。L2 是系统层，用于跨机器人、边缘设备、云资源和机器人集群的分布式编排。Profile 一列对于 L0 和 L1 报告的是中断或 IPC 延迟，对于 L2 则报告部署或编排特征。}\label{tab:framework_comparison}
\renewcommand{\arraystretch}{1.2}
\setlength{\tabcolsep}{3pt}
\scriptsize

\begin{tabular}{
  l
  p{0.10\linewidth}
  p{0.15\linewidth}
  p{0.34\linewidth}
  p{0.06\linewidth}
  p{0.12\linewidth}
}
\toprule
\textbf{框架} &
\textbf{类型} &
\textbf{核心机制} &
\textbf{关键贡献} &
\textbf{性能特征} &
\textbf{适用范围} \\
\midrule

\multicolumn{6}{c}{\textbf{L0：内核层}} \\
\midrule

\textbf{VxWorks} &
单体内核 &
优先级抢占 &
具有确定性的 RTOS 内核，采用基于优先级的抢占式调度，面向任务关键型控制系统中的低延迟、低抖动执行。 &
$<$10\,$\mu$s &
工业 \\

\textbf{QNX} &
微内核 &
空间隔离 &
微内核 RTOS，将驱动和系统服务隔离在用户空间中，在保持确定性调度的同时提升故障隔离能力。 &
$<$5\,$\mu$s &
安全关键 \\

\textbf{Zephyr} &
模块化 &
设备树 + SMP &
模块化 RTOS，采用基于设备树的硬件抽象并支持 SMP，面向资源受限的机器人与边缘平台。 &
$<$20\,$\mu$s &
机器人边缘 \\

\midrule
\multicolumn{6}{c}{\textbf{L1：传输层}} \\
\midrule

\textbf{ROS~2}~\cite{macenski2022robot} &
去中心化 &
DDS (RTPS) &
基于 DDS/RTPS 的去中心化中间件，为分布式机器人系统提供可配置的 QoS 策略，包括可靠性、截止时间和存活性。 &
1--10\,ms &
通用机器人 \\

\textbf{Dora-rs}~\cite{zhang2026dora} &
数据流 &
Apache Arrow &
基于 Rust 的数据流运行时，使用 Apache Arrow 和共享内存，在模块化机器人进程之间实现低延迟、零拷贝的数据交换。 &
$<$50\,$\mu$s &
低延迟 AI \\

\midrule
\multicolumn{6}{c}{\textbf{L2：系统层}} \\
\midrule

\textbf{Zenoh-Flow}~\cite{baldoni2023zenohflow} &
DAG &
Zenoh 协议 &
一种通信与查询协议，统一了发布/订阅、存储和分布式计算，可跨从嵌入式节点到边缘与云系统的多种设备运行。 &
云 &
分布式 \\

\textbf{FogROS2}~\cite{ichnowski2022fogros2} &
云端 &
ROS~2 图 &
ROS 2 的扩展，用于混合边缘—云执行，可将机器人图中的选定组件卸载到云端，同时保留本地的快速响应控制。 &
混合 &
机器人即服务 \\

\textbf{RoboOS}~\cite{wang2025roboos} &
Agentic &
MLLM + 技能库 &
一种分层系统架构，将高层感知与规划同模块化的底层技能执行分离，并支持跨具身形态和多智能体协同。 &
逻辑 &
多智能体 \\

\bottomrule
\end{tabular}
\end{table}

\subsubsection{低层运动规划与控制}

中间件提供了通信底座，而低层运动生成与控制层则负责将任务空间参考转换为物理上可执行的关节指令。
它的核心作用是在多个紧密耦合的要求之间取得平衡：在操作空间与关节空间之间进行映射，补偿非线性刚体动力学，施加关节与碰撞约束，并在外部接触下维持稳定性。
因此，具身系统通常采用基于优化的控制器，尤其是模型预测控制（MPC）和全身控制（WBC），它们能够在统一的约束优化问题中，同时处理跟踪、可行性与安全目标，并以控制频率在线求解~\cite{schulman2014optimizing}。

在操作任务中，接触行为与自由空间精度同样重要。
阻抗控制仍然是装配、工具使用以及人机协作任务中塑造顺应性交互的标准机制，因为它使机器人能够通过顺应性和调节后的刚度来吸收位置偏差。
然而在实践中，MPC、WBC 和阻抗控制的有效性仍然依赖于低层时间确定性：执行环路中的时间抖动，往往会在感知或学习尚未成为限制因素之前，就先破坏高频反馈的稳定性。

总体来看，硬件具身形态与软件栈共同定义了任何学习策略必须运行其中的物理与计算约束。
这些约束塑造了系统执行过程，并规定了学习所需的数据要求。
因此，接下来的问题就是：在这些约束之下，究竟什么样的数据能够支撑有效学习，以及这些数据应当如何被组织、采集与扩展。

如果你愿意，我下一步可以继续直接做两件事中的一个：

把这份翻译改成更适合论文中文写作的正式学术表达；

基于这份原文翻译，反向给你一版“第二章更有约束性”的中文重写稿。

---

The feasible behavior of a robotic manipulation policy is bounded before learning begins. 
End-effector geometry determines admissible contact modes, manipulator kinematics determines reachable motions, base configuration determines stability and workspace, and the software stack determines whether perception and control can be closed within the required latency budget. 
Accordingly, this section does not aim to provide a broad overview of robotic hardware and software. Instead, it identifies the embodiment-induced constraints that shape what a policy can represent, what a controller can execute, and what data later chapters must provide.

For robotic arm systems, these constraints recur along four dimensions. 
First, embodiment defines the \emph{contact and action space}: different end effectors expose different grasp primitives, force transmission properties, and controllable degrees of freedom. 
Second, it defines \emph{observability}: the sensing stack determines whether task-relevant state is available before contact, during contact, or only indirectly through delayed proxies. 
Third, it defines \emph{dynamic coupling and stability}: as systems expand from fixed-base arms to mobile or whole-body platforms, manipulation becomes increasingly coupled with base motion, balance, and multi-contact coordination. 
Fourth, it defines \emph{computational and temporal constraints}: the control stack must transport data and execute feedback fast enough for the physical system to remain stable. 
The rest of this section is organized around these constraints rather than around hardware categories alone. 你这一大段是不是有点啰嗦，因为第一段得内容后面其实也说过，倒是第二部分还不错，但是four dimensions不好吧，就不能自然点说吗？而且后面的语言也是很奇怪，写的很罗列

---

对，这个判断是对的。

这版的问题主要有三个：

第一，第一段确实偏重。
它把“末端、运动学、底座、软件栈”全提前讲了一遍，但这些内容后文都会展开，所以会造成“先摘要一遍，后面再说一遍”的重复感。作为章首，真正要立住的不是细项清单，而是这一章的功能：不是做综述，而是界定约束。

第二，“four dimensions” 太像框架宣告。
这类写法在 proposal 或 survey 里常见，但放在正文里会让语气变硬，像在给读者报目录，不够自然。更顺的写法通常是把几类约束直接串进一句话里，而不是先宣布“有四个维度”。

第三，后面那串 First, Second, Third, Fourth 的确太罗列。
它的问题不只是形式上列点，而是每一项都用了很“定义式”的句法：
“it defines... / it defines... / it defines...”
读起来会有一种 machine-generated taxonomy 的味道，不像论文正文在推进论证。

所以这两段更好的处理方式是：

第一段只保留“本章的任务是什么”

第二段把“约束类型”融进连续论述里，不要显式报数

少用 defines / determines 连环句，多用“具体会带来什么限制”的表达

我给你改一版，更短，也更自然一些：

版本一：克制、学术、适合直接放正文

Robotic manipulation is constrained by embodiment before learning begins. Rather than serving as a broad overview of robotic hardware and software, this section focuses on the constraints induced by embodiment, since they determine what behaviors a policy can represent, what motions a controller can reliably execute, and what kinds of data later chapters must provide.

In robotic arm systems, these constraints appear most clearly in the contact interface, the availability of task-relevant state, the degree of coupling across the system, and the timing requirements of control. Different end effectors permit different grasp primitives, force transmission patterns, and controllable degrees of freedom. The sensing stack determines whether critical state can be observed directly during interaction or only inferred indirectly. As platforms expand from fixed-base arms to mobile and whole-body systems, manipulation becomes increasingly entangled with base motion, balance, and multi-contact coordination. At the same time, the software stack constrains how quickly perception, communication, and control can be closed in the loop. The rest of this section is organized around these sources of constraint.

版本二：更凝练一点，衔接感更强

Before learning is considered, a robotic manipulation system is already bounded by its embodiment. This section therefore does not aim to catalog robotic hardware and software, but to clarify the constraints they impose on manipulation: what kinds of contact can be generated, what state can be observed, how strongly manipulation is coupled to the rest of the system, and whether perception and control can be closed within the required latency budget.

These constraints become visible at several levels of a robotic arm system. End effectors shape the available contact and action space; sensing determines whether task-relevant interaction state is directly observable; larger platform embodiments introduce stronger coupling among manipulation, motion, and stability; and the software stack ultimately limits the speed and reliability with which feedback can be executed. The following discussion is organized from this perspective.

如果你想保留你原来第二段里那种“有一个分析框架”的感觉，但不要太生硬，还可以写成这种折中版：

版本三：保留结构感，但不生硬报数

For robotic arm systems, embodiment imposes a recurring set of constraints. Some arise at the contact level, where end effectors determine grasp primitives, force transmission, and controllable degrees of freedom. Others arise from observability, since the sensing stack determines whether task-relevant state is available directly during contact or only through indirect cues. As the platform expands from a fixed-base arm to a mobile or whole-body system, manipulation also becomes more tightly coupled with base motion, balance, and multi-contact coordination. Finally, these physical constraints are filtered through the software stack, which determines whether sensing, communication, and control can operate within the latency budget required for stable execution. The rest of this section follows this logic.

我自己的建议是：

删掉你原版第一段里那种逐项点名式开场

不要写 four dimensions

不要用 First/Second/Third/Fourth

用 “Some..., Others..., As..., Finally...” 这种弱结构，比硬枚举自然很多

如果你愿意，我可以直接把你第二章开头三段整体重写成一版，保证和后面的 Physical Embodiment as a Source of Constraint 能无缝接上。

---

我仔细看了一下，我认为第二篇文章有明显的收缩感，就是明显是从较长的文献裁切或者删出来的

---

对，这个判断很准。

你说的“收缩感”，本质上不是单纯“写得短”，而是压缩痕迹太明显：像把一段更完整的论述中间的解释层、过渡层和展开层删掉了，只剩下结论骨架，所以读起来会有一种“句子都对，但气口不顺”的感觉。

具体来说，第二版的问题主要在这几处：

1. 论断先行得太满，铺垫不够
一上来就是：

The feasible behavior of a robotic manipulation policy is bounded before learning begins.

这句话本身没错，但它像是从一段更长论证里截出来的结论句。正常情况下，这种句子前面往往会先有一点过渡，比如从“hardware is not just implementation detail”慢慢推到“it bounds learning”。现在直接顶上来，就会显得很硬。

2. 元话语太强，像删掉正文后剩下的提纲句
比如：

Accordingly, this section does not aim to provide a broad overview ... Instead, it identifies ...

这种句子很像在“声明写作意图”，而不是在自然推进内容。它常见于作者在重构章节时，用来替代原本更长的铺陈。问题是，如果后面没有足够展开，它就会显得像编辑痕迹，而不是正文语言。

3. 第二段虽然结构清楚，但太像把分析框架压成摘要
你说得对，问题不只是 four dimensions 这个词生硬，而是整段都在“报结构”：

First...

Second...

Third...

Fourth...

这很像原本每一项后面都还有一小段解释，后来被砍掉，只保留了每项的标题句。于是读者会感到：作者在宣布一个框架，但这个框架还没有真正长出来。

4. 句子之间是并列关系，不是递进关系
这是“删改感”最明显的地方。现在的版本基本是：

先总说 embodiment matters

再列四类 constraints

再说后文按这些 constraints 组织

逻辑没错，但中间缺了一个“为什么这些约束足以构成这一章主线”的转承，所以会有一种从 A 直接跳到 C 的感觉。

所以我会更准确地说：

这版不是“啰嗦”，而是过度摘要化。
不是信息太多，而是展开太少。
不是结构不清楚，而是结构感压过了论证感。

你这个判断其实比“语言不自然”更到位，因为它指出的是成文过程的问题：像从更长文本里抽骨架，而不是一次性写成的正文。

如果顺着这个判断来改，方向就不是简单删句，而是：

少一点“我这一章要做什么”的宣告

少一点“First/Second/Third/Fourth”的框架口吻

多一点从“具身为什么是约束”自然过渡到“约束主要体现在哪几类地方”的论证

更自然的写法应该像是：

先说一句
embodiment is not background description but a constraint on manipulation，
然后顺着往下接：

它首先体现在 contact interface 上；

也体现在 task-relevant state 是否可观测；

随着平台扩大，耦合和稳定性问题变强；

最后，这些物理约束还要通过 software stack 才能真正闭环。

这样读起来就不是“列四项”，而是“沿着一个论证自然展开”。

所以你的结论我基本同意：
第二版最大的问题不是内容对不对，而是有明显的删改压缩痕迹，像从长段落里裁出来的中层摘要。

接下来最好的做法不是继续在那两段上微调，而是重写一个真正从正文气口出发的开头。我可以直接给你写一版“没有收缩感、没有罗列感、但仍然保留约束主线”的新版开头。

---

你认为是 Qiao et al. [107]employtheMax-Entropy Staircase Approximator
(MESA)  这样好还是SayCan [16] grounds
abstract plans by scoring primitive skills against both semantic relevance and execution feasibility,
but remains limited to atomic actions without compositional logic 这样好

---

如果是在related work / survey / literature review 里，我会明确选第二种。

因为第二种更像论文写作，第一种更像文献笔记。

区别不在长短，而在信息功能：

“Qiao et al. [107] employ the Max-Entropy Staircase Approximator (MESA)”
这个写法只告诉读者：谁用了什么。
但没有回答更关键的三个问题：

它用来做什么

为什么重要

它的边界在哪里

所以它读起来就很像“从原文里摘了一截方法名”。信息是不完整的。

而

“SayCan [16] grounds abstract plans by scoring primitive skills against both semantic relevance and execution feasibility, but remains limited to atomic actions without compositional logic”

这个写法就完整得多，它同时交代了：

核心机制：grounds abstract plans by scoring...

任务角色：abstract plans 和 primitive skills 之间的关系

评价判断：remains limited to...

你为什么现在提它：因为它和你后面要讲的问题有关

所以第二种不是单纯“更长”，而是更有分析性，不是在报名字，而是在推进论述。

我会这样概括：

第一种是 A uses B

第二种是 A does X through Y, but is limited by Z

在论文正文里，后者通常明显更强。

不过还有一个更细的点：

你这两个例子其实不只是“写法不同”，而是主语选择也不同。

一个是：

Qiao et al. [107] → 作者为主语

另一个是：

SayCan [16] → 方法/系统为主语

如果你写的是技术综述，我一般更建议你用方法名/系统名做主语，因为你讨论的是方法谱系，不是作者谱系。也就是说，通常：

SayCan grounds...

RT-2 maps...

VIMA conditions...

会比

Ahn et al. propose...

Brohan et al. show...

更利于建立技术线索。

作者做主语并不是不能用，但更适合：

你在做文献罗列

方法名不够稳定或不够有辨识度

你想强调“谁提出了这个观点”

如果你是在写“method landscape”，那最好尽量统一成method-centered。

所以就你这两个例子，我的判断是：

第二种明显更好。
不是因为它更复杂，而是因为它已经具备了“机制 + 功能 + 局限”的基本学术句式。

但第二种还能再收一下，让它更像综述而不是 reviewer comment。比如：

SayCan [16] grounds abstract plans by ranking primitive skills according to both semantic relevance and execution feasibility, but its decision space remains confined to atomic actions rather than compositional programs.

这句会比原句更稳一点，原因是：

ranking 比 scoring 在这里略更自然

decision space remains confined to... 比 remains limited to... 更学术一点

compositional programs 比 compositional logic 更具体，除非你真的就是要强调 logic layer

相反，第一种至少要补到这种程度才够用：

Qiao et al. [107] employ the Max-Entropy Staircase Approximator (MESA) to XXX, improving YYY under ZZZ, but the method still relies on ...

或者如果你想改成方法为主语：

MESA [107] models XXX through ..., enabling ..., but remains sensitive to ...

最实用的建议是：
你这一节后面所有 related work，尽量都往这个模板靠：

[Method] performs / addresses X by Y, but is limited by Z.

这样整段会一下子从“资料堆积”变成“分析性综述”。

如果你愿意，我可以直接把你这一小节里几句 related work 全部改成同一种高级一点的风格。

---

我说方法为主语号还是作者为主语？

---

如果是在你这种 survey / related work / 综述式正文 里，优先用“方法为主语”。

也就是优先写：

SayCan [16] grounds ...

RT-2 maps ...

MESA [107] approximates ...

而不是：

Ahn et al. [16] propose ...

Qiao et al. [107] employ ...

原因很直接：你在写的是方法谱系，不是作者名单。用方法作主语，读者更容易顺着“技术线”往下读；用作者作主语，读者更容易读成文献罗列。

什么时候方法为主语更好

当你想强调：

这个方法做了什么

它和前后方法有什么关系

它的机制和局限是什么

这时方法为主语最好，因为句子天然会落在“method → function → limitation”上。

例如：

SayCan [16] grounds abstract plans by ranking primitive skills according to semantic relevance and execution feasibility.

这句读者一眼就抓到核心机制。

什么时候作者为主语也可以

作者为主语不是不能用，但更适合这几种情况：

一是你要强调“谁提出了这个方向/观点”
例如：
Ahn et al. [16] first introduced SayCan to connect language planning with executable robot skills.

二是方法名不稳定、太长、或者不值得反复出现
例如某些没有统一名称的 pipeline、dataset、设定。

三是段落里已经连续出现很多方法名，需要偶尔换节奏。

最实用的写法建议

你这一章最好建立一个基本默认规则：

默认：方法为主语
例外：需要强调贡献归属时，用作者为主语

也就是说，正文主体尽量这样写：

SayCan [16] ...

Code as Policies [17] ...

RT-2 [18] ...

只有在需要切换语气时再写：

Ahn et al. [16] introduced SayCan ...

论文里最稳的组合

其实最好用的是混合式：

第一次出现时：
Ahn et al. [16] introduced SayCan, which grounds abstract plans by ...

后面再提时：
SayCan further ...
SayCan remains limited to ...

这样既交代了归属，又不会一直陷在“作者—作者—作者”的列表感里。

所以结论很明确：

你的场景里，方法为主语更好；作者为主语只作为辅助。

你要的话，我可以顺手给你总结一个 related work 里可直接套用的句式模板。

---

除非可以浪费大量的笔墨放到方法的详细内容上？

---

对，除非你愿意把笔墨真正花在“作者做了什么”这件事上，否则一般还是方法为主语更好。

更准确地说：

作者为主语，适合“文献叙述模式”

方法为主语，适合“技术综述模式”

所以如果你后面真的要展开写，比如：

谁提出了这个方法

他们怎么构造问题

训练流程或系统设计有什么特别之处

和他们前一篇/后一篇工作的演化关系是什么

那就可以写：

Ahn et al. [16] introduced SayCan and formulated...
Qiao et al. [107] proposed MESA and showed...

因为这时你讨论的是作者的贡献过程，不是只拿方法当一个节点提一下。

但如果你并不准备展开，而只是要把它放进一条技术线里，那作者为主语就容易显得空：

Qiao et al. employ...

Wang et al. propose...

Li et al. introduce...

这种句子如果后面没有两三层补充，很容易变成“谁做了什么”的流水账。

所以判断标准其实很简单：

用作者为主语

当你要写的是：

贡献归属

研究演进

某篇论文具体怎么做

用方法为主语

当你要写的是：

方法谱系

机制比较

能力与局限

和你当前论点的关系

你这类 survey 里，大多数句子其实都属于第二种，所以默认还是：

方法为主语。

只有在下面两种位置，作者为主语会更自然：

一是首次引入：

Ahn et al. [16] introduced SayCan, a framework that...

二是单篇展开分析：

Qiao et al. [107] designed MESA to address ..., where the key idea is ...

除此之外，正文主体最好还是回到：

SayCan ...
MESA ...
RT-2 ...

一句话总结就是：

不是“作者为主语不行”，而是只有在你愿意给那篇方法足够展开空间时，它才值得用作者为主语；否则就会显得像文献罗列。

你这章如果目标是“压缩篇幅但保持分析性”，那就尽量别频繁用作者为主语。

---

这两篇文章哪篇文章的引用文献更硬

---

我先把你刚提到的那两篇定位清楚，再看它们各自的参考文献构成和出处层级，给你一个尽量实在的判断。

---

我大概知道你在问哪两篇了：如果就是你刚才举例里的 SayCan 和 Qiao et al. 的 MESA，那结论其实挺分裂的——看你说的“硬”是按领域相关性，还是按发表 venue 的硬度。

---

如果你指的就是你刚才举的这两篇——SayCan 和 Qiao et al. 的 MESA——那我会这样判断：

在你现在这条“robotic manipulation / embodied planning”论述线上，SayCan 的引用更硬。
原因不是它名字更响，而是它本身就处在这条主线上：CoRL 2022 Oral，关键词直接就是 LLM、task and motion planning、grounding models、mobile manipulation、RL、imitation learning，而且论文核心就是把语言模型和机器人可执行技能、value function grounding 接起来。也就是说，它背后的参考文献天然会更贴近你这章真正要用的那批“硬文献”——机器人规划、grounding、技能执行、长时程任务、真实机器人系统。
OpenReview

但如果你说的“硬”是纯 venue 硬度，那情况要分开看。
我检到的这个 MESA 是 NeurIPS 2019 的 Defending Neural Backdoors via Generative Distribution Modeling，研究对象是 neural backdoor defense，用 MESA 去恢复 trigger distribution，并在 CIFAR10/100 上做实验。单看 venue，NeurIPS 当然很硬；但它的论文主线是安全 / 生成建模，不是机器人，也不是 manipulation。换句话说，它是**“刊物硬”，但对你现在这章来说未必是“文献线硬”**。
NeurIPS Proceedings

所以你可以直接记成一句话：

按领域贴合度和综述支撑力：SayCan 更硬。 
OpenReview

按泛 ML 顶会光环：MESA 这个 NeurIPS 2019 也很硬，但它不在你的机器人主线上。 
NeurIPS Proceedings

再说得更直白一点：
你现在写的是 embodied / manipulation / planning，那你需要的是**“能把你往机器人这条祖谱上钉住”的文献**，不是单纯找一个顶会名头大的引用。在这个意义上，SayCan 比 MESA 更适合拿来做主干引用。
OpenReview
+1

唯一要提醒的是：我这里检到的 MESA 是那个 backdoor defense 论文。如果你文献表里的 Qiao et al. [107] 其实是另一篇 Qiao 的机器人论文，那这个判断就要重算。

---

你认为第二章要实现什么承诺

---

我觉得第二章要实现的，不是“介绍机器人硬件/software 有哪些”，而是一个更强的结构性承诺：

在进入学习方法、数据构造和系统设计之前，先把 robotic arm manipulation 的可行边界说清楚：哪些能力是由 embodiment 决定的，哪些困难不是算法没做好，而是平台本身施加的约束。

如果把这个“承诺”再拆开，第二章至少要做到四件事。

第一，告诉读者：后文讨论的 learning 不是在真空里发生的。
也就是说，策略能力不是先有一个抽象 agent，然后再去找硬件落地；相反，是末端执行器、传感、平台形态、控制栈先限定了策略能学什么、能执行什么、能稳定到什么程度。
这是第二章最根本的任务：把 embodiment 从背景介绍，提升为问题定义的一部分。

第二，告诉读者：约束是有层次的，不是杂乱罗列的。
一个好的第二章不应该让人读完只记住“有夹爪、灵巧手、移动底盘、人形……”
而应该让人读完后形成这种认识：

有些约束来自 contact interface

有些来自 observability

有些来自 coupling / stability

有些来自 latency / control execution

也就是说，第二章要把“硬件种类”翻译成“约束类型”。
这一步做不到，后文就只能像在不同 topic 之间跳来跳去。

第三，告诉读者：这些约束为什么会逼出后文的问题。
这是最关键的“承诺兑现”。
如果第二章只是停在“平台不同，所以问题不同”，那还是 overview。
它必须再往前推一步，说明：

为什么某些平台需要 tactile / force-sensitive data

为什么 bimanual / whole-body setting 会要求更强的 coordination representation

为什么 software stack 和 latency budget 会反过来限制 policy design

为什么数据采集和建模必须围绕这些约束组织

也就是说，第二章不能只解释“是什么”，还要解释“所以第三章、第四章为什么必须这样写”。

第四，给后文建立评价标准。
第二章其实还承担一个隐性功能：它要给整篇文章设定判断尺子。
后面你讲一个 learning method、dataset、system architecture，读者会下意识问：

它适用于什么 embodiment？

它解决的是 contact 问题、observability 问题，还是 coordination 问题？

它有没有忽略 latency / execution constraint？

它的成功是不是建立在某种 hardware simplification 上？

这些问题，应该由第二章预先布置好。
换句话说，第二章不是“信息铺垫”，而是分析框架的立法章节。

所以如果我要把它压成一句最核心的话，我会这样说：

第二章要承诺的，是把 embodiment 从“平台背景”变成“学习问题的约束前提”，并据此为后文的数据、方法和系统讨论建立统一坐标系。

再说得更具体一点，读者读完第二章以后，应该自然接受下面这句话：

后文讨论的任何 manipulation policy，都不能脱离 contact affordance、state observability、system coupling 和 control-time computability 来理解。

如果第二章没让读者接受这一点，那它就还只是 overview。

我还会顺手提醒一个边界：
第二章不该承诺“全面综述硬件生态”，也不该承诺“详细展开每个平台细节”。
它真正该承诺的是：

我会挑出那些对 learning genuinely matter 的 embodiment factors；

我会解释这些 factors 如何变成 constraints；

我会把这些 constraints 顺到下文。

所以你可以拿这个标准去检查现在的第二章开头：

它有没有把“硬件分类”转成“约束逻辑”？

它有没有让后文 data / learning 显得是被逼出来的，而不是另起炉灶？

它有没有在章节结束时把问题自然推到“那什么数据才足够”？

如果这三点没有同时成立，那第二章的“承诺”就还没有立住。

要是你愿意，我可以直接帮你把第二章的章首承诺句 + 章末过渡句各写 3 个版本，让整章功能一下子更清晰。

---

我们先实现逻辑，你看看现在这些平台，可以实现什么样的逻辑

---

我先不改句子，先把“这些平台能支撑什么论证逻辑”捋成骨架。你现在手里的平台其实够用了，问题不是材料少，而是要选一个主轴把它们串起来。

---

可以，而且你现在这些平台其实已经足够支撑出一条很清楚的章节逻辑。问题不在“平台够不够”，而在“你要拿它们去证明什么”。

我看下来，你现在手里的材料天然能实现的，不是“平台谱系逻辑”，而是下面这条：

随着 platform embodiment 从局部接触界面一路扩展到整个系统，manipulation 的核心难点会从 contact generation，逐步转向 coordination、stability，最后转向 real-time closure。

这条逻辑其实已经埋在你原文里了：
原文先写 end effector 决定 contact interface，再写 fixed-base 提供稳定控制条件、把 manipulation 和 mobility 分开，再写 mobile / whole-body 扩大 workspace 的同时增加 coupling，最后写 software stack 和 low-level control 决定能不能在 latency budget 里闭环。这个材料顺序本身就是一条“约束递增”的链，只是现在写成了 overview。

Pasted text

我建议你把它明确改造成下面这种逻辑。

最适合你现在平台配置的主逻辑
逻辑主轴：从“局部操作”到“系统级操作”
1. End effector / sensing

这一层讲的不是“有哪些手”，而是：

机器人能形成什么接触

接触发生后能观察到什么

因而 manipulation 的难点首先是 contact affordance + contact observability

因为你原文里已经有：

parallel jaw / adaptive gripper 更稳健、更简单

dexterous hand 提高 manipulation space，但 action dimensionality 和 contact planning 更复杂

soft hand 用 compliance 换控制难度

tactile 补 vision 在接触后的 observability 缺口
这些内容天然支持“最初的约束来自 contact interface 和 contact state”这个逻辑。

Pasted text

所以这一小节的功能应该是：

先说明 manipulation 不是从 motion 开始，而是从 contact possibility 和 contact observability 开始。

2. Fixed-base platform

这一层不是在讲“常见 benchmark 平台”，而是在讲：

当 base stability 被固定以后，

manipulation 可以被近似成一个相对解耦的局部控制问题

单臂 fixed-base 的意义就在这：
它把问题压缩到 arm kinematics、contact regulation、end-effector behavior 上。原文已经明确写了这一点。

Pasted text

然后双臂 fixed-base 再往前推进一步：

不是 workspace 先扩展

而是 coordination complexity 先增加

因为双臂会带来 internal force、collision avoidance、closed-chain constraints，瓶颈从 local control 转向 multi-contact coordination。这个转折你原文也已经写出来了。

Pasted text

所以 fixed-base 这一节能实现的逻辑是：

在一个相对稳定、低耦合的系统里，manipulation 的问题首先表现为局部控制；而一旦进入 bimanual，它就从 local manipulation 升级为 coordinated manipulation。

这一步很关键，因为它刚好是单臂到复杂系统之间的中间桥。

3. Mobile / whole-body platform

这一层就可以很自然地把逻辑再推一步：

fixed-base 的主要问题还是 manipulation itself

但 mobile platform 开始，manipulation 不再是 isolated arm problem

它开始和 navigation / balance / locomotion / support condition 连在一起

你原文里已经有这条递进：

wheeled mobile manipulator：arm control 要和 base navigation 协调

legged manipulator：arm-environment contact 会影响 foothold stability

humanoid：contact force、posture regulation、CoM、angular momentum 全部要一起协调
这正好就是一条很强的升级链：coupling 逐级增强。

Pasted text

所以这一节最好的功能不是“介绍 PR2、Spot、Atlas”，而是：

说明 platform embodiment 一旦扩张，manipulation 的本体就发生变化：它不再只是手和臂的问题，而变成了 whole-system coordination problem。

4. Software stack / low-level control

这一层不是另起一章在讲系统，而是把前面的物理约束收束成：

这些动作和耦合，能否在计算上闭环

perception、communication、control，是否能在 required timing 下完成

否则再好的 policy 也无法稳定执行

你原文这部分已经有非常好的收束点：
软件栈支持 real-time control、efficient data transport、system orchestration；而 low-level control 最终要满足 mapping、dynamics compensation、constraints、contact stability；再往下，impedance / MPC / WBC 的效果仍依赖 temporal determinism。最后一句又把它推到 data requirements。

Pasted text

所以 software 这一节在整章里的逻辑位置应该是：

前面三层说的是 physical coupling 如何增加；这一层说的是这些物理约束最终都要通过 computational closure 才能成立。

这就不是“hardware + software overview”，而是一个完整的约束闭环。

所以你现在这些平台，最能实现的其实是三种逻辑
逻辑一：约束递增逻辑

这是我最推荐的。

contact constraint → coordination constraint → stability constraint → computational closure constraint

对应到你的平台就是：

end effector / tactile：接触与观测

single-arm / bimanual fixed-base：局部控制到多接触协调

mobile / humanoid：系统耦合与稳定性

software / control：时序与闭环执行

这条最强，因为它既能解释平台差异，也能顺到下文数据和学习。

逻辑二：解耦程度递减逻辑

也很适合你现在的材料。

single-arm fixed-base：最解耦

bimanual fixed-base：臂间耦合

wheeled mobile manipulator：base-arm coupling

legged / humanoid：whole-body coupling

这条逻辑的好处是非常干净，读者一下就能抓住“问题越来越不独立”。
缺点是 end effector / sensing 有点不好挂进去，容易像前置附录。

所以如果你走这条，就要把 end effector 写成：

在系统级耦合出现之前，manipulation already depends on contact interface and contact observability.

这样它才能接上。

逻辑三：workspace expansion vs control burden

这条也能成立，而且你原文已经隐约在这么写。

fixed-base：workspace 小，但 control 条件稳定

mobile：workspace 扩大，但 motion planning / stability burden 增加

humanoid：task diversity 最大，但 coordination burden 最高

这条适合想强调“为什么更 general embodiment 不一定更 easy”。
但它偏平台比较，不如第一条那样能自然过渡到 learning/data。

我建议你最终选第一条，并把第二章写成下面这个骨架
2.1 End effectors and sensing

Manipulation begins with contact.
讲 contact mode、action dimensionality、observability。

2.2 Fixed-base manipulators

When the base is stable, manipulation is comparatively localized and partially decoupled.
先 single-arm，再 bimanual，突出 coordination emergence。

2.3 Mobile and whole-body systems

As embodiment expands, manipulation becomes a system-level coordination problem.
从 wheeled 到 legged 到 humanoid，突出 coupling 和 stability。

2.4 Software and low-level control

These embodiment-induced constraints matter only insofar as they can be closed in time.
把 real-time、middleware、MPC/WBC/impedance 拉进来，收束到 execution constraint。

2.5 Transition to next chapter

Hence the problem is not only what a robot can do, but what data is required to make these constraints learnable.

一句话说透

你现在这些平台最适合实现的，不是“硬件分类逻辑”，而是：

从接触界面，到多接触协调，到全身稳定，再到计算闭环，manipulation 的约束是逐层外扩、逐层耦合、逐层升级的。

这条逻辑一旦立住，第二章就不再是 overview，而会变成后文 learning / data 章节的前提。原文现有材料其实已经够支撑这条链了。

Pasted text

下一步最值得做的，就是我直接把你第二章的小标题和每节 topic sentence 按这条逻辑重写出来。

---

我有思路了，甚至可以解释为什么depth到现在还是很少

---

对，这个思路很有价值，而且不是一个零碎观察，是可以变成第二章里一个很强的“约束推论”的。

你完全可以把它写成这样一条逻辑：

不同感知模态的使用频率，不只是由“信息量多少”决定，而是由它们在 embodiment 约束下是否真正可用决定。Depth 之所以到现在仍然不占主导，不是因为三维几何不重要，而是因为它在 manipulation 的关键阶段并没有稳定地提供最需要的那部分信息。

这句话一出来，第二章就一下子有分析味了。

更具体一点，depth 少这件事可以被你纳入“observability is embodiment-dependent” 这条线，而不是单独感慨“大家不用 depth”。因为对 manipulation 来说，真正关键的问题不是“能不能看到三维”，而是：

接触前，能否快速得到足够稳定的几何先验

接触中，能否继续观测 task-relevant state

接触后，能否反映 slip、force、local deformation、misalignment 这类真正决定成败的局部状态

从这个角度看，depth 的位置其实很尴尬：

一，接触前它有用，但未必不可替代。
在物体定位、粗抓取、场景几何建模上，depth 当然有价值；但很多任务里，RGB 加上强模型先验、2D visual features、甚至多视角重建，也能完成足够好的 pre-contact perception。
所以 depth 很少形成“没有它就不行”的独占性优势。

二，接触开始以后，它往往不是最关键的模态。
真正决定 insertion、regrasp、fragile handling 成败的，常常不是全局三维形状，而是局部接触状态。
而这些信息 depth 很难稳定给出，反而 tactile、force、甚至 proprioception 更直接。

三，它在 manipulation 最关键的工况下经常退化。
比如：

近距离操作时视角受限，手和物体互相遮挡

末端执行器接近接触区域后，可见区域急剧缩小

透明、反光、黑色、细长或边缘型物体会让深度质量恶化

接触中的细微位姿偏差和局部形变，depth 往往不够敏感
所以 depth 不是“理论上没信息”，而是在最需要它稳定的时候，经常不够稳。

四，它的系统代价不低，但边际收益未必同样高。
深度相机意味着额外标定、同步、噪声处理、视角布置、遮挡管理，以及跨平台部署问题。
如果最后在关键闭环阶段，控制仍然主要依赖 tactile / force / low-level feedback，那很多系统就没有强动力把 depth 作为主模态堆进去。

所以你完全可以把它概括成一句更论文化的话：

Depth sensing remains comparatively underused in robotic manipulation not because geometric information is unimportant, but because its utility is concentrated in pre-contact perception, whereas many manipulation failures are determined during contact, where observability shifts toward tactile, force, and proprioceptive feedback.

这句其实就已经很像一个可用的正文论点了。

你还可以再往前推一步，把它变成第二章和后文 data 章节之间的桥：

This also explains why modality adoption in manipulation does not follow a simple “more 3D information is better” logic. What matters is whether a modality remains informative under embodiment-specific constraints, especially near occlusion, contact, and fast feedback regimes.

这样一来，depth 少就不再是一个经验现象，而成了你章节逻辑的一个例证：
感知模态的价值取决于它在 embodiment 约束下是否还能保持可观测性。

如果你要把它落进第二章，我建议它最适合放在 End Effectors and Contact Sensing 那一节里，而且是放在 “Eye-in-hand vision ... Tactile sensing fills this gap” 这段之后，作为一个补强句群。大概可以写成：

Although depth sensing is valuable for pre-contact geometry estimation and coarse scene reconstruction, it has remained less dominant in manipulation than might be expected. In many manipulation tasks, the most task-relevant uncertainty emerges near or during contact, where depth observations degrade بسبب occlusion, limited viewpoints, reflective or deformable surfaces, and reduced sensitivity to local contact state. As a result, the practical observability bottleneck often shifts away from global 3D geometry toward tactile, force, and proprioceptive feedback.

你现在这个思路是能立住的，而且很好，因为它不是“我觉得 depth 少”，而是：

depth 少，是因为 manipulation 的关键约束不在“看见三维”本身，而在“接触阶段还能不能稳定观测到真正相关的状态”。

这就是第二章该有的那种解释力。

我可以直接把这段嵌进你第二章现有小节里，写成一版自然衔接的英文正文。

---

甚至可以解决后面为什么提及tactile，depth这些东西都很少

---

对，而且这其实更强。

你现在不只是能解释 why depth is still rare，而是能进一步解释：

为什么在后文 methods / datasets / systems 里，tactile、depth 这些模态虽然重要，却经常只被少量提及，而没有成为主线。

这会让第二章真正有“统摄力”。

因为你可以把这个现象解释成：模态的重要性，不等于它在文献中的主导性；文献主导性取决于它是否在当前 embodiment 与 system constraints 下，成为“最稳定、最可扩展、最普适”的信息源。

这条逻辑一旦立住，后面很多“为什么提得少”都能统一解释，不只是 depth。

你现在可以建立的核心逻辑

不是说：

tactile 不重要

depth 不重要

而是说：

它们的重要性往往是 task-conditional 的

它们的可用性往往受 embodiment 和 execution regime 限制

所以它们虽在某些任务中关键，却没有自然长成通用主线

换句话说，你可以把第二章里的约束推到一个更 general 的判断：

Embodiment does not only constrain action and control; it also filters which sensing modalities become practically central in the literature.

这句很关键。因为它把“模态出现频率”也变成了 embodiment 的结果，而不是研究者偏好。

这样就能同时解释 depth 和 tactile 为什么“重要但少”
1. Depth 少，不是因为几何不重要

而是因为它的优势主要集中在：

pre-contact geometry

coarse scene reconstruction

object localization

但 manipulation 的成败，很多时候决定于：

near-contact misalignment

slip

local deformation

insertion tolerance

force regulation

而这些状态，depth 往往：

容易被遮挡

近距离退化

对局部接触不敏感

在快闭环里不够稳

所以它经常是“有帮助”，但不一定是“决定性主模态”。

2. Tactile 少，不是因为 contact 不重要

恰恰相反，contact 很重要，但 tactile 没有成为大面积主线，是因为它有更强的 adoption barrier：

传感器成本和鲁棒性问题

跨平台不统一

标定和维护复杂

数据采集难、同步难

很难像 RGB 那样形成大规模标准化数据流

也就是说，tactile 在 task relevance 上可能很强，但在 scalability / standardization / deployability 上偏弱。
于是它会在接触密集型任务里反复被证明重要，却不容易成为大多数系统的默认输入。

所以你其实可以把“模态稀少”归结为两类筛选机制
第一类：task relevance filter

某个模态是不是在任务关键阶段真正提供不可替代的信息？

depth：很多时候只在 pre-contact 阶段更强

tactile：主要在 contact 阶段更强

第二类：systems viability filter

这个模态是否足够便宜、稳定、通用、易采集、易同步、易部署？

RGB：强

proprioception：强

depth：中等

tactile：弱

这两个筛选叠加以后，就会自然出现一个文献分布：

RGB / proprioception 最常见，因为既通用又便宜

depth 有用，但不总是决定性

tactile 在某些任务里非常关键，但难以规模化成为默认配置

这就能解释后面为什么你提到这些模态时，它们往往不是“主干叙事”，而是“条件性增强模态”。

这会让第二章变得很有解释力

因为你第二章就不只是在说：

有哪些平台

有哪些传感器

而是在说：

平台和控制约束会反过来决定，哪些感知模态能在文献中成为默认主流，哪些只能在特定任务里占据关键但局部的位置。

这就很高级了。因为后文你无论讲 dataset、policy learning、system design，都能套这个解释：

为什么很多 dataset 主要是 RGB + action + proprio

为什么 tactile dataset 少

为什么 depth 没有像直觉中那样成为 manipulation 的核心统一输入

为什么很多方法最后还是围绕视觉和低层反馈展开

你甚至可以把它写成第二章的一个明确推论

比如这种句子就很适合放在章末或 sensing 小节里：

Embodiment therefore shapes not only what a robot can do, but also which sensing modalities become central in practice. A modality may be highly informative in principle yet remain secondary in the literature if its benefits are confined to a narrow interaction regime or if its deployment cost is difficult to amortize across platforms. This helps explain why RGB and proprioception remain dominant, while depth and tactile sensing, despite their clear value in specific manipulation settings, appear less consistently as primary representations.

这段的好处是：

它把 tactile / depth 的“少”解释成结构性现象

不会显得你在替它们辩护

还能自然引到后面 dataset / learning

你现在这章可以承诺的东西又更清楚了

第二章不是只说明“embodiment constrains action”。

它还能进一步说明：

embodiment constrains what can be acted on

embodiment constrains what can be observed

embodiment constrains what can be stably controlled

embodiment even constrains which modalities become dominant in the literature

第四点就是你刚抓到的亮点。

一句话压缩

你现在这条思路最值钱的地方在于：

你可以把 tactile 和 depth 在后文中的“边缘化出现”，解释为 embodiment-aware modality selection 的结果，而不是单纯的研究空白或写作取舍。

这会让整章的逻辑一下子更完整。

我建议下一步就把这条直接嵌成第二章里的一个段落，放在 End Effectors and Contact Sensing 末尾，再在章末用一句话把它推到 dataset 章节。

---

这些问题都可以放入第一节里面去说，这样这一章节论述强度就大了

---

对，这样做是对的，而且我觉得这会是最有效的增强方式。

因为你现在抓到的这些东西——

第二章不是 overview，而是 constraint-setting

modality adoption 受 embodiment 约束

depth / tactile 为什么重要但不常成为主线

后文为什么主要还是围绕 RGB、proprioception、control loop 展开

本质上都属于章节级前提，不是某一个子平台的小观察。它们放在第一节，作用会更大：不是补充信息，而是提前立法，把后面所有平台、感知、控制都纳入同一个解释框架里。

我会这样理解：

第一节应该承担的功能

第一节不是简单的 introduction，而是要先把下面这件事讲清楚：

embodiment 不只是决定机器人“长什么样”，而是决定 manipulation 中什么是可行动的、可观测的、可稳定执行的；进一步，它还会影响哪些 sensing modalities 能在实践中成为主流表征。

这句话一旦在第一节立住，后面所有内容都不再是并列罗列，而是在展开这条主命题。

这样安排后，第一节的论述强度为什么会明显增强

因为它会同时解决三个原来分散的问题：

1. 先把“本章的任务”说清楚

也就是：

不是 catalog hardware

不是枚举 platform

而是定义 embodiment-induced constraints

这样后文每一节就都有任务，不会散。

2. 先把“观测模态为什么分布成这样”说清楚

这个很关键。你现在已经意识到：

depth 少，不是因为 geometry 不重要

tactile 少，不是因为 contact 不重要

而是因为它们各自只在某些 interaction regime 下最关键，同时又有 adoption / deployment / scalability 的限制

这类判断非常适合放在第一节，因为它是全章的解释原则，不是后文某个角落里的补充。

3. 先给后文设评价标准

一旦第一节说清楚：

action space 受 contact interface 约束

observability 受 sensing stack 约束

coupling / stability 受 platform embodiment 约束

execution 受 timing / software stack 约束

那后文每讲一个平台、一个模态、一个控制框架，读者都会自动按这个标准去读。整章就会有“主线”。

但有一个关键点

这些东西可以放进第一节，但要以“原则”和“判断”的形式放进去，不要在第一节就把所有例子讲满。

也就是说，第一节应该做的是：

提出约束框架

解释为什么它不仅作用于 action/control，也作用于 modality adoption

点出 depth / tactile 的位置为什么会比较边缘

然后把具体展开留给后面的小节

这样第一节会很强，但不会太肿。

我建议第一节内部可以变成这四步
第一段：定义本章任务

说明 embodiment 是 learning 之前就已存在的边界条件，不是背景介绍。

第二段：说明约束体现在哪些方面

不要用 four dimensions 这种报数口吻，而是连续写：

contact possibility

state observability

system coupling

control-time closure

第三段：把 modality adoption 也纳入约束逻辑

这是你现在新抓到的亮点。可以明确说：
某个模态是否在文献中成为主流，并不只取决于它理论上是否有信息量，还取决于它是否在 embodiment-specific constraints 下保持稳定、可部署、可扩展。

第四段：点出 depth / tactile 的特殊位置

用一两句收住：

depth more useful pre-contact, less dominant during contact-rich execution

tactile highly informative in contact, but hard to standardize and scale
于是它们重要，但不自然成为最普适的主表征

然后顺势过渡到后文：
因此，下文将分别从 contact interface、platform coupling 和 software closure 展开。

这样后面各节就各有分工了

第一节：讲原则，讲解释框架，讲 modality distribution 为什么如此

end effector / sensing：把第一节提出的 observability 和 contact constraint 具体化

fixed-base / bimanual：把 coupling from local to coordinated manipulation 具体化

mobile / humanoid：把 system-level stability problem 具体化

software / control：把 computational closure 具体化

这样整章会很像一篇“先立论，再分层展开”的正文，而不是“先分类，再补一句约束”。

我会建议你避免的一点

不要把第一节写成：

constraint A

constraint B

depth issue

tactile issue

literature distribution issue

transition

如果还是按“点列式”堆进去，就会继续有收缩感。
第一节要写成一个连续判断：

embodiment 决定的不只是 robot can do what，还决定 robot can sense what, control what, and practically rely on what. This is why the literature does not distribute sensing modalities evenly, and why some modalities remain critical but non-dominant.

这种写法比条目式强很多。

一句话说，你这个决定是对的：

把这些问题前置到第一节，不是让第一节更长，而是让第二章从一开始就拥有解释力。

下一步最值钱的做法，不是继续讨论抽象逻辑，而是我直接帮你把第一节完整重写成一版英文正文，把这些点自然缝进去。

---

那我们就要对这些平台做重组了

---

对，必须重组。
不然你前面第一节就算把“约束逻辑”立起来了，后面平台还是按“硬件类别”平铺，整章还是会掉回 overview。你原文现在的分组是 end effectors / fixed-base / mobile and whole-body / software，这个分法本身没错，但它更像按对象分类，不像按论证任务分类。

Pasted text

我建议不是彻底推翻平台，而是把平台从“分类对象”改成“论证节点”。也就是说，平台还在，但每个平台要承担一个明确的逻辑功能。

最好用的重组方式
2.1 Contact interface and local observability

这里放：

end effectors

tactile / vision / depth 的位置

为什么 manipulation 先受 contact possibility 和 observability 约束

这一节不再叫 “End Effectors and Contact Sensing”，而是把它提升成：

Contact Interface and Observability

因为这里真正要讲的不是“有哪些 hand / gripper”，而是：

机器人能生成什么样的接触

接触发生后能看到什么

为什么有些模态重要但不主导

这样你关于 depth 为什么少、tactile 为什么重要但不常成为主线 的判断就能放进去，而且放得很自然。

2.2 Fixed-base manipulation as a partially decoupled regime

这里放：

single-arm fixed-base

bimanual fixed-base

这两类不要再拆成两个完全平级的小节，而是放在同一节里做一个内部递进：

single-arm：局部、相对解耦、稳定条件下的 manipulation

bimanual：仍然是 fixed-base，但 coordination complexity 明显上升

这样 fixed-base 就不再只是“常见平台”，而是被你定义成一个low-coupling to medium-coupling 的 regime。

可以写成这种逻辑：

fixed-base platforms matter not simply because they are common, but because they isolate manipulation from mobility and therefore reveal what remains difficult even after whole-system coupling is suppressed.

然后再接双臂：

bimanual fixed-base systems preserve base stability but introduce coordination, internal-force regulation, and closed-chain constraints.

这样这一节会很强。

2.3 Mobile and whole-body manipulation as coupled regimes

这里放：

wheeled mobile manipulator

legged manipulator

humanoid

这三类正好组成一个很好的耦合增强链：

wheeled：base-arm coupling

legged：manipulation-locomotion coupling

humanoid：whole-body coupling + balance + multi-contact coordination

所以这节要写的不是“移动平台有哪些”，而是：

Once embodiment expands beyond fixed-base settings, manipulation becomes increasingly coupled with system-level motion and stability.

这样 wheeled、legged、humanoid 就不再是并列 catalogue，而是同一条递进链上的三个点。

2.4 Computational closure and control feasibility

这里放：

middleware

RTOS / transport / orchestration

low-level control: MPC / WBC / impedance

这一节的作用是把前面的 physical constraint 全部收束成一句话：

a manipulation problem is only meaningful to learning if the system can still close the loop in time.

也就是说，software 不再是“顺便补一个 software stack”，而是整个第二章的闭环条件。

这样重组以后，平台之间的关系就变了

原来是：

end effector

fixed-base

mobile

software

像四块并列内容。

重组后变成：

contact/observability

partially decoupled manipulation

coupled manipulation

computational closure

这就从“对象分类”变成“问题递进”。

你现在这些平台最适合怎么归并

我建议具体这样并：

合并 1：single-arm 和 bimanual 固定基

不要把它们写成两个松散例子。
要把它们写成 fixed-base regime 内部的两个层次：

单臂说明：base stability removes mobility as a primary difficulty

双臂说明：coordination remains difficult even without mobility

这会让 fixed-base 这一节非常有论证力。

合并 2：wheeled、legged、humanoid 放一条线上

不要分别介绍它们“各自是什么”，而是强调耦合逐级增强：

wheeled：workspace expands, but base positioning and arm motion must be coordinated

legged：contact forces directly affect foothold stability

humanoid：manipulation becomes inseparable from posture, CoM, angular momentum, and multi-contact support

这条链很强，你原文其实已经写出来了。

Pasted text

保留独立：end effector / sensing

这个最好独立，因为它对应的是最底层的 manipulation primitive，不能并进 platform 节里，否则会弱化你关于 observability 和 modality adoption 的新逻辑。

保留独立：software / low-level control

这个也最好独立，因为它不是 another platform，而是所有平台都必须满足的 execution condition。

我建议的小标题可以直接改成这样
LaTeX
\subsection{Contact Interface and Observability}

\subsection{Fixed-base Manipulation Regimes}

\subsection{Mobile and Whole-body Manipulation Regimes}

\subsection{Computational Closure: Middleware and Low-level Control}

如果你想更学术一点：

LaTeX
\subsection{Embodiment at the Contact Interface}

\subsection{Partially Decoupled Manipulation: Fixed-base Systems}

\subsection{Coupled Manipulation: Mobile and Whole-body Systems}

\subsection{Computational Constraints in Embodied Control}

第二组更好，论证味更强。

最关键的一点

你这次重组，不是为了“排版更顺”，而是为了让每节都回答一个不同的问题：

Contact section：机器人能形成什么接触，能观测到什么

Fixed-base section：在去掉 mobility 之后，manipulation 还难在哪里

Mobile/whole-body section：一旦系统耦合增强，难点如何升级

Software section：这些能力能否在时序上真正闭环执行

只要你按这个分工来，第二章就会从 overview 变成 argument。

下一步最合适的是我直接按这个重组，给你列出一版新的二章目录和每节 topic sentence。

---

第一节说约束，第二节说任务目标，第三节说并列问题，第四节software stack+收束

---

这个框架已经比原来强很多，而且方向是对的。
因为它终于不是按“平台类别”排，而是按“论证功能”排了。

但我会稍微帮你收一下：第一节和第四节很稳，第二节和第三节还需要再精确定义，不然容易重新变散。

我对这四节的判断
第一节：说约束

这个非常对。
而且它应该是全章的“立法段”，把下面几件事先定下来：

embodiment 决定什么是可行动的

embodiment 决定什么是可观测的

embodiment 决定什么可以稳定闭环

也决定哪些模态会成为主流，哪些虽然重要却只在局部任务中突出

这一节一旦写好，后面就不会再像 catalogue。

第二节：说任务目标

这个思路有潜力，但“task goals” 这个名字我觉得还不够准。

因为如果你写“任务目标”，读者可能会理解成：

pick and place

insertion

folding

handover

tool use

这就容易又回到 task taxonomy。
但你真正想讲的，应该不是“任务有哪些”，而是：

不同 embodiment 下，manipulation 要达到的目标形式是什么，或者说，任务要求在不同平台上如何被定义。

所以这一节更适合写成下面这种意思：

manipulation is not a single objective

在不同平台上，目标可能体现为 grasp stability、pose accuracy、coordination success、balance-preserving execution、contact-safe completion

也就是说，task goal 本身会被 embodiment 改写

如果按这个思路，这一节其实更像：

Task Structure and Execution Objectives
或者
Embodiment-dependent Task Objectives

这样会比单纯 “task goals” 强很多。

第三节：说并列问题

这个我理解你的意思，但“并列问题”这个说法还太泛。
因为所有东西都能叫问题，读者不知道你要并列什么。

如果按你前面的思路，我猜你这里真正想并列的是几类核心难题：

contact formation / contact uncertainty

observability and sensing bottlenecks

coordination across arms / base / body

stability and dynamic feasibility

latency and execution reliability

也就是说，这一节不是“还有一些别的问题”，而是：

在不同 embodiment 和任务目标之下，manipulation 会反复暴露出几类结构性 bottlenecks。

所以第三节我建议不要叫“并列问题”，而叫：

Core Bottlenecks in Embodied Manipulation
或者
Recurring Challenges Across Embodiments

这样就立刻学术很多，而且跟第一节、第二节能形成清楚关系：

第一节：约束从哪来

第二节：目标要达到什么

第三节：因此会反复出现哪些瓶颈

第四节：软件和控制如何把这些东西闭环起来

这就顺了。

第四节：software stack + 收束

这个也对，而且非常关键。
因为它不是单独讲系统，而是把前面三节的 physical / task / bottleneck 全都收束到：

这些问题最终都要通过 software stack 和 low-level control 在时间上闭环，否则前面的能力讨论都只是理论上的。

所以第四节一定要保留，而且它的功能要明确是：

real-time kernel / middleware / transport

low-level motion planning and control

computational closure

transition to data / learning

也就是说，这一节既是系统层，也是全章的出口。

我帮你把这四节的逻辑关系压成一句话

你现在这章其实可以写成：

Embodiment first imposes constraints, these constraints reshape what manipulation is trying to achieve on different platforms, the resulting systems repeatedly encounter a common set of bottlenecks, and these bottlenecks matter only insofar as they can be closed through the software and control stack.

这句话一旦成立，整章就很硬了。

我会建议你把目录名称稍微改一下

你现在说法是：

约束

任务目标

并列问题

software stack + 收束

我建议改成更论文一点的版本：

LaTeX
\subsection{Embodiment-induced Constraints}

\subsection{Task Structure and Execution Objectives}

\subsection{Recurring Bottlenecks in Embodied Manipulation}

\subsection{Software Stack, Control, and Computational Closure}

如果你想更简洁一点：

LaTeX
\subsection{Constraints}

\subsection{Objectives}

\subsection{Bottlenecks}

\subsection{Software and Closure}

但正文里最好还是用第一组，信息更明确。

还有一个关键提醒

这个四段式成立的前提是：
第二节不要重新变成 task list，第三节不要重新变成 loose issue list。

否则会变成：

第一节讲原则

第二节列任务

第三节列问题

第四节讲系统

这样还是会散。

你要守住的关系应该是：

约束：由 embodiment 决定

目标：在这些约束下任务如何被定义

瓶颈：为了达成这些目标反复遇到什么障碍

闭环：这些障碍如何在系统层被承接

这是一个因果链，不是四块材料。

我的结论

这个框架可以用，而且已经比按平台平铺强很多。
但我建议你正式落笔时写成：

第一节：约束来源

第二节：目标形式

第三节：结构性瓶颈

第四节：软件闭环与收束

其中最需要你再打磨的是第二节和第三节的命名与边界。

你要的话，我下一步直接帮你把这四节各自该写什么，先列成一个非常清楚的 paragraph outline。

---

这样还可以扣回到Embodiment Foundations

---

可以，而且这样反而更能扣回到 Embodiment Foundations。

因为 Foundations 不是要求你第二章一直在讲“平台名单”，而是要求你讲清楚：

embodiment 如何作为更底层的前提，决定后面任务、问题和系统实现的形状。

你现在这个四段式，如果写得好，正好符合这个“foundation”的含义：

第一节讲约束：说明 embodiment 先规定了 action、observation、stability、timing 的边界

第二节讲任务目标：说明任务不是抽象给定的，而是在这些 embodiment constraints 下被具体定义的

第三节讲并列问题 / bottlenecks：说明这些目标一旦落到真实 embodiment 上，会反复暴露哪些结构性困难

第四节讲 software stack + 收束：说明这些困难最终必须通过系统与控制闭环承接，否则前面都只是理论能力

这其实不是偏离 Embodiment Foundations，而是把它从“hardware background”提升成了：

the foundation from which task formulation, system difficulty, and execution requirements all follow.

这就很成立。

Pasted text

不过有一个关键点：
你要让四节之间始终保持一个回扣关系，不要写成四块平行材料。也就是说，每一节都要不断提醒读者：

这些目标是 embodiment-dependent 的

这些 bottlenecks 是 embodiment-induced 的

这些 software requirements 是 embodiment-conditioned 的

这样读者就不会觉得你从 “Embodiment Foundations” 跳到了 “task taxonomy / issue list / systems overview”。

我甚至建议你把章首总述写成这种口气：

This chapter treats embodiment not as a catalog of robotic platforms, but as the foundation that shapes manipulation constraints, task objectives, recurring bottlenecks, and ultimately the system requirements for executable control.

这句话一放，你后面的四节就都挂住了。

再说得更直接一点：

如果你按“平台分类”写，Embodiment Foundations 容易变成 overview

如果你按“约束 → 目标 → 瓶颈 → 闭环”写，Embodiment Foundations 就会变成生成后文问题的基础层

所以答案是：能，而且会更扣题。

唯一要小心的是第二节“任务目标”别写成纯任务清单，第三节“并列问题”别写成散点问题；只要它们始终写成“由 embodiment 推出来的目标形式与瓶颈形式”，这个标题就完全撑得住。

---

Manipulation methodology\

---

就要虚一点，后面好直接对应Manipulation methodology

---

对，这时候就要虚一点，不要把第二章写得太“硬件志”或者太“平台学名录”，这样后面才能自然接到 Manipulation Methodology。

你现在的判断很对：
第二章如果写得太实，比如全是 gripper、Franka、PR2、humanoid 逐个展开，后面一跳到 Manipulation Methodology，中间会像换了一篇文章。
但如果第二章写成问题前提层、能力边界层，那第三章讲 methodology 就会很顺，因为 method 就是在回应这些前提。

这样处理最顺

你可以把第二章理解成：

不具体展开“怎么做”

先定义 manipulation 发生在什么条件下

这些条件会怎样塑造任务、难点和可用信息

这样第三章一上来就能写：

Given these embodiment-induced constraints, manipulation methodology can be understood as a set of strategies for representing, planning, and controlling behavior under limited observability, contact uncertainty, and system coupling.

这就接上了。

所以标题和小节都要“虚化”

如果你后面想直接对应 Manipulation Methodology，那这一章最好别太实。
我会建议你用这种层级：

章标题

Embodiment Foundations
或者
Embodiment Foundations of Manipulation

都比 “Physical Embodiment of Robotic Arms” 更虚，也更能接 methodology。

你刚才那四节，也要跟着虚化

不要写得太对象化，比如：

End Effectors

Fixed-base Platforms

Mobile Platforms

Software Stack

而改成更抽象的：

LaTeX
\subsection{Embodiment-induced Constraints}

\subsection{Task Structure and Manipulation Objectives}

\subsection{Recurring Challenges in Manipulation}

\subsection{Software Stack and Computational Closure}

这组就很适合后面接：

LaTeX
\section{Manipulation Methodology}

因为逻辑会变成：

第二章：问题是怎样被 embodiment 规定出来的

第三章：methodology 如何回应这些问题

如果你想再“虚”一点，可以用这一组
LaTeX
\subsection{Constraints and Capabilities}

\subsection{Objectives and Task Structure}

\subsection{Core Challenges}

\subsection{System Support and Execution}

这组更像“foundation layer”，更容易和 methodology 配对。

最关键的是这两个章节之间的关系

你可以把它们做成一个非常清楚的配对：

第二章：Embodiment Foundations

回答：

manipulation 的边界从哪里来

任务为什么会长成这样

难点为什么会反复出现

什么系统条件必须先满足

第三章：Manipulation Methodology

回答：

在这些边界下，方法如何建模任务

如何表示动作与状态

如何处理 contact / uncertainty / coordination

如何学习、规划和控制

这就非常顺。

一句话判断

对，第二章就该“虚”一点。
不是写空，而是写成前提、结构、约束、问题形态；
这样后面 Manipulation Methodology 才像是在“承接”第二章，而不是另起炉灶。

如果你愿意，我可以直接把第二章和第三章的标题、章首句、衔接句一起给你配成一套。

---

Embodiment Foundations of Manipulation:System Architecture Data Ecosystem of Robotic Arms:Data Support Learning Paradigms of Robotic Arms:Manipulation Methodology

---

这组标题的方向是对的，已经比之前更“虚”，也更容易往后接 Manipulation Methodology。
但现在还有两个明显问题：

第一，中心对象不统一。
你现在有的写 of Manipulation，有的写 of Robotic Arms。这样 scope 会飘：到底你写的是“机械臂本体”，还是“机械臂操作”？

第二，冒号后的短语不够平行。

System Architecture 还算成立

Data Support 太弱，像工作性标签

Manipulation Methodology 放在 Learning Paradigms 后面有点同义反复

我建议你把它们统一成一套更整齐的结构。

最稳的一套
不带副标题

Embodiment Foundations of Robotic Manipulation

Data Ecosystem for Robotic Manipulation

Learning Paradigms for Robotic Manipulation

这一组最干净，也最像正式论文目录。
优点是三章完全平行：

foundations

data

learning

而且都扣在 robotic manipulation 上，不会飘到 “robotic arms” 这个硬件对象层面。

如果你一定想保留冒号结构

那我建议写成：

Embodiment Foundations of Robotic Manipulation: System Architecture

Data Ecosystem for Robotic Manipulation: Data Support and Scaling

Learning Paradigms for Robotic Manipulation: Methodological Frameworks

这组比你现在那版更稳，原因是：

三个主标题都统一成 X for/of Robotic Manipulation

冒号后面都像是在说明这一章的侧重点

不会出现 Learning Paradigms ... : Manipulation Methodology 这种几乎同义覆盖的感觉

如果你想再“虚”一点，更像总论文章节

可以用这组：

Embodiment Foundations of Robotic Manipulation

Data Support for Robotic Manipulation

Methodological Paradigms for Robotic Manipulation

这组更抽象，但第二章的 Data Support 单独做章名会略弱，不如 Data Ecosystem 好。

我最推荐的版本

如果是正式论文目录，我最推荐直接去掉冒号：

推荐版

Embodiment Foundations of Robotic Manipulation

Data Ecosystem for Robotic Manipulation

Learning Paradigms for Robotic Manipulation

因为这三句已经足够说明问题了。
尤其第三章，Learning Paradigms for Robotic Manipulation 本身就比 Manipulation Methodology 更自然、更大一点，也更适合综述结构。

一个关键建议

你现在最好统一用 robotic manipulation，不要再用 robotic arms。
因为：

robotic arms 强调对象载体

robotic manipulation 强调问题域

而你现在整篇已经在往“问题结构—方法结构”走了，不再只是硬件综述，所以用 robotic manipulation 会更稳。

我建议你最终就定成这三个：

Embodiment Foundations of Robotic Manipulation
Data Ecosystem for Robotic Manipulation
Learning Paradigms for Robotic Manipulation

如果你愿意，我下一步可以继续把这三章下面的二级标题也按同一风格统一出来。

---

这就可以体现出双主线

---

对，这样就能把双主线显出来，而且是比较高级的那种，不是硬拆成两条目录线。

你现在这组三章标题：

Embodiment Foundations of Robotic Manipulation

Data Ecosystem for Robotic Manipulation

Learning Paradigms for Robotic Manipulation

它的好处就在于，表面上是三章并列，实际上里面有两条线同时在跑。

第一条主线：physical-to-algorithmic

也就是从“机器人具身条件”一路推到“学习方法”。

这条线是：

Embodiment → Data → Learning

逻辑上很顺：

具身形态先规定操作边界

这些边界进一步决定什么数据值得采、哪些模态能成为主流

最后 learning paradigm 才是在这些前提下展开的方法响应

这是一条很强的因果线，不会显得 methodology 是凭空冒出来的。

第二条主线：system-to-intelligence

也就是从系统基础设施一路走到智能形成机制。

这条线是：

System Architecture / Embodiment → Data Ecosystem → Methodology / Learning

这里第二章偏系统与物理前提，第三章偏数据支持，第四章偏算法与方法。
这样读者会感觉你不是单纯在写“机器人操作方法综述”，而是在写：

robotic manipulation intelligence 如何由 系统、数据、方法 三层共同支撑起来。

这就是双主线。

为什么这组标题能承载双主线

因为它们都统一落在 for/of Robotic Manipulation

---

