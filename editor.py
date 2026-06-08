import os
import shutil

def process_video(input_path, prompt):
    
    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/final.mp4"

    shutil.copy(input_path, output_path)

    return output_path