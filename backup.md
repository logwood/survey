Chapter 2 defines the embodied interfaces and constraints of manipulation systems; 
Chapter 3 reinterprets datasets as executable, temporally structured traces of embodied behavior; 
Chapter 4 then asks how such traces can be generated, composed, and scaled automatically.

Embodiment Foundations of Robotic arms: System Architecture
Data Ecosystem for Robotic arms: Data Support
Learning Paradigms for Robotic arms: Methodological Frameworks


The sensing stack plays a major role in whether contact-rich control can remain closed loop. Eye-in-hand vision resolves object geometry before contact, but it provides only indirect information about force, slip, and local deformation once contact occurs. 
Tactile sensing fills this gap: vision-based tactile sensors such as GelSight~\cite{zhao2023gelsightsveltehumanfingershaped} and DIGIT convert contact geometry into images, while force- and vibration-sensitive sensors such as BioTac provide signals for slip detection and contact regulation. 
In practice, visuo-tactile integration matters most in insertion, re-grasping, and fragile-object handling, where task-relevant feedback comes primarily from contact state.
