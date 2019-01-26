from collections import deque
import audioop
import os
import subprocess

import pyaudio
from pocketsphinx import pocketsphinx
import pyttsx3

FORMAT = pyaudio.paInt16
SAMPLE_WIDTH = pyaudio.get_sample_size(FORMAT)
SAMPLE_RATE = 16000
CHUNK = 2048

buffer_duration = CHUNK / SAMPLE_RATE
pre_length = int(0.3 / buffer_duration + 1)
post_length = int(0.8 / buffer_duration + 1)

engine = pyttsx3.init()

class Speech:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.threshold = 300
        self.calibrated = False
        self.stream = self.open_stream()

    def open_stream(self):
        stream = self.p.open(
            channels=1, format=FORMAT, rate=SAMPLE_RATE,
            frames_per_buffer=CHUNK,
            input=True
        )
        return stream

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def calibrate(self, duration=1):
        print("Calibrating.", end="", flush=True)
        for _ in range(int(duration / buffer_duration)):
            buffer = self.stream.read(CHUNK, exception_on_overflow=False)
            power = audioop.rms(buffer, SAMPLE_WIDTH)
            self.threshold = self.threshold * 0.8 + power * 0.3
            print(".", end="", flush=True)
        print()
        self.calibrated = True
        print("Calibrated to", self.threshold)

    def listen(self, grammar=None):
        while True:
            audio = self.hear()
            text = self.parse(audio, grammar=grammar)
            if text is not None:
                print(text)
                return text
            print("Unknown audio")
            self.say("repeat phrase")

    def hear(self):
        if not self.calibrated:
            self.calibrate()

        waiting = True
        silence_num = 0
        speech_num = 0
        frames = deque()
        print("Listening.", end="", flush=True)
        while True:
            buffer = self.stream.read(CHUNK, exception_on_overflow=False)
            if len(buffer) == 0:
                break
            frames.append(buffer)
            power = audioop.rms(buffer, SAMPLE_WIDTH)

            if waiting:
                print(".", end="", flush=True)
                if len(frames) > pre_length:
                    frames.popleft()
                if power > self.threshold:
                    waiting = False
                    print()
                    print("Detected.", end="", flush=True)
                self.threshold = self.threshold * 0.8 + power * 0.3
            else:
                print(".", end="", flush=True)
                speech_num += 1
                if power > self.threshold:
                    silence_num = 0
                else:
                    silence_num += 1
                if silence_num > post_length:
                    if speech_num - silence_num >= pre_length:
                        print()
                        break
                    else:
                        waiting = True
                        silence_num = 0
                        speech_num = 0
                        frames = deque()
                        print()
                        print("Listening.", end="", flush=True)

        for _ in range(silence_num - post_length):
            frames.pop()
        return b"".join(list(frames))

    def parse(self, raw_audio, grammar=None):
        root = os.path.dirname(os.path.normpath(__file__))
        model_dir = os.path.join(root, "pocketsphinx")
        hmm = os.path.join(model_dir, "en-us")
        lm = os.path.join(model_dir, "en-us.lm")
        dict = os.path.join(model_dir, "cmudict.dict")

        config = pocketsphinx.Decoder.default_config()
        config.set_string("-hmm", hmm)
        config.set_string("-dict", dict)
        config.set_string("-logfn", os.devnull)

        if grammar is not None:
            grammar_file = os.path.join(root, grammar)
            if not os.path.isfile(grammar_file):
                raise IOError("missing grammar file")
            config.set_string("-jsgf", grammar)
        else:
            config.set_string("-lm", lm)

        decoder = pocketsphinx.Decoder(config)
        decoder.start_utt()
        decoder.process_raw(raw_audio, False, True)
        decoder.end_utt()

        text = decoder.hyp()
        if text is None:
            return None
        return text.hypstr

    def say(self, text):
        print(text)
        engine.say(text)
        engine.runAndWait()
