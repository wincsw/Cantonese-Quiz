import azure.cognitiveservices.speech as speechsdk
import pandas as pd
import time


def tts(text, name):
    print('Audio of "' + text + '"...')
    speech_config = speechsdk.SpeechConfig(
        subscription="30f36cae2d1144d48a2655dd33184124", region="eastasia"
    )

    # Note: if only language is set, the default voice of that language is chosen.
    speech_config.speech_synthesis_language = "zh-HK"  # For example, "de-DE"
    # The voice setting will overwrite the language setting.
    # The voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = "zh-HK-HiuGaaiNeural"

    audio_config = speechsdk.audio.AudioOutputConfig(filename="../" + name + ".mp3")

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )
    synthesizer.speak_text_async(text)
    print(name + ".mp3 complete \n")


word = pd.read_csv("../../Data/final_word.csv")
for i in range(word.shape[0]):
    tts(str(word.iloc[i][0]), str(word.iloc[i][4]))
    time.sleep(len(word.iloc[i][0]) ** 2 + 1)

