import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave

import matplotlib.pyplot as plt

sonido = SinSignal(freq=440, amp=1, offset=0)

waveSonido = sonido.make_wave(duration=1, start=0, framerate=44100)

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")
#waveSonido.plot()
#plt.show()

waveSonido.write("sonido_original.wav")

print(type(waveSonido))
print("inicio " + str(waveSonido.start))
print("duracion " + str(waveSonido.duration))
print("frecuencia de muestreo " + str(waveSonido.framerate))

waveSonido.framerate = waveSonido.framerate / 2

waveSonido.write("sonido_modificado.wav")

print("frecuencia de muestreo modificado: " + str(waveSonido.framerate))

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")
#waveSonido.plot()
#plt.show()

campana = read_wave('dsp-recursos/18871__zippi1__sound-bell-440hz.wav')
segmentoCampana = campana.segment(8,1)

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")
campana.plot()
plt.show()

segmentoCampana.write("campana_original.wav")
segmentoCampana.framerate = segmentoCampana.framerate / 2
segmentoCampana.write("campana_modificado.wav")