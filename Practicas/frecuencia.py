import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
import thinkplot

senalUno = SinSignal(freq=380, amp=0.1, offset=0)
senalDos = SinSignal(freq=200, amp=1, offset=0)

mezcla = senalUno + senalDos

waveMezcla = mezcla.make_wave(duration=2, start=0, framerate=44100)
waveMezcla.plot()
decorate(xLabel="Tiempo (s)")
thinkplot.show()

espectro = waveMezcla.make_spectrum()
espectro.plot()
decorate(xLabel="Frecuencia (Hz)")
thinkplot.show()