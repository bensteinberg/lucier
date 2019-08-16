import midside
from sounddevice import PortAudioError
from thready import Playback
from datetime import datetime


def sitting(
    input_file, output_base, cycles, playback_device, recording_device, fs=44100
):
    """I am sitting in a room"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    for i in range(0, cycles):
        output_file = "{0}_{1}_{2:02d}.wav".format(output_base, timestamp, i)
        # try-retry from http://stackoverflow.com/a/2083996
        while True:
            try:
                t = Playback(input_file, playback_device)
                t.start()
                # how to manage levels?  normalize here?  in midside?  need to watch levels manually?
                midside.record(output_file, recording_device, t.samps, fs)
                input_file = output_file
            except PortAudioError:
                continue
            break
