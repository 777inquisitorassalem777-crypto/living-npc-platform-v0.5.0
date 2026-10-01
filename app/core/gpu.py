"""Optional GPU capability detection."""

def gpu_info():
    try:
        import torch
    except ImportError:
        return {"available": False, "reason": "PyTorch is not installed"}
    return {
        "available": bool(torch.cuda.is_available()),
        "device_count": int(torch.cuda.device_count()),
        "device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
    }
