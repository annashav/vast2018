#!/usr/bin/env python


from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import os


directory = "/Users/annashaverdian/Downloads/ABSounds/ABWavs"
csvfile = open('/Users/annashaverdian/Downloads/ABSounds/mfcc_wavs.csv', 'r')
#parsedfile = open('/Users/annashaverdian/Downloads/ABSounds/mfcc_wavs_parsed.csv', 'w')

with csvfile as f:
    for x in f:
        print(x)
        firstrow = x.split(".wav,")
        birdID = firstrow[0]
        print(birdID.split("111"))

        if firstrow[1] == "[[-36.04365339 -36.04365339 -36.04365339 -36.04365339 -36.04365339":
            nextBad = next(f)
            while(
            endBad = nextBad.split("]]")
        else
            break
            print(birdID+','+
            #parsedfile.write(birdID+','+ feature); 
        break


#for filename in os.listdir(directory):
#    (rate,sig) = wav.read(directory+"/"+filename)
#    mfcc_feat = mfcc(sig,rate)
#    d_mfcc_feat = delta(mfcc_feat, 2)
#    fbank_feat = logfbank(sig,rate)
#    #csvfile.write(filename+','+str(fbank_feat[1:3,:])+'\n')
#    print(filename+','+str(fbank_feat[2,:]))
#    break

csvfile.close()
#parsedfile.close()
