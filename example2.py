#!/usr/bin/env python


from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import numpy
import scipy.io.wavfile as wav
import os
numpy.set_printoptions(threshold=numpy.nan)

directory = "/Users/annashaverdian/Downloads/ABSounds/KasiosWavs"
csvfile = open('/Users/annashaverdian/Downloads/ABSounds/mfcc_wavs.csv', 'w')

for filename in os.listdir(directory):
    (rate,sig) = wav.read(directory+"/"+filename)
    #print(rate)
    #print(sig)
    mfcc_feat = mfcc(sig,rate)
    d_mfcc_feat = delta(mfcc_feat, 2)
    fbank_feat = logfbank(sig,rate)
    csvfile.write(filename+','+str(fbank_feat[1:3,:])+'\n')
    #print(filename+','+str(fbank_feat))

csvfile.close()
