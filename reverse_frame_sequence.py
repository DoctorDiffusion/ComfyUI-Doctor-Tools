import torch

class ReverseFrameSequence:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Images": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "reverse_sequence"
    CATEGORY = "🎬🔀MediaMixer"

    def reverse_sequence(self, Images):
        # Ensure input is a 4D tensor (batch of images)
        if Images.dim() == 3:
            Images = Images.unsqueeze(0)
        
        # Reverse the order of images along the batch dimension (first dimension)
        reversed_images = Images.flip(dims=[0])
        
        return (reversed_images,)

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "ReverseFrameSequence": ReverseFrameSequence
}

# A dictionary that contains the friendly/human-readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ReverseFrameSequence": "Reverse Frame Sequence"
}
