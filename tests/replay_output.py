# this is a test script for recording your speaker audio and replay it for you in your speaker
# the 'mic' needs to be set to your default output for it to work
# it will also save the audio in .wav format
 
import soundcard as sc
import soundfile as sf
import pickle as pkl
import time

# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()

# get a list of all microphones:v
mics = sc.all_microphones(include_loopback=True)
# get the current default microphone on your system:
default_mic = mics[0]

for i in range(len(mics)):
    try:
        print(f"{i}: {mics[i].name}")
    except Exception as e:
        print(e)

with default_mic.recorder(samplerate=148000) as mic, default_speaker.player(samplerate=148000) as sp:
    print("Recording...")
    data = mic.record(numframes=1000000)
    print(data.shape)
    with open("audio.pkl", 'wb') as f:
        pkl.dump(data, f)
    # print("Done...Stop your sound so you can hear playback")
    # time.sleep(2)
    # sp.play(data)

sf.write("filename.wav", data, 148000)