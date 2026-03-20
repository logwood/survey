# The Deployment of Large Robotic Models: A 3-Stage Lifecycle Analysis of Embodied Foundation Models

## Introduction

The field of Embodied Artificial Intelligence is undergoing a structural shift from strictly defined, task-specific analytical models to highly generalized Vision-Language-Action (VLA) foundation models. While these massive architectures promise zero-shot generalization and semantic reasoning, deploying them from the digital realm onto continuous, physically constrained robotic hardware introduces severe algorithmic and engineering bottlenecks. To systematically analyze these challenges, this report categorizes 39 recent, top-tier papers strictly into a "3-Stage Real-World Deployment Lifecycle." This framework traces the trajectory of a robotic foundation model from offline preparation to online adaptation, and finally to real-time execution on the edge.

## Stage 1: Offline Pre-deployment (The Preparation Phase)

**Context:** The model is still in the cloud or simulation. During this phase, researchers focus on bridging the sim-to-real gap, compressing massive models or token spaces, injecting physical priors into simulations, and handling cross-embodiment data translation before the model touches the physical hardware.

| **Title** | **Venue & Year** | **Deployment Problem** | **Proposed Solution** |
| --- | --- | --- | --- |
| Transic: Sim-to-Real Transfer with Diffusion Transformers | ICRA 2024 | Purely simulated training for manipulation tasks fails upon physical deployment due to unmodeled contact-rich dynamics and visual domain gaps. | Proposes a holistic human-in-the-loop method that utilizes online correction to effectively bridge the sim-to-real gap for short-horizon skills without requiring massive real-robot datasets. |
| --- | --- | --- | --- |
| UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | ICRA 2025 | Standard end-effector pose action representations struggle to generalize to novel objects with different shapes, sizes, and orientations. | Introduces a Chain of Moving Oriented Keypoints (CoMOK) formulation to distill affordances without human supervision, enabling natural generalization to diverse objects. |
| --- | --- | --- | --- |
| FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models | AAAI 2026 | The generalization of VLA models is severely bottlenecked by their heavy reliance on massive, redundant, and unevenly valued offline datasets. | Implements an influence-aware data distillation framework that systematically evaluates and curates optimal, high-value training subsets for efficient offline pre-training. |
| --- | --- | --- | --- |
| X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real | CoRL 2025 | Cross-embodiment foundation pre-training is restricted by the absolute scarcity of paired, multi-robot real-world datasets. | Deploys a Real-to-Sim-to-Real pipeline that transfers manipulation skills seamlessly across fundamentally different robotic embodiments. |
| --- | --- | --- | --- |
| ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills | RSS 2025 | Simulation-to-reality physics mismatches prevent agile, whole-body humanoid skills from safely and stably transferring to hardware. | Aligns physical parameters offline by combining advanced simulation environments with real-world system identification data to lower tracking errors during deployment. |
| --- | --- | --- | --- |
| Latent Action Diffusion for Cross-Embodiment Manipulation | CoRL 2025 | Heterogeneous action spaces across different robots prevent the unified offline pre-training of a single foundation model. | Constructs a shared latent action space where diffusion models generate modality-agnostic representations prior to deployment. |
| --- | --- | --- | --- |
| Cross-Embodiment Robotic Manipulation Synthesis via Guided Demonstrations through CycleVAE and Human Behavior Transformer | IROS 2025 | The lack of paired cross-embodiment datasets and the complexity of designing intricate controllers impede offline manipulation synthesis. | Uses unsupervised CycleVAE with bidirectional subspace alignment to align latent motion sequences, paired with a human behavior transformer to learn intrinsic dynamics. |
| --- | --- | --- | --- |
| Shallow-: Knowledge Distillation for Flow-based VLAs | Arxiv 2026 | Multi-billion parameter flow-based VLAs are structurally too deep and computationally heavy for on-device edge deployment. | Introduces a knowledge distillation framework that jointly compresses the VLM backbone and action head by up to 70% while preserving crucial layer-wise feature transfer. |
| --- | --- | --- | --- |
| FAST: Efficient Action Tokenization for Vision-Language-Action Models | RSS 2025 | Standard per-dimension, per-timestep action binning schemes perform poorly when learning dexterous skills from high-frequency robot data, causing severe quantization errors. <sup>1</sup> | Employs Frequency-space Action Sequence Tokenization (FAST) via the Discrete Cosine Transform to compress continuous action sequences smoothly for autoregressive VLAs. <sup>1</sup> |
| --- | --- | --- | --- |

## Stage 2: Online Physical Alignment (The Adaptation Phase)

**Context:** The model is deployed on the physical robot and encounters real-world friction, out-of-distribution objects, and contact forces. This stage focuses on fine-tuning, residual learning, human-in-the-loop corrections, and RL-based physical alignment directly on the hardware.

| **Title** | **Venue & Year** | **Deployment Problem** | **Proposed Solution** |
| --- | --- | --- | --- |
| RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning | RSS 2025 | Fine-tuning VLAs via supervised learning relies on costly human demonstrations and converges to a single solution, capping performance in complex tasks. | Uses sample-efficient real-world RL to autonomously generate high-quality trajectory data via reward maximization, which is then distilled into the generalist VLA. |
| --- | --- | --- | --- |
| SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | ICLR 2026 | Online RL fine-tuning on massive VLAs suffers from severe instability, often oscillating heavily during out-of-distribution physical evaluation. | Simplifies RL scaling using exploration-enhancing strategies and Group Relative Policy Optimization (GRPO) to stabilize long-horizon planning under data scarcity. |
| --- | --- | --- | --- |
| Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | RSS 2025 | The optimal architecture and objective function for efficiently fine-tuning massive VLAs on specific physical tasks remain ambiguous. | Identifies an Optimized Fine-Tuning (OFT) recipe leveraging parallel decoding, continuous actions, and an L1 loss function for fast, high-success adaptation. |
| --- | --- | --- | --- |
| ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy | RSS 2025 | Online fine-tuning in contact-rich environments is highly sample-inefficient and poses physical safety risks to the hardware during unconstrained exploration. | Proposes a two-phase approach integrating offline behavior cloning/Q-learning with an online consistency policy safely guided by human-in-the-loop interventions. |
| --- | --- | --- | --- |
| Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning | Science Robotics 2025 | Pure autonomous RL fails completely on sub-millimeter dexterous tasks (e.g., tight insertions) due to severe exploration bottlenecks. | Deploys an interactive RL system where humans periodically intervene during online training to safely guide the robot into high-reward states. |
| --- | --- | --- | --- |
| DASP: Hierarchical Offline Reinforcement Learning via Diffusion Autodecoder and Skill Primitive | RA-L 2025 | Adapting pre-trained models to novel physical tasks via RL often induces catastrophic forgetting of prior manipulation skills. | Employs hierarchical offline RL using a diffusion autodecoder and skill primitives to safely adapt behavior without destroying foundational knowledge. |
| --- | --- | --- | --- |
| What can rl bring to vla generalization? an empirical study | NeurIPS 2025 | The actual generalization benefits of RL over standard supervised fine-tuning (SFT) during VLA adaptation are not systematically understood. | Empirically proves that online PPO fine-tuning significantly enhances semantic understanding and execution robustness without requiring additional imitation stages. |
| --- | --- | --- | --- |
| Consistency Regularization for Vision-Language-Action Models in Robotic Manipulation | RSS 2024 | Online physical fine-tuning causes severe distribution shifts, degrading the VLA's pre-trained visual reasoning priors and causing overfitting. | Applies consistency regularization to distill the diffusion process, ensuring the fine-tuned model's feature space avoids overfitting to the training demonstrations. |
| --- | --- | --- | --- |
| Steering Your Diffusion Policy with Latent Space Reinforcement Learning | CoRL 2025 | Fine-tuning diffusion policies online via standard RL is computationally intensive, unstable, and alters carefully pre-trained base weights. | Introduces DSRL, which uses black-box access to the base policy and applies RL strictly in the latent space to guide generation without altering base weights. |
| --- | --- | --- | --- |
| ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning | CVPR 2025 | Directly transferring human bimanual skills to dexterous robots suffers from severe kinematic mismatches and physically implausible motions. | Implements a two-stage residual framework that pre-trains a generalist trajectory imitator, then fine-tunes a specialist residual module under strict interaction constraints. |
| --- | --- | --- | --- |
| Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | ICLR 2026 | Gathering real-world online correction data via teleoperation is human-intensive, slow, and completely non-scalable for self-improving models. <sup>2</sup> | PLD (Probe, Learn, Distill) trains lightweight residual actors via off-policy RL to autonomously probe failure states and distill curated recoveries back into the VLA. <sup>2</sup> |
| --- | --- | --- | --- |
| FLaRe: Achieving Masterful and Adaptive Robot Policies with Large-Scale Reinforcement Learning Fine-Tuning | ICRA 2025 | Generalist policies struggle to master specific, complex physical tasks online without degrading their broad capabilities. | Utilizes a large-scale RL fine-tuning framework that adaptively balances highly generalized priors with targeted, task-specific physical optimization. |
| --- | --- | --- | --- |
| Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions | CoRL 2025 | Scaling offline RL to large autoregressive models is mathematically challenging due to the continuous nature of robotic action spaces. | Discretizes the action space and utilizes autoregressive Q-functions to successfully scale offline actor-critic learning to massive transformer architectures. |
| --- | --- | --- | --- |
| ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | ICML 2025 | Mixed-quality demonstration data leads to suboptimal behavior cloning policies that cannot autonomously improve online. | Integrates RL principles by predicting dense returns to leverage sub-optimal data and amplify VLM-guided manipulation via reward maximization. |
| --- | --- | --- | --- |
| Offline Actor-Critic Reinforcement Learning Scales to Large Models | ICML 2025 | Traditional actor-critic RL algorithms become highly unstable when applied to billion-parameter foundational transformer architectures. | Stabilizes offline actor-critic methods via critical architectural modifications, enabling stable adaptation on multi-billion parameter foundation models. |
| --- | --- | --- | --- |
| VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning | IROS 2025 | Bimanual physical assembly requires microscopic coordination that standard visual sim-to-real transfer fails to achieve due to severe inter-arm occlusions. | Employs an online fine-tuning protocol heavily reliant on continuous, multi-modal visuo-tactile feedback to physically align dual robotic arms. |
| --- | --- | --- | --- |

## Stage 3: Inference-Time Execution (The Runtime Phase)

**Context:** The model is running continuously on the robot. This stage addresses the critical runtime bottlenecks of massive model sizes, focusing on inference acceleration, parallel decoding, strict safety guarantees, and autonomous failure recovery during 10Hz+ real-time control.

| **Title** | **Venue & Year** | **Deployment Problem** | **Proposed Solution** |
| --- | --- | --- | --- |
| AUTOQVLA: NOT ALL CHANNELS ARE EQUAL IN VISION-LANGUAGE-ACTION MODEL’S QUANTIZATION | ICLR 2026 | Applying uniform-bit LLM quantization to VLAs causes catastrophic physical task failures by ignoring how minor action deviations compound. | Proposes an action-centric, channel-wise bit allocation guided by action-space sensitivity, unifying quantization and pruning into a single optimization process. |
| --- | --- | --- | --- |
| Policy Contrastive Decoding for Robotic Foundation Models | ICLR 2026 | VLA policies often over-rely on spurious visual correlations (e.g., background textures) during runtime, causing out-of-distribution physical failures. | Contrasts action probability distributions derived from original versus object-masked inputs via a KDE-based probabilistic modeling scheme to redirect focus to task-relevant features. |
| --- | --- | --- | --- |
| PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding | IROS 2025 | Action chunking in autoregressive VLAs linearly scales up action dimensions, causing severe temporal latency that cripples real-time 10Hz+ control. <sup>3</sup> | Reformulates autoregressive decoding into parallel fixed-point (Jacobi) iterations, enabling the simultaneous generation of entire action chunks without architectural changes. <sup>3</sup> |
| --- | --- | --- | --- |
| TinyVLA: Toward Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation | RA-L 2025 | Multi-billion parameter counts make VLAs entirely too slow for dynamic, closed-loop execution on constrained edge compute. | Distills massive VLAs into extremely fast, data-efficient, lightweight models that preserve semantic reasoning while heavily accelerating action decoding. |
| --- | --- | --- | --- |
| SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead | CVPR 2026 | Aggressively compressed, lightweight VLA models lose the ability to capture the complex spatiotemporal dynamics required for fluid movement. | Unlocks spatiotemporal dynamics with minimal compute overhead by intelligently routing spatiotemporal features, balancing inference speed and kinematic performance. |
| --- | --- | --- | --- |
| Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies | RSS 2025 | Detecting execution failures at runtime traditionally requires training on massive datasets of failed trajectories, which are dangerous to collect. | Introduces FAIL-Detect, an uncertainty-aware failure detection system using flow-based density estimators to identify anomalies without explicit failure data. |
| --- | --- | --- | --- |
| RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning | ICRA 2025 | Generating large-scale failure datasets via simulation perturbations is constrained by the sim-to-real gap, limiting efficiency in real-world settings. | Deploys Rich Language-Guided Failure Recovery Policies that utilize real-time visual-language reasoning to autonomously diagnose and correct physical failures. |
| --- | --- | --- | --- |
| The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning | ICLR 2026 | VLA models waste immense computational resources processing redundant visual background tokens during steady-state physical actions. | Implements LightVLA, a differentiable token pruning mechanism adopting Gumbel softmax that adaptively drops irrelevant visual tokens based strictly on task execution requirements. |
| --- | --- | --- | --- |
| Neural MP: A Generalist Neural Motion Planner | CoRL 2024 | End-to-end neural networks cannot mathematically guarantee the collision-free, kinematically feasible trajectories required for precise manipulation phases. <sup>4</sup> | Deploys a hybrid execution model that automatically switches between coarse waypoint-based navigation and dense action controllers for precise, collision-free movement. <sup>4</sup> |
| --- | --- | --- | --- |
| AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation | ICLR 2025 | VLMs can plan actions but lack the introspective capability and mechanisms to recognize and logically reason about their own physical mistakes. | Fine-tunes an open-source VLM via procedurally generated failure trajectories (FailGen) to autonomously detect and generate free-form language rationales for physical failures. |
| --- | --- | --- | --- |
| HBVLA: Pushing 1-Bit Post-Training Quantization for Vision-Language-Action Models | Arxiv 2026 | Extreme VRAM constraints on edge hardware prohibit large models, but standard binarization creates error accumulation under long-horizon closed-loop execution. | Instantiates a 1-bit post-training quantization framework combining policy-grounded saliency and Haar wavelet transforms to preserve crucial mathematical precision. |
| --- | --- | --- | --- |
| EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | NeurIPS 2025 | Training-based compression methods require massive compute clusters and complex datasets to compress the model prior to deployment. | Introduces a completely training-free acceleration and compression algorithm that optimizes the KV cache and prunes tokens on the fly during inference. |
| --- | --- | --- | --- |
| Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution | Arxiv 2026 | High inference latency during real-world rollouts causes jerky, stuttering motion, ruining continuous bimanual coordination tasks. <sup>5</sup> | Deploys an asynchronous execution pipeline with adaptive loss re-weighting and a lambda-shape attention mask, achieving ultra-low 80ms latency. <sup>5</sup> |
| --- | --- | --- | --- |
| SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration | ICLR 2026 | Deep transformer layers are exhaustively evaluated at every timestep, even during simple, straight-line robotic reaches, wasting severe amounts of compute. | Employs action-aware model scheduling to dynamically switch between the heavy VLA and a lightweight generator, paired with spatio-semantic token pruning. |
| --- | --- | --- | --- |

#### Works cited

1.  FAST: Efficient Action Tokenization for Vision-Language-Action Models - arXiv, accessed February 27, 2026, https://arxiv.org/html/2501.09747v1
2.  Self-Improving Vision-Language-Action Models with ... - Wenli Xiao, accessed February 27, 2026, https://www.wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf
3.  PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding - arXiv.org, accessed February 26, 2026, https://arxiv.org/html/2503.02310v2
4.  What's the Move? Hybrid Imitation Learning via Salient Points | OpenReview, accessed February 27, 2026, https://openreview.net/forum?id=r0pLGGcuY6
5.  Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution - arXiv, accessed February 27, 2026, https://arxiv.org/html/2602.12684v1