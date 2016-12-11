import midside
import sounddevice as sd
import soundfile as sf
from thready import Playback
from datetime import datetime

def sitting(input_file, output_base, cycles, playback_device, recording_device):
    """I am sitting in a room"""
    for i in range (0, cycles):
        output_file = "%s_%s_%d.wav" % (output_base, datetime.now().strftime("%Y%m%d%H%M"), i)
        # try-retry from http://stackoverflow.com/a/2083996
        while True:
            try:
                t = Playback(input_file, playback_device)
                t.start()
                # how to manage levels?  normalize here?  in midside?  need to watch levels manually?
                midside.record(output_file, recording_device, t.samps, 44100)
                input_file = output_file
            except PortAudioError:
                continue
            break
