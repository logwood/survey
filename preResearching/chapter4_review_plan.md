# Chapter 4 Review: Learning Paradigms of Robotic Arms

## 1. 这一章在全文中的角色

第四章是全文最有作者性的部分，也是风险最高的部分。

前面两章在建立系统边界和数据基础，第四章负责回答一个更难的问题：  
**这些不同来源、不同粒度、不同质量的数据，最终是如何被不同类型的方法转化为 manipulation intelligence 的。**

你这篇文章真正和一般 manipulation survey、VLA survey 拉开差距的地方，主要就在第四章：

1. `Brain / Cerebellum / Integration` 的总框架
2. `B1-B5 / P1-P3 / Type I-II-III / Deployment Lifecycle` 这些互相关联的 taxonomy
3. 最后用 `data_learning_map` 把第三章和第四章连起来

所以第四章不是“多列几种模型”就行，而必须做到：

1. taxonomy 真正稳
2. taxonomy 之间的关系真正清楚
3. 文献服务于 taxonomy，而不是 taxonomy 被文献拖着走

## 2. 当前版本的主要优点

1. 这是全文最有原创框架感的一章。`Cognitive Planning / Policy Learning / Integration Models / Deployment Lifecycle` 这四段式结构是成立的。
2. `5B + 3P + Type I/II/III` 确实能把很多已有综述里混在一起的工作拆开。
3. `Deployment Lifecycle` 这个加入是有价值的，因为它把“方法能训练出来”与“方法能部署”放到了同一个分析框架里。
4. `tab:data_learning_map` 的方向非常好，它是你把第三章和第四章真正缝起来的地方。

## 3. 这一章当前最核心的问题

### 3.1 最大的问题是 taxonomy 太多，但层级关系没有完全讲透

第四章现在同时存在五套组织轴：

1. `B1-B5`：cognitive planning paradigms，见 `survey.tex:697-703`
2. `P1-P3`：policy families，见 `survey.tex:818-824`
3. `Type I/II/III`：integration architectures，见 `survey.tex:893-1042`
4. `Stage 1/2/3`：deployment lifecycle，见 `survey.tex:1043-1121`
5. `K1/K2/K3 -> B/P/Type`：data-learning map，见 `survey.tex:1122-1158`

这五套东西各自都有道理，但当前最大的问题是读者不一定能立刻明白：

1. `B/P` 是功能层分类
2. `Type I/II/III` 是系统整合层分类
3. `Stage 1/2/3` 是工程部署轴
4. `K1/K2/K3` 是数据 regime

如果这层元关系不讲清楚，这一章就会显得“taxonomy 很多，但有点像 taxonomy 套 taxonomy”。

### 3.2 `Brain / Cerebellum` 这个 framing 有辨识度，但目前仍有“类比先行”的风险

见 `survey.tex:693-697`。

这个 framing 的优势很明显：好记，而且和你整篇 survey 的 systems flavor 相匹配。  
但它的风险也很明显：

1. 如果它只是把 `high-level planning / low-level control` 换了个名字，那会显得包装大于实质。
2. 如果后文没有稳定地把它写成功能分工与 architectural coupling，它会被读者当作修辞。

目前这套框架已经比纯修辞强，但还需要更明确的技术化定义。

### 3.3 B taxonomy 目前最容易被质疑

见 `survey.tex:697-703` 与 `survey.tex:756-816`。

主要问题有三个：

1. `B1-B5` 混合了不同层级的分类标准。
   - 有的按输出形式分，如 code / PDDL / reward
   - 有的按表示分，如 multimodal / geometric / predictive
   - 有的按目标分，如 task decomposition / physical imagination
2. `B4`、`B5` 与后面的 `Type III` 有较大内容重叠。
3. 叙述中 `Foundation Reasoning Models`、`Grounded Multimodal Reasoning` 等称呼之间还存在轻微口径波动。

换句话说，B taxonomy 现在有 insight，但还没完全做到“判别标准足够单一”。

### 3.4 P taxonomy 有价值，但 `P1` 的边界需要更稳的解释

见 `survey.tex:818-885`。

现在的 `P1` 是 `Explicit Continuous Policies`，但里面放了：

1. BC-Z / MVP / PointPolicy
2. Decision Transformer
3. ACT / Mobile ALOHA / BAKU

这会带来一个潜在疑问：  
既然 DT / ACT 已经明显有 sequence modeling 和 chunking 结构，为什么它们仍然属于 `P1`？

如果没有明确解释“你按 action parameterization 分，而不是按 decoder form 分”，读者会觉得这套分类有些随意。

### 3.5 `Type I / II / III` 是最该成为主卖点的部分，但当前开头太弱、正文太满

见 `survey.tex:893-1042`。

这里的问题不是 taxonomy 不好，而是它还没有被写成“读者一眼就懂的分界条件”。

当前表现为：

1. `Integration Models` 的总开头只有很短几句，无法承担这么重要的 taxonomy。
2. `Type I` 小节里塞了太多东西：unified VLA、continuous-action bridge、compression、adapter、grounding、多模态扩展。
3. `Type II` 小节比 `Type I` 更稳，但仍有 list-heavy 问题。
4. `Type III` 的范围最大，也最容易失控，目前几乎把 3D grounding、4D world models、video-as-action、multi-modal grounding 全装进去了。

### 3.6 `Type III` 目前是第四章里最需要重构的一块

见 `survey.tex:1027-1042`。

这部分的问题最集中：

1. 它同时覆盖 3D perception、geometry priors、3DGS、tracking、spatial referring、world models、video prediction、latent actions、tactile/audio grounding。
2. 这些方向都有关联，但现在缺少一个足够强的中间骨架。
3. 结果是这节很容易给人“什么都相关，所以全放进来”的感觉。

我的判断是：  
这节内容不是不对，而是**至少需要更强的内部层级**，否则读者会觉得 Type III 的边界比 Type I/II 更松。

### 3.7 `Deployment Lifecycle` 很有价值，但现在略像后加的一轴

见 `survey.tex:1043-1121`。

这一节本身是有意义的，而且我认为不应该删。  
但当前的问题是：

1. 它在第四章中的逻辑地位还不够明确。
2. 前面三节是“方法结构”，这一节突然切成“部署阶段”，轴换得比较快。
3. 读者可能会问：为什么 deployment 在 Chapter 4，而不是 System chapter，或者单独成章？

你其实已经有答案了：deployment 不是基础设施本身，而是 learned models 进入 physical operation 的生命周期。  
但这个答案现在还没有在章节开头讲明白。

### 3.8 `tab:data_learning_map` 是亮点，但现在说得仍然有点太满

见 `survey.tex:1118-1158`。

这张表的方向非常好，但问题有两个：

1. 它和前面 `K_1 \subset K_2 \subset K_3` 一样，容易被读成强因果或硬约束。
2. 表中配对关系更像“dominant pattern”而不是“necessary mapping”。

如果不加 caveat，它很容易被 challenge：

1. foundation-level data 不一定只配 Type I / Type III
2. task-level data 并不排斥 P3
3. B4/B5 与 Type III 的对应关系也不是唯一的

### 3.9 第四章存在一批会削弱可信度的硬伤

这些问题虽然不都是结构问题，但必须改，因为它们会让最有原创性的章节看起来不稳：

1. `logic slovers`，见 `survey.tex:773`
2. `modern robotic integation models`，见 `survey.tex:893`
3. `systems like Hi Robot ... employs`，见 `survey.tex:1025`
4. `the model need sustain`，见 `survey.tex:1106`
5. `trajectories.MolmoAct` 缺空格，见 `survey.tex:1033-1034` 附近
6. HTML 注释残留 `<!- ... >`，见 `survey.tex:910`
7. `brain_timeline / brain_structure / policy_timeline / policy_structure` 仍是 TODO，占位未闭合，见 `survey.tex:698-699`、`survey.tex:819-820`

## 4. 分块诊断与修改建议

### 4.1 Chapter 4 opening (`survey.tex:691-697`)

**问题**

1. 章节 opening 现在已经有了总框架，但仍然没有显式说明四套 taxonomy 的层级关系。

**建议**

1. 在 chapter opening 里补一条非常明确的元说明：
   - `B1-B5` describes planning functions
   - `P1-P3` describes action-generation families
   - `Type I-III` describes system integration patterns
   - `Stage 1-3` describes deployment phases
2. 把 “brain / cerebellum” 定义为 analysis shorthand，而不是生物学主张。

### 4.2 Cognitive Planning / B1-B5 (`survey.tex:695-816`)

**问题**

1. B taxonomy 很有 insight，但分类标准略混。
2. B4 和 B5 的材料量远大于 B1-B3，容易让 taxonomy 失衡。
3. `Geometric Grounding and Spatial Intelligence` 与 Type III 有重复风险。

**建议**

1. 在 `tab:brain_paradigms` 前或 caption 后补一句“B taxonomy classifies the dominant function of the planning module, not the full architecture.”
2. 每个 B section 的开头都加一句判别标准，回答“为什么它属于这个 B，而不是别的 B”。
3. B4 收紧到 “geometry used to localize executable contact or pose targets”。
4. B5 收紧到 “predictive models used to simulate future physical states or outcomes”。

### 4.3 Policy Learning / P1-P3 (`survey.tex:816-891`)

**问题**

1. `P1` 与 DT/ACT 的关系需要理论化说明。
2. 目前 policy section 读起来还比较顺，但 taxonomy justification 不够显式。

**建议**

1. 在 P-section opening 补一句：policy families are grouped primarily by action representation and generation process, not by whether sequence context is used.
2. 如果不想加解释，也可以把 `Explicit Continuous Policies` 改成 `Continuous Action Policies`，减少概念负担。
3. `P1` 内部可以改成：
   - direct regression
   - chunked continuous prediction
   - residual/recovery continuous control

### 4.4 Integration Models / Type I-II-III (`survey.tex:893-1042`)

**问题**

1. 这是最值得打的贡献，但现在“开篇定义强度 < 后续文献密度”。
2. Type I/II/III 的分界标准尚未压缩成 1-2 句可复述的定义。

**建议**

1. 在 `Integration Models` 开头先给一个三句式定义：
   - Type I: unified end-to-end backbone
   - Type II: explicit temporal or functional hierarchy
   - Type III: explicit spatial or predictive state modeling
2. 明确说明它们不是互斥集合，而是按 primary architectural commitment 分类。
3. 把表前开头扩成一个真正能“立住 taxonomy”的小引言，不要只用三句交代。

### 4.5 Type I (`survey.tex:899-907`)

**问题**

1. 内容太多，主题有点散。
2. 当前段落里同时在讲 scaling、continuous action bridge、inference acceleration、parameter-efficient tuning、grounding extension。

**建议**

1. 只保留四条主线：
   - unified action token generation
   - continuous-action bridge
   - scaling/open-source democratization
   - efficiency/compression pressures
2. 其余例子要么压缩，要么交给表格。
3. Type I 的结尾要更明确指出它的核心短板：latency and weak explicit 3D structure。

### 4.6 Type II (`survey.tex:1017-1025`)

**问题**

1. 这节逻辑已经比较稳，但仍然有 list-heavy 倾向。
2. reasoning medium、dual-speed control、safety/deployment 三件事现在被放在一层里。

**建议**

1. 改成三段：
   - why hierarchy emerges
   - what intermediate reasoning or latent planning looks like
   - how hierarchy supports safety, adaptation, and deployment
2. 保留 hierarchy 作为唯一主轴，不要让 CoT、memory、safe RL 这些子支线抢主线。

### 4.7 Type III (`survey.tex:1027-1042`)

**问题**

1. 这是当前最需要重构的部分。
2. 它现在实际上包含三块：
   - 3D spatial representations
   - predictive/world models
   - multi-modal grounding beyond vision

**建议**

1. 最稳的改法不是砍掉，而是明确拆层：
   - 3D spatial state construction
   - predictive world modeling
   - multi-modal physical grounding
2. 明确说明：Type III 的核心不是“用 3D”或“有 world model”，而是**maintaining an executable world state**。
3. 把一些次要例子压到表中，正文只保留每层 3-5 个 anchor works。

### 4.8 Deployment Lifecycle (`survey.tex:1043-1121`)

**问题**

1. 这一节本身是好的，但目前像一个 orthogonal axis 突然插进来。

**建议**

1. 在 `Deployment Lifecycle` 开头加一句：deployment is not another model family but an engineering axis orthogonal to Type I-III.
2. 每个 stage 的小节都保留“what propagates to the next stage”这种写法，因为这正是它区别于普通 deployment survey 的地方。
3. 如果篇幅太紧，也可以考虑把 Stage 1/2/3 的文献覆盖度收一点，让其更偏“deployment bottlenecks”而不是“再做一遍方法综述”。

### 4.9 Data-Learning Map (`survey.tex:1122-1158`)

**问题**

1. 方向很对，但语气需要再稳一点。

**建议**

1. caption 里补一条 caveat：the table highlights dominant pairings rather than exclusive mappings.
2. 正文里再补一句：counterexamples exist, especially in hybrid systems and data mixtures.
3. 如果保留 `K_i` 体系，最好在这里再次弱化其“集合论含义”。

## 5. 这一章建议怎么改

### 5.1 最关键的，不是删 taxonomy，而是讲清 taxonomy 的层级

我建议把第四章明确写成下面这个层次：

1. `B1-B5`: planning function taxonomy
2. `P1-P3`: policy/action generation taxonomy
3. `Type I-III`: system integration taxonomy
4. `Stage 1-3`: deployment engineering axis

只要这四层关系讲明白，第四章就会从“很多 taxonomy”变成“多层分析框架”。

### 5.2 要把最强的贡献集中到 Type I-II-III 上

如果我按“论文主卖点”排序，第四章最该打的是：

1. `Type I/II/III`
2. `data-learning map`
3. `B1-B5`
4. `Deployment Lifecycle`
5. `P1-P3`

也就是说，Type I/II/III 应该成为这章最稳定、最容易被记住的东西。  
其余 taxonomy 都应该服务它，而不是和它抢中心。

### 5.3 文献处理建议

第四章的一个大问题是“框架对了，但很多段落仍然像高密度 literature dump”。  
建议每个 subsection 都强制遵守：

1. 先写 1 句核心问题
2. 再写 1 句判别标准
3. 再用 3 到 6 个 anchor works 展开
4. 最后写 1 句局限与过渡

如果一个段落在没有文献名的情况下仍然能成立，那这个 taxonomy 才真正站住。

## 6. 我建议的修改优先级

### 第一优先级：必须先改

1. 修掉所有硬伤：
   - `logic slovers`
   - `integation`
   - `the model need sustain`
   - `systems like Hi Robot ... employs`
   - HTML 注释残留
   - TODO placeholders
   - 缺空格等 source-level 问题
2. 在 Chapter 4 opening 明确四套 taxonomy 的层级关系
3. 强化 `Integration Models` 总开头
4. 重构 `Type III`

### 第二优先级：非常值得改

1. 给 B taxonomy 增加更明确的判别标准
2. 给 P taxonomy 增加 “按 action representation 分” 的解释
3. 给 `data_learning_map` 增加 caveat
4. 把 deployment 的 “orthogonal axis” 身份说清楚

### 第三优先级：如果还有时间

1. 进一步压缩 Type I 的 example density
2. 重新平衡 B1-B5 的篇幅
3. 给 Type I/II/III 增加一个更醒目的 summary comparison figure 或 boxed definition

## 7. 总结判断

第四章已经有了这篇 survey 最重要的原创骨架，但它目前仍处于“框架非常好、稳定性还差最后一截”的状态。  
最大的改进方向不是继续加 papers，而是让 taxonomy 之间的关系更清楚、Type I/II/III 更像真正的中心轴、Type III 更有内部层级、deployment 更明确是工程正交轴。只要这些地方收稳，第四章会成为整篇文章最能拉开档次的章节。
