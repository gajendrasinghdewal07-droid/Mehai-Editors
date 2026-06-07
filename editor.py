import subprocess

def process_video(input_path, prompt):
    output_path = "outputs/final.mp4"

    # basic auto resize + export
    command = [
        "ffmpeg",
        "-i", input_path,
        "-vf", "scale=1080:1920",
        "-preset", "fast",
        output_path
    ]

    subprocess.run(command)

    return output_path