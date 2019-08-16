import sounddevice as sd
import numpy as np
import soundfile as sf


def record(filepath, device, samps, fs, mix=1.0, side_gain=1.0):
    """
    mid-side recording: assume R channel is mid

    reduce mix to eliminate clipping if necessary; 1.0 / math.sqrt(2) is a possibility
    increase side_gain to widen the stereo image
    """
    raw = sd.rec(samps, samplerate=fs, channels=2, device=device)
    sd.wait()
    mid = raw[:, 1]
    side = side_gain * raw[:, 0]

    left = mix * (mid + side)
    right = mix * (mid + (-side))

    output = np.column_stack((left, right))

    # should we just remix if there's clipping?
    if np.any(abs(output) >= 1.0):
        # seems like counting clipped samples should be simpler
        clip = len(filter(lambda x: any([y >= 1.0 for y in abs(x)]), output))
        msg = "Clipping in {count} sample{s}: consider reducing the mix argument."
        print(msg.format(count=clip, s="" if clip == 1 else "s"))

    sf.write(filepath, output, fs)
