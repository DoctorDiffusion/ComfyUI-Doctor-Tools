import os
import yt_dlp
import subprocess
import re

class YouTubeVideoDownloader:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "youtube_url": ("STRING", {"default": ""}),
                "download_path": ("STRING", {"default": "D:/ComfyUI_downloads"}),
                "resolution": (["360p", "480p", "720p", "1080p"], {"default": "720p"}),
                "save_as_mp4": ("BOOLEAN", {"default": False}),
                "audio_only": ("BOOLEAN", {"default": False})
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("video_path", "audio_path")
    FUNCTION = "download_youtube_video"
    CATEGORY = "Doctor-Tools"
    
    def sanitize_filename(self, title):
        """Convert title to safe filename"""
        # Remove invalid characters
        safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
        # Replace spaces with underscores
        safe_title = safe_title.replace(' ', '_')
        # Remove any other problematic characters
        safe_title = re.sub(r'[^\w\-_.]', '', safe_title)
        # Limit length
        safe_title = safe_title[:100]  # Limit to 100 characters
        return safe_title
    
    def convert_mkv_to_mp4(self, mkv_path):
        """Convert MKV to MP4 using FFmpeg"""
        mp4_path = mkv_path.replace('.mkv', '.mp4')
        try:
            cmd = ['ffmpeg', '-i', mkv_path, '-codec', 'copy', mp4_path, '-y']
            subprocess.run(cmd, check=True, capture_output=True)
            # Remove original MKV if MP4 conversion successful
            if os.path.exists(mp4_path) and os.path.getsize(mp4_path) > 0:
                os.remove(mkv_path)
                return mp4_path
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] FFmpeg conversion failed: {e}")
            return mkv_path
        return mkv_path
    
    def download_youtube_video(self, youtube_url, download_path, resolution, save_as_mp4, audio_only):
        try:
            # Ensure the download directory exists
            os.makedirs(download_path, exist_ok=True)
            print(f"[INFO] Download path verified or created at: {download_path}")
            
            # First get video info to get the title
            print("[INFO] Getting video information...")
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(youtube_url, download=False)
                video_title = self.sanitize_filename(info['title'])
                print(f"[INFO] Video title: {info['title']}")
            
            # Create filenames based on video title
            base_filename = video_title
            # If file already exists, append number
            counter = 1
            while os.path.exists(os.path.join(download_path, f"{base_filename}.mkv")) or \
                  os.path.exists(os.path.join(download_path, f"{base_filename}.mp4")) or \
                  os.path.exists(os.path.join(download_path, f"{base_filename}.wav")):
                base_filename = f"{video_title}_{counter}"
                counter += 1
            
            video_path = os.path.join(download_path, f"{base_filename}.mkv")
            audio_path = os.path.join(download_path, f"{base_filename}.wav")
            final_video_path = video_path
            
            # Download audio as WAV
            print("[INFO] Downloading and extracting audio...")
            ydl_opts_audio = {
                'format': 'bestaudio',
                'outtmpl': audio_path[:-4],  # Remove .wav as it will be added by postprocessor
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
                'quiet': False,
                'no_warnings': False,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
                ydl.extract_info(youtube_url, download=True)
            
            # Verify audio file
            if not os.path.exists(audio_path):
                raise FileNotFoundError(f"Audio file not found at {audio_path}")
            if os.path.getsize(audio_path) == 0:
                raise ValueError(f"Downloaded audio file is empty: {audio_path}")
            
            # If audio_only is True, skip video download
            if audio_only:
                print("[INFO] Audio-only mode: Skipping video download")
                return ("", audio_path)
            
            # Download video
            print("[INFO] Downloading video...")
            height = resolution[:-1]  # Remove 'p' from resolution
            
            ydl_opts_video = {
                'format': f'bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': video_path,
                'merge_output_format': 'mkv',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mkv',
                }],
                'quiet': False,
                'no_warnings': False,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
                ydl.extract_info(youtube_url, download=True)
                print(f"[INFO] Video download completed")
            
            # Convert to MP4 if requested
            if save_as_mp4:
                print("[INFO] Converting to MP4...")
                final_video_path = self.convert_mkv_to_mp4(video_path)
                if final_video_path.endswith('.mp4'):
                    print("[INFO] Successfully converted to MP4")
                else:
                    print("[WARNING] MP4 conversion failed, keeping MKV format")
            
            # Verify video file
            if not os.path.exists(final_video_path):
                raise FileNotFoundError(f"Video file not found at {final_video_path}")
            if os.path.getsize(final_video_path) == 0:
                raise ValueError(f"Downloaded video file is empty: {final_video_path}")
            
            print(f"[INFO] Files saved to:\nVideo: {final_video_path}\nAudio: {audio_path}")
            
            return (final_video_path, audio_path)
            
        except Exception as e:
            error_message = f"[ERROR] Error during download: {str(e)}"
            print(error_message)
            return (error_message, error_message)

# Register node class mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "YouTubeVideoDownloader": YouTubeVideoDownloader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "YouTubeVideoDownloader": "YouTube Video Downloader"
}