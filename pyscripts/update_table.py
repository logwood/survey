import re

file_path = r"c:\Users\ASUS\Desktop\ACM_Computing_Draft\survey.tex"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

replacements = {
    "RT-2": r"Real: Google Robot (700+ tasks)",
    "$\\pi$0": r"Real: ALOHA, UR5 (Dexterous)",
    "RoboVLMs": r"Sim: CALVIN (ABC$\rightarrow$D)",
    "OpenVLA": r"Real: Franka, WidowX (Bridge/OXE)",
    "UniVLA": r"Sim: LIBERO (95.5\%) | Real: Franka",
    "NORA-1.5": r"Sim: SimplerEnv, LIBERO",
    "Interleave-VLA": r"Real: Franka (Zero-shot OOD)",
    "RDT-2": r"Real: ALOHA (Zero-shot Bimanual)",
    "ReconVLA": r"Sim: CALVIN (ABCD$\rightarrow$D) | Real: PiPer",
    "RT-H": r"Real: Google Robot (Lang Correction)",
    "OK-Robot": r"Real: Stretch (10 homes, 82\% SR)",
    "CoT-VLA": r"Real: Franka (Long-horizon)",
    "ThinkAct": r"Sim: CALVIN | Real: Franka",
    "FiS-VLA": r"Real: Franka (117Hz real-time)",
    "HAMSTER": r"Real: Diverse (Cross-morphology)",
    "Hi Robot": r"Real: Diverse (+40\% intent align)",
    "GO-1": r"Real: AgiBot (Bimanual)",
    "GR00T~N1": r"Sim: Isaac Sim | Real: Humanoids",
    "GR-2": r"Sim: CALVIN | Real: Franka",
    "V-JEPA 2": r"Sim: Habitat (Zero-shot plan)",
    "DreamVLA": r"Sim: CALVIN | Real: Franka",
    "3D-VLA": r"Sim: RLBench, CALVIN | Real: Franka",
    "SpatialVLA": r"Sim: RLBench | Real: Franka, WidowX",
    "BridgeVLA": r"Real: Franka (Sample efficiency)",
    "RoBridge": r"Real: WidowX (Domain randomization)",
    "PointVLA": r"Real: Franka (Real-vs-Photo)"
}

new_lines = []
for line in lines:
    matched = False
    for key, new_val in replacements.items():
        if line.strip().startswith(f"\\textbf{{{key}}}"):
            parts = line.split('&')
            if len(parts) >= 7:
                last_part = parts[-1]
                trailing = last_part[last_part.rfind('\\\\'):] if '\\\\' in last_part else '\n'
                parts[-1] = f" {new_val} {trailing}"
                line = "&".join(parts)
                matched = True
                break
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Table updated successfully.")
