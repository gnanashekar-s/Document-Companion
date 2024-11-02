import subprocess
import os

def convert_webm_to_mp4(webm_file_path, mp4_file_path):
    """
    Converts a WebM file to MP4 format using FFmpeg.
    
    Args:
    - webm_file_path: str, path to the input WebM file.
    - mp4_file_path: str, path to save the converted MP4 file.
    """
    command = [
        'ffmpeg',
        '-i', webm_file_path,  # Input file
        '-c:v', 'libx264',     # Use H.264 codec for video
        '-c:a', 'aac',         # Use AAC codec for audio
        '-strict', 'experimental',  # Allow experimental codecs
        mp4_file_path          # Output file
    ]

    # Run the command
    subprocess.run(command, check=True)

# Example usage
webm_path = "input_file.webm"  # Replace with your WebM file path
mp4_path = "output_file.mp4"    # Replace with your desired output path

try:
    convert_webm_to_mp4(webm_path, mp4_path)
    print(f"Conversion successful: {mp4_path}")
except subprocess.CalledProcessError as e:
    print(f"Error during conversion: {e}")
