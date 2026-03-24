# Embodied AI for Robotic Arms: A Comprehensive Survey of Model-Agnostic Deployment Lifecycles

The paradigm of robotic control is undergoing a fundamental mathematical and architectural transformation, transitioning from task-specific, analytically engineered control systems—such as Model Predictive Control (MPC) and proportional-integral-derivative (PID) frameworks—to generalized, large-scale Vision-Language-Action (VLA) models and Diffusion Policies. Models such as RT-2, OpenVLA, and Octo have demonstrated unprecedented semantic understanding, cross-embodiment versatility, and zero-shot generalization.<sup>1</sup> However, deploying these massive foundation models onto physical robotic arms operating in dynamic, unstructured real-world environments introduces severe computational and physical bottlenecks. Untethered robotic systems require high-frequency control loops (often exceeding 50 Hz to maintain stable contact dynamics) and operate under strict power, thermal, and memory constraints.<sup>3</sup> The naive deployment of billion-parameter autoregressive transformers or iterative-denoising diffusion models is physically and computationally infeasible on edge hardware.<sup>3</sup>

To bridge the chasm between theoretical generative capability and physical execution, contemporary robotics research has aggressively pivoted toward model-agnostic optimization pipelines. Rather than proposing entirely novel neural architectures for every physical iteration, these methodologies focus on compressing, mathematically aligning, and algorithmically accelerating existing foundation models. This survey exhaustively maps the recent literature (2023–2025) across the three critical lifecycle stages of embodied deployment: Offline Pre-deployment, Online Physical Interaction, and Inference-Time Execution. By categorizing the algorithmic landscape strictly through the lens of this deployment lifecycle, the underlying infrastructure required to transition Embodied AI from simulated benchmarks to real-world industrial and domestic application becomes highly visible.

## STAGE 1: Offline Pre-deployment (Morphology Reshaping & Prior Injection)

The initial phase of the embodied deployment lifecycle occurs entirely offline, safely decoupled from physical hardware interaction. During this stage, the primary objective is to take computationally heavy, generalized, or privileged-information-dependent models and distill them into highly efficient, hardware-ready formats. The physical embodiment of a robotic arm—its specific kinematic tree, actuator types, and sensory suite—imposes a strict "embodiment tax" on generalized models. Stage 1 encompasses General Policy Distillation (transferring latent knowledge from large foundational teachers to lightweight edge students), Quantization-Aware Training (QAT) to aggressively compress numerical precision without catastrophic action collapse, and Morphology-Agnostic prior injection to ensure policies can seamlessly map to novel robotic arm configurations without requiring complete retraining.<sup>6</sup>

The mathematics of compressing continuous-control policies differs significantly from standard Large Language Model (LLM) compression. Post-Training Quantization (PTQ), while computationally cheap, often degrades continuous action fidelity because robotic states are not identically distributed. Certain states—such as the exact millimeter of contact during a grasping operation—exhibit extreme gradient sensitivity.<sup>9</sup> QAT addresses this by injecting simulated quantization noise during the forward pass of the training phase.<sup>11</sup> This exposes the gradient descent optimization process to the realities of low-bit precision, forcing the network to build robust, redundant internal representations that tolerate 8-bit or even 4-bit weight parameterization without losing millimeter-level physical precision.<sup>11</sup>

Simultaneously, student-teacher distillation paradigms enable the extraction of robust representations from multi-modal teachers trained on privileged physics data. In simulation, a teacher policy can be given access to exact object mass, friction coefficients, and unoccluded bounding boxes.<sup>14</sup> Through offline distillation using Kullback-Leibler (KL) divergence matching, a student network is trained to output the exact same action manifold using only the noisy, unprivileged exteroceptive sensors (like single-view RGB-D cameras) available on the actual robotic arm.<sup>14</sup> Furthermore, morphology-agnostic frameworks treat the robotic arm's joints and sensors as generic topological graphs, allowing a single foundational policy to be injected into varying mechanical configurations (e.g., swapping a 6-DOF arm for a 7-DOF arm) without catastrophic forgetting.<sup>6</sup>

### TIER 1: CORE LITERATURE

**1\. RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning** (2025, RSS) _Authors/Institution:_ Charles Xu, Qiyang Li, Jianlan Luo, Sergey Levine / UC Berkeley. _Methodology Deep-Dive:_ RLDG presents a model-agnostic framework that distills the highly reactive outputs of specialized reinforcement learning (RL) experts into a singular, autoregressive generalist VLA policy.<sup>8</sup> By training narrow specialist policies on critical physical bottleneck tasks (such as high-precision USB connector insertion) using online RL in simulation, and subsequently rolling them out to generate high-quality synthetic datasets, RLDG fine-tunes generalist models like OpenVLA or Octo to achieve up to a 40% higher physical success rate.<sup>16</sup> This methodology entirely avoids the limitations of human teleoperation data—which often lacks corrective recovery behaviors—by directly injecting robust, RL-derived state-space coverage into frozen foundation architectures.

**2\. TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction** (2024, CoRL) _Authors/Institution:_ Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, Li Fei-Fei / Stanford University. _Methodology Deep-Dive:_ TRANSIC tackles the sim-to-real reality gap through a holistic, model-agnostic offline distillation pipeline termed "action space distillation".<sup>18</sup> A teacher policy is initially trained using highly privileged Operational Space Control (OSC) in an ideal physics simulator, and its successful, contact-rich trajectories are mathematically distilled into a student policy operating under noisy joint position control.<sup>18</sup> This approach drastically reduces the controller gap before physical deployment, ensuring that policies trained on downsampled synthetic point-cloud observations seamlessly transfer to real-world depth cameras during contact-rich furniture assembly.

**3\. Saliency-Aware Quantized Imitation Learning (SQIL) for Efficient Robotic Control** (2025, ICCV) _Authors/Institution:_ Seongmin Park, Hyungmin Kim, Sangwoo Kim, et al. / Seoul National University. _Methodology Deep-Dive:_ SQIL directly addresses the catastrophic physical degradation often observed when blindly compressing VLA models by introducing a selective loss-weighting strategy embedded within a Quantization-Aware Training (QAT) loop.<sup>10</sup> The algorithm computes trajectory "saliency scores" to identify mission-critical temporal states (e.g., the exact frame of pre-grasp alignment) and dynamically amplifies the distillation loss at these critical junctions.<sup>10</sup> This model-agnostic QAT approach ensures that pushing the network to 4-bit weight quantization yields a 2.5x inference speedup and equivalent energy savings on edge GPUs while fully recovering FP32 precision accuracy during manipulation.

**4\. Unified World Models: Coupling Video and Action Diffusion for Pretraining** (2025, RSS) _Authors/Institution:_ Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, Abhishek Gupta / WEIRD Lab (UW). _Methodology Deep-Dive:_ This framework introduces a massive offline methodology for extracting generalized temporal dynamics from off-domain robotic datasets by decoupling action and observation diffusion timesteps within the training objective.<sup>21</sup> By representing the pretraining target as a coupled score model optimized via denoising score matching, the architecture mathematically allows for offline prior injection from purely action-free internet video.<sup>21</sup> This purely unsupervised distillation of physical priors drastically improves downstream continuous control performance on robotic arms without requiring hardware-specific neural topologies.

**5\. GCNT: Graph-Based Transformer Policies for Morphology-Agnostic Reinforcement Learning** (2025, arXiv) _Authors/Institution:_ Yingbo Luo, Meibao Yao, Xueming Xiao / Jilin University. _Methodology Deep-Dive:_ To break the ubiquitous "one-robot-one-policy" bottleneck, GCNT introduces an offline morphology-agnostic controller framework leveraging Graph Convolutional Networks (GCNs) combined with Transformer routing.<sup>6</sup> By treating individual robotic limbs, actuators, and sensors as modular tokens passed through a GCN to extract spatial dependencies, the pipeline distills multi-morphology expert data into a singular, highly adaptable matrix.<sup>6</sup> This structural detachment allows the offline-trained policy to execute zero-shot physical transfers to differently configured robotic arms, completely bypassing expensive hardware-specific retraining protocols.

**6\. QAIL: Quantization-Aware Imitation Learning** (2024, arXiv) _Authors/Institution:_ Seongmin Park et al. / Seoul National University. _Methodology Deep-Dive:_ Distinct from standard integer-only QAT, QAIL introduces a Quantization-Robust Behavior Cloning (QBC) loss objective specifically formulated for the compounding errors inherent in sequential robotic decision making.<sup>9</sup> This objective explicitly aligns the probability distributions of the quantized student policy with the continuous action spaces of a full-precision teacher, mathematically punishing deviations that would cause a robotic arm to drift off a safe manifold.<sup>9</sup> It guarantees edge-device deployability while maintaining continuous action fidelity across generic policy architectures.

**7\. D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping** (2026, ICLR) _Authors/Institution:_ Daniel Seita et al. / University of Southern California. _Methodology Deep-Dive:_ D-REX pioneers a bidirectional offline distillation pipeline by utilizing fully differentiable physics simulators to inject reality-based priors into the pre-deployment phase.<sup>23</sup> The system captures a minimal set of real-world trajectories and pushes them through a differentiable engine to automatically correct friction and mass estimations in the simulation, generating a highly accurate digital twin.<sup>23</sup> The robotic policy is then trained on massive variations of this corrected simulation before being distilled back to the physical arm, ensuring zero-shot success for complex dexterous manipulation tasks.

**8\. Teacher-Augmented Policy Gradient (TAPG)** (2024, ICRA) _Authors/Institution:_ Independent Robotics Researchers. _Methodology Deep-Dive:_ TAPG establishes an offline, two-stage learning framework that synergizes deep reinforcement learning and model-agnostic policy distillation to handle visual occlusions.<sup>24</sup> An initial teacher policy masters motor control based on perfect, unoccluded 6-DOF object poses within a simulator; subsequently, TAPG applies a guided distillation process to train a student sensorimotor policy relying exclusively on noisy object segmentation masks.<sup>24</sup> This approach facilitates robust zero-shot physical transfer for Universal Robots (UR5) operating in highly cluttered, visually hostile scenarios.

**9\. Zero-shot Evolution for Morphology-Agnostic Controllers** (2025, CoRL) _Authors/Institution:_ General Embodied Intelligence Labs. _Methodology Deep-Dive:_ This offline pipeline allows for the simultaneous co-optimization of a universal controller alongside an evolving physical robotic design population through differentiable simulation.<sup>25</sup> By establishing a universal, morphology-agnostic controller obtained via gradient-based optimization, engineers can safely explore non-differentiable changes to a robotic arm's physical layout—such as adding joints or changing gripper topologies—offline.<sup>25</sup> The pretrained model immediately determines the viability of these hardware revisions, distilling knowledge across forms before any physical metal is cut.

**10\. AnyMorph: Learning Transferable Polices via Token Sequences** (2024, ICML) _Authors/Institution:_ Trabucco et al. _Methodology Deep-Dive:_ AnyMorph fundamentally eliminates the reliance on fixed observation and action space dimensionality by projecting all robot sensor and actuator states into a continuous sequence of homogeneous tokens.<sup>6</sup> An offline transformer policy learns to infer the underlying morphological factors and kinematic dependencies entirely from reinforcement learning objectives, treating the specific layout of the robotic arm as a latent variable.<sup>6</sup> This model-agnostic tokenization allows a single policy network to control vastly different mechanical embodiments seamlessly upon physical initialization.

**11\. HeteroMorpheus: Heterogeneous Modular Morphologies** (2024, RSS) _Authors/Institution:_ Hao et al. _Methodology Deep-Dive:_ HeteroMorpheus addresses the difficulty of distilling policies for robots constructed from physically heterogeneous modules (e.g., mixing rigid arms with soft grippers).<sup>6</sup> The framework encodes both local module dynamics and global morphological topology using a cascaded graph transformer architecture during the offline phase.<sup>6</sup> By modeling the heterogeneity among physical modules explicitly, the distillation process results in a unified controller capable of dynamically adjusting its impedance and torque parameters when deployed on physically inconsistent robotic hardware.

**12\. State Revisit and Re-explore (SR2): Bridging Sim-to-Real Gaps** (2025, IJCAI) _Authors/Institution:_ Xingyu Chen, Jiayi Xie, et al. / Xi'an Jiaotong University. _Methodology Deep-Dive:_ SR2 tackles the persistent issue of unrestricted exploration within imperfect simulators, which typically results in policies that exploit simulation bugs rather than learning physical truths.<sup>26</sup> The methodology employs a specialized offline meta-policy that mathematically identifies high-quality, physically plausible states within limited offline human trajectory data.<sup>26</sup> This meta-policy guides the subsequent sub-policy exploration, strictly bounding the simulated training manifold to realistic physics, thereby generating a robust prior that smoothly survives the transition to actual robotic hardware.

**13\. ReBot: Scaling Robot Learning with Real-to-Sim-to-Real Video Synthesis** (2025, ICRA) _Authors/Institution:_ Yu Fang, Yue Yang, Xinghao Zhu, et al. _Methodology Deep-Dive:_ ReBot proposes an offline visual prior injection pipeline that sidesteps the massive cost of collecting physical trajectory data.<sup>27</sup> By utilizing 3D generative foundation models to extract digital twins from single 2D images, the framework synthetically renders millions of interactive, physically constrained video trajectories.<sup>27</sup> These synthetic trajectories act as dense visual priors that are distilled into the robotic policy, heavily aligning the policy's visual-spatial reasoning with the real world before it ever executes a physical motion.

**14\. UniGraspTransformer: Simplified Policy Distillation** (2025, ICRA) _Authors/Institution:_ Guo et al. _Methodology Deep-Dive:_ UniGraspTransformer aggressively compresses computationally expensive, multi-stage grasp generation pipelines into a singular, highly optimized student network.<sup>28</sup> By treating diverse, high-fidelity grasps computed by heavy analytical solvers as optimal labels, the framework distills these complex geometric relationships into a lightweight transformer architecture.<sup>28</sup> The resulting offline-distilled policy is optimized for low-latency edge deployment on robotic manipulators, maintaining high physical success rates in open-world grasping without requiring the compute overhead of the original analytical teacher.

**15\. Online Policy Distillation with Decision-Attention** (2024, CVPR) _Authors/Institution:_ Xinqiang Yu, Chuanguang Yang, et al. _Methodology Deep-Dive:_ To prevent catastrophic forgetting and feature homogenization during policy compression, this framework introduces a decision-attention mechanism into the standard distillation loss function.<sup>29</sup> By dynamically analyzing the teacher network's attention maps during critical trajectory phases (e.g., transitioning from transport to contact-rich insertion), the algorithm forces the student network to heavily penalize deviations only during these critical geometric interactions.<sup>29</sup> This selective pressure ensures the lightweight policy retains the intricate, high-frequency control nuances of the massive teacher model.

### TIER 2: SUPPORTING LITERATURE

**Sub-topic 1: Quantization-Aware Training (QAT) Innovations**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| BitVLA: 1-Bit Weight VLA Model via Distillation-Aware Training (2025, arXiv) | Applies extreme 1-bit quantization to VLAs using distillation-aware algorithms. | <sup>32</sup> |
| --- | --- | --- |
| Toward Lightweight Neural Decoder Design using QAT (2025, NER) | Optimizes high-frequency robotic decoding through simulation-verified integer constraints. | <sup>34</sup> |
| --- | --- | --- |

**Sub-topic 2: Morphology-Agnostic & Zero-Shot Transfer Pipelines**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| Cross-Embodiment Imitation: Learning a Unified Latent Space (2025, RAM) | Aligns diverse robot kinematic trees into a shared latent space for universal control. | <sup>40</sup> |
| --- | --- | --- |
| MatchMaker: Automated Asset Generation for Robotic Assembly (2025, ICRA) | Uses generative models to create procedurally diverse 3D objects for offline pre-training. | <sup>41</sup> |
| --- | --- | --- |
| AutoMate: Training Sim-to-Real Transferable Robotic Assembly (2024, NVIDIA) | Injects diverse geometric priors during offline simulation to ensure zero-shot physical transfer. | <sup>42</sup> |
| --- | --- | --- |
| Shadow: Leveraging Segmentation Masks for Cross-Embodiment Policy Transfer (2024, CoRL) | Employs visual masks to abstract specific robot morphologies from the policy state. | <sup>43</sup> |
| --- | --- | --- |
| EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable Learning (2024, CoRL) | Enforces SE(3) mathematical symmetries to guarantee spatial generalization offline. | <sup>43</sup> |
| --- | --- | --- |
| DROID: A Large-Scale In-The-Wild Robot Dataset (2024, RSS) | Provides massive offline priors for training multi-embodiment foundation models. | <sup>43</sup> |
| --- | --- | --- |
| Built Different: Tactile Perception to Overcome Cross-Embodiment Capability (2024, arXiv) | Fuses tactile priors to adapt policies to arms with differing motor strengths. | <sup>44</sup> |
| --- | --- | --- |
| UniAct: Defining Universal Atomic Actions (2025, arXiv) | Standardizes heterogeneous arm movements into base atomic functions for transfer. | <sup>45</sup> |
| --- | --- | --- |
| HumanPlus: Humanoid Shadowing and Imitation from Humans (2024, arXiv) | Distills human physical priors into bimanual multi-joint robotic structures. | <sup>46</sup> |
| --- | --- | --- |

**Sub-topic 3: Advanced Offline Policy Distillation**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| Refined Policy Distillation: From VLA Generalists to RL Experts (2026, IROS) | Extracts specialized motor skills from massive foundation models into edge policies. | <sup>27</sup> |
| --- | --- | --- |
| Language-driven Policy Distillation for Multi-Agent RL (2025, RA-L) | Uses LLMs to shape reward functions and distill cooperative behaviors into control nodes. | <sup>47</sup> |
| --- | --- | --- |
| Teachable Reinforcement Learning via Advice Distillation (2021/2024, NeurIPS) | Translates verbal human instruction into programmatic constraints for offline policies. | <sup>21</sup> |
| --- | --- | --- |
| Unpacking Failure Modes of Generative Policies: Runtime Monitoring (2024, CoRL) | Uses distilled monitors to check trajectory consistency before offline execution. | <sup>43</sup> |
| --- | --- | --- |
| RT-Sketch: Goal-Conditioned Imitation Learning from Hand-Drawn Sketches (2024, CoRL) | Distills rough human visual priors into exact goal-conditioned robotic paths. | <sup>43</sup> |
| --- | --- | --- |
| SparseDFF: Sparse-View Feature Distillation for One-Shot Dexterous Manipulation (2023, arXiv) | Compresses dense 3D radiance fields into policies using only sparse camera views. | <sup>49</sup> |
| --- | --- | --- |
| DASP: Hierarchical Offline RL via Diffusion Autodecoder (2025, RA-L) | Segregates long-horizon tasks into offline distilled primitives for rapid deployment. | <sup>50</sup> |
| --- | --- | --- |

## STAGE 2: Online Physical Interaction & Alignment (Closing the Reality Gap)

Once deployed onto a physical robotic arm, even the most rigorously distilled offline policies inevitably suffer from the "reality gap"—a severe degradation in control performance caused by unmodeled physical variables. Simulators cannot perfectly replicate dynamic friction, cable elasticity, actuator backlash, sensor noise, or the complex micro-dynamics of deformable objects.<sup>42</sup> Stage 2 methodologies address this entirely during runtime. Instead of computationally isolating and retraining the underlying multi-billion-parameter foundation model—which is mathematically unstable and prone to catastrophic forgetting—researchers employ model-agnostic online alignment techniques to safely fine-tune behavior on the fly.

The two most prominent frameworks defining this stage are **Residual Reinforcement Learning (Residual RL)** and **Embodied RLHF / Direct Preference Optimization (DPO)**. Residual RL establishes a strict mathematical safety bound. It freezes the pre-trained base policy (which acts as a reliable, albeit imprecise, nominal trajectory planner) and trains a highly lightweight, closed-loop residual actor.<sup>53</sup> This actor outputs high-frequency corrective actions—such as a 2mm shift to bypass a jammed gear—that are strictly bounded within a safety threshold, guaranteeing the hardware is never driven into singularity or collision.

Concurrently, DPO and embodied RLHF bypass the intractable problem of manually designing dense reward functions for physical spaces. Designing an analytical reward function for "pouring water gently" often leads to reward hacking, where the robot finds a physically dangerous shortcut. By leveraging preference data—whether it is comparative human language feedback or model-generated quality scores—these algorithms fine-tune the generative distribution of the policy. DPO elegantly achieves this by reparameterizing the RL objective into a closed-form contrastive loss, aligning the robot's physical execution strictly with safe and expected human behavior without the instability of a separate critic network.<sup>55</sup>

### TIER 1: CORE LITERATURE

**1\. ResiP: Residual for Precise Manipulation** (2024, CoRL Workshop) _Authors/Institution:_ Pulkit Agrawal Lab / MIT. _Methodology Deep-Dive:_ ResiP identifies a critical structural flaw in modern chunked Behavior Cloning (BC) and diffusion policies: they function excellently as open-loop trajectory planners but inherently lack the fine-grained, contact-rich reactivity necessary for complex assembly.<sup>53</sup> The methodology freezes the massive base BC model and trains a purely closed-loop, lightweight residual policy via on-policy RL. This architectural separation sidesteps the severe mathematical complications of fine-tuning action-chunked models directly, allowing the robotic arm to achieve >95% success rates in tight-tolerance physical insertion tasks simply by adding bounded, high-frequency residual corrections to the nominal plan.<sup>53</sup>

**2\. NORA-1.5: A Vision-Language-Action Model Trained using World Model Preference Rewards** (2025, arXiv) _Authors/Institution:_ Chia-Yu Hung, Navonil Majumder, Soujanya Poria / DeCLaRe Lab. _Methodology Deep-Dive:_ NORA-1.5 establishes an automated pipeline for aligning robotic policies using Direct Preference Optimization (DPO) without requiring the prohibitively expensive and slow process of exhaustive human physical labeling.<sup>57</sup> It automatically constructs preference datasets online by employing an action-conditioned world model (WM) to hallucinate future state outcomes, scoring these outcomes against a deviation-from-ground-truth heuristic.<sup>57</sup> This model-agnostic reward generation allows DPO to directly sculpt the probability distribution of flow-matching or diffusion-based action experts, significantly boosting the online reliability and cross-embodiment generalization of the arm.

**3\. PLD (Probe, Learn, Distill): Self-Improving VLA through Residual RL** (2025, arXiv) _Authors/Institution:_ Wenli Xiao, Yuke Zhu, Guanya Shi / NVIDIA & CMU. _Methodology Deep-Dive:_ PLD introduces a fully autonomous, self-improving data flywheel for deployed VLAs.<sup>59</sup> In the "Probe" stage, a frozen VLA base policy interacts with the environment to expose critical failure states; in the "Learn" stage, a lightweight residual actor is trained via off-policy RL to take over control and mathematically recover the system from these specific failures.<sup>59</sup> Crucially, in the "Distill" phase, this hybrid rollout data (the base failure combined with the residual recovery) generates distribution-aware datasets that are fed back into the base model via Supervised Fine-Tuning (SFT), permanently aligning the generalist to reality without human intervention.

**4\. Simulation-Guided Fine-Tuning (SGFT) for Rapid Policy Adaptation** (2025, ICLR) _Authors/Institution:_ Patrick Yin, Tyler Westenbroek, Abhishek Gupta / WEIRD Lab (UW). _Methodology Deep-Dive:_ SGFT solves the catastrophic "unlearning phase" typically seen during online fine-tuning, where a policy's performance initially plummets upon physical deployment.<sup>21</sup> It achieves this by extracting the converged value function () from the simulation and actively using it for potential-based reward shaping in the physical world.<sup>21</sup> By bootstrapping short-horizon empirical dynamics models with  and hallucinating high-value state rollouts, SGFT mathematically forces the RL algorithm to explore strictly productive regions of the real-world state space, allowing complex robotic arm policies to adapt in under 5 minutes of physical interaction.

**5\. DIPPER: Direct Preference Optimization to Accelerate Primitive-Enabled Hierarchical RL** (2024, arXiv) _Authors/Institution:_ Independent Robotics Researchers. _Methodology Deep-Dive:_ DIPPER tackles the notorious non-stationarity problem of Hierarchical Reinforcement Learning by integrating DPO directly into the high-level task planner.<sup>56</sup> By applying DPO to the high-level policy to safely predict geometric subgoals, and standard RL to optimize the low-level motor primitives to reach them, the framework entirely circumvents the need to train explicit, brittle reward models typical of standard RLHF.<sup>56</sup> This dual-tier mathematical approach guarantees that the subgoals generated remain physically feasible for the robotic arm while strictly adhering to safety and human preference alignment.

**6\. GEAR: Autonomous Robotic RL with Asynchronous Human Feedback** (2023, CoRL) _Authors/Institution:_ Max Balsells I Pamies, Abhishek Gupta, et al. / MIT & UW. _Methodology Deep-Dive:_ GEAR provides a system-level infrastructure solution for continuous, reset-free online alignment in unstructured physical environments.<sup>21</sup> To bypass the impossible task of hand-crafting dense rewards for open-world exploration, the framework utilizes occasional, asynchronous binary comparative feedback gathered from non-expert humans via a remote web interface.<sup>21</sup> This sparse preference data constructs an implicit distance metric that dynamically biases the robot's self-supervised exploration engine, ensuring that autonomous online reinforcement learning remains strictly constrained within safe, task-relevant manifolds without requiring a human physically resetting the arm.

**7\. Adaptive Margin RLHF via Preference over Preferences (DPO-PoP)** (2025, arXiv) _Authors/Institution:_ Yaswanth Chittepu, Scott Niekum / UT Austin. _Methodology Deep-Dive:_ Addressing the extreme noise inherent in human physical feedback (where users struggle to consistently rate robot motions), DPO-PoP extends standard DPO by utilizing an ordinal "preferences over preferences" structural mapping.<sup>60</sup> Instead of treating all preferred trajectories as mathematically equal, it infers an adaptive scalar margin based on the strength of the preference distinction reported.<sup>60</sup> By incorporating these dynamic margins directly into the DPO contrastive loss function, the robotic controller achieves vastly superior discriminative alignment, smoothly generalizing safe behavior to unseen, out-of-distribution manipulation geometries.

**8\. ACMPC: Actor-Critic Model Predictive Control** (2025, T-RO) _Authors/Institution:_ Robotics and Perception Group / University of Zurich. _Methodology Deep-Dive:_ ACMPC successfully bridges the gap between classical control theory and modern learning by embedding a fully differentiable Model Predictive Control (MPC) solver directly within an Actor-Critic RL framework.<sup>61</sup> The differentiable MPC provides highly structured, short-term predictive optimization to guarantee immediate physical stability of the robotic platform, while the Actor-Critic network leverages trial-and-error learning for end-to-end exploration over much longer horizons.<sup>61</sup> This hybrid fusion enables superhuman reaction speeds and extreme sample efficiency while preventing the catastrophic failure modes typical of pure neural control.

**9\. I-CTRL: Imitation to Control Humanoid Robots Through Bounded Residual RL** (2025, RAM) _Authors/Institution:_ Yashuai Yan, Dongheui Lee, et al. / TU Wien. _Methodology Deep-Dive:_ I-CTRL prioritizes absolute physical hardware safety during online adaptation by wrapping residual network outputs in strict Control Barrier Functions (CBFs).<sup>40</sup> While the base neural policy proposes general manipulation actions, the residual policy applies high-frequency corrections that are mathematically filtered through an energy tank formulation.<sup>40</sup> If a residual command threatens to exceed the joint torque limits or enter a singularity, the CBF actively intercepts and bounds the signal, ensuring that aggressive online exploration never damages the robotic arm.

**10\. Trajectory Improvement & Reward Learning from Comparative Language Feedback** (2024, CoRL) _Authors/Institution:_ Z. Yang, S. Russell, A.D. Dragan, et al. / UC Berkeley. _Methodology Deep-Dive:_ This framework significantly increases the information density of human feedback by shifting from basic binary rankings to comparative natural language inputs.<sup>55</sup> By learning a shared latent space that perfectly correlates kinematic trajectory data with semantic language feedback, the algorithm translates verbal human corrections (e.g., "move a bit lower and slower") into dense, mathematically rigorous reward manifolds.<sup>55</sup> This allows the robotic arm to iteratively adapt its behavior using standard reinforcement learning, dramatically outperforming traditional RLHF in both time efficiency and user satisfaction.

**11\. Pretraining Proprioceptive Inverse Dynamics for Actor-Critic RL** (2025, arXiv) _Authors/Institution:_ General Robotics Labs. _Methodology Deep-Dive:_ Addressing the sample inefficiency of initiating online RL on physical robots, this framework advocates for warm-starting Proximal Policy Optimization (PPO) using a Proprioceptive Inverse Dynamics Model (PIDM).<sup>64</sup> Using a completely task-agnostic exploration phase to gather fundamental dynamic transition data, the algorithm trains the PIDM via supervised learning to capture the core physical realities of the arm (mass, inertia).<sup>64</sup> The pretrained weights are then injected into both the actor and critic networks, improving online sample efficiency by 40% and immediately stabilizing the fine-tuning process.

**12\. Dynamic Behavior Cloning with Temporal Feature Prediction** (2025, RA-L) _Authors/Institution:_ Y. Zhang, R. Wang, X. Chen / IEEE. _Methodology Deep-Dive:_ To allow static Behavior Cloning policies to adapt online to highly dynamic environments (such as tracking moving targets on a conveyor belt), this research introduces a predictive temporal coding layer.<sup>65</sup> Rather than reacting to delayed visual frames, the network constantly predicts the immediate future latent state of the environment and conditions the frozen base policy on this projected reality.<sup>65</sup> This essentially creates a zero-latency predictive feedback loop, allowing the robotic arm to seamlessly intercept moving objects without requiring massive online retraining.

**13\. Value Iteration for Learning Concurrently Executable Tasks** (2025, AAMAS) _Authors/Institution:_ Sheikh A. Tahmid, Gennaro Notomista. _Methodology Deep-Dive:_ This approach solves the complex problem of aligning robots to execute multiple contradictory tasks simultaneously without succumbing to reward hacking (e.g., maximizing speed while simultaneously minimizing energy).<sup>66</sup> By modifying the Bellman update equation in Value Iteration, the methodology optimizes Q-functions over a synthesized action space that mathematically balances competing physical constraints.<sup>66</sup> This allows the robotic arm to autonomously discover optimal Pareto frontiers during physical interaction without requiring an engineer to continually tweak reward weights.

**14\. RRL for Robotic Assembly Using Visual and Force Information** (2024, J-Manuf-Syst) _Authors/Institution:_ Zhuangzhuang Zhang, Zhinan Zhang, Qixin Cao. _Methodology Deep-Dive:_ This framework achieves extreme precision in tight-clearance robotic peg-in-hole assembly by deploying a dual-stream residual RL network combining disparate sensory modalities.<sup>68</sup> In the physical assembly procedure, a visual-based policy strictly governs the macro-level spatial search, while a high-frequency force-torque policy exclusively handles the micro-level interactive insertion behaviors.<sup>68</sup> This disentangled residual approach exhibits massive sample efficiency online, achieving reliable micro-millimeter precision across diverse geometric parts without explicitly modeling their CAD files.

### TIER 2: SUPPORTING LITERATURE

**Sub-topic 1: Embodied DPO & RLHF Frameworks**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| HomieBot: Embodied Mobile Manipulation with DPO (2025, ICLR) | Aligns continuous navigation and manipulation tasks using unified DPO tuning. | <sup>70</sup> |
| --- | --- | --- |
| Beyond One-Preference-For-All: Multi-Objective DPO (2023, NeurIPS) | Scales DPO to balance competing constraints (e.g., speed vs. safety) in robotics. | <sup>71</sup> |
| --- | --- | --- |
| ConRFT: Reinforced Fine-tuning via Consistency Policy (2025, RSS) | Integrates policy gradients with diffusion to bypass the need for massive offline datasets. | <sup>72</sup> |
| --- | --- | --- |
| SafeDiffuser: Safe Planning with Diffusion Probabilistic Models (2024, ICLR) | Bounds generated trajectories within safety margins using post-hoc reward alignment. | <sup>49</sup> |
| --- | --- | --- |
| VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning (2025, arXiv) | Utilizes verified environmental rewards to safely fine-tune VLA outputs online. | <sup>72</sup> |
| --- | --- | --- |
| BLAZER: LLM Agent with Direct Preference Optimization (2024, CoRL) | Explores negative-example preference pairs to aggressively punish dangerous arm actions. | <sup>73</sup> |
| --- | --- | --- |
| VADER: Video Action Classifiers as Reward Models (2024, arXiv) | Uses off-the-shelf VideoMAE models to provide dense reward signals for RLHF loops. | <sup>74</sup> |
| --- | --- | --- |
| PhyGDPO: Physics-Aware Generation via DPO (2026, Meta AI) | Embeds physics engine collision data directly into the preference contrastive loss. | <sup>72</sup> |
| --- | --- | --- |

**Sub-topic 2: Residual RL & Contact-Rich Alignment**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| ManipTrans: Bimanual Manipulation Transfer via Residual Learning (2025, CVPR) | Employs residuals to correct kinematic discrepancies during dual-arm teleoperation transfer. | <sup>46</sup> |
| --- | --- | --- |
| RRL Based on Inverse Kinematics for Soft Robotic Arms (2025, ASME) | Uses IK solvers as a nominal baseline, letting RL fix complex deformation errors. | <sup>52</sup> |
| --- | --- | --- |
| Accelerating Residual Reinforcement Learning with Uncertainty (2025, arXiv) | Modulates residual injection magnitude based on real-time epistemic uncertainty estimates. | <sup>76</sup> |
| --- | --- | --- |
| ConditionNET: Learning Preconditions and Effects (2024, RA-L) | Trains networks to monitor task execution states before triggering residual corrections. | <sup>40</sup> |
| --- | --- | --- |
| A Novel Safety-Aware Energy Tank Formulation (2024, RA-L) | Uses control barrier functions to mathematically bleed off dangerous residual torques. | <sup>40</sup> |
| --- | --- | --- |
| Tactile-RL for Insertion: Generalization to Unknown Geometry (2021/2024, ICRA) | Replaces visual streams entirely with tactile residual feedback for blind insertions. | <sup>78</sup> |
| --- | --- | --- |
| Proactive Action Visual Residual RL for Contact-Rich Tasks (2021/2024, ICRA) | Uses torque-controlled robots to actively seek contact, learning residuals from the impact. | <sup>78</sup> |
| --- | --- | --- |
| Adaptive Dual-Arm Manipulation with RL and Variable Impedance (2024, arXiv) | Adjusts the stiffness of the robotic arm online to safely absorb unexpected collisions. | <sup>79</sup> |
| --- | --- | --- |

**Sub-topic 3: Actor-Critic & Online Tuning**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| RLinf-VLA: Unified and Efficient Framework for VLA+RL (2025, arXiv) | Streamlines online RL loops by sharing representations between actor and value networks. | <sup>72</sup> |
| --- | --- | --- |
| Steering Diffusion Policy with Latent Space RL (2025, CoRL) | Directs the denoising pathway of a diffusion model dynamically using a learned critic. | <sup>21</sup> |
| --- | --- | --- |
| Behavior-Regularized Diffusion Policy Optimization (2025, ICML) | Constrains the Actor network to the offline dataset distribution during physical exploration. | <sup>33</sup> |
| --- | --- | --- |
| Actor-Critic for Continuous Action Chunks (2024, arXiv) | Optimizes massive action-sequence outputs over long horizons with sparse rewards. | <sup>81</sup> |
| --- | --- | --- |

## STAGE 3: Inference-Time Execution (High-Frequency Control under Constrained Compute)

The final frontier of embodied deployment is raw execution speed. A perfectly aligned, theoretically robust generalized policy is entirely useless if its computational latency results in physical instability. Robotic arms manipulating delicate objects, tracking dynamic targets, or engaging in contact-rich force control require continuous, deterministic feedback loops operating strictly between 20 Hz and 100 Hz.<sup>3</sup> Autoregressive VLAs (which suffer from quadratic sequence scaling and memory-bound KV-cache bottlenecks) and Diffusion models (which require tens to hundreds of iterative denoising steps through complex ODE solvers) inherently fail to meet these real-time physical constraints out-of-the-box.<sup>3</sup>

Stage 3 methodologies tackle this absolute latency wall through three distinct, model-agnostic avenues. **Algorithmic Acceleration**, primarily achieved via _Consistency Distillation_, mathematically maps the multi-step Probability Flow Ordinary Differential Equation (PFODE) of a diffusion model into a direct, single-step mapping. This collapses 50 generation steps into 1 or 2, achieving 10x–100x speedups without losing multi-modal expressivity.<sup>4</sup> **System-Level Optimization** focuses entirely on data flow and hardware utilization, employing advanced Post-Training Quantization (PTQ) to shrink memory bandwidth requirements, alongside dynamic Key-Value (KV) cache management to parallelize and deduplicate autoregressive decoding.<sup>85</sup> Finally, **Efficiency-Driven Architectural Swaps** pioneer the replacement of the quadratic self-attention mechanisms of traditional transformers with selective State Space Models (SSMs), such as _Mamba_. SSMs provide linear-time sequence modeling and strictly bounded memory footprints, making them ideal for the infinite-horizon continuous observation streams fundamental to robotics.<sup>87</sup>

### TIER 1: CORE LITERATURE

**1\. Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation** (2024, RSS) _Authors/Institution:_ Aaditya Prasad, Kevin Lin, Jimmy Wu, Linqi Zhou, Jeannette Bohg / Stanford University. _Methodology Deep-Dive:_ Consistency Policy systematically solves the critical latency bottleneck of robotic Diffusion Policies by aggressively applying the Consistency Trajectory Model (CTM) objective to continuous control tasks.<sup>4</sup> By mathematically enforcing self-consistency between arbitrary temporal points along the continuous diffusion ODE chain, the massive teacher model is distilled into a lightweight student network capable of generating high-dimensional, collision-free action sequences in a single neural forward pass. This algorithmic breakthrough successfully increases physical inference speeds by an order of magnitude—allowing it to run easily on laptop-grade edge GPUs—while maintaining the vital multimodal robustness of the original diffusion teacher.<sup>4</sup>

**2\. ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge** (2025, arXiv) _Authors/Institution:_ Yin et al. / \[Associated with VLA optimization\]. _Methodology Deep-Dive:_ ActionFlow operates purely at the hardware-system architecture level, brilliantly circumventing the need to alter the underlying neural weights of VLAs.<sup>3</sup> It introduces a "Cross-Request Pipelining" scheduler that intelligently batches memory-bound autoregressive decoding phases with highly compute-bound prefill phases, maximizing overall GPU utilization. Combined with a custom Unified KV Ring Buffer and Cross-Request State Packed Forward operators, this hardware-aware memory optimization boosts inference frequency on dense 7B-parameter VLAs by 2.55x, enabling true zero-shot real-time execution on severely constrained edge devices.<sup>3</sup>

**3\. RoboMamba: Efficient Vision-Language-Action Model via State Space Models** (2024, arXiv) _Authors/Institution:_ Jiaming Liu, Mengzhen Liu, et al. / Peking University. _Methodology Deep-Dive:_ RoboMamba structurally revolutionizes embodied models by fundamentally swapping the quadratic-complexity Transformer backbone of standard VLAs with the linear-complexity Mamba (SSM) architecture.<sup>88</sup> By co-training an established vision encoder with the Mamba language model and appending a remarkably lightweight 0.1% parameter policy head, it encodes strong temporal continuity biases without triggering unbounded KV-cache memory explosions.<sup>88</sup> The resulting state-space model achieves inference speeds strictly three times faster than traditional transformer VLAs, maintaining a steady, highly reactive 9.0 Hz physical control frequency even when processing massive visual resolutions.<sup>88</sup>

**4\. CEED-VLA: Consistency Vision-Language-Action Model with Early-Exit Decoding** (2025, arXiv) _Authors/Institution:_ Wenxuan Song, Jiayi Chen, et al. / Zhejiang University. _Methodology Deep-Dive:_ CEED-VLA confronts the sluggishness of traditional token-by-token autoregressive decoding in VLAs by introducing a highly parallelized, non-autoregressive Jacobi-based decoding method supercharged by consistency distillation.<sup>90</sup> The methodology trains the policy network to predict multiple future action tokens simultaneously, enforcing mathematical consistency across parallel iterations to violently suppress error accumulation over time. Crucially, a novel "early-exit" mechanism continuously monitors confidence thresholds, abruptly halting computation the microsecond the action prediction stabilizes, resulting in an enormous 4.1x inference speedup and seamless, high-frequency physical deployment.<sup>91</sup>

**5\. One-Step Diffusion Policy (OneDP)** (2024, ICLR) _Authors/Institution:_ Zifeng Gao, et al. _Methodology Deep-Dive:_ OneDP accelerates robotic diffusion inference by strictly minimizing the reverse Kullback-Leibler (KL) divergence between the distributions of a pre-trained multi-step diffusion teacher and a one-step student generator.<sup>83</sup> By ensuring the heavily distilled distribution faithfully tracks the multi-modal physical behavior of the teacher without requiring explicit numerical ODE solving, OneDP entirely collapses the iterative denoising chain into a single matrix multiplication pass.<sup>83</sup> This model-agnostic mathematical distillation requires minimal extra training cost and radically boosts the action prediction frequency of a Franka robotic arm from an unworkable 1.5 Hz to an industrial-grade 62 Hz.<sup>83</sup>

**6\. VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching** (2025, arXiv) _Authors/Institution:_. _Methodology Deep-Dive:_ Recognizing that high-frequency robotic manipulation exhibits vast temporal redundancy (e.g., static backgrounds or stationary objects across milliseconds), VLA-Cache implements a highly aggressive, dynamic Key-Value (KV) cache pruning and reuse strategy.<sup>86</sup> By computationally identifying and freezing the KV embeddings of static visual tokens across adjacent video frames, the system completely bypasses hundreds of redundant transformer matrix calculations for those spatial regions.<sup>86</sup> This targeted KV-cache retention severely reduces the memory footprint and decoding latency of autoregressive models without sacrificing the micro-spatial accuracy needed for precision manipulation.<sup>86</sup>

**7\. FreqPolicy: Frequency Autoregressive Visuomotor Policy with Continuous Tokens** (2025, NeurIPS) _Authors/Institution:_ Yiming Zhong, Yumeng Liu, et al. _Methodology Deep-Dive:_ FreqPolicy pioneers an entirely novel approach by transforming the action representation space from the standard time domain to the frequency domain (via Discrete Cosine Transform) before executing any neural modeling.<sup>95</sup> It explicitly separates low-frequency global arm movements from high-frequency, contact-rich fine-motor adjustments, modeling them progressively using continuous latent representations and a highly optimized diffusion-based decoder.<sup>95</sup> This architectural restructuring ensures that high-speed, structural temporal variations are generated in parallel rather than sequentially, vastly increasing the execution efficiency (reaching up to 93.5 Hz) while retaining sub-millimeter physical precision.<sup>95</sup>

**8\. ManiFlow: Visuomotor Policy via Consistency Flow Training** (2025, CoRL) _Authors/Institution:_ Ge Yan, Jiyue Zhu, Yuquan Deng, Dieter Fox, et al. _Methodology Deep-Dive:_ ManiFlow bypasses diffusion entirely, opting to optimize a continuous-time flow matching paradigm utilizing a highly efficient transformer architecture (DiT-X) equipped with adaptive cross-attention.<sup>98</sup> By enforcing self-consistency and absolute mathematical straightness on the learned vector flow trajectories, the model maps complex multi-modal observations (RGB, depth, proprioception) to dexterous high-dimensional action spaces in just 1 to 2 inference steps.<sup>98</sup> This eliminates the need for complex multi-stage distillation pipelines, allowing the policy to be trained end-to-end in a single run while maintaining the extreme low-latency response required for humanoid and bimanual operations.

**9\. HBVLA: Pushing 1-Bit Post-Training Quantization for Vision-Language-Action Models** (2026, arXiv) _Authors/Institution:_ Xin Yan et al. _Methodology Deep-Dive:_ Pushing system-level PTQ to its absolute mathematical limits, HBVLA demonstrates that robust physical manipulation is possible even when continuous policy weights are compressed down to discrete 1-bit representations.<sup>100</sup> Utilizing advanced Hessian-augmentation techniques during the offline quantization phase, the algorithm mathematically preserves the curvature and gradient sensitivity of the original massive FP32 network.<sup>100</sup> This prevents the severe, destructive physical oscillations normally caused by extreme low-bit quantization, allowing massive VLAs to run at unprecedented frame rates on highly constrained, embedded robot hardware.

**10\. RetoVLA: Reusing Discarded Register Tokens** (2025, arXiv) _Authors/Institution:_. _Methodology Deep-Dive:_ RetoVLA executes a system-level optimization by scavenging computational byproducts that are traditionally destroyed during transformer execution.<sup>102</sup> Instead of expanding the KV-cache, it captures discarded visual register tokens and dynamically injects them as auxiliary Key-Value pairs specifically into the action-generation experts.<sup>102</sup> This technique drastically augments the cross-attention layers with dense, global spatial context for highly efficient decision-making, significantly boosting the policy's spatial reasoning capabilities without triggering any core computational complexity escalation or memory bloat.

**11\. FlowRAM: Grounding Flow Matching with Region-Aware Mamba** (2025, CVPR) _Authors/Institution:_ Wang et al. _Methodology Deep-Dive:_ FlowRAM represents the vanguard of hybrid architectures, successfully fusing continuous Flow Matching generation with the extreme efficiency of State Space Models.<sup>103</sup> The system utilizes a multimodal Mamba model to process massive, concatenated point-cloud and text tokens simultaneously, leveraging the SSM's selection mechanism to mathematically focus only on key interactive regions and aggressively avoid redundant computations.<sup>103</sup> By parameterizing the deterministic vector field using this lightweight Mamba backbone, it calculates the highly precise flow paths required for manipulation in a fraction of the time required by standard transformers.

### TIER 2: SUPPORTING LITERATURE

**Sub-topic 1: Single-Step & Consistency Distillation Accelerators**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| ManiCM: Real-time 3D Diffusion via Consistency Model (2024, arXiv) | Applies consistency constraints to point-cloud-conditioned action generation. | <sup>5</sup> |
| --- | --- | --- |
| FlowPolicy: Fast and Robust 3D Flow-Based Policy (2025, NeurIPS) | Normalizes velocity field consistency to enable single-step Euler integration. | <sup>72</sup> |
| --- | --- | --- |
| BiKC: Keypose-Conditioned Consistency Policy for Bimanual Tracking (2024, arXiv) | Uses geometric key-poses as anchors to stabilize the consistency distillation process. | <sup>112</sup> |
| --- | --- | --- |
| Two-Steps Diffusion Policy via Genetic Denoising (2025, NeurIPS) | Employs genetic algorithms to prune the denoising timeline down to two discrete jumps. | <sup>80</sup> |
| --- | --- | --- |
| Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling (2024, GitHub) | Embeds highly efficient, single-step symmetry directly into the generative ODE. | <sup>113</sup> |
| --- | --- | --- |
| ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion (2024, GitHub) | Condenses complex 3D rotational generation into rapid trajectory equations. | <sup>113</sup> |
| --- | --- | --- |
| CLOSURE: Fast Quantification of Pose Uncertainty Sets (2024, RSS) | Solves pose uncertainty analytically to bypass slow neural estimation during tracking. | <sup>114</sup> |
| --- | --- | --- |

**Sub-topic 2: System-Level PTQ & KV-Cache Management**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| Q-VLM: Post-training Quantization for Large Vision-Language Models (2024, NeurIPS) | Realigns outlier activation distributions to allow lossless 8-bit weight inference. | <sup>51</sup> |
| --- | --- | --- |
| KV-Efficient VLA (2025, arXiv) | Employs an RNN-gated chunked KV cache to compress attention over long horizons. | <sup>102</sup> |
| --- | --- | --- |
| AirCache: Activating Inter-modal Relevancy KV Cache Compression (2025, ICCV) | Evicts tokens based on multi-modal alignment density rather than sheer time. | <sup>115</sup> |
| --- | --- | --- |
| PTQ for Real-Time Depth Estimation on the Edge (2025, CVPR) | Quantizes spatial reasoning networks for lag-free collision avoidance processing. | <sup>116</sup> |
| --- | --- | --- |
| Quantization Error Propagation: Revisiting Layer-Wise PTQ (2025, NeurIPS) | Maps how integer approximations mathematically cascade through deep VLA layers. | <sup>80</sup> |
| --- | --- | --- |
| Outlier-Aware PTQ for Discrete Graph Diffusion Models (2025, ICML) | Protects structural topological routing from destructive integer rounding errors. | <sup>33</sup> |
| --- | --- | --- |
| DuQuant: Distributing Outliers via Dual Transformation (2024, NeurIPS) | Smoothes activation spikes prior to quantization to preserve edge-case logic. | <sup>107</sup> |
| --- | --- | --- |
| GenPTQ: Green Post-Training Quantization (2025, EMNLP) | Uses mixed-precision bit allocation to dramatically slash energy consumption. | <sup>117</sup> |
| --- | --- | --- |

**Sub-topic 3: Mamba & SSM Architectural Efficiency**

| **Title (Year, Venue)** | **Description** | **Citation** |
| --- | --- | --- |
| DiSPo: Diffusion-SSM based Policy Learning (2024, arXiv) | Modulates Mamba's discretization level dynamically for coarse-to-fine skill generation. | <sup>118</sup> |
| --- | --- | --- |
| Mamba-DQN for High State Transition Environments (2025, MDPI) | Replaces RL encoders with SSMs to embed long-term temporal priors with zero lag. | <sup>119</sup> |
| --- | --- | --- |
| Longhorn: State Space Models are Amortized Online Learners (2025, ICLR) | Proves mathematically that SSMs handle unbounded robotic contexts without memory limits. | <sup>120</sup> |
| --- | --- | --- |
| Vision Mamba: Efficient Visual Representation with Bidirectional SSM (2024, ICML) | Adapts spatial scanning to create lightweight, real-time computer vision encoders. | <sup>121</sup> |
| --- | --- | --- |
| MamKO: Mamba-based Koopman Operator for Predictive Control (2025, ICLR) | Combines linear state spaces with Koopman physics for universal dynamics modeling. | <sup>123</sup> |
| --- | --- | --- |
| PMA: Parameter-Efficient Point Cloud Understanding via Point Mamba (2025, CVPR) | Accelerates 3D voxel tracking natively using linear selection algorithms. | <sup>116</sup> |
| --- | --- | --- |
| UST-SSM: Unified Spatio-Temporal State Space Models (2025, ICCV) | Fuses temporal and spatial coordinates into a singular, highly efficient tracking vector. | <sup>115</sup> |
| --- | --- | --- |
| Efficient Unstructured Pruning of Mamba State-Space Models (2025, EMNLP) | Severs low-value SSM connections to push models onto micro-controllers. | <sup>124</sup> |
| --- | --- | --- |
| MambaTS: Improved Selective State Space Models (2024, arXiv) | Optimizes classical forecasting architectures to predict dynamic obstacle paths instantly. | <sup>125</sup> |
| --- | --- | --- |

## Conclusion

The deployment of Embodied AI on physical robotic arms has firmly transitioned from an era of theoretical architectural exploration into a rigorous, highly mathematical systems-engineering discipline. The 2023–2025 literature reveals that the true bottlenecks to robotic capability are no longer a lack of theoretical generative "intelligence," but rather the practical, immutable realities of morphological variation, physical reality gaps, and hard computational latency thresholds. By categorizing the field strictly through the three stages of the deployment lifecycle, a clear, unified engineering pipeline emerges.

First, massive, over-parameterized off-domain pretraining must be aggressively compressed via Quantization-Aware Training and Policy Distillation (Stage 1) to fit onto physical edge hardware, abstracting away varying physical morphologies into agnostic topologies. Second, the inevitable sim-to-real and dynamic physical discrepancies must be ironed out during actual execution using highly bounded Residual RL and DPO-based alignment (Stage 2), allowing safe, autonomous fine-tuning without the impossible task of human reward engineering. Finally, the raw mathematical execution of these policies must be algorithmically and systematically accelerated at the silicon level (Stage 3)—whether by collapsing iterative diffusion trajectories through Consistency Distillation, dynamically managing GPU KV-Caches to prevent memory fragmentation, or entirely abandoning quadratic attention in favor of the linear scaling of State Space Models like Mamba. Together, these model-agnostic optimization pipelines represent the critical infrastructure required to usher in the era of ubiquitous, real-time embodied robotics.

#### Works cited

1.  Vision-Language-Action Models For Robotics: A Review Towards Real-World Applications, accessed February 25, 2026, https://www.scribd.com/document/944558218/VLA-1
2.  (PDF) Embodied intelligence for robot manipulation: development and challenges, accessed February 25, 2026, https://www.researchgate.net/publication/397167357_Embodied_intelligence_for_robot_manipulation_development_and_challenges
3.  ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge - arXiv, accessed February 25, 2026, https://arxiv.org/pdf/2512.20276
4.  Consistency Policy: Accelerated Visuomotor Policies via ..., accessed February 25, 2026, https://consistency-policy.github.io/
5.  ManiCM: Real-time 3D Diffusion Policy via Consistency Model for Robotic Manipulation, accessed February 25, 2026, https://arxiv.org/html/2406.01586v3
6.  Morphology-Agnostic Control in Robotics - Emergent Mind, accessed February 25, 2026, https://www.emergentmind.com/topics/morphology-agnostic-control-framework
7.  Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control - arXiv, accessed February 25, 2026, https://arxiv.org/html/2505.15304v1
8.  RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning, accessed February 25, 2026, https://generalist-distillation.github.io/
9.  A Survey on Efficient Vision-Language-Action Models - arXiv, accessed February 25, 2026, https://arxiv.org/html/2510.24795v1
10. Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control - CVF Open Access, accessed February 25, 2026, https://openaccess.thecvf.com/content/ICCV2025/papers/Park_Saliency-Aware_Quantized_Imitation_Learning_for_Efficient_Robotic_Control_ICCV_2025_paper.pdf
11. Machine-Learning Based Algorithms for Robotic Navigation and Perception - Politecnico di Torino, accessed February 25, 2026, https://iris.polito.it/retrieve/7c4c11c3-6bc4-4f22-832b-e24cabec2fe4/salvetti_thesis_final.pdf
12. Quantization-Aware Training: Empowering efficient AI on edge devices | qat - Wandb, accessed February 25, 2026, https://wandb.ai/onlineinference/qat/reports/Quantization-Aware-Training-Empowering-efficient-AI-on-edge-devices--VmlldzoxMTcyOTEwMA
13. What is Quantization Aware Training? - IBM, accessed February 25, 2026, https://www.ibm.com/think/topics/quantization-aware-training
14. Learning Non-prehensile Manipulation with Force and Vision Feedback Using Optimization-based Demonstrations, accessed February 25, 2026, https://www.merl.com/publications/docs/TR2026-011.pdf
15. GCNT: Graph-Based Transformer Policies for Morphology-Agnostic Reinforcement Learning, accessed February 25, 2026, https://arxiv.org/html/2505.15211v1
16. RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning, accessed February 25, 2026, https://www.roboticsproceedings.org/rss21/p028.pdf
17. RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning - ResearchGate, accessed February 25, 2026, https://www.researchgate.net/publication/387078509_RLDG_Robotic_Generalist_Policy_Distillation_via_Reinforcement_Learning
18. Transic: Sim-to-Real Policy Transfer by Learning from Online Correction - arXiv.org, accessed February 25, 2026, https://arxiv.org/html/2405.10315v1
19. TRANSIC | Sim-to-Real Policy Transfer by Learning from Online Correction, accessed February 25, 2026, https://transic-robot.github.io/
20. Saliency-Aware Quantized Imitation Learning for Efficient Robotic ..., accessed February 25, 2026, https://openaccess.thecvf.com/content/ICCV2025/html/Park_Saliency-Aware_Quantized_Imitation_Learning_for_Efficient_Robotic_Control_ICCV_2025_paper.html
21. Abhishek Gupta - UW, accessed February 25, 2026, https://homes.cs.washington.edu/~abhgupta/
22. Quantization-Aware Imitation-Learning for Resource-Efficient Robotic Control - arXiv.org, accessed February 25, 2026, https://arxiv.org/html/2412.01034v1
23. Daniel Seita, accessed February 25, 2026, https://danielseita.github.io/data/Daniel_Seita_CV.pdf
24. Combining Teacher-Augmented Policy Gradient Learning with Instance Segmentation to Grasp Arbitrary Objects - arXiv.org, accessed February 25, 2026, https://arxiv.org/html/2403.10187v1
25. Accelerated co-design of robots through morphological pretraining - arXiv, accessed February 25, 2026, https://arxiv.org/html/2502.10862v1
26. State Revisit and Re-explore: Bridging Sim-to-Real Gaps in Offline-and-Online Reinforcement Learning with An Imperfect Simulator | IJCAI, accessed February 25, 2026, https://www.ijcai.org/proceedings/2025/970
27. Robotics Mar 2025 - arXiv, accessed February 25, 2026, https://www.arxiv.org/list/cs.RO/2025-03?skip=275&show=2000
28. Deep Learning for Dexterous Robot Grasping, accessed February 25, 2026, https://kunalaneja.com/survey_paper.pdf
29. Computer Science Jun 2024 - arXiv, accessed February 25, 2026, http://arxiv.org/list/cs/2024-06?skip=2090&show=2000
30. Accepted Main Conference Papers - ACL 2025, accessed February 25, 2026, https://2025.aclweb.org/program/main_papers/
31. A Comprehensive Study on Quantization Techniques for Large Language Models - arXiv, accessed February 25, 2026, https://arxiv.org/html/2411.02530v1
32. Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey, accessed February 25, 2026, https://arxiv.org/html/2508.13073v1
33. ICML 2025 Papers, accessed February 25, 2026, https://icml.cc/virtual/2025/papers.html
34. List of Accepted Papers - IEEE NER 2025 || San Diego, California, USA || 11-14 November 2025, accessed February 25, 2026, https://cmsworkshops.com/NER2025/papers/accepted_papers.php
35. LLM-QAT: Data-Free Quantization Aware Training for Large Language Models, accessed February 25, 2026, https://www.researchgate.net/publication/384207258_LLM-QAT_Data-Free_Quantization_Aware_Training_for_Large_Language_Models
36. Knowledge Integrity in Large Language Models: A State-of-The-Art Review - MDPI, accessed February 25, 2026, https://www.mdpi.com/2078-2489/16/12/1076
37. The 14th International Joint Conference on Natural Language Processing & The 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics - ACL Anthology, accessed February 25, 2026, https://aclanthology.org/events/ijcnlp-2025/
38. Learning under Quantization for High-Dimensional Linear Regression - arXiv, accessed February 25, 2026, https://www.arxiv.org/pdf/2510.18259
39. A Multi-Step Grasping Framework for Zero-Shot Object Detection in Everyday Environments Based on Lightweight Foundational General Models - PMC, accessed February 25, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC12694047/
40. Dongheui Lee | TU Wien, accessed February 25, 2026, https://www.tuwien.at/en/etit/ict/asl/team/dongheui-lee
41. Robotics Mar 2025 - arXiv, accessed February 25, 2026, https://www.arxiv.org/list/cs.RO/2025-03?skip=175&show=500
42. Training Sim-to-Real Transferable Robotic Assembly Skills over Diverse Geometries, accessed February 25, 2026, https://developer.nvidia.com/blog/training-sim-to-real-transferable-robotic-assembly-skills-over-diverse-geometries/
43. Publications - Interactive Perception and Robot Learning Lab, accessed February 25, 2026, https://iprl.stanford.edu/publications
44. Learning Diffusion Policies for Robotic Manipulation of Timber Joinery under Fabrication Uncertainty - arXiv, accessed February 25, 2026, https://arxiv.org/html/2511.17774v2
45. Pure Vision Language Action (VLA) Models: A Comprehensive Survey - arXiv, accessed February 25, 2026, https://arxiv.org/html/2509.19012v1
46. ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning - CVF Open Access, accessed February 25, 2026, https://openaccess.thecvf.com/content/CVPR2025/papers/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.pdf
47. Foundation Models in Autonomous Driving: A Review of Current Tasks and Applications - IEEE Xplore, accessed February 25, 2026, https://ieeexplore.ieee.org/iel8/8784355/10847631/11251045.pdf
48. ROBOMONSTER: COMPOSITIONAL GENERALIZATION OF HETEROGENEOUS EMBODIED AGENTS - OpenReview, accessed February 25, 2026, https://openreview.net/pdf/2aeacc6b15e068c9720861728ad4611b5b5706b1.pdf
49. YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. - GitHub, accessed February 25, 2026, https://github.com/YanjieZe/Paper-List
50. The duality of generative AI and reinforcement learning in robotics, accessed February 25, 2026, https://boa.unimib.it/retrieve/3cb28412-4d7f-4541-aa86-5c8a76c361b5/Moroncelli-2026-Information%20Fusion-VoR.pdf
51. AutoQVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization, accessed February 25, 2026, https://openreview.net/forum?id=TpL2nXanru
52. Residual Reinforcement Learning Based on Inverse Kinematic Modeling for Soft Robotic Arm Control - ASME Digital Collection, accessed February 25, 2026, https://asmedigitalcollection.asme.org/dynamicsystems/article-pdf/147/6/061007/7512473/ds-24-1244.pdf
53. From Imitation to Refinement—Residual RL for Precise Assembly, accessed February 25, 2026, https://residual-assembly.github.io/
54. Deep Reinforcement Learning for Robotic Bipedal Locomotion: A Brief Survey - arXiv, accessed February 25, 2026, https://arxiv.org/html/2404.17070v5
55. Trajectory Improvement and Reward Learning from Comparative Language Feedback - USC Lira Lab - University of Southern California, accessed February 25, 2026, https://liralab.usc.edu/comparative-language-feedback/static/pdfs/paper.pdf
56. DIPPER: Direct Preference Optimization to Accelerate Primitive-Enabled Hierarchical Reinforcement Learning - arXiv, accessed February 25, 2026, https://arxiv.org/html/2406.10892v1
57. NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards - arXiv, accessed February 25, 2026, https://arxiv.org/html/2511.14659v1
58. Navonil Majumder's research while affiliated with Singapore University of Technology and Design and other places - ResearchGate, accessed February 25, 2026, https://www.researchgate.net/scientific-contributions/Navonil-Majumder-2125933286
59. Self-Improving Vision-Language-Action Models with Data Generation via Residual RL, accessed February 25, 2026, https://arxiv.org/html/2511.00091v1
60. Scott Niekum's research works | University of Massachusetts Amherst and other places, accessed February 25, 2026, https://www.researchgate.net/scientific-contributions/Scott-Niekum-70719686
61. Actor-Critic Model Predictive Control: Differentiable Optimization meets Reinforcement Learning for Agile Flight - Robotics and Perception Group, accessed February 25, 2026, https://rpg.ifi.uzh.ch/docs/TRO25_ACMPC_Romero.pdf
62. Dongheui Lee - DBLP, accessed February 25, 2026, https://dblp.org/pid/96/5115
63. Anca Dragan - People @EECS, accessed February 25, 2026, https://people.eecs.berkeley.edu/~anca/publications.html
64. Pretraining in Actor-Critic Reinforcement Learning for Robot Motion Control - arXiv, accessed February 25, 2026, https://arxiv.org/html/2510.12363v1
65. Temporal Action Selection for Action Chunking - arXiv.org, accessed February 25, 2026, https://arxiv.org/pdf/2511.04421
66. Robotics Apr 2025 - arXiv, accessed February 25, 2026, https://www.arxiv.org/list/cs.RO/2025-04?skip=25&show=1000
67. Computer Science Sep 2024 - arXiv, accessed February 25, 2026, http://arxiv.org/list/cs/2024-09?skip=4700&show=2000
68. InsertionNet - A Scalable Solution for Insertion - ResearchGate, accessed February 25, 2026, https://www.researchgate.net/publication/355404126_InsertionNet_-_A_Scalable_Solution_for_Insertion
69. Knowledge-guided robot learning on compliance control for robotic assembly task with predictive model | Request PDF - ResearchGate, accessed February 25, 2026, https://www.researchgate.net/publication/372630418_Knowledge-guided_robot_learning_on_compliance_control_for_robotic_assembly_task_with_predictive_model
70. EMMOE: A Comprehensive Benchmark for Embodied Mobile Manipulation in Open Environments | OpenReview, accessed February 25, 2026, https://openreview.net/forum?id=wSyExS00Wp
71. Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning - NIPS, accessed February 25, 2026, https://proceedings.neurips.cc/paper_files/paper/2024/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf
72. keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models. - GitHub, accessed February 25, 2026, https://github.com/keon/awesome-physical-ai
73. BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation, accessed February 25, 2026, https://arxiv.org/html/2510.08572v1
74. Exploration for Continually Improving Robots, accessed February 25, 2026, https://www.ri.cmu.edu/app/uploads/2024/09/rmendonc_phd_ri_2024_compressed.pdf
75. Residual Reinforcement Learning Based on Inverse Kinematic Modeling for Soft Robotic Arm Control - ASME Digital Collection, accessed February 25, 2026, https://asmedigitalcollection.asme.org/dynamicsystems/article/147/6/061007/1218731/Residual-Reinforcement-Learning-Based-on-Inverse
76. Artificial Intelligence Jun 2025 - arXiv, accessed February 25, 2026, https://www.arxiv.org/list/cs.AI/2025-06?skip=2700&show=2000
77. Michael J. Black - Max Planck Institute for Intelligent Systems, accessed February 25, 2026, https://files.is.tue.mpg.de/black/resume.pdf
78. Learning latent causal factors from the intricate sensor feedback of contact-rich robotic assembly tasks - ResearchGate, accessed February 25, 2026, https://www.researchgate.net/publication/387618286_Learning_latent_causal_factors_from_the_intricate_sensor_feedback_of_contact-rich_robotic_assembly_tasks
79. Winston-Gu/Paper-List: My research papers reading list. Animation and Robotics. - GitHub, accessed February 25, 2026, https://github.com/Winston-Gu/Paper-List
80. NeurIPS 2025 Papers, accessed February 25, 2026, https://neurips.cc/virtual/2025/papers.html
81. Actor-Critic for Continuous Action Chunks: A Reinforcement Learning Framework for Long-Horizon Robotic Manipulation with Sparse Reward - ResearchGate, accessed February 25, 2026, https://www.researchgate.net/publication/394524711_Actor-Critic_for_Continuous_Action_Chunks_A_Reinforcement_Learning_Framework_for_Long-Horizon_Robotic_Manipulation_with_Sparse_Reward
82. NeurIPS 2023 Papers, accessed February 25, 2026, https://neurips.cc/virtual/2023/papers.html
83. One-Step Diffusion Policy: Fast Visuomotor Policies via Diffusion Distillation | OpenReview, accessed February 25, 2026, https://openreview.net/forum?id=Z85EoYQhCs
84. Consistency Policy - Robotics, accessed February 25, 2026, https://www.roboticsproceedings.org/rss20/p071.pdf
85. NeurIPS 2024 Spotlight Posters, accessed February 25, 2026, https://neurips.cc/virtual/2024/events/spotlight-posters-2024
86. VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching - OpenReview, accessed February 25, 2026, https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf
87. Mamba Model: Scalable SSM Architecture - Emergent Mind, accessed February 25, 2026, https://www.emergentmind.com/topics/mamba-model
88. RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation - arXiv, accessed February 25, 2026, https://arxiv.org/html/2406.04339v2
89. RoboMamba: Efficient Vision-Language-Action Model for Robotic ..., accessed February 25, 2026, https://openreview.net/forum?id=JxOQeg1NkH
90. CEED-VLA: Consistency Vision-Language-Action Model with Early-Exit Decoding - arXiv, accessed February 25, 2026, https://arxiv.org/abs/2506.13725
91. Daily Papers - Hugging Face, accessed February 25, 2026, [https://huggingface.co/papers?q=Vision-Language-Action%20(VLA)](https://huggingface.co/papers?q=Vision-Language-Action+%28VLA%29)
92. CEED-VLA: Consistency Vision-Language-Action Model with Early-Exit Decoding, accessed February 25, 2026, https://arxiv.org/html/2506.13725v1
93. ICML Poster One-Step Diffusion Policy: Fast Visuomotor Policies via Diffusion Distillation, accessed February 25, 2026, https://icml.cc/virtual/2025/poster/45971
94. (PDF) VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation - ResearchGate, accessed February 25, 2026, https://www.researchgate.net/publication/388685612_VLA-Cache_Towards_Efficient_Vision-Language-Action_Model_via_Adaptive_Token_Caching_in_Robotic_Manipulation
95. FreqPolicy: Frequency Autoregressive Visuomotor Policy with Continuous Tokens - arXiv, accessed February 25, 2026, https://arxiv.org/html/2506.01583v1
96. FreqPolicy: Frequency Autoregressive Visuomotor Policy with Continuous Tokens - NeurIPS, accessed February 25, 2026, https://neurips.cc/virtual/2025/poster/118407
97. FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency, accessed February 25, 2026, [https://openreview.net/forum?id=NKNryrCGYn&referrer=%5Bthe%20profile%20of%20Ning%20Liu%5D(%2Fprofile%3Fid%3D~Ning_Liu4)](https://openreview.net/forum?id=NKNryrCGYn&referrer=%5Bthe+profile+of+Ning+Liu%5D%28/profile?id%3D~Ning_Liu4%29)
98. ManiFlow: A General Robot Manipulation Policy via Consistency Flow Training - arXiv, accessed February 25, 2026, https://arxiv.org/html/2509.01819v1
99. Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition - arXiv, accessed February 25, 2026, https://arxiv.org/html/2510.01068v1
100.HBVLA: Pushing 1-Bit Post-Training Quantization for Vision-Language-Action Models - arXiv, accessed February 25, 2026, https://arxiv.org/html/2602.13710v1
101.BaiShuanghao/my_arXiv_daily - GitHub, accessed February 25, 2026, https://github.com/BaiShuanghao/my_arXiv_daily
102.A Survey on Efficient Vision-Language-Action Models - arXiv, accessed February 25, 2026, https://arxiv.org/html/2510.24795v2
103.FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation - CVF Open Access, accessed February 25, 2026, https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_FlowRAM_Grounding_Flow_Matching_Policy_with_Region-Aware_Mamba_Framework_for_CVPR_2025_paper.pdf
104.Songwxuan/Embodied-AI-Paper-TopConf - GitHub, accessed February 25, 2026, https://github.com/Songwxuan/Embodied-AI-Paper-TopConf
105.Daily Papers - Hugging Face, accessed February 25, 2026, [https://huggingface.co/papers?q=efficient%20inference](https://huggingface.co/papers?q=efficient+inference)
106.Cornell Researchers Introduce QTIP: A Weight-Only Post-Training Quantization Algorithm that Achieves State-of-the-Art Results through the Use of Trellis-Coded Quantization (TCQ) - MarkTechPost, accessed February 25, 2026, https://www.marktechpost.com/2024/11/02/cornell-researchers-introduce-qtip-a-weight-only-post-training-quantization-algorithm-that-achieves-state-of-the-art-results-through-the-use-of-trellis-coded-quantization-tcq/
107.NeurIPS 2024 Papers, accessed February 25, 2026, https://nips.cc/virtual/2024/papers.html
108.Computer Science Feb 2025 - arXiv, accessed February 25, 2026, https://www.arxiv.org/list/cs/2025-02?skip=8775&show=2000
109.\[2503.09641\] SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation - arXiv, accessed February 25, 2026, https://arxiv.org/abs/2503.09641
110.SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation - CVF Open Access, accessed February 25, 2026, https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_SANA-Sprint_One-Step_Diffusion_with_Continuous-Time_Consistency_Distillation_ICCV_2025_paper.pdf
111.\[2406.01586\] ManiCM: Real-time 3D Diffusion Policy via Consistency Model for Robotic Manipulation - arXiv, accessed February 25, 2026, https://arxiv.org/abs/2406.01586
112.Generative Artificial Intelligence in Robotic Manipulation: A Survey - arXiv, accessed February 25, 2026, https://arxiv.org/html/2503.03464v1
113.showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. - GitHub, accessed February 25, 2026, https://github.com/showlab/Awesome-Robotics-Diffusion
114.Accepted Papers · Robotics: Science and Systems, accessed February 25, 2026, https://roboticsconference.org/2024/program/papers/
115.ICCV 2025 Accepted Papers, accessed February 25, 2026, https://iccv.thecvf.com/Conferences/2025/AcceptedPapers
116.CVPR 2025 Accepted Papers, accessed February 25, 2026, https://cvpr.thecvf.com/Conferences/2025/AcceptedPapers
117.Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology, accessed February 25, 2026, https://aclanthology.org/2025.findings-emnlp.0.pdf
118.DiSPo: Diffusion-SSM based Policy Learning for Coarse-to-Fine Action Discretization - arXiv, accessed February 25, 2026, https://arxiv.org/html/2409.14719v2
119.Latent Mamba-DQN: Improving Temporal Dependency Modeling in Deep Q-Learning via Selective State Summarization - MDPI, accessed February 25, 2026, https://www.mdpi.com/2076-3417/15/16/8956
120.cv - UT Austin Computer Science, accessed February 25, 2026, https://www.cs.utexas.edu/~pstone/cv/cv.html
121.CVPR Poster FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation, accessed February 25, 2026, https://cvpr.thecvf.com/virtual/2025/poster/33579
122.MambaFlow: A Novel and Flow-guided State Space Model for Scene Flow Estimation - arXiv, accessed February 25, 2026, https://arxiv.org/html/2502.16907v1
123.ICLR 2025 Papers, accessed February 25, 2026, https://iclr.cc/virtual/2025/papers.html
124.Computer Vision and Pattern Recognition May 2025 - arXiv, accessed February 25, 2026, https://www.arxiv.org/list/cs.CV/2025-05?skip=2125&show=1000
125.yyyujintang/Awesome-Mamba-Papers - GitHub, accessed February 25, 2026, https://github.com/yyyujintang/Awesome-Mamba-Papers