import subprocess
import pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()
import re

exec = {
    "spotify aç" : {
        "exec" : lambda query :   subprocess.run("spotify")
    },
    "müzik oynat": {
        "exec": lambda query: {
            keyboard.press(Key.media_play_pause)}
    },
    "müziği devam ettir": {
        "exec": lambda query: {
            keyboard.press(Key.media_play_pause)
        }
    },
    "müziğe devam ettir": {
        "exec": lambda query: {
            keyboard.press(Key.media_play_pause)
        }
    },
   
    "müziğe devam et": {
        "exec": lambda query: {
            keyboard.press(Key.media_play_pause)
        }
    },
   
    "müziği devam et": {
        "exec": lambda query: {
            keyboard.press(Key.media_play_pause)
        }
    },
   
    "müziği oynat": {
        "exec": lambda query: {
            keyboard.press(Key.media_play_pause)
        }
    },
      "müziği değiştir": {
        "other": ["bunu da değiştir"],
        "exec": lambda query: {
            keyboard.press(Key.media_next)
        }
    },
         "müziği değiştir sene": {
        "other": ["bunu da değiştir"],
        "exec": lambda query: {
            keyboard.press(Key.media_next)
        }
    },
    "müziği durdur": {
        "exec": lambda query: keyboard.press(Key.media_play_pause)

    },
    "müzik durdur": {
        "exec": lambda query: keyboard.press(Key.media_play_pause)

    },
    "sıradaki müziğe geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "bir sonrakine geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "bir sonrakini aç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "sıradaki müzike geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "bu müziği geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "bu müziği de geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "sıradakine geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "müziği geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "bu müziği geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "bu müziği de geç": {
        "exec": lambda query: keyboard.press(Key.media_next)

    },
    "önceki müziğe geç": {
        "exec": lambda query: {
            keyboard.press(Key.media_previous),
            keyboard.press(Key.media_previous)
        }

    },
    "önceki müzike geç": {
        "exec": lambda query: {
            keyboard.press(Key.media_previous),
            keyboard.press(Key.media_previous)
        }

    },
    "öncekine geç": {
        "exec": lambda query: {
            keyboard.press(Key.media_previous),
            keyboard.press(Key.media_previous)
        }

    },
    "önceki geç": {
        "exec": lambda query: {
            keyboard.press(Key.media_previous),
            keyboard.press(Key.media_previous)
        }

    },
    "bir öncekine geç": {
        "exec": lambda query: {
            keyboard.press(Key.media_previous),
            keyboard.press(Key.media_previous)
        }

    },
    "önceki güzeldi": {
        "exec": lambda query: {
            keyboard.press(Key.media_previous),
            keyboard.press(Key.media_previous)
        }

    },
    "bir önceki güzeldi": {
        "exec": lambda query: {
            keyboard.press(Key.media_previous),
            keyboard.press(Key.media_previous)
        }

    }


}
