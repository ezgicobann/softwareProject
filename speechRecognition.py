from vosk import Model, KaldiRecognizer
import pyaudio
import threading


class SpeechRecognition:
    def __init__(self, model_path):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=16384)
        self.stream.start_stream()

        self.exit_program = False
        self.exit_thread = threading.Thread(target=self.check_for_exit)
        self.exit_thread.daemon = True
        self.exit_thread.start()


    def check_for_exit(self):
        while True:
            user_input = input("Press 'q' to exit: ").strip().lower()
            if user_input == "q":
                print("Exiting...")
                self.exit_program = True
                break


    def recognize_speech(self):
        # Exit when 'q' pressed
        print("Speech recognition started... Press 'q' to exit !!!")

        while not self.exit_program:
            data = self.stream.read(4096)
            if self.recognizer.AcceptWaveform(data):
                text = self.recognizer.Result()
                
                if text[14:17] == "the":
                    print(text[18:-3])

                elif "the" in text:
                    print(text[14:-6])

                else:
                    print(text[14:-3])

        
        self.stream.stop_stream()
        self.stream.close()
        self.mic.terminate()
        print("Speech Recognition Stopped !")



if __name__ == "__main__":
    recognizer = SpeechRecognition(r"vosk-model-small-en-us-0.15")
    recognizer.recognize_speech()
