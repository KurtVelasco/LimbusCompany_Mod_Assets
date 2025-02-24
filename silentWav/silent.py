import os
from pydub import AudioSegment

def replace_wav_files(folder_path, selected_wav_path):
    try:
        selected_audio = AudioSegment.from_wav(selected_wav_path)
    except Exception as e:
        print(f"Error loading selected WAV file: {e}")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.lower().endswith('.wav'):
            try:
                selected_audio.export(file_path, format="wav")
                print(f"Replaced content of: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

folder_path = input("\nEnter the folder path containing WAV files: ").strip()
selected_wav_path = input("\nEnter the path to the selected WAV file: ").strip()
# Updated To Provide User Feedback   
if not os.path.isdir(folder_path):
    print("\nThe folder path provided is not valid.")
elif not os.path.isfile(selected_wav_path) or not selected_wav_path.lower().endswith('.wav'):
    print("\nThe selected WAV file path is not valid.")
else:
    replace_wav_files(folder_path, selected_wav_path)