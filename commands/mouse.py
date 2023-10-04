from pynput.mouse import Button, Controller
mouse = Controller()
exec = {
  "aşağı kaydır": {
    "exec": lambda query : mouse.scroll(0,-15)  # Örnek bir işlem
  },
  "aşağıya kaydır": {
    "exec": lambda query : mouse.scroll(0,-15)  # Örnek bir işlem
  },
  "yukarı kaydır": {
    "exec": lambda query : mouse.scroll(0,15)  # Örnek bir işlem
  },
  "yukarıya kaydır": {
    "exec": lambda query : mouse.scroll(0,15)  # Örnek bir işlem
  },
   "tıkla": {
    "exec": lambda query :{
      mouse.click(Button.left)
    }
  },
   "sol tıkla": {
    "exec": lambda query :{
      mouse.click(Button.left)
    }
  },
}