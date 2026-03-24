# Comprehensive Revision Plan for Survey Paper

## Executive Summary

After systematic scanning of all chapters, I've identified the following priorities:

**Overall Status**: The paper has strong structure and taxonomy, but suffers from:
1. **文献密度不均** — 某些章节文献过多（Integration Models ~30篇），某些过少（Energy ~5篇）
2. **论述深度不足** — 很多段落是文献堆砌，缺少"为什么这个方向重要"的论述
3. **营销化语言残留** — 仍有大量"pioneered", "revolutionary", "cutting-edge"等表述
4. **时间线混乱** — 部分章节2023年文献出现在2025年文献之后

---

## Chapter-by-Chapter Analysis

### Chapter 1: Introduction (Lines 262-279)

**Current Status**: ✅ 基本合格

**Strengths**:
- 清晰的 scope 界定
- 四个 contribution 明确
- 结构总览清楚

**Minor Issues**:
- Line 264: "struggle to generalize beyond structured settings" — 稍显营销化，可改为 "remain limited to structured settings"
- Line 266: "have made clear that" — 可改为 "demonstrate that"

**Action**: 微调用词，无需大改

---

### Chapter 2: System Architecture (Lines 280-447)

**Current Status**: ✅ 基本合格

**Strengths**:
- Physical Embodiment 分类清晰（End Effectors / Stationary / Mobile）
- Software Framework 三层架构（L0/L1/L2）合理
- Table~\ref{tab:framework_comparison} 信息密度适中

**Issues**:
1. **End Effectors 段落过短** (Line 303, 仅3句话) — 可以补充更多 sensing modality 的论述
2. **Mobile Platforms 缺少具体数字** (Line 311) — 提到 Spot、Unitree、Humanoids 但没有给出 DoF、payload 等关键参数
3. **Software Framework 表格过长** (Lines 327-447) — 120行表格占据过多篇幅，建议压缩到80行以内

**Suggested Actions**:
- 补充 End Effectors 的 tactile sensing 论述（GelSight, DIGIT, BioTac）
- 为 Mobile Platforms 添加一个简表总结 DoF/Payload/Speed
- 压缩 Software Framework 表格：删除 Player/YARP/Orocos（已过时），保留 ROS2/Isaac/Zenoh 主线

---

### Chapter 3: Data Ecosystem (Lines 448-682)

**Current Status**: ⚠️ 需要中等修改

#### 3.1 Embodied Datasets (Lines 452-584)

**Strengths**:
- $\mathcal{K}_1 / \mathcal{K}_2 / \mathcal{K}_3$ 分类清晰
- Skill-level / Task-level / Foundation-level 三层递进合理

**Issues**:
1. **Skill-level 段落已压缩但仍可优化** (Lines 464-476)
   - 当前12句话，可以压到8句
   - Jacquard、ACRONYM 可以完全删除（表格里有就够了）

2. **Task-level 段落文献堆砌** (Lines 524)
   - 一句话里塞了10+篇文献："MT-Opt, BC-Z, RT-1, BridgeData V2, Dobb-E, DROID, FMB, RoboMIND..."
   - 建议拆成3-4句，每句2-3篇主文献

3. **Foundation-level 缺少论述** (Lines 589-591, 仅3句话)
   - 只列举了 RoboNet, OXE, ARIO, RH-20T, AgiBot World, Ego-Exo4D
   - 缺少"为什么需要 foundation-level data"的论述

**Suggested Actions**:
- Skill-level: 删除 Jacquard, ACRONYM 正文提及
- Task-level: 重写为3段：(1) 早期 fleet-scale (MT-Opt), (2) language-conditioned (BC-Z, RT-1), (3) distributed + failure-aware (DROID, RoboMIND)
- Foundation-level: 补充2-3句论述"cross-embodiment transfer 的核心挑战"

#### 3.2 Data Acquisition (Lines 585-658)

**Strengths**:
- Real-world / Simulation / Automatic 三条线清晰
- Real-world Data Gathering 已经按时间线重构过

**Issues**:
1. **Real-world Data Gathering 仍然偏长** (Line 591, 一段话塞了15+篇文献)
   - 建议拆成2段：(1) Teleoperation + Distributed (MIME → ALOHA → DROID), (2) Robot-decoupled + Autonomy (UMI → OmniH2O → RoboCat)

2. **Simulation Data Ecosystems 表格过大** (Lines 597-639, 43行)
   - 可以压缩到30行
   - 删除 PyBullet/CoppeliaSim 的详细描述（已过时）

3. **Automatic Data Generation 缺少总结句** (Lines 649-657)
   - 三个 axis (environment / demonstration / world-model) 讲完后没有收束
   - 建议加一句："These three axes collectively shift data production from manual collection to automated synthesis at scale."

**Suggested Actions**:
- Real-world: 拆成2段
- Simulation: 压缩表格，删除 PyBullet/CoppeliaSim 行
- Automatic: 加总结句

#### 3.3 Data Refinement (Lines 659-678)

**Current Status**: ✅ 已经压缩过，基本合格

**Minor Issue**:
- Correction and Recovery 段落 (Line 677) 只有1句话，可以补充1-2句论述"为什么 failure recovery data 重要"

#### 3.4 Data Pipeline (Lines 679-682)

**Current Status**: ⚠️ 需要重写

**Issues**:
1. **只有4行** (Lines 679-682) — 太短，不足以支撑一个 subsection
2. **缺少论述** — 只列举了 RoboTwin, GRUtopia, MimicLabs，没有说明"什么是 data pipeline"

**Suggested Actions**:
- 补充2-3句论述："Data pipelines integrate acquisition, synthesis, and refinement into end-to-end production systems."
- 或者：考虑把这个 subsection 合并到 Large-Scale Data Pipelines (Chapter 3 末尾)

---

### Chapter 4: Learning Paradigms (Lines 683-1049)

**Current Status**: ⚠️ 需要大量修改

#### 4.1 Cognitive Planning (Lines 687-762)

**Strengths**:
- B1-B5 分类有原创性
- Table~\ref{tab:brain_paradigms} 信息密度合理

**Issues**:
1. **B1-B5 的判别标准仍然不够单一** (Line 689)
   - 当前按"output artifact"分，但 B3 的定义是"joint processing"（按输入模态分）
   - 建议在 opening 明确说明："We classify by the primary artifact produced for execution, with B3 serving as the perceptual substrate."

2. **B3 段落过短** (Lines 752-754, 仅3句话)
   - PaLM-E, RoboBrain, EmbodiedGPT, ECoT 四篇文献挤在一起
   - 建议扩展到6-8句，补充"为什么 B3 是 intermediate role"的论述

3. **B5 段落缺少 LAPA/Moto** (Lines 760-762)
   - 之前说要加回来，但现在还没加

**Suggested Actions**:
- B3: 扩展到6-8句
- B5: 加入 LAPA, Moto 两篇（按你之前的建议）
- Opening: 明确判别标准

#### 4.2 Policy Learning (Lines 764-824)

**Current Status**: ✅ 基本合格

**Strengths**:
- P1/P2/P3 分类清晰
- 每个段落长度适中（8-10句）

**Minor Issue**:
- P1 段落 (Lines 768-770) 提到 Decision Transformer 和 ACT，但没有解释"为什么它们仍然是 P1"
- 建议加一句："These methods remain in P1 because they output continuous action vectors, despite using sequence modeling for temporal context."

#### 4.3 Integration Models (Lines 825-999)

**Current Status**: ⚠️ 需要中等修改

**Strengths**:
- Type I/II/III 分类是全文最大亮点
- Table~\ref{tab:data_learning_map} 方向很好

**Issues**:
1. **Opening 仍然不够强** (Lines 826-827)
   - 当前只有2句话，不足以"立住 taxonomy"
   - 建议扩展到5-6句，明确说明：
     - Type I: no explicit intermediate state
     - Type II: explicit temporal hierarchy
     - Type III: explicit world state

2. **Type I 表格缺少 RDT-2 和 UniVLA** (你刚才提到的)
   - 需要补回去

3. **Type II 段落仍然偏长** (Lines 925-950, 26句话)
   - 可以压到18-20句
   - 删除 OK-Robot（不是 manipulation 主线）

4. **Type III 段落文献过多** (Lines 951-999, 49句话)
   - 当前提到了 20+ 篇文献
   - 建议压到 30句，保留主线：3D-VLA, SpatialVLA, UWM, GR-2, BridgeVLA, TrackVLA, DreamZero

**Suggested Actions**:
- Opening: 扩展到5-6句
- Type I 表格: 补回 RDT-2, UniVLA
- Type II: 删除 OK-Robot，压到20句
- Type III: 压到30句

#### 4.4 Deployment Pipeline (Lines 1000-1049)

**Current Status**: ✅ 已经按时间线重构过，基本合格

**Minor Issues**:
- Stage 1 提到 "system identification" (Line 1034) — 按之前建议应该改为 "delta action compensation"
- Stage 3 提到 "certifiable planning" (Line 1027) — 应该改为 "motion planning"

---

### Chapter 5: Evaluation (Lines 1051-1119)

**Current Status**: ⚠️ 需要大量修改

**Issues**:
1. **Opening 过长且营销化** (Lines 1051-1054)
   - "the evaluation bottleneck has become acute" — 营销化
   - "synthesizes the emerging landscape" — 套话
   - 建议压缩到3-4句

2. **Task Execution 段落公式过多** (Lines 1089-1110)
   - SPARC, LDLJ, DTW, Fréchet Distance 的公式推导占了20行
   - 建议删除公式，只保留概念

3. **Data & Sample 段落也有公式堆砌** (Lines 1093-1097)
   - DemInf 的 mutual information 公式、CUPID 的 influence function 公式
   - 建议只保留 influence function 公式（核心），删除 mutual information 推导

4. **Benchmarking 段落 WorldArena 展开过多** (Lines 1114-1118)
   - 用了5句话讲 WorldArena 的三个 functional role
   - 建议压到2句

5. **Energy 段落已经补充了引用，但仍然偏长** (Lines 1114-1119)
   - ECDP 的四个 component 详细分解占了太多篇幅
   - 建议压缩

**Suggested Actions**:
- Opening: 压到3-4句，去营销化
- Task Execution: 删除 SPARC/LDLJ/DTW/Fréchet 公式
- Data & Sample: 只保留 influence function 公式
- Benchmarking: WorldArena 压到2句
- Energy: 压缩 ECDP 详细分解

---

### Chapter 6: Challenges (Lines 1120-1145)

**Current Status**: ⚠️ 需要中等修改

**Issues**:
1. **三个 subsection 长度不均**
   - Representation (Lines 1124-1130): 7句
   - Deployment (Lines 1131-1137): 7句
   - Ecosystem (Lines 1138-1145): 8句
   - 都太短，每个应该扩展到12-15句

2. **缺少具体例子**
   - 当前都是抽象论述："morphology-agnostic generalization", "catastrophic forgetting"
   - 建议每个 challenge 补充1-2个具体例子

**Suggested Actions**:
- 每个 subsection 扩展到12-15句
- 补充具体例子

---

## Priority Ranking

### 🔴 High Priority (Must Fix)

1. **Chapter 4.3 Integration Models Opening** — 扩展到5-6句，明确 Type I/II/III 定义
2. **Chapter 4.3 Type I 表格** — 补回 RDT-2, UniVLA
3. **Chapter 5 Evaluation** — 删除公式推导，压缩到合理长度
4. **Chapter 3.1 Task-level** — 重写为3段，避免文献堆砌
5. **Chapter 3.4 Data Pipeline** — 补充论述或合并到其他 section

### 🟡 Medium Priority (Should Fix)

6. **Chapter 4.1 B3** — 扩展到6-8句
7. **Chapter 4.1 B5** — 加入 LAPA, Moto
8. **Chapter 4.3 Type II/III** — 压缩文献数量
9. **Chapter 3.2 Real-world Data Gathering** — 拆成2段
10. **Chapter 6 Challenges** — 每个 subsection 扩展到12-15句

### 🟢 Low Priority (Nice to Have)

11. **Chapter 2 End Effectors** — 补充 tactile sensing 论述
12. **Chapter 2 Software Framework 表格** — 压缩到80行
13. **Chapter 3.2 Simulation 表格** — 删除 PyBullet/CoppeliaSim
14. **Chapter 1 Introduction** — 微调用词

---

## Estimated Workload

- **High Priority**: ~4-6 hours
- **Medium Priority**: ~3-4 hours
- **Low Priority**: ~2-3 hours
- **Total**: ~10-13 hours

---

## Next Steps

建议按以下顺序执行：

1. ✅ **先修 High Priority 1-2** (Integration Models Opening + Type I 表格) — 这是全文核心
2. ✅ **再修 High Priority 3** (Evaluation 公式删除) — 影响篇幅最大
3. ✅ **然后修 High Priority 4-5** (Task-level + Data Pipeline)
4. 🔄 **Medium Priority 逐个处理**
5. 🔄 **Low Priority 根据时间决定是否处理**

你想从哪个开始？
