from gtts import gTTS
import io
from pydub import AudioSegment
from pydub.playback import play
from deep_translator import GoogleTranslator

def speak_translated_text(text, lang):
    print(text, lang)
    languages = {
        'tamil': 'ta',
        'hindi': 'hi',
        'telugu': 'te'
    }

    lang = languages[lang]

    # Translated text
    translated_text = GoogleTranslator(source="auto", target=lang).translate(text)

    """Speak translated text in different languages."""
    print(f"ASSISTANT ({lang.upper()}) -> {translated_text}")

    tts = gTTS(text=translated_text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    
    audio = AudioSegment.from_file(fp, format="mp3")
    play(audio)

