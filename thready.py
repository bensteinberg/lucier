from threading import Thread
import sounddevice as sd
import soundfile as sf


class Playback(Thread):
    def __init__(self, input_file, device):
        Thread.__init__(self)

        (self.inp, self.fs) = sf.read(input_file)
        self.device = device
        self.samps = len(self.inp)

    def run(self):
        sd.play(self.inp, self.fs, device=self.device)
        sd.wait()
