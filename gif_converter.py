import argparse
from vid_to_gif import convert_video_to_gif

def main():
    parser = argparse.ArgumentParser(description="Convert video to GIF.")
    parser.add_argument("video", help="Path to the video file")
    parser.add_argument("output", help="Path to save the GIF")
    parser.add_argument("--fps", type=int, default=10, help="Frames per second for GIF (default: 10)")

    args = parser.parse_args()
    convert_video_to_gif(args.video, args.output, args.fps)

if __name__ == "__main__":
    main()

