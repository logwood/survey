import urllib.request, urllib.parse, json, os, re

papers = [
    'Transic: Sim-to-Real Transfer with Diffusion Transformers',
    'AUTOQVLA: NOT ALL CHANNELS ARE EQUAL INVISION-LANGUAGE-ACTIONMODEL’SQUANTIZATION',
    'RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning',
    'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning',
    'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success',
    'VLA-FT: Fine-Tuning Vision-Language-Action Models for Robotic Tasks',
    'Policy Contrastive Decoding for Robotic Foundation Models',
    'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy',
    'UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation',
    'Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning',
    'PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding',
    'TinyVLA: Toward Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation',
    'FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models',
    'X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real',
    'DASP: Hierarchical Offline Reinforcement Learning via Diffusion Autodecoder and Skill Primitive',
    'SwiftVLA:Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead',
    'What can rl bring to vla generalization? an empirical study',
    'Consistency Regularization for Vision-Language-Action Models in Robotic Manipulation',
    'Steering Your Diffusion Policy with Latent Space Reinforcement Learning',
    'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills',
    'Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies',
    'RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning',
    'ManipTrans:Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning',
    'The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning',
    'Neural MP: A Generalist Neural Motion Planner',
    'Self-Improving Vision-Language-Action Models with Data Generation via Residual RL',
    'Latent Action Diffusion for Cross-Embodiment Manipulation',
    'Cross-Embodiment Robotic Manipulation Synthesis via Guided Demonstrations through CycleVAE and Human Behavior Transformer',
    'FLaRe: Achieving Masterful and Adaptive Robot Policies with Large-Scale Reinforcement Learning Fine-Tuning',
    'Shallow-π: Knowledge Distillation for Flow-based VLAs',
    'AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation',
    'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions',
    'ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning',
    'Offline Actor-Critic Reinforcement Learning Scales to Large Models',
    'HBVLA: Pushing 1-Bit Post-Training Quantization for Vision-Language-Action Models',
    'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models',
    'Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution',
    'FAST: Efficient Action Tokenization for Vision-Language-Action Models',
    'SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration'
]

out_dir = r'c:\Users\ASUS\Desktop\ACM_Computing_Draft\pdf_library\Section_4.4_Deployment'
os.makedirs(out_dir, exist_ok=True)

def search_arxiv(title):
    query = urllib.parse.quote(f'ti:"{title}"')
    url = f'http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=1'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml = response.read().decode('utf-8')
            match = re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>', xml)
            if match:
                return f'https://arxiv.org/pdf/{match.group(1)}.pdf'
    except Exception as e:
        print(f'Error searching {title}: {e}')
    return None

for i, title in enumerate(papers):
    print(f'[{i+1}/{len(papers)}] Searching for: {title[:50]}...')
    pdf_url = search_arxiv(title)
    if pdf_url:
        print(f'  Found PDF URL: {pdf_url}')
        safe_title = re.sub(r'[^a-zA-Z0-9]', '_', title[:50])
        pdf_path = os.path.join(out_dir, f'{safe_title}.pdf')
        if not os.path.exists(pdf_path):
            try:
                print(f'  Downloading to {pdf_path}...')
                req = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(pdf_path, 'wb') as out_file:
                    out_file.write(response.read())
                print('  Success!')
            except Exception as e:
                print(f'  Failed to download: {e}')
        else:
            print('  Already exists.')
    else:
        print('  Not found on arXiv.')
