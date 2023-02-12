from  win32com.client import  Dispatch

def speakanand(str):
    speakanand= Dispatch("SAPI.SpVoice")
    speakanand.Speak(str)

if __name__ == '__main__':
    for i in range(1):
      speakanand("WELCOME ANAND SINGH  ")
