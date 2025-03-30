import argparse
import json
import os
import time

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
start = time.time()
result = model.transcribe(args.audio, verbose=True)
running_time = time.time() - start
# Print the running time in HH:MM:SS format
hours, remainder = divmod(running_time, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"Transcription completed in {int(hours):02}:{int(minutes):02}:{int(seconds):02}")

# Save the transcription to a file
os.makedirs(args.output_dir, exist_ok=True)
filename = os.path.splitext(os.path.basename(args.audio))[0]
with open(os.path.join(args.output_dir, f"{filename}.txt"), "w") as f:
    f.write(result["text"])
with open(os.path.join(args.output_dir, f"{filename}.json"), "w") as f:
    json.dump(result["segments"], f, indent=4)
