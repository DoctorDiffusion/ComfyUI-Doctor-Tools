# 🎬🔀MediaMixer
A node suite for downloading audio and video from youtube as we all sevral useful video utilits such as a final frame selector and a node that merges two videos into one.
****

## Installation
Use the world famous [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) or manually install:

Navagate to your custom node folder `...ComfyUI/custom_nodes`
```
git clone https://github.com/DoctorDiffusion/ComfyUI-MediaMixer.git
```
```
cd ComfyUI-MediaMixer
```
```
pip install -r requirements.txt
```
If this fails to install yt_dlp to your desired python environment, use the following comand:
```bash
.\python_embed\python.exe -s -m pip install yt_dlp
```

## Nodes

### Prompt Journal

Take a list of text and output a single row as a string of text from the top outout string and/or the full text from the second string output. Use with a primitive to randomize or have further control.

![Screenshot 2024-11-23 150431](https://github.com/user-attachments/assets/b5e8eaab-5d51-4e91-b17f-07c1cb422d52)

### Video Merge Node

The Video Merge node allows you to combine two video clips within ComfyUI.
Plug the input video into "Video_A" and your output render into "Video_B" to combine your extended video.

### Final & First Frame Selector

Final Frame Selector takes an image sequence or video and passes through the final frame as an image node. 
This works great for extending video with image-to-video tools like Pyramid-Flow, CogVideoX, and LTX-Video. <br>
<br>
First Frame Selector will do the same but with the first frame, this was a requested node.

![Screenshot 2024-11-01 190029](https://github.com/user-attachments/assets/be4a1d0b-ae14-4ece-92f0-87fbcc98fe0f)

### YouTube Video Downloader

![Screenshot 2024-11-26 121720](https://github.com/user-attachments/assets/a110e845-81e3-43aa-b547-b123ca4d98fb)

### Reverse Frame Sequence

Inverse the order of the images in a frame sequence with this node to easily reverse videos.

![Screenshot 2024-11-26 121318](https://github.com/user-attachments/assets/6122641e-0b72-4c8a-96f9-c819b80f6711)

## Credits

- [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

- [ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

- [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)

⭐ If you like the project, please give it a star! ⭐

## License
CC0-1.0 license
