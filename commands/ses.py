from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
 

exec = {
  "sesi kıs": {
    "exec": lambda query : (volume.SetMasterVolumeLevel(-10.0, None))  
  },
   "sesi kız": {
    "exec": lambda query : (volume.SetMasterVolumeLevel(-10.0, None)) 
  },
  "ses aç": {
    "exec": lambda query : volume.SetMasterVolumeLevel(0.0, None)  
  },
  "sesi aç": {
    "exec": lambda query : volume.SetMasterVolumeLevel(0.0, None)  
  },
   "ses kapat": {
    "exec": lambda query : (volume.SetMasterVolumeLevel(-35.0, None))  
  },
   "sesi kapat": {
    "exec": lambda query : (volume.SetMasterVolumeLevel(-35.0, None))  
  }
}