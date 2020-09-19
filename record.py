# Records audio directly from the computer
import sounddevice as sd
import soundfile as sf
import wavio
# Initial recording is saved as a np file
import numpy as np
from scipy.io.wavfile import write

# Used to dictate how long we are recording for
import time

# Record audio for duration seconds
def record(duration, filename):
    # Record the audio for duration time and save it into filename + ".wav" 
    fs = 44100
    sd.default.samplerate = fs
    sd.default.channels = 2


    myarray = sd.rec(int(duration * fs))
    sd.wait()
    wavio.write(filename + '.wav', myarray, fs, sampwidth=2)

    return myarray

# Plays back an audio file once recorded
def playback(myarray):
    fs = 44100
    sd.play(myarray, fs)

# Converts a .wav file to .flac
def wavToFlac(filename):
    wav, samplerate = sf.read(filename + '.wav')
    sf.write(filename + '.flac', wav, samplerate)