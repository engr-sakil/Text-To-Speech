from gtts import gTTS
import os

myText = '''আমার সোনার বাংলা আমি তোমায় ভালোবাসি চিরদিন  তোমার আকাশ তোমার বাতাস আমার প্রাণে বাজায় বাঁশি'''

language = 'bn'

output = gTTS(text=myText,lang=language,slow=False)

output.save("output.mp3")

os.system("start output.mp3")


languageList =  {'af': 'Afrikaans',
        'ar': 'Arabic',
        'bn': 'Bengali',
        'bs': 'Bosnian',
        'ca': 'Catalan',
        'cs': 'Czech',
        'cy': 'Welsh',
        'da': 'Danish',
        'de': 'German',
        'el': 'Greek',
        'en': 'English',
        'eo': 'Esperanto',
        'es': 'Spanish',
        'et': 'Estonian',
        'fi': 'Finnish',
        'fr': 'French',
        'gu': 'Gujarati',
        'hi': 'Hindi',
        'hr': 'Croatian',
        'hu': 'Hungarian',
        'hy': 'Armenian',
        'id': 'Indonesian',
        'is': 'Icelandic',
        'it': 'Italian',
        'ja': 'Japanese',
        'jw': 'Javanese',
        'km': 'Khmer',
        'kn': 'Kannada',
        'ko': 'Korean',
        'la': 'Latin',
        'lv': 'Latvian',
        'mk': 'Macedonian',
        'ml': 'Malayalam',
        'mr': 'Marathi',
        'my': 'Myanmar (Burmese)',
        'ne': 'Nepali',
        'nl': 'Dutch',
        'no': 'Norwegian',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'ro': 'Romanian',
        'ru': 'Russian',
        'si': 'Sinhala',
        'sk': 'Slovak',
        'sq': 'Albanian',
        'sr': 'Serbian',
        'su': 'Sundanese',
        'sv': 'Swedish',
        'sw': 'Swahili',
        'ta': 'Tamil',
        'te': 'Telugu',
        'th': 'Thai',
        'tl': 'Filipino',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'vi': 'Vietnamese',
        'zh-CN': 'Chinese'
    }
