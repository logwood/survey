$papers = @(
    'TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction',
    'QVLA: NOT ALL CHANNELS ARE EQUAL INVISION-LANGUAGE-ACTIONMODEL’SQUANTIZATION',
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
)

$out_dir = "c:\Users\ASUS\Desktop\ACM_Computing_Draft\pdf_library\Section_4.4_Deployment"
if (-not (Test-Path $out_dir)) {
    New-Item -ItemType Directory -Force -Path $out_dir | Out-Null
}

$i = 1
foreach ($title in $papers) {
    $shortTitle = $title
    if ($shortTitle.Length -gt 50) {
        $shortTitle = $shortTitle.Substring(0, 50)
    }
    Write-Host "[$i/$($papers.Count)] Searching for: $shortTitle..."
    
    $encodedTitle = [uri]::EscapeDataString("ti:`"$title`"")
    $url = "http://export.arxiv.org/api/query?search_query=$encodedTitle&start=0&max_results=1"
    
    try {
        $response = Invoke-WebRequest -Uri $url -UseBasicParsing
        $xml = $response.Content
        if ($xml -match "<id>http://arxiv.org/abs/([^<]+)</id>") {
            $pdf_url = "https://arxiv.org/pdf/$($matches[1]).pdf"
            Write-Host "  Found PDF URL: $pdf_url"
            
            $safe_title = $shortTitle -replace "[^a-zA-Z0-9]", "_"
            $pdf_path = Join-Path $out_dir "$safe_title.pdf"
            
            if (-not (Test-Path $pdf_path)) {
                Write-Host "  Downloading to $pdf_path..."
                Invoke-WebRequest -Uri $pdf_url -OutFile $pdf_path -UseBasicParsing
                Write-Host "  Success!"
            } else {
                Write-Host "  Already exists."
            }
        } else {
            Write-Host "  Not found on arXiv."
        }
    } catch {
        Write-Host "  Error searching or downloading: $_"
    }
    Start-Sleep -Seconds 10
    $i++
}