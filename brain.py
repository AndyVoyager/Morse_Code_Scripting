from morse_code_alph import MORSE_CODE_DICT
from pydub import AudioSegment
from pydub.playback import play
import time


def morse_convert(sent):
    """
    :param sent: A sentence to turn into the alphabet of the sea
    :return: A Morse Code
    """
    # Split the sentence into words characters:
    list_chars = []
    for char in sent.lower():
        # Check if the character is a letter or number:
        if char != " ":
            if char in MORSE_CODE_DICT:
                list_chars.append(char)
        else:
            list_chars.append("/")

    # Convert the list to Morse Code:
    morse_code_list = []
    for char in list_chars:
        if char in MORSE_CODE_DICT:
            morse_code_list.append(MORSE_CODE_DICT[char])
        else:
            morse_code_list.append(char)

    return morse_code_list


def play_morse_code(morse):
    # Add the sounds:
    short_song = AudioSegment.from_wav("sounds/point_sound.wav")
    long_song = AudioSegment.from_wav("sounds/line_sound.wav")

    # Playing sounds in relation to characters:
    for char in morse:
        if char == "•":
            play(short_song)
        elif char == "－":
            play(long_song)
        else:
            time.sleep(1)
