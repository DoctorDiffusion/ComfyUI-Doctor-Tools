import torch

class VideoMerge:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Video_A": ("IMAGE",),
                "Video_B": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "merge_videos"
    CATEGORY = "🎬🔀MediaMixer"

    def merge_videos(self, Video_A, Video_B):
        # Ensure both inputs are 4D tensors
        if Video_A.dim() == 3:
            Video_A = Video_A.unsqueeze(0)
        if Video_B.dim() == 3:
            Video_B = Video_B.unsqueeze(0)

        # Concatenate the images along the first dimension (batch dimension)
        Video = torch.cat((Video_A, Video_B), dim=0)
        
        return (Video,)

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "VideoMerge": VideoMerge
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "VideoMerge": "Video Merge"
}