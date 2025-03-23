from moviepy import VideoFileClip

def convert_video_to_gif(video_path: str, output_gif: str, fps: int = 10):
    """
    Converts a short video to GIF.
    
    :param video_path: Path to the input video file.
    :param output_gif: Path to save the output GIF.
    :param fps: Frames per second for the GIF (default: 10).
    """
    clip = VideoFileClip(video_path)
    clip = clip.set_fps(fps)
    clip.write_gif(output_gif, fps=fps)
    print(f"GIF saved at: {output_gif}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python vid_to_gif.py <video_path> <output_gif>")
    else:
        convert_video_to_gif(sys.argv[1], sys.argv[2])
