import os
import simpleaudio as sa
import eel

#we can use that in main.js now
@eel.expose
def play_startup_sound():
    """Plays the assistant's startup sound."""
    try:
        # Path to the audio file from this Python file's location
        base_dir = os.path.dirname(os.path.abspath(__file__))  # e.g., /path/to/engine/
        sound_path = os.path.join(base_dir, '..', 'www', 'assets', 'audio', 'start_sound.wav')

        # Load and play the .wav file
        wave_obj = sa.WaveObject.from_wave_file(sound_path)
        wave_obj.play()
    except Exception as e:
        print(f"[ERROR] Could not play sound: {e}")
