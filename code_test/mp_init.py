import numpy as np
import matplotlib.pyplot as plt
# generate data
def test_signal( n):
    # use sin as test signal
    f_si = 1      # frequency of signal
    t_si = 1.0/f_si # cycle of signal
    f_sa = 10.0*f_si# sample rate 10 times of the signal frequency
    t_sa = 1.0/f_sa # cycle of sampling
    #--------------------------------------
    t=np.arange(0,1.5, 1.0/n) # splite length is 1
    y=array([np.sin( 2*np.pi*f_si*t_i ) for t_i in t])
    return t, y

t, data=test_signal(256)
# plt.plot(t, y)
# plt.show()

# set iterative time
iterative_number=10
N = len(data)
# set
signal_reconstruct=np.zeros(N)
signal_r=data
# set
a_base=2
j_min=0
j_max=
