from draw import draw_signal
from cosine_wave import generate_cosine_signal
from sino_waves import generate_sinusoidal_signal
from comparesignals import SignalSamplesAreEqual


button = 2
if button == 1:
    draw_signal("signal1.txt",'m')
elif button == 2:
    t,sig = generate_sinusoidal_signal(3,1.96349540849362,360,720,1)
    SignalSamplesAreEqual("SinOutput.txt",0,sig)
else:
    t,sig = generate_cosine_signal(3,2.35619449019235,200,500,1)
    SignalSamplesAreEqual("CosOutput.txt",0,sig)