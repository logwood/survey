# §5 Open Challenges and Future Directions — 大纲

---

## 预备知识（写作时引用，不出现在正文）

| # | 素材 | 归属 |
|---|------|------|
| 1 | PhysBench (ICLR 2025): 75 VLMs, best O-1 = 55.11%, human = 95.87% | §5.1 三连击 |
| 2 | QuantiPhy (Stanford, arXiv:2512.19526): 21 VLMs 定量物理推理, best = 53.1% MRA < human 55.6%; 去掉视频后性能几乎不降 → 模型靠记忆不靠视觉推理; CoT 对 18/21 模型反而有害 | §5.1 三连击 |
| 3 | VBVR (arXiv:2602.20159): 视频生成模型, best open-source Wan2.2 = 37.1%, Sora 2 = 54.6%, 数据 scaling 饱和~0.77 | §5.1 三连击 |
| 4 | 三者共享 ViT/CLIP 骨干 → 结构性天花板论证 | §5.1 |
| 5 | 不同硬件/传感器产生的数据互不兼容 | §5.2 碎片化 |
| 6 | Sim-to-Real 迁移可靠性 | §5.1 Type I (最依赖 sim data) |
| 7 | 训练→适应→推理三阶段串行独立优化，缺乏 joint optimization | §5.2 安全与可持续性 |
| 8 | 形式化安全验证 vs 神经网络策略的理论鸿沟 | §5.2 安全与可持续性 |
| 9 | WorldArena 首个统一具身世界模型标准
| 10 | LingBot-VA DreamDojo DreamZero RoboChallenge PointWorld OmniVTLA
| 11 | Bridging Embodiment Gaps: Deploying VLA on Soft Robots (Su et al., NeurIPS 2025 SpaVLE WS): 开箱 VLA 在软体臂完全失败，finetuning 后追平刚性臂 | §5.1.1 embodiment gap + §5.2.1 数据质量 | ForceVLA
| 12 | BadVLA
---

## §5 Open Challenges and Future Directions

**开头段**（~4句）：本 survey 覆盖了硬件→数据→模型→部署全链条。本节从三个层面诊断瓶颈并指明方向：
- §5.1 **架构层**：以 Type I/II/III 分类为锚点，诊断各架构范式固有的瓶颈；
- §5.2 **跨架构层**：识别不依赖于特定模型架构、所有系统共同面临的通用瓶颈；
- §5.3 **生态层**：识别跨技术栈的系统性短板（数据、评测、可持续性）。
每个 challenge 诊断之后紧接对应的 future direction。

---

### §5.1 Architecture-Specific Bottlenecks

#### 开头：物理推理的结构性天花板（三连击，~1段）
- **诊断**：PhysBench → VLM 定性物理理解仅 55%（人类 96%）；QuantiPhy → 定量物理推理 53% MRA（人类 56%），且去掉视频输入性能几乎不降——模型在"回忆"而非"推理"；VBVR → 视频生成模型同样无法遵守基本物理定律（scaling 饱和~0.77）。
- **根因**：三类系统共享 ViT/CLIP 视觉骨干，该骨干在 internet-scale 图文对上训练，物理因果知识**结构性缺失**于训练数据——不是 scale 不够，而是数据本身不含物理真值。
- **意义**：这一天花板是下述架构瓶颈的**上游共因**。

#### §5.1.1 Type I/II 共享瓶颈：VLM Backbone 的物理推理缺陷
> 合并理由：Type I（端到端）和 Type II（层级式）的核心困境同源——均继承自 VLM backbone 的物理推理天花板，只是缺陷的**传导路径**不同。

- **诊断（共通根因）**：
  - 两类系统共享同一 VLM backbone（ViT/CLIP → LLM），三连击已论证该 backbone 在物理因果推理上存在结构性缺陷。
  - **本体感觉（proprioception）整体缺失**：关节位姿、力矩、电流反馈等本体信号在多数 Type I/II 模型中要么缺席要么仅作为 token 拼接——没有深度融合。

- **诊断（Type I 表现 — Modality Alignment Gap）**：
  - V-L 对齐不充分：ViT 冻结 + projection layer 是主流做法，但 projection layer 只做线性映射，无法弥补视觉编码器缺失的物理语义。
  - 端到端模型最依赖大规模 simulation 数据，但 sim 数据的 dynamics gap 直接继承为策略失败。

- **诊断（Type II 表现 — Brain→Policy Interface Loss）**：
  - 当前 hierarchical 系统的 Brain 只下发**语义子目标**（"pick up the cup"），Policy 独立负责力控和轨迹。
  - Brain 即使拥有某些物理知识（如从 VLM 继承的空间推理），也**无通道**传递给 Policy（力约束、接触预期、可操作性先验全部丢失）。
  - Brain 自身继承上游 VLM 的物理推理天花板（三连击），再经浅接口衰减 → **双重损耗**。

- **Direction**：
  - 寻找超越 linear projection 的对齐方法（如对比学习 + 物理约束损失），通过 PhysBench/QuantiPhy 式 benchmark 驱动迭代。
  - 将本体感觉从"附加 token"提升为一等模态（first-class modality），设计专用编码器或 cross-attention 机制。
  - 设计**多粒度 Brain→Policy 接口**：不仅传递语义意图，还传递力约束 / 接触预测 / affordance prior，让 Brain 的物理知识穿透到 Policy 层。
  - 探索 Brain-Policy 联合训练（end-to-end gradient flow through the interface），而非当前的分离优化。

#### §5.1.2 Type III 瓶颈：Components Exist but Do Not Compose
- **诊断**：
  - 力/触觉编码器（ForceVLA）、3D 表征（3D-VLA, SpatialVLA）、世界模型（Cosmos, V-JEPA 2）、物理仿真器（PhysTwin）——**零件齐备**。
  - 但「能预测下一帧 ≠ 理解物理因果」：当前世界模型是**外挂数据工厂**（生成训练数据/想象 rollout），而非内化的**因果物理引擎**。
  - 力/触觉信号仍是 token 拼接而非与视觉-语言表征深度融合。
  - VBVR 的证据：共享 ViT 骨干的视频生成模型在物理推理上 scaling 饱和——说明「更多数据+更大模型」路线对物理理解的边际收益递减。
- **Direction**：
  - 需要的不是更多零件，而是将零件**统一为因果物理引擎的架构范式**：world model 从"latent video predictor"进化为"causal simulator"（可回答反事实 what-if 查询）。
  - 多模态深度融合：force/tactile 不应仅做 token concatenation，而需 cross-modal attention 或 shared latent space。
  - 增强物理接地（physical grounding）：用物理仿真器的真值监督世界模型训练，使表征包含可操作的物理量（力、刚度、摩擦）。

---

### §5.2 Cross-Architecture Challenges（模型无关的通用瓶颈）

> 本节诊断的问题不依赖于 Type I/II/III 的具体架构选择——无论端到端、层级式还是世界模型，均无法回避。

#### §5.2.1 跨具身泛化（Embodiment Transfer Gap）
- **诊断**：
  - 现有 VLA 模型的泛化几乎局限于训练时覆盖的刚性串联臂（Franka、WidowX）。Su et al.（item 11）直接证实：OpenVLA-OFT 和 π₀ 在软体连续臂上开箱即用**完全失败**，finetuning 后才追平刚性臂表现——说明当前"泛化"仅是**内插**而非**外推**。
  - 不同形态之间（刚性臂 vs 软体臂 vs 灵巧手 vs 移动操作）的运动学/动力学鸿沟，远超 latent action space 等当前手段的弥合能力。
  - Cross-embodiment 数据集（OXE）的 embodiment 覆盖严重偏斜（>80% 来自 2-3 种刚性臂平台），加剧了分布偏差。
- **Direction**：
  - 构建形态无关（morphology-agnostic）的策略表征：将动作空间从关节级提升到任务级（如 SE(3) 工具末端表征 + 形态适配层），使 policy 在形态间迁移。
  - 有意识地扩展 embodiment 覆盖面——激励软体/灵巧手/非标平台的数据贡献（呼应 §5.3 数据质量）。
  - 开发 embodiment gap 的可量化指标（如基于 dynamics 距离的迁移难度预测），使跨形态泛化从"试一试"走向可预测。

#### §5.2.2 长程任务通用失败（Long-Horizon Fragility）
- **诊断**：
  - 所有架构类型在 >10 步的长程任务中成功率均急剧下降（LIBERO-Long、BEHAVIOR-1K 等基准均显示指数级衰减）。
  - 根因是**误差累积**：每步决策误差在开环/半闭环执行中逐步放大，尤其当任务存在不可逆节点（如液体倾倒、物体破碎）时，单步错误导致不可恢复失败。
  - 当前 CoT / 层级规划虽可分解子目标，但**子目标间的依赖关系和约束传播**缺乏形式化建模，导致规划与执行脱节。
- **Direction**：
  - 引入显式的**状态检查点与回退机制**：在关键任务节点进行可逆性判断（reversibility-aware planning），对不可逆操作提前验证。
  - 开发面向长程的**闭环自纠错策略**：结合 failure detection（如 FAIL-Detect）和 language-guided recovery（如 RACER）实现 runtime 回复。
  - 统一长程评测：推动社区采纳步数可控、难度可配的标准 benchmark（如可参数化的 BEHAVIOR 变体）。

#### §5.2.3 Sim-to-Real 系统性风险
- **诊断**：
  - Sim-to-Real gap 影响所有使用仿真数据的架构（Type I 的预训练、Type II 的 planner 验证、Type III 的世界模型训练）——不是某一架构的专属问题。
  - 当前 gap 量化手段缺乏标准化：没有公认的 metric 描述"sim 和 real 的 dynamics 距离"，导致迁移结果不可预测、不可比较。
  - 仿真器本身的保真度瓶颈：接触力学（friction、deformable body）、传感器噪声模型的精度上限制约了 sim data 的价值上限。
- **Direction**：
  - 建立 **sim-to-real fidelity metric**：可量化、可比较的 domain gap 指标（如基于 dynamics residual 的统计检验），使迁移研究可复现。
  - 推动 sim-real co-evolution：用 real-world residual 自动校正仿真参数（system identification in the loop），使 sim 持续逼近 real。
  - 对仿真器接触力学精度设立社区基准（contact benchmark），为 sim data 的可靠性建立信任锚点。

#### §5.2.4 安全与可解释性
- **诊断**：
  - **形式化安全的理论空白**：barrier certificate、reachability analysis 等形式方法无法直接应用于 billion-parameter 神经网络策略；当前安全手段（Robot Constitution, FAIL-Detect）是事后补救而非先验保证。
  - **可解释性困境**：所有 VLA 架构（包括 CoT 型）的决策过程本质上是黑箱——语言化 CoT（ThinkAct、Fast-ThinkAct）虽提供"推理痕迹"，但其忠实度（faithfulness）未经验证，latent CoT 更是完全不可审计。
  - **分布外行为不可预测**：在训练分布之外，neural policy 可能产生完全无法预期的动作，且缺乏 graceful degradation 机制。
- **Direction**：
  - **混合安全架构**：neural policy 生成候选动作 + 可验证的 safety shield（control barrier function）做最终裁决——不是替代神经网络，而是约束它。
  - 开发 CoT faithfulness 评测方法：验证语言化推理是否真正反映内部决策逻辑，而非事后合理化（post-hoc rationalization）。
  - 构建 OOD 检测 + 安全降级管线：在检测到分布外输入时自动切换至保守策略或请求人类干预。

#### §5.2.5 实时性与资源约束
- **诊断**：
  - 10 Hz+ 闭环控制是硬约束，但当前大模型推理（尤其多步 CoT、diffusion denoising、world model rollout）的延迟远超此阈值。
  - 量化/剪枝/蒸馏等压缩手段多针对 autoregressive VLA 设计；**diffusion policy 的去噪延迟**、**hierarchical 系统的 brain-body 通信延迟**、**world model 的 imagination rollout 开销**缺乏专门的加速方案。
  - **能耗盲区**：没有 surveyed work 报告 Joules-per-action；电池供电的移动操作平台没有可参照的能效基准；模型碳足迹完全未追踪。
- **Direction**：
  - 推动**架构感知的加速方案**：为 diffusion policy 设计专用去噪加速器、为 hierarchical 系统设计异步推理管线、为 world model 设计选择性 rollout。
  - Hardware-software co-design：联合优化模型架构和边缘硬件（如 diffusion denoising 的定制加速器）。
  - 将 Joules-per-action 纳入标准评测指标；推动 energy-aware model design（动态精度切换、NAS 中加入能耗约束）。

---

### §5.3 Ecosystem-Level Challenges

#### §5.3.1 数据生态：碎片化与质量瓶颈
- **诊断 A — 碎片化**：
  - **数据集碎片化**：不同硬件平台（Franka vs UR5 vs Aloha）、不同传感器配置、不同动作空间定义 → 数据互不兼容，无法汇聚。
  - **训练模型碎片化**：RT-2、OpenVLA、π0 各有私有数据管线和预处理流程，可复现性低。
  - **训练体系碎片化**：Stage 1/2/3（预训练→适应→推理）各阶段独立优化，缺乏 unified lifecycle（如 Stage 3 failure episodes 无法自动回流 Stage 1）。
- **诊断 B — 数据质量**：
  - **Embodiment 分布偏斜**：现有大规模数据集（OXE、BridgeData V2、DROID 等）几乎全部来自刚性串联臂（Franka、WidowX），软体臂、连续体臂、高自由度灵巧手的数据近乎空白。Su et al.（item 11）直接证实：VLA 在软体臂上开箱即用完全失败——不仅是 sim-to-real gap，更是**训练数据本身从未覆盖该形态**。
  - **演示质量参差不齐**：众包/分布式采集（RoboTurk、Dobb-E）带来规模但牺牲一致性——操作者技能差异大、标注噪声高、次优轨迹混入训练集。目前缺乏自动化轨迹质量评估与过滤机制。
  - **负样本/失败数据稀缺**：绝大多数数据集只记录成功轨迹，失败案例（如 RoboMIND 的 5k failure demos）是极少数例外。策略因此缺乏对失败边界的认知，在 OOD 场景下无法安全降级。
  - **物理模态覆盖不足**：Force/Torque、触觉、音频信号仅在少数数据集（RH-20T、FMB）中出现，大量训练数据是纯视觉——导致模型对接触力学"先天失明"（呼应 §5.1 物理推理天花板的数据根因）。
- **Direction（碎片化）**：
  - 统一动作空间与数据格式标准（类似 NLP 的 HuggingFace 生态），降低跨硬件数据复用门槛。
  - 推动数据集 / 模型 / 评测标准的**开源民主化**，促进社区共识。
  - 建立 cross-stage lifecycle：failure data → retraining data 的闭环。
- **Direction（数据质量）**：
  - 开发自动化轨迹质量评分与过滤管线（如基于 reward model 的 demo ranking），从源头提升训练数据信噪比。
  - 有意识地扩展 embodiment 覆盖面——激励软体/灵巧手/非标平台的数据贡献，打破刚性臂数据垄断。
  - 将失败轨迹系统化纳入训练（对比学习 success vs failure、failure-aware policy），使策略具备安全降级能力。
  - 将力/触觉/音频模态作为数据采集的**标配**而非可选项，从数据层面消除物理模态盲区。

#### §5.3.2 评测方法论（Evaluation Methodology）
- **诊断**：
  - **缺乏统一 real-world benchmark**：各模型在不同硬件、不同任务集、不同评分标准上报告结果，横向比较几乎不可能。
  - **sim-to-real 评估自身不可靠**：SimplerEnv 等 sim benchmark 的预测效度（与 real-world ranking 的相关性）未经系统验证。
  - **物理推理评测刚刚起步**：PhysBench/QuantiPhy 是首批量化物理理解的 benchmark，但覆盖面有限（仅限视觉观察，不含交互式物理推理）。WorldArena（item 9）为世界模型评测提供了首个统一标准，但尚未被广泛采纳。
  - **缺乏 failure-mode 分类学**：当前评测只报告成功率，不分析**为什么失败**（感知错误 vs 规划错误 vs 执行错误），妨碍了有针对性的改进。
- **Direction**：
  - 推动社区建立**标准化 real-world evaluation protocol**：统一硬件基准（参考 YCB / NIST 式物体集）、统一任务定义与评分标准。
  - 开发 **failure taxonomy**：系统化分类失败模式（perception / planning / execution / recovery），使评测从"pass/fail"升级为"诊断式评估"。
  - 扩展物理推理评测维度：从静态视觉判断（PhysBench）走向**交互式物理推理**（agent 需通过动作探索来推断物理属性）。
  - 建立 sim benchmark 的 **predictive validity** 验证框架：量化 sim ranking 与 real-world ranking 的相关性，使 sim 评测结果有明确的置信区间。

#### §5.3.3 可持续部署与生命周期
- **诊断**：
  - **三阶段 joint optimization 缺位**：Stage 1 蒸馏限制 Stage 2 自由度，Stage 2 分布偏移产生 Stage 3 新故障模式——但跨阶段联合优化几乎未被探索。
  - **Over-the-air 更新空白**：安全、增量式的权重更新协议在实时约束下尚不存在。
  - **能耗与碳足迹**：整个社区尚无 Joules-per-action 的报告规范，模型训练和推理的环境成本完全不透明。
- **Direction**：
  - 探索三阶段 joint optimization（如 compression-aware fine-tuning + quantization-in-the-loop training）。
  - 设计安全增量更新协议，使边缘设备能在不停机的情况下接收模型更新。
  - 推动碳足迹与能效报告标准化，使可持续性成为模型评估的显性维度。

---

## 行文原则备忘
- 每个 challenge: 先**诊断**（evidence + 根因），再**direction**（具体可操作的研究方向），一气呵成
- 风格：direct declarative, 不用 contrastive pattern, 不用绝对化表述
- 三连击在 §5.1 开头集中展开一次，后续 Type I/II/III 中引用即可，不重复展开
- 框架简单（两大节 + 子节），内容深入（每个 direction 要具体到方法论级别）
