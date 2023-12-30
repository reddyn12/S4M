import wave

def convertToWav(arr, outputFileName, numChannels, sampleWidth, frameRate):
    newFrames = arr.tobytes()
    # Write audio data back into a .wav file
    with wave.open(outputFileName, 'wb') as audio_file:
        audio_file.setnchannels(numChannels)
        audio_file.setsampwidth(sampleWidth)
        audio_file.setframerate(frameRate)
        audio_file.writeframes(newFrames)