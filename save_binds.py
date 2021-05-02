import os
import pickle
from tkinter import messagebox


class SaveFiles:
    @property
    def saved_binds(self):
      with open('binds.bin','rb') as f:
        return pickle.load(f)
    
    @property
    def file_exist(self):
        if 'binds.bin' in os.listdir('./'):
            return True
        else:
            return False

    def save_text(self):
         if self.file_exist:
            os.remove('binds.bin')
         with open('binds.bin','wb') as f:
           for i in range(1,10):
                binds = []
                binds.append((self.text_from_entrys[i],'f' + str(i + 3)))
                pickle.dump(self.text_from_entrys,f)
           messagebox.showinfo("Info", "All changes have been saved")
           f.close()