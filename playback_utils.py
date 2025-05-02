import os
import subprocess
import requests
import pretty_midi
from IPython.display import Audio, display
from ipywidgets import Button
from google.colab import files


# Install fluidsynth (safe to rerun in Colab)
subprocess.call(['apt-get', 'install', '-y', 'fluidsynth'])

# SoundFont location and URL
soundfont_path = "/content/FluidR3_GM.sf2"
soundfont_url = "https://www.dropbox.com/scl/fi/ruczr63ev3ac4xxi3q9fd/FluidR3_GM.sf2?rlkey=ih7q2m0vpp5cvvjxq1cq3s23i&dl=1"

 #Ensure SoundFont exists
if not os.path.exists(soundfont_path):
    print("🎵 Downloading SoundFont...")
    urllib.request.urlretrieve(soundfont_url, soundfont_path)
else:
    print("🎵 SoundFont already exists.")



def save_and_play(midi_object, filename="output.mid", show_info=None):
    import urllib.request
    import subprocess

    # Ensure fluidsynth is installed
    subprocess.call(['apt-get', 'install', '-y', 'fluidsynth'])

    # Paths
    soundfont_path = "/content/FluidR3_GM.sf2"
    soundfont_url = "https://www.dropbox.com/scl/fi/ruczr63ev3ac4xxi3q9fd/FluidR3_GM.sf2?rlkey=ih7q2m0vpp5cvvjxq1cq3s23i&dl=1"

    # Download SoundFont if needed
    if not os.path.exists(soundfont_path):
        print("🎵 Downloading SoundFont...")
        urllib.request.urlretrieve(soundfont_url, soundfont_path)

    # Save MIDI file
    midi_object.write(filename)

    # Convert to WAV
    wav_filename = filename.replace(".mid", ".wav")
    os.system(f"fluidsynth -ni {soundfont_path} {filename} -F {wav_filename} -r 44100")

    if not os.path.exists(wav_filename):
        print("❌ Failed to create WAV file. Check fluidsynth and MIDI input.")
        return

    # Playback
    from IPython.display import Audio, display
    display(Audio(filename=wav_filename, rate=44100))

    # Print metadata
    if show_info:
        print("🎛️ Parameters used:")
        for k, v in show_info.items():
            print(f" - {k}: {v}")

    # Download button
    from ipywidgets import Button
    from google.colab import files
    button = Button(description="⬇️ Download MIDI File")
    button.on_click(lambda b: files.download(filename))
    display(button)
