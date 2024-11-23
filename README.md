# MediaMixer
A node suite for downloading audio and video from youtube as we all sevral useful video utilits such as a final frame selector and a node that merges two videos into one.
****

## Installation
Use the world famous [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) or manually install:
```
git clone https://github.com/DoctorDiffusion/ComfyUI-MediaMixer.git
```
```
cd MediaMixer
```
```
pip install -r requirements.txt
```
If this fails to install yt_dlp:
```bash
.\python_embed\python.exe -s -m pip install yt_dlp
```

## Nodes

### Prompt Journal

Take a list of text and output a single row as a string of text. Use with a primitive to randomize or have further control.

![Screenshot 2024-11-23 150431](https://github.com/user-attachments/assets/b5e8eaab-5d51-4e91-b17f-07c1cb422d52)

### Video Merge Node

The Video Merge node allows you to combine two video clips within ComfyUI.
Plug the input video into "Video_A" and your output render into "Video_B" to combine your extended video.

### Final Frame Selector

Final Frame Selector takes an image sequence or video and passes through the final frame as an image node. 
This works great for extending video with image-to-video tools like Pyramid-Flow, CogVideoX, and LTX-Video. 

![Screenshot 2024-11-01 190029](https://github.com/user-attachments/assets/be4a1d0b-ae14-4ece-92f0-87fbcc98fe0f)

### YouTube Video Downloader

![Screenshot 2024-11-01 190304](https://github.com/user-attachments/assets/0ed0e432-1c7c-4911-8110-39d9be58e43e)

### Reverse Frame Sequence

Inverse the order of the images in a frame sequence with this node to easily reverse videos.

## Credits

- [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

- [ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

- [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)

⭐ If you like the project, please give it a star! ⭐

## License
CC0-1.0 license
