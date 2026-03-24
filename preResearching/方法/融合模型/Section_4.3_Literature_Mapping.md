# Section 4.3: Unified Foundation Models - Literature Mapping

This document maps the literature from the provided list of 329 papers to the specific subsections of Section 4.3, focusing on expanding the literature mapping for Type I, Type II, and Type III VLAs. It also explicitly lists which papers are categorized into other sections of the survey.

## 4.3.1 Type I: Unified End-to-End Foundation Models
**Core Definition:** Monolithic architectures that map multi-modal inputs (vision, language, proprioception) directly to low-level robot actions without intermediate symbolic or spatial representations.

### Included Literature (Expanded):
*   **Pioneering Architectures & Scaling:**
    *   `RT-2` (1), `RT-2-X` (2), `OpenVLA` (4), `GR00T N1` (8), `RDT-1B` (11), `RoboFlamingo` (13), `Gemini Robotics 1.5` (15), `RFM-1` (16), `Skild Brain` (17), `Vayu VLA` (18), `UniVLA` (19), `RoboVLMs` (321), `InternVLA-A1` (322), `WALL-OSS` (323), `UniAct` (329), `Helix` (320)
*   **Action Representation & Generative Paradigms:**
    *   `Pi-Zero` (6), `RoboMamba` (9), `Instruct2Act` (14), `VQ-VLA` (30), `F1-VLA` (37), `HybridVLA` (40), `Continuous Parallel Decoding` (113), `Action Space Design` (314)
*   **Efficiency & Lightweight Deployment:**
    *   `TinyVLA` (10), `BitVLA` (20), `SmolVLA` (21), `Edge VLA` (31, 109), `NORA` (35), `Evo-1` (36), `MoLe-VLA` (39, 111), `DeeR-VLA` (101), `FAST` (102), `VLA-Cache` (103), `RTC` (104), `VOTE` (106), `VLA-RAIL` (107), `OpenVLA-OFT` (108), `Knowledge Insulating VLA` (110), `Quantized OpenVLA` (114), `BAKU` (117), `VLA-Adapter` (325)
*   **Enhanced Modalities & Task Alignment:**
    *   `Prismatic VLMs` (23), `Transic` (25), `MDT` (26), `BridgeVLA` (34), `Distilled Feature Fields` (115), `Theia` (116), `Mobile ALOHA` (118), `ALOHA Unleashed` (119), `Robot Fine-Tuning Made Easy` (120), `ReconVLA` (229, 324), `RGB-D BitVLA` (266), `BFA` (267), `Interleave-VLA` (268), `Feature-Constraint` (294), `Task Adaptation of VLA` (301), `STEER` (306), `Local Policies Enable Zero-Shot` (308), `OPEN TEACH` (309), `SuSIE` (326), `VLAS` (327)

---

## 4.3.2 Type II: Hierarchical/Modular Models
**Core Definition:** Models that explicitly decouple high-level semantic reasoning (the "Brain") from low-level continuous execution (the "Policy"). Often involves Chain-of-Thought, intermediate planning, or dual-system architectures.

### Included Literature (Expanded):
*   **Chain-of-Thought & Reasoning in VLAs:**
    *   `ECoT` (41), `CoT-VLA` (42), `ThinkAct` (43), `GraphCoT-VLA` (45), `PromptCoT` (56), `CoA-VLA` (57), `ManualVLA` (58), `Cosmos-Reason1` (248), `RAD` (249), `CiteAgent` (303)
*   **Dual-System & Hierarchical Architectures:**
    *   `RT-H` (32), `Fast-in-Slow (FiS)` (44, 112), `Maestro` (49), `HAMSTER` (53), `RoBridge` (59), `Embodied-Reasoner` (60), `RoboBrain` (61), `A0` (62), `From Seeing to Doing` (63), `Generative Skill Chaining` (64), `Intent-Aware Planning` (274), `Sequence-Based Plan Feasibility` (280), `iPlanner` (283), `Broadcasting Support Relations` (291), `Octopi` (293)
*   **Adaptive Reasoning, Safety & Task Switching:**
    *   `Onetwovla` (38), `AutoVLA` (68, 167), `AlphaDrive` (69, 166), `SwitchVLA` (158), `ControlVLA` (159), `PALO` (251), `AEGIS` (258), `SC-VLA` (259), `RuleFuser` (260), `ATACOM` (261), `Deception Game` (262), `Lyapunov-Stable Neural Control` (263)

---

## 4.3.3 Type III: Spatial/World Models
**Core Definition:** Models that explicitly incorporate 3D spatial awareness, geometric priors, or predictive world models to ground actions in physical reality.

### Included Literature (Expanded):

*   **3D & Spatial VLAs:**
    *   `3D-VLA` (71), `SpatialVLA` (72), `ForceVLA` (74), `Tactile-VLA` (75), `3D-ViTac` (76), `AnySkin` (77, 238), `PolyTouch` (78), `PointVLA` (80), `GenDP` (83), `PhysTwin` (84), `PhysDreamer` (85), `Neural Jacobian Fields` (86), `FoundationPose` (87), `LERF-TOGO` (88), `EquiGraspFlow` (94, 208), `3D Diffuser Actor` (95, 209), `RoboTracer` (96), `RoboRefer` (97), `3DAffordSplat` (98), `SeqAfford` (99), `GEAL` (100), `CubicVLA` (202), `TraceVLA` (231), `TrackVLA` (232), `EndoVLA` (233), `Moto` (234), `Dita` (235), `LaVA-Man` (237), `Symmetry-Aware Generative Modeling` (239), `TrackPGD` (240), `xRAG` (241), `ENAT` (242), `Humanoid Locomotion as Next Token` (243), `Trajectory Flow Matching` (244), `SGFormer` (245), `ConceptFactory` (246), `DiffuseBot` (247), `VLM-Grounder` (250), `OWG` (252), `Body Transformer` (253), `Gameplay Filters` (254), `RP1M` (255), `Learning to Walk from 3 Minutes` (256), `An Open-Source Soft Robotic Platform` (257), `ManiWAV` (264), `Audio-Visual Traffic Light Detection` (265), `Diff-LfD` (269), `On the Utility of Koopman Operator` (270), `HANDLOOM` (271), `Stabilize to Act` (272), `Language-Guided Traffic Simulation` (273), `DATT` (275), `Robot Parkour Learning` (276), `InstaLoc` (277), `HDVIO` (278), `CoDEPS` (279), `Reachability-based Trajectory Design` (281), `Progressive Learning` (282), `RFUniverse` (284), `CLOSURE` (286), `Stein Variational Ergodic Search` (287), `Parallel and Proximal LQR` (288), `Differentiable Robust MPC` (289), `Computation-Aware Learning` (290), `An Abstract Theory of Sensor Eventification` (292), `Neural MP` (310), `ClearDepth` (311), `Blox-Net` (312), `Sampling-Based MPC` (313), `LucidSim` (315), `D3RoMa` (316), `Dynamic 3D Gaussian Tracking` (317), `Object-Centric Dexterous Manipulation` (318), `Learning Robotic Locomotion Affordances` (319), `MolmoAct` (328)
*   **World Models & Video Prediction:**
    UniSim:Learning Interactive Real-World Simulators
    RoboDreamer: Learning Compositional World Models for Robot Imagination
    *   `VideoVLA` (27), `Unified World Models` (28), `Unified Video Action Model` (29, 132), `RT-Sketch` (33), `DINO-WM` (89), `Gen2Act` (121), `Dreamitate` (122), `Video Prediction Policy (VPP)` (123), `FLIP` (124), `GEVRM` (125), `VidMan` (131), `SplatSim` (133, 304), `AVDC` (134), `Dream2Real` (139), `SpawnNet` (140), `Embodied VideoAgent` (236), `GWM` (296), `DyWA` (297), `Diffusion-Based Imaginative Coordination` (298), `Learning 4D Embodied World Models` (299), `Generalist Robot Manipulation beyond Action Labeled Data` (300), `Residual Semantic Steering (RSS)` (302)

---


## 4.4 Type IV: Hybrid Symbolic-Sensorimotor Models
**Core Definition:** Models that integrate explicit symbolic reasoning (e.g., logic, program synthesis)
safevla is categorized  model due to its focus on safety and adaptive reasoning, which aligns with the characteristics of hierarchical/modular architectures that decouple high-level reasoning from low-level execution.
simpleVLA-RL is categorized into the policy/RL section (Section 4.2.2) because it focuses on reinforcement learning and policy optimization, which are central themes in that section.


## 4.3.4 Other Sections (Excluded from 4.3)

The remaining papers from the 329 list are categorized into other sections of the survey:

*   **Brain/Planners (Section 4.2.1):** `PaLM-E` (3), `SayPlan` (46), `VoxPoser` (47), `ViLa` (48), `Code-as-Policies` (50), `LLM+P` (51), `ReAct` (52), `Robots That Ask For Help` (54), `ConceptFusion` (65), `LEO Agent` (66), `Grounded Decoding` (67)
*   **Policy/RL (Section 4.2.2):** `Octo` (5), `Q-Transformer` (12), `PoliFormer` (55), `Consistency Policy` (105)
*   **Data Generation & Simulation (Section 4.1):** `LAPA` (22, 137), `LLaRA` (24), `HoloDeck` (90), `ManiSkill3` (91), `PhyScene` (92), `EmbodiedScan` (93), `UniSim` (126), `MimicPlay` (127), `ZeroMimic` (128), `RoboAct-CLIP` (129), `HOP` (130), `EgoVLA` (135), `Hand-VLA` (136), `Slot-Level Robotic Placement` (138), `RoboCrowd` (305), `SkillGen` (307)
*   **RL & Post-Training (Category F):** `VLA-RL` (141), `RLinf-VLA` (142), `VLA-RFT` (143), `ConRFT` (144), `APO` (145), `Embodied-R1` (146), `GRAPE` (147), `ReWiND` (148), `DigiRL` (149), `POLICEd RL` (150), `POLITE` (151), `RLDG` (152), `STARE-VLA` (153), `Safe-GIL` (154), `Stability-Aware PI2` (155), `Yell At Your Robot` (156), `KitchenVLA` (157), `Stable-BC` (160)
*   **Autonomous Driving & Mobility (Category G):** `DriveVLM` (161), `Alpamayo 1` (162), `CoVLA` (163), `EMMA` (164), `VLM-E2E` (165), `ReCogDrive` (168), `RAG-Driver` (169), `LaMPilot` (170), `Mobility VLA` (171), `ViNT` (172), `GNM` (173), `Uni-NaVid` (174), `NaVILA` (175), `GOAT` (176), `HomeRobot` (177), `Bumble` (178), `MoManipVLA` (179), `MoTo` (180), `SafeVL` (181), `SHRED` (182), `RegNav` (183), `VLPG-Nav` (184), `MapExRL` (185)
*   **Dexterous Hand & Embodiments (Category H):** `HumanPlus` (186), `OKAMI` (187), `DexVLA` (188), `DexGraspVLA` (189), `METIS` (190), `Dex1B` (191), `DexGraspNet 2.0` (192), `UniFucGrasp` (193), `LEAP Hand` (194), `ROSE` (195), `Vegetable Peeling` (196), `Twisting Lids Off` (197), `Tool-as-Interface` (198), `AnyPlace` (199), `MOKA` (200), `AutoMate` (201), `HumanoidBench` (203), `Expressive Whole-Body Control` (204), `ASAP` (205), `Robot Utility Models` (206), `ScissorBot` (207), `Touch2Touch` (210)
*   **Generalization & Benchmarks (Category I):** `Behavior-1K` (211), `HomeSafeBench` (212), `OpenEQA` (213), `RoboCerebra` (214), `SIMPLER` (215), `FetchBench` (216), `LIBERO` (217), `CALVIN` (218), `RoboArena` (219), `Winoground for Robotics` (220), `FurnitureBench` (221), `Colibri5` (222), `MAC-VO` (223), `Caging in Time` (224), `OmniManip` (225), `KUDA` (226), `A3VLM` (227), `SoFar` (228), `LLM2CLIP` (230), `Arena-Web` (285)