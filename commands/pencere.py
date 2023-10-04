from pynput.keyboard import Key, Controller
keyboard = Controller()
import subprocess

def alt():
   keyboard.press(Key.alt_l)

def tab():
    keyboard.press(Key.tab)
def release():
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)
exec = {
  "bir önceki pencereye geç": {
    "exec": lambda query :     {
       alt(),
       tab(),
       release()
     }
  },
  "önceki pencereye geç": {
    "exec": lambda query :     {
       alt(),
       tab(),
       release()
     }
  },
 "iki önceki pencereye geç": {
    "exec": lambda query :     {
       alt(),
       tab(),
       tab(),
       tab(),
       release()
     }
   },
   "2 önceki pencereye geç": {
    "exec": lambda query :     {
       alt(),
       tab(),
       tab(),
       tab(),
       release()
     }
   },
 "üç önceki pencereye geç": {
    "exec": lambda query :     {
       alt(),
       tab(),
       tab(),
       tab(),
       tab(),
       release()
     }
   },
 "3 önceki pencereye geç": {
    "exec": lambda query :     {
       alt(),
       tab(),
       tab(),
       tab(),
       tab(),
       release()
     }
   },
  
}