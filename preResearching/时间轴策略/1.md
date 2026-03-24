你到底在写什么

你这节真正该讲的是四层东西：

1. evaluation target

到底在评什么：

task completion
trajectory quality
coordination
generalization
data value
efficiency / energy
2. failure mode

为什么要评这个：

binary success 太粗
看不出中途失败
看不出动作抖动
看不出双臂不同步
看不出 OOD 崩溃
看不出能耗代价
3. metric family

为了解决这个问题，哪些指标族被提出：

stage-wise success / task progression
SPARC / LDLJ
DTW / Fréchet
Bradley-Terry
MMRV / RMSD
AULC / influence score
CoT / TEI / ECDP
4. interpretation

这些指标怎么读：

越大越好还是越小越好
它反映的是 robustness、smoothness、efficiency 还是 coordination
它适合单臂、双臂、sim-to-real、world-model evaluation 中的哪一种
所以这一节应该是什么形态
不是“过程”

如果你写成“先采轨迹，再算指标，再比较”，那就太 procedural 了，像实验手册。

也不是“参数大全”

如果你写成“这里有 20 个公式，每个都列一下”，那就会很像附录或工具书。

最合适的是：

“问题驱动的指标框架”

即：

每一小节先定义一个 evaluation problem，再介绍这个问题下最有代表性的 metric family，最后说明它们各自解决什么盲点。

一个最好的写作模板

你每个 subsection 都按这个模板写，基本就顺了：

第一句：这个维度为什么重要

例如：

Binary success rates cannot distinguish early catastrophic failure from near-complete but unstable execution.

第二句：传统做法为什么不够

例如：

This limitation becomes acute in long-horizon and bimanual tasks, where partial progress and coordination failures matter.

第三句：因此出现了哪一类指标

例如：

Recent work therefore moves from binary success to stage-wise progress metrics and trajectory-level diagnostics.

后面：挑 1–3 个代表指标展开

每个指标只讲三件事：

它测什么
公式/定义是什么
它比前一个指标多看到了什么
最后一句：这一类指标的局限

例如：

These metrics improve diagnostic resolution, but still do not capture subjective quality or out-of-distribution robustness.

这样下一小节就能自然接上。

具体到你这节，我建议这样理解
1. Task Execution Evaluation

这节不是在列：

success
SPARC
LDLJ
DTW
Fréchet
epsilon metric
v metric

而是在讲一个故事：

manipulation evaluation 从“成没成功”走向“失败在哪里、动作质量如何、抓取是否稳定、双臂是否协调”。

所以这一节的内部顺序应该是：

binary / stage-wise completion
trajectory quality
grasp stability
dual-arm coordination

也就是说，从粗到细，从结果到机制。

2. Data and Sample Evaluation

这节不是在列 mutual information、influence function、AULC。
它真正讲的是：

当模型越来越大时，评测对象不再只是 policy，也包括 data 本身：哪些 demonstration 有用，哪些样本贡献大，哪些方法更省样本。

所以这里的组织逻辑是：

dataset quality
data contribution / valuation
sample efficiency
3. Human Preference and Generalization

这节不该写成“人类偏好 + OOD + sim2real 凑一起”，而应该写成：

当 automated metrics 不够时，评测开始转向更接近真实使用场景的问题：人怎么看、换环境还能不能行、仿真能不能代表现实、世界模型能不能代表仿真。

所以这里更像一个 benchmarking / trustworthiness 小节。

4. Energy and Efficiency

这节不是纯物理公式展示。
它真正讲的是：

一旦系统进入长期部署，task success 不再是唯一目标，energy becomes part of evaluation.

所以这里的逻辑是：

为什么 energy 变重要
怎样从 power model 到 component decomposition
怎样做跨平台 normalized comparison
公式到底要不要写？

要写，但只能作为论点的支撑，不能喧宾夺主。

一个小节里，公式最好的状态是：

1 个核心定义公式
1 个扩展或归一化公式
其余用文字解释

不要每个指标都给一个大公式，不然整节会变得很“硬”，读者会失去主线。

你应该追求的不是“指标全”，而是“指标有层次”

最理想的状态是，读者读完会记住：

success rate 不够
所以要看 progress
progress 不够
所以要看 trajectory quality / grasp / coordination
自动指标不够
所以要看 human preference / OOD / sim-to-real validity
模型评完了还不够
数据和能耗也要评

这就是故事。