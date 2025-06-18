# EduVideoBot

This repository contains a minimal example of generating a narrated slideshow
video from a text prompt. Images are generated using Pillow with the scene text,
audio narration is produced with `pyttsx3`, and the final video is assembled
with `moviepy`.

## Requirements

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/) (for video rendering)
- A TTS engine supported by `pyttsx3` (e.g. `espeak` on Linux)

Install Python dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python edu_video_bot.py "Explain photosynthesis with a happy tree and sun shining down"
```

This will create placeholder images, generate narration from the text, and
produce `output.mp4` in the current directory.
