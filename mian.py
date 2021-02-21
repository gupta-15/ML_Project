import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.io import wavfile
from scipy.fft import fftfreq,rfftfreq,rfft
from scipy import fftpack
import scipy
import pandas as pd
rate,audio=wavfile.read(r'D:\Documents\Academics\semester VI\ES 654- ML\project\renamed data\recording0_315_1_s1_US_W_T1_P0_D1.wav')


N = audio.shape[0]
##----Distinction of low frequency and high frequency-----###
xf=rfftfreq(N,1/rate)
for i in range(len(xf)):
    if xf[i] >7000:
        index = i
        break

L = N / rate
##----FFT and separation in low spectrum and high spectrum-----###
spectrum = rfft(audio)
spectrum = np.abs(spectrum)
low_spec = spectrum[:index]
high_spec = spectrum[index:]

#######----Sum power of low frequencies-----###
p_low = np.sum(np.square(np.array(low_spec)))
#print(p_low)

#######----Sum power of high frequencies-----###
p_high = np.sum(np.square(np.array(high_spec)))
#print(p_high)

#######----Ration of the high vs low-----###
p_ratio = p_low/p_high
#print(p_ratio)

###----3 degree polynomial fit to a fft-----###
coef_3D_poly = np.polyfit(xf, spectrum, 3)
# print(coef_3D_poly)
a,b,c,d = coef_3D_poly
y_3D = d + c*xf + b*xf**2 + a*xf**3
# plt.plot(xf,y_3D)
# plt.plot(xf, spectrum)
# plt.show()

###----linear degree polynomial fit to a fft-----###
coef_linear_poly = np.polyfit(xf, spectrum, 1)
x1, x0 = coef_linear_poly
y_linear = x1*xf + x0
# plt.plot(xf,y_linear)
# plt.plot(xf, spectrum)
# plt.show()

# new = spectrum.sort()
# print(new)

##----creating csv/datafram-----## 

import os
path = "D:\\Documents\\Academics\\semester VI\\ES 654- ML\\project\\renamed data\\"
dir_list = os.listdir(path)
# print(dir_list)
data = {'audio file':dir_list}
df = pd.DataFrame(data) 
print(df.head())


'''

plt.plot(xf,spectrum)
plt.ylabel('Magnitude')
plt.xlabel('Frequency')
plt.show()

'''
'''
num = math.ceil(rate/(2*256))
bins = []
for i in range(num-1):
    bins.append(spectrum[i:i+256])
bins.append(spectrum[i:])
print(bins)
'''