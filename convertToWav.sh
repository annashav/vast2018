#!/bin/sh

r="/Users/annashaverdian/Downloads/ABSounds/Kasios"
s="/Users/annashaverdian/Downloads/ABSounds/KasiosWavs"

echo "Test" + $r
echo $s


for i in "$r"/*
do
        echo "Test 2" + $i
        p="$(cut -d'/' -f7 <<<"$i")"
	n="$(cut -d'.' -f1 <<<"$p")"
	echo "Test 3" + $n
        ffmpeg -i "$i" "$s/$n.wav"
done
