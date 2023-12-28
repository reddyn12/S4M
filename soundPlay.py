import os
import sys
import wave
import numpy as np
import matplotlib.pyplot as plt

folderPre = 'audio/songs/'
fileName = 'Thank_God_Travis.wav'

with wave.open(folderPre + fileName, 'rb') as audio_file:
    num_channels = audio_file.getnchannels()
    sample_width = audio_file.getsampwidth()
    frame_rate = audio_file.getframerate()
    num_frames = audio_file.getnframes()

    # Read audio frames
    audio_frames = audio_file.readframes(num_frames)

# Convert binary audio data to a numpy array
audio_data = np.frombuffer(audio_frames, dtype=np.int16)

# Calculate time array in seconds
time = np.linspace(0, len(audio_data) / frame_rate, num=len(audio_data))

# Plot the sound curve
plt.figure(figsize=(10, 4))
plt.plot(time, audio_data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sound Waveform')
plt.show()