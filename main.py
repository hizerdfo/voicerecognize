import sys
import librosa
import speech_recognition as sr
import subprocess

r = sr.Recognizer()

# recognize_google() : Google Web Speech API
# recognize_google_cloud() : Google Cloud Speech API
# recognize_bing() : Microsoft Bing Speech API
# recognize_houndify() : SoundHound Houndify API
# recognize_ibm() : IBM Speech to Text API
# recognize_wit() : Wit.ai API
# recognize_sphinx() : CMU Sphinx (오프라인에서 동작 가능)

for i in range (17):
    wavplayname=('filename%d.wav' % (i))
    txtplayname=('filename%d.txt' % (i))
    srtplayname=('filename%d.srt' % (i))

    #print(srtplayname)
    #print(txtplayname)
    #print(wavplayname)

    sample_wav, rate = librosa.core.load(wavplayname)
    korean_audio = sr.AudioFile(wavplayname)

    with korean_audio as source:
        audio = r.record(source)
    sys.stdout = open(txtplayname, 'w')
    r.recognize_google(audio_data=audio, language='ko-KR')
    print(r.recognize_google(audio,language='ko-KR'))

    sys.stdout.close()


    with open(txtplayname, 'r') as f:
        for line in f:
            pass
        last_line = line

    with open(srtplayname,'w') as ff:
        ff.write('1\n')
        ff.write('00:00:00,000 --> 00:00:05,000\n')

        ff.write(last_line)

    ff.close()
    f.close()

with open('input.txt', 'w') as file:
    for i in range(17):
     file.write('file filename%d.srt\n' % (i))






subprocess.run("ffmpeg -f concat -i input.txt -c copy videoplay.srt")
    #print(last_line)