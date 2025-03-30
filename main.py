import argparse
import os

import whisper

parser = argparse.ArgumentParser()
parser.add_argument(
    "--audio", type=str, default="audio.mp3", help="Path to the audio file"
)
parser.add_argument(
    "--output_dir", type=str, default="outputs", help="Directory to save the output"
)
args = parser.parse_args()

# Load the model
model = whisper.load_model("turbo")
# Transcribe the audio file
result = model.transcribe(args.audio)

# Save the transcription to a file
os.makedirs(args.output_dir, exist_ok=True)
filename = os.path.splitext(os.path.basename(args.audio))[0]
with open(os.path.join(args.output_dir, f"{filename}.txt"), "w") as f:
    f.write(result["text"])
