# Section 3.5 Generative Dynamics and Physical Imagination - 重构方案

## 一、核心定位

**Section 3.5 的核心问题**：Can robots predict and simulate physical consequences before acting?

**范式转换**：Reactive perception → Predictive imagination → Physics-informed foresight

**与其他章节的区别**：
- 3.3 Foundation Reasoning：理解当前状态（"what is happening"）
- 3.4 Geometric Grounding：精确定位动作（"where to act"）
- **3.5 Generative Dynamics**：预测未来状态（"what will happen if I act"）

---

## 二、4段落结构设计

### 段落 1：World Models — Learning Predictive Simulators

**范式转换**：Model-free RL → Model-based RL with learned dynamics → Foundation world models

**核心思想**：Learn a compact model of the world that can simulate future states given actions

**文献方向**：

#### 1.1 Classic World Models (2018-2020)
- **World Models** (Ha & Schmidhuber, NeurIPS 2018)
  - 开创性工作：VAE + RNN + Controller
  - 在 latent space 中学习世界模型
- **PlaNet** (Hafner et al., ICML 2019)
  - 第一个在视觉控制任务上超越 model-free 的 model-based RL
- **Dreamer** (Hafner et al., ICLR 2020)
  - 在 latent space 中做 planning
- **DreamerV2** (Hafner et al., ICLR 2021)
  - Discrete latent representations
- **DreamerV3** (Hafner et al., 2023)
  - 统一的 world model，从 Minecraft 到机器人

#### 1.2 Latent World Models for Robotics (2022-2025)
- **TD-MPC** (Hansen et al., ICML 2022)
  - Model-based RL with implicit planning
- **TD-MPC2** (Hansen et al., ICLR 2024)
  - Massively scaled world model for manipulation
- **IRIS** (Micheli et al., NeurIPS 2023)
  - Discrete world models with transformers
- **STORM** (2024)
  - Spatial-temporal world model

#### 1.3 Foundation World Models (2023-2025)
- **Genie** (Bruce et al., 2024)
  - Generative interactive environments from video
- **Genie 2** (Google DeepMind, 2024)
  - 3D world generation
- **DIAMOND** (Alonso et al., 2024)
  - Diffusion world model
- **UniSim** (Yang et al., NeurIPS 2024)
  - Universal world simulator
- **Pandora** (2024)
  - Autoregressive world model
- **Cosmos** (NVIDIA, 2025)
  - Physical world foundation model

**写作要点**：
- 开头：The ability to learn predictive models of the world has long been a central goal in embodied AI. Early approaches...
- 经典工作：World Models pioneered the paradigm of learning compact latent representations... Dreamer series advanced this by...
- 机器人应用：Translating these ideas to robotics, TD-MPC demonstrated that...
- Foundation models：Recent foundation world models scale this paradigm to internet-scale data. Genie learns to generate interactive environments from video... DIAMOND employs diffusion models for world simulation...
- 结尾：These foundation world models provide robots with the ability to simulate diverse physical scenarios, but translating pixel-level predictions into actionable control remains challenging.

---

### 段落 2：Video Prediction as Physical Forward Models

**范式转换**：Static image understanding → Temporal video prediction → Action-conditioned forward simulation

**核心思想**：Predict future video frames conditioned on actions to verify plan feasibility

**文献方向**：

#### 2.1 Action-Conditioned Video Prediction (2020-2023)
- **SVG** (Stochastic Video Generation)
- **Video prediction for manipulation** (相关工作)
- **SuSIE** (Unterthiner et al., 2024)
  - Structured world models from video

#### 2.2 Video Diffusion for Planning (2023-2025)
- **VILA** (Du et al., ICML 2024) ← 从 3.3 移入并展开
  - Video diffusion 预测 pixel-level consequences
  - 用生成的视频验证 plan feasibility
- **GVM** (Hu et al., 2024) ← 从 3.3 移入并展开
  - 用生成的视频帧作为 visual sub-goals
  - 训练 goal-conditioned policy
- **Video prediction for long-horizon manipulation**
  - 需要找相关工作

#### 2.3 Video-Based World Models for Robotics
- **RT-Trajectory** (Zitkovich et al., 2024)
  - Video tokenization for robot learning
- 其他 video-based robot learning 工作

**写作要点**：
- 开头：While latent world models operate in abstract embedding spaces, video prediction models provide explicit pixel-level forward simulation...
- 经典方法：Early action-conditioned video prediction models like SVG...
- Diffusion for planning：VILA employs video diffusion to "imagine" the pixel-level consequences of a plan... GVM utilizes the synthesized frames as explicit visual sub-goals...
- 结尾：However, pixel-level prediction is computationally expensive and may encode irrelevant visual details. This motivates latent predictive reasoning.

---

### 段落 3：Latent Predictive Reasoning and Physics-Informed Simulation

**范式转换**：Pixel-level prediction → Latent-space prediction → Physics-informed latent dynamics

**核心思想**：Predict in abstract embedding space, prioritizing physical dynamics over visual details

**文献方向**：

#### 3.1 Latent Predictive Models
- **V-JEPA2** (Bardes et al., 2025) ← 从 3.3 移入并展开
  - Predict future states in embedding space
  - Prioritize temporal dynamics over pixel reconstruction
- **JEPA** (Joint-Embedding Predictive Architecture)
  - Yann LeCun 的 vision
- 其他 latent prediction 工作

#### 3.2 Differentiable Physics Simulation
- **DiffTaichi** (Hu et al., ICLR 2020)
  - Differentiable physics engine
- **Brax** (Google, 2021)
  - Differentiable physics for RL
- **PlasticineLab** (Huang et al., NeurIPS 2021)
  - Differentiable soft-body simulation
- **DiffRL** 相关工作

#### 3.3 Neural Physics Engines
- **Graph Network Simulator** (Sanchez-Gonzalez et al., ICML 2020)
  - Learning to simulate complex physics with GNNs
- **Learning to simulate** (相关工作)
- **Physics-informed neural networks for robotics**

#### 3.4 Physics-Aware Generative Models
- **Physically plausible video generation**
- **Physics-guided diffusion models**
- 需要找相关工作

**写作要点**：
- 开头：Arguing that pixel reconstruction is redundant, latent predictive models prioritize physical dynamics over visual details...
- V-JEPA2：V-JEPA2 shifts to latent predictive reasoning, predicting future states in an abstract embedding space...
- Differentiable physics：Complementing learned dynamics, differentiable physics simulators like DiffTaichi and Brax enable gradient-based optimization through physical interactions...
- Neural physics：Neural physics engines learn to simulate complex physical phenomena from data...
- 结尾：These physics-informed approaches enable robots to reason about physical constraints, but lack the ability to explore counterfactual scenarios.

---

### 段落 4：Counterfactual Reasoning and Mental Simulation

**范式转换**：Forward prediction → Counterfactual reasoning → Imagination-augmented decision making

**核心思想**："What if I do X instead of Y?" — exploring alternative futures before committing to action

**文献方向**：

#### 4.1 Imagination-Augmented Agents
- **Imagination-Augmented Agents** (Weber et al., NeurIPS 2017)
  - 经典工作：用 imagination 辅助 RL
- **I2A** (Imagination-Augmented Agents for Deep RL)
- 相关工作

#### 4.2 Causal Reasoning in Embodied AI
- **Causal reasoning for robotic manipulation**
- **Causal world models**
- **Interventional reasoning**
- 需要找相关工作

#### 4.3 "What-If" Reasoning for Planning
- **Counterfactual planning**
- **Mental simulation for manipulation**
- **Exploring alternative action sequences**
- 需要找相关工作

#### 4.4 Unified Physical Intelligence
- **Physical reasoning benchmarks** (PHYRE, IntPhys)
- **Emergent physical reasoning in LLMs/VLMs**
- **Foundation models with physical common sense**
- 需要找相关工作

**写作要点**：
- 开头：The ultimate goal of generative dynamics is not merely to predict the most likely future, but to reason about alternative outcomes—"what if I do X instead of Y?"
- Imagination-augmented：Imagination-Augmented Agents pioneered this paradigm by using learned world models to simulate multiple action sequences...
- Causal reasoning：Causal reasoning enables robots to understand interventions and their consequences...
- Physical intelligence：Recent work explores whether foundation models exhibit emergent physical reasoning capabilities...
- 结尾：As robots acquire the ability to imagine, simulate, and reason about physical consequences, they transition from reactive agents to proactive planners with physical intuition.

---

## 三、文献搜索 Prompts

### Prompt 1: World Models 文献搜索

```
I need papers on world models and model-based reinforcement learning for robotics. Focus on:

1. Classic world models (2018-2020):
   - World Models (Ha & Schmidhuber, 2018)
   - PlaNet, Dreamer series (Hafner et al.)
   - Early model-based RL with learned dynamics

2. Latent world models for robotics (2022-2025):
   - TD-MPC / TD-MPC2
   - IRIS, STORM (discrete latent world models)
   - Latent dynamics models for manipulation and locomotion

3. Foundation world models (2023-2025):
   - Genie / Genie 2 (Google DeepMind)
   - DIAMOND (diffusion world model)
   - UniSim (universal world simulator)
   - Pandora (autoregressive world model)
   - Cosmos (NVIDIA physical world foundation model)
   - Any other large-scale world models

Time range: 2018-2025
Venues: NeurIPS, ICML, ICLR, CoRL, RSS, ICRA

For each paper, provide:
- Full title
- Authors (first author + et al.)
- Year and venue
- 2-3 sentence description of key contribution
- Why it's important for robotic world modeling

Please find 15-20 papers, organized chronologically within each category.
```

### Prompt 2: Video Prediction 文献搜索

```
I need papers on video prediction for robotic planning and manipulation. Focus on:

1. Action-conditioned video prediction (2020-2023):
   - SVG (Stochastic Video Generation)
   - Video prediction models for manipulation
   - SuSIE (structured world models from video)

2. Video diffusion for planning (2023-2025):
   - Video diffusion models for robotic planning
   - Using generated videos as visual goals
   - Video-based trajectory optimization

3. Video-based world models for robotics (2023-2025):
   - RT-Trajectory (video tokenization)
   - Video transformers for robot learning
   - Any video-based robot learning systems

Already covered (DO NOT repeat): VILA, GVM, V-JEPA2

Time range: 2020-2025
Venues: ICML, NeurIPS, ICLR, CoRL, RSS, CVPR, ICCV

For each paper, provide:
- Full title
- Authors
- Year and venue
- 2-3 sentence description
- How it uses video prediction for robotics

Please find 10-15 papers.
```

### Prompt 3: Physics-Informed Simulation 文献搜索

```
I need papers on differentiable physics, neural physics engines, and physics-informed learning for robotics. Focus on:

1. Differentiable physics simulators (2019-2025):
   - DiffTaichi
   - Brax (Google)
   - PlasticineLab
   - Other differentiable simulators for robotics

2. Neural physics engines (2020-2025):
   - Graph Network Simulator (Sanchez-Gonzalez et al.)
   - Learning to simulate complex physics
   - Neural ODE for physical systems
   - Physics-informed neural networks for robotics

3. Physics-aware generative models (2022-2025):
   - Physically plausible video generation
   - Physics-guided diffusion models
   - Generative models with physical constraints

4. Combining learned and physics-based models:
   - Hybrid models (neural + physics)
   - Physics priors in learning
   - Differentiable physics for robot learning

Time range: 2019-2025
Venues: ICML, NeurIPS, ICLR, CoRL, RSS, ICRA

For each paper, provide:
- Full title
- Authors
- Year and venue
- 2-3 sentence description
- How it incorporates physics into learning/simulation

Please find 15-20 papers.
```

### Prompt 4: Counterfactual Reasoning 文献搜索

```
I need papers on counterfactual reasoning, imagination-augmented agents, and causal reasoning for robotics. Focus on:

1. Imagination-augmented agents (2017-2023):
   - Imagination-Augmented Agents (Weber et al., 2017)
   - I2A (Imagination-Augmented Agents for Deep RL)
   - Using mental simulation for decision making

2. Causal reasoning in embodied AI (2020-2025):
   - Causal world models
   - Interventional reasoning for robotics
   - Causal discovery in physical interactions
   - Causal reasoning for manipulation

3. Counterfactual planning (2020-2025):
   - "What-if" reasoning for robotic planning
   - Exploring alternative action sequences
   - Counterfactual policy evaluation
   - Mental simulation for manipulation

4. Physical reasoning and intuitive physics (2020-2025):
   - Physical reasoning benchmarks (PHYRE, IntPhys)
   - Emergent physical reasoning in LLMs/VLMs
   - Foundation models with physical common sense
   - Intuitive physics in embodied AI

Time range: 2017-2025
Venues: NeurIPS, ICML, ICLR, CoRL, RSS, CVPR, ICCV

For each paper, provide:
- Full title
- Authors
- Year and venue
- 2-3 sentence description
- How it enables counterfactual/causal reasoning

Please find 15-20 papers. Note: This is a challenging area and papers may be sparse. Include related work on mental simulation, causal inference, and physical reasoning even if not explicitly robotic.
```

---

## 四、与 3.3 Foundation Reasoning 的协调

### 需要从 3.3 移走的文献

1. **VILA** (Du et al., ICML 2024)
   - 当前位置：3.3 Foundation Reasoning
   - 移动到：3.5 段落 2（Video Prediction）
   - 理由：video diffusion 预测未来，是 generative dynamics 的核心

2. **GVM** (Hu et al., 2024)
   - 当前位置：3.3 Foundation Reasoning
   - 移动到：3.5 段落 2（Video Prediction）
   - 理由：用生成的视频做 visual goal，是 imagination-to-action

3. **V-JEPA2** (Bardes et al., 2025)
   - 当前位置：3.3 Foundation Reasoning
   - 移动到：3.5 段落 3（Latent Predictive Reasoning）
   - 理由：latent space 预测，是 latent world model

### 3.3 需要添加的过渡句

在移走 VILA/GVM/V-JEPA2 后，3.3 的 temporal reasoning 段落需要添加：

> However, symbolic logic lacks physical foresight. The paradigm of \textbf{Predictive Reasoning via Generative Dynamics}—including video-based forward models and latent-space predictive reasoning—is discussed in detail in Section~\ref{sec:generative_dynamics}, where we examine how robots learn to imagine and simulate physical consequences before execution.

---

## 五、引言段落更新

### 当前引言（第 861-863 行）

> We categorize the evolution of this interface into five primary streams: **Semantic Logic and Code Generation**, which transitions from probabilistic scoring to Turing-complete program synthesis; **Long-Horizon Task Decomposition**, which employs formal solvers and hierarchical structures to mitigate planning hallucinations; **Foundation Reasoning Models**, which serves as the semantic engine for multimodal understanding and physical common sense; **Affordance Mapping**, which grounds semantic knowledge into physical geometric constraints; and **Spatiotemporal Representation**, which maintains explicit world memories for robust interaction.

### 更新后的引言

> We categorize the evolution of this interface into five primary streams: **Semantic Logic and Code Generation**, which transitions from probabilistic scoring to Turing-complete program synthesis; **Long-Horizon Task Decomposition**, which employs formal solvers and hierarchical structures to mitigate planning hallucinations; **Foundation Reasoning Models**, which serves as the semantic engine for multimodal understanding and physical common sense; **Geometric Grounding and Spatial Intelligence**, which translates semantic intent into precise geometric actions through continuous 3D representations and constraint reasoning; and **Generative Dynamics and Physical Imagination**, which enables agents to predict and simulate physical consequences before execution, evolving from learned world models to physics-informed counterfactual reasoning.

---

## 六、预期效果

重构后的 3.5 应该让读者感受到：

1. **清晰的演进链**：
   - Classic world models → Latent world models → Foundation world models
   - Pixel prediction → Latent prediction → Physics-informed prediction
   - Forward simulation → Counterfactual reasoning

2. **与其他章节的区别**：
   - 3.3 理解"现在"，3.5 预测"未来"
   - 3.4 定位"在哪做"，3.5 预测"做了会怎样"

3. **前沿方向**：
   - Physical imagination 是具身智能的最前沿
   - 从 reactive 到 predictive 到 counterfactual
   - 最终目标：robots with physical intuition

4. **范式意义**：
   - 不再是 trial-and-error，而是 mental simulation
   - 不再是 reactive response，而是 proactive planning
   - 机器人正在获得"物理直觉"

---

## 七、工作流程

1. **第一步**：使用 4 个 prompts 并行搜索文献（预计 30-60 分钟）
2. **第二步**：筛选和整理文献（预计 1-2 小时）
3. **第三步**：按 4 段落结构写初稿（预计 2-3 小时）
4. **第四步**：调整 3.3 的过渡句（预计 30 分钟）
5. **第五步**：更新引言段落（预计 15 分钟）
6. **第六步**：通读全文，检查连贯性（预计 1 小时）

总预计时间：**1-2 天**（如果全职投入）

---

## 八、需要确认的问题

1. **段落 4 的重点**：
   - 你更希望强调"counterfactual reasoning"（探索替代方案）
   - 还是"physical intuition"（类人的物理直觉）？

2. **文献时间范围**：
   - 是否需要包含 2017-2018 的经典工作（如 Imagination-Augmented Agents）？
   - 还是只关注 2020 年后的工作？

3. **技术深度**：
   - 每篇文献 2-3 句话是否合适？
   - 还是需要更详细的技术描述？

4. **与 3.3 的边界**：
   - 是否同意将 VILA/GVM/V-JEPA2 移到 3.5？
   - 还是保留在 3.3 并在 3.5 中简要提及？

请确认后我开始执行文献搜索。
