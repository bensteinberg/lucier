import sounddevice as sd
import numpy as np
import soundfile as sf


def record(filepath, device, samps, fs):
    """mid-side recording: assume R channel is mid"""
    raw = sd.rec(samps, samplerate = fs, channels = 2, device = device)
    sd.wait()
    mid = raw[:, 1]
    side = raw[:, 0]

    left = mid + side
    right = mid + (-side)

    output = np.column_stack((left, right))

    sf.write(filepath, output, fs)
    
