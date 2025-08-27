import sounddevice as sd
from scipy.io.wavfile import write

def get_time_length():
    length_inputed = False
    while not length_inputed:
        length = input("Write the desired lenght in seconds").strip()
        try:   
            length = float(length)
            length_inputed = True
        except ValueError:
            length_inputed = False
    return length

length = get_time_length()
fs = 44100

print("recording...")
recording = sd.rec(int(length * fs), samplerate=fs, channels=2)
sd.wait()
print("Recorded")

filename = input("Write the name for the file") + ".wav"
write(filename,fs,recording)