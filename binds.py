#pip install keyboard
import keyboard


class Binds:  
    def callback1(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[0],delay=0.001)
        keyboard.press('enter')
    def callback2(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[1],delay=0.001)
        keyboard.press('enter')
    def callback3(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[2],delay = 0.001)
        keyboard.press('enter')
    def callback4(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[3],delay = 0.001)
        keyboard.press('enter')
    def callback5(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[4],delay = 0.001)
        keyboard.press('enter')
    def callback6(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[5],delay = 0.001)
        keyboard.press('enter')
    def callback7(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[6],delay = 0.001)
        keyboard.press('enter')
    def callback8(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[7],delay = 0.001)
        keyboard.press('enter')
    def callback9(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[8],delay = 0.001)
        keyboard.press('enter')
    def callback10(self,callback):
        pyautogui.press('t')
        keyboard.write(self.text_from_entrys[9],delay = 0.001)
        keyboard.press('enter')
    
    def bind_keys(self):
        keyboard.on_press_key('f3', callback = self.callback1)
        keyboard.on_press_key('f4', callback = self.callback2)
        keyboard.on_press_key('f5', callback = self.callback3)
        keyboard.on_press_key('f6', callback = self.callback4)
        keyboard.on_press_key('f7', callback = self.callback5)
        keyboard.on_press_key('f8', callback = self.callback6)
        keyboard.on_press_key('f9', callback = self.callback7)
        keyboard.on_press_key('f10', callback = self.callback8)
        keyboard.on_press_key('f11', callback = self.callback9)
        keyboard.on_press_key('f12', callback = self.callback10)
    
    
    
      
   
