import argparse
import subprocess

def compress_video(input_file, output_file, bitrate="1000k", codec="libx264", preset="medium", crf=23):
    # ffmpeg command to compress the video
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vcodec", codec,
        "-b:v", bitrate,
        "-preset", preset,
        "-crf", str(crf),
        output_file
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress a video using ffmpeg.")
    parser.add_argument("input_file", type=str, help="Input video file.")
    parser.add_argument("output_file", type=str, default="output.mp4", help="Output compressed video file.")
    parser.add_argument("-b", "--bitrate", type=str, default="1000k", help="Target bitrate for the video (e.g. 1000k).")
    parser.add_argument("-c", "--codec", type=str, default="libx264", help="Video codec to use (e.g. libx264).")
    parser.add_argument("-p", "--preset", type=str, default="medium", choices=["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"], help="Preset for compression speed/quality tradeoff.")
    parser.add_argument("--crf", type=int, default=23, help="Constant Rate Factor (CRF). Lower values mean better quality but larger file size. Range: 0-51.")

    args = parser.parse_args()

    compress_video(args.input_file, args.output_file, bitrate=args.bitrate, codec=args.codec, preset=args.preset, crf=args.crf)
