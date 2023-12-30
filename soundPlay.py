import os
import sys
import utils
import wave
import numpy as np
import matplotlib.pyplot as plt

REDUCE_FACTOR = 2

folderPre = 'audio/songs/'
fileName = 'Thank_God_Travis.wav'

with wave.open(folderPre + fileName, 'rb') as audio_file:
    num_channels = audio_file.getnchannels()
    sample_width = audio_file.getsampwidth()
    frame_rate = audio_file.getframerate()
    num_frames = audio_file.getnframes()

    # Read audio frames
    audio_frames = audio_file.readframes(num_frames)
print('Num Channels: ', num_channels)
print('Sample Width: ', sample_width)
print('Frame Rate: ', frame_rate)
print('Num Frames: ', num_frames)
# print('Audio Frames: ', audio_frames)
# Convert binary audio data to a numpy array
audio_data = np.frombuffer(audio_frames, dtype=np.int16)
truncInd = audio_data.shape[0] - (audio_data.shape[0] % REDUCE_FACTOR)
audio_data = audio_data[:truncInd]
print('Audio Data Shape POST_TRUNC: ', audio_data.shape)
# sys.exit()

# Calculate time array in seconds
# time = np.linspace(0, len(audio_data) / frame_rate, num=len(audio_data))
time = np.arange(len(audio_data)) / frame_rate

utils.convertToWav(audio_data, 'testOutput.wav', num_channels, 
                   sample_width, frame_rate) 

# print(type(audio_data[0]))
# print(audio_data[0])
# print(audio_data.shape[0])
# sys.exit()


curr = audio_data[0]
# newData = np.zeros(audio_data.shape)
newData = audio_data.copy()
newData = []
for i in range(0, audio_data.shape[0], REDUCE_FACTOR):
    newData.append(audio_data[i])

newData = np.array(newData)
frame_rate = frame_rate//REDUCE_FACTOR
print('newData Shape: ', newData.shape)
print('prevData Shape: ', audio_data.shape)
print('NEW Frame Rate: ', frame_rate)
utils.convertToWav(newData, 'testDataOutput.wav', num_channels, 
                   sample_width, frame_rate) 
   
       
# print(audio_data.shape)
# print(audio_data[300000:300200])
# print(audio_data.mean())

# # Plot the sound curve
# plt.figure(figsize=(10, 4))
# # plt.plot(time, audio_data)
# plt.plot(time[::10000], audio_data[::10000])
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.title('Sound Waveform')
# plt.show()