
import os

if __name__ == '__main__':
    print("Hello this Project is being built by Shivansh")
    while True:
        x = input("Enter what you want to say pls:")
        if x == "exit":
            break
        command = f'powershell -c "Add-Type –AssemblyName System.Speech; ' \
                  f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                  f'$speak.Speak(\'{x}\');"'
        os.system(command)



