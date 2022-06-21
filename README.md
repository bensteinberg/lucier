lucier
------

Tools for realizing Alvin Lucier's *[I Am Sitting in a Room](https://en.wikipedia.org/wiki/I_Am_Sitting_in_a_Room)* using a [Blumlein pair](https://en.wikipedia.org/wiki/Blumlein_Pair) for [mid-side recording](http://www.uaudio.com/blog/mid-side-mic-recording/).

I *think* this requires two audio devices, but haven't tried it with one yet. Set up a Blumlein pair on one interface and a speaker or monitor on the other. [Install Poetry](https://python-poetry.org/docs/#installation) and identify your interfaces with `poetry run python -m sounddevice` (or use `requirements.txt` to set up a virtual environment in whatever way you like; run `poetry export -f requirements.txt --output requirements.txt` if you make any changes to `poetry.lock`).

You can record an initial track like this, after starting Python with `poetry run python`:

```
import midside
midside.record("somefile.wav", <devicenumber>, x * fs, fs)
```

where x is the number of seconds you want to record and fs is the sampling rate, usually 44100 -- or find an input file somewhere.

To record the recording x times, do this:

```
import lucier
lucier.sitting("somefile.wav", "somefile", x, <playbackdevice>, <recordingdevice>)
```

and ride the volume or gain controls so that each recording is neither too quiet nor too loud.
