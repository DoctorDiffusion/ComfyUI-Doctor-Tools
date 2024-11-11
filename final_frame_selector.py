import torch

class FinalFrameSelector:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process_images"
    CATEGORY = "MediaMixer"

    def process_images(self, images):
        # Handle multiple images
        if images.dim() == 4:  # Multiple images
            final_image = images[-1]
            
            # Ensure the image is in the correct format
            if final_image.dim() == 3:
                final_image = final_image.unsqueeze(0)
            
            return (final_image,)
        
        # Handle single image
        elif images.dim() == 3:
            return (images.unsqueeze(0),)
        
        else:
            # Unexpected input
            return (None,)

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "FinalFrameSelector": FinalFrameSelector
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FinalFrameSelector": "Final Frame Selector"
}