import os
import yt_dlp

class YouTubeVideoDownloader:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "youtube_url": ("STRING", {"default": ""}),
                "download_path": ("STRING", {"default": "D:\ComfyUI_windows_portable\ComfyUI\downloads"}),
                "resolution": (["360p", "480p", "720p", "1080p"], {"default": "720p"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("video_path",)
    FUNCTION = "download_youtube_video"
    CATEGORY = "Doctor-Tools"
    
    def download_youtube_video(self, youtube_url, download_path, resolution):
        try:
            # Ensure the download directory exists
            os.makedirs(download_path, exist_ok=True)
            print(f"[INFO] Download path verified or created at: {download_path}")
            
            # Create unique filename
            import time
            timestamp = int(time.time())
            video_path = os.path.join(download_path, f'video_{timestamp}.mkv')  # Using MKV as container
            
            # More explicit format selection
            height = resolution[:-1]  # Remove 'p' from resolution
            
            ydl_opts = {
                'format': f'bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': video_path,
                'merge_output_format': 'mkv',  # Using MKV as it's more flexible with codecs
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mkv',
                }],
                'quiet': False,
                'no_warnings': False,
                'verbose': True,  # Add verbose output for debugging
            }
            
            # Download video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=True)
                print(f"[INFO] Download completed with format: {info.get('format', 'unknown')}")
            
            print(f"[INFO] Video downloaded to: {video_path}")
            
            # Verify file exists and has size > 0
            if not os.path.exists(video_path):
                raise FileNotFoundError(f"Video file not found at {video_path}")
            
            if os.path.getsize(video_path) == 0:
                raise ValueError(f"Downloaded file is empty: {video_path}")
                
            return (video_path,)
            
        except Exception as e:
            error_message = f"[ERROR] Error during download: {str(e)}"
            print(error_message)
            return (error_message,)

# Register node class mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "YouTubeVideoDownloader": YouTubeVideoDownloader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "YouTubeVideoDownloader": "YouTube Video Downloader"
}