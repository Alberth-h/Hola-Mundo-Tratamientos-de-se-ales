import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

seno = SinSignal(freq=440, amp=1, offset=0)
seno2 = SinSignal(freq=340, amp=1, offset=0)
seno3 = SinSignal(freq=600, amp=0.7, offset=0)

waveSeno = seno.make_wave(duration=1, start=0, framerate=44100)
waveSeno2 = seno2.make_wave(duration=1, start=1, framerate=44100)
waveSeno3 = seno3.make_wave(duration=1, start=2, framerate=44100)

resultante = waveSeno + waveSeno2 + waveSeno3

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")

resultante.plot()

resultante.write("sonido.wav")

plt.show()