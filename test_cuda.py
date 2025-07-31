import torch

print("🚀 CUDA Available :", torch.cuda.is_available())

if torch.cuda.is_available():
    print("🔧 CUDA Device Count :", torch.cuda.device_count())
    print("🎮 GPU Name         :", torch.cuda.get_device_name(0))
    print("📦 CUDA Version     :", torch.version.cuda)
    print("💡 PyTorch CUDA Capabilities:", torch.cuda.get_device_capability(0))
else:
    print("❌ CUDA not available.")
