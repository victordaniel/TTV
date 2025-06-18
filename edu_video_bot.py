import os
import argparse
from PIL import Image, ImageDraw, ImageFont
import pyttsx3
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip


def text_to_scenes(text):
    """Split text into scenes using periods."""
    scenes = [s.strip() for s in text.split('.') if s.strip()]
    return scenes


def generate_image(text, index, out_dir="scenes"):
    os.makedirs(out_dir, exist_ok=True)
    img = Image.new('RGB', (640, 480), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    # Wrap text if necessary
    lines = []
    words = text.split()
    line = ''
    for word in words:
        if draw.textsize(line + ' ' + word, font=font)[0] < 600:
            line += ' ' + word
        else:
            lines.append(line.strip())
            line = word
    lines.append(line.strip())
    y = 200
    for line in lines:
        w, h = draw.textsize(line, font=font)
        draw.text(((640 - w) / 2, y), line, fill=(0, 0, 0), font=font)
        y += h + 5
    path = os.path.join(out_dir, f"scene_{index:03d}.png")
    img.save(path)
    return path


def generate_images(scenes):
    paths = []
    for i, scene in enumerate(scenes):
        paths.append(generate_image(scene, i))
    return paths


def generate_narration(text, out_file="narration.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(text, out_file)
    engine.runAndWait()
    return out_file


def create_video(image_paths, audio_path, out_file="output.mp4", duration_per_image=3):
    clips = [ImageClip(p).set_duration(duration_per_image) for p in image_paths]
    video = concatenate_videoclips(clips, method="compose")
    if audio_path:
        narration = AudioFileClip(audio_path)
        video = video.set_audio(narration)
    video.write_videofile(out_file, fps=24)


def main():
    parser = argparse.ArgumentParser(description="EduVideoBot simple demo")
    parser.add_argument("text", help="Input description text")
    parser.add_argument("--output", default="output.mp4", help="Output video file")
    args = parser.parse_args()

    scenes = text_to_scenes(args.text)
    image_paths = generate_images(scenes)
    audio_path = generate_narration(args.text)
    create_video(image_paths, audio_path, args.output)


if __name__ == "__main__":
    main()
