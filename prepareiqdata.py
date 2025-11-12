import numpy as np

iq = np.fromfile('ble_capture.iq', dtype=np.int8)

#converts to complex valued signal
iq_complex = iq[::2] + 1j * iq[1::2]

#prints first 10 samples
print(iq_complex[:10])

#could normalize with this for NN or ML usage
#x = np.stack([np.real(iq_complex), np.imag(iq_complex)], axis=1)
#x.shape = (num_samples, 2)
