# Stage 3 文献替换分析

## 当前 Stage 3 文献列表

### Quantization & Pruning
- QVLA (2026) - action-centric channel-wise bit allocation
- HBVLA (2026) - 1-bit PTQ via policy-grounded saliency
- LightVLA (2025) - adaptive visual token pruning
- EfficientVLA (2025) - training-free KV cache optimization

### Decoding Acceleration
- PD-VLA (2025) - parallel fixed-point decoding
- TinyVLA (2025) - distillation to compact variants
- SwiftVLA (2025) - spatiotemporal feature routing
- SARA-RT (2024) - self-adaptive robust attention (linear complexity)
- Xiaomi-Robotics-0 (2026) - asynchronous execution pipeline
- SP-VLA (2025) - dynamic model switching

### Safety & Robustness
- Policy Contrastive Decoding (2026) - object-masked contrastive decoding
- Neural MP (2024) - neural intent + certifiable motion planning

### Failure Recovery
- FAIL-Detect (2025) - flow-based OOD detection
- RACER (2024) - language-guided failure recovery
- AHA (2024) - VLM-based failure diagnosis
- Reflective Test-Time Planning (2026) - self-supervised runtime updates

---

## 从 Type I 移入的 efficiency 文献

### 需要移入的文献
1. **DeeR-VLA** (2024) - dynamic early-exit mechanism
2. **MoLe-VLA** (2025) - Mixture-of-Layers dynamic layer-skipping
3. **VLA-Cache** (2025) - autoregressive caching optimization
4. **BitVLA** (2025) - 1-bit weight quantization
5. **VLA-Adapter** (2025) - parameter-efficient tuning for tiny models
6. **SmolVLA** (2025) - compact VLA variant
7. **Edge VLA** (2025) - edge-deployable VLA
8. **Evo-1** (2025) - compact VLA variant
9. **OpenVLA-OFT** (2025) - fine-tuning optimization
10. **RoboMamba** (2024) - SSM for linear-time complexity

---

## 替换建议

### 原则
1. **保留核心代表**：每个类别保留 2-3 篇最有代表性的工作
2. **删除重复定位**：功能高度重叠的只保留一篇
3. **优先保留新方法**：architectural innovation > engineering optimization

---

### Quantization & Pruning 类别

**当前 4 篇**：QVLA, HBVLA, LightVLA, EfficientVLA

**建议保留 3 篇**：
- **QVLA** (2026) - 保留，action-centric mixed-precision 是核心方法
- **HBVLA** (2026) - 保留，1-bit extreme quantization 代表压缩极限
- **BitVLA** (2025) - **替换 LightVLA**，同样是 1-bit 但更通用

**删除**：
- LightVLA - token pruning 不如 quantization 核心
- EfficientVLA - KV cache optimization 太工程化

**新增**：
- **BitVLA** (2025) - 1-bit weight quantization，比 LightVLA 更基础

---

### Decoding Acceleration 类别

**当前 6 篇**：PD-VLA, TinyVLA, SwiftVLA, SARA-RT, Xiaomi-Robotics-0, SP-VLA

**建议保留 4 篇**：
- **PD-VLA** (2025) - 保留，parallel decoding 是核心 architectural innovation
- **DeeR-VLA** (2024) - **替换 SwiftVLA**，dynamic early-exit 更有原创性
- **MoLe-VLA** (2025) - **替换 SP-VLA**，Mixture-of-Layers 比 dynamic switching 更系统
- **VLA-Cache** (2025) - **替换 SARA-RT**，autoregressive caching 更直接针对 VLA

**删除**：
- TinyVLA - 已在 Type I 侧提过，不需要重复
- SwiftVLA - spatiotemporal routing 不如 early-exit 清晰
- SARA-RT - attention complexity reduction 太底层
- Xiaomi-Robotics-0 - 工业系统，不是方法论贡献
- SP-VLA - dynamic switching 不如 MoLe 的 layer-skipping 系统

---

### Safety & Robustness 类别

**当前 2 篇**：Policy Contrastive Decoding, Neural MP

**建议保留 2 篇**（不变）：
- **Policy Contrastive Decoding** (2026) - 保留
- **Neural MP** (2024) - 保留

**理由**：这两篇已经是最核心的代表，一个处理 spurious correlation，一个提供 formal guarantee

---

### Failure Recovery 类别

**当前 4 篇**：FAIL-Detect, RACER, AHA, Reflective Test-Time Planning

**建议保留 3 篇**：
- **FAIL-Detect** (2025) - 保留，OOD detection 是基础
- **RACER** (2024) - 保留，language-guided recovery 是主流
- **Reflective Test-Time Planning** (2026) - 保留，runtime self-improvement 是前沿

**删除**：
- AHA - VLM-based diagnosis 和 RACER 功能重叠

---

## 最终 Stage 3 文献配置

### Quantization & Pruning (3 篇)
1. QVLA - action-centric mixed-precision
2. HBVLA - 1-bit extreme quantization
3. BitVLA - 1-bit weight quantization

### Decoding Acceleration (4 篇)
1. PD-VLA - parallel decoding
2. DeeR-VLA - dynamic early-exit
3. MoLe-VLA - Mixture-of-Layers layer-skipping
4. VLA-Cache - autoregressive caching

### Safety & Robustness (2 篇)
1. Policy Contrastive Decoding - spurious correlation handling
2. Neural MP - formal safety guarantee

### Failure Recovery (3 篇)
1. FAIL-Detect - OOD detection
2. RACER - language-guided recovery
3. Reflective Test-Time Planning - runtime self-improvement

---

## 总结

**删除 7 篇**：LightVLA, EfficientVLA, TinyVLA, SwiftVLA, SARA-RT, Xiaomi-Robotics-0, SP-VLA, AHA

**新增 3 篇**：BitVLA, DeeR-VLA, MoLe-VLA, VLA-Cache

**最终数量**：12 篇（原 16 篇）

**含金量提升**：
- 删除了工程优化类（EfficientVLA, SARA-RT, Xiaomi-Robotics-0）
- 删除了功能重叠类（TinyVLA 已在 Type I 提过，AHA 和 RACER 重叠）
- 新增了 architectural innovation 类（DeeR-VLA early-exit, MoLe-VLA layer-skipping, VLA-Cache）
- 保留了极限压缩代表（HBVLA 1-bit, BitVLA 1-bit）
- 保留了核心方法（PD-VLA parallel decoding, Policy CD, Neural MP, Reflective TTP）
