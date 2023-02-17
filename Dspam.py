import pyautogui, time

print("[!]} Welcome to IZE Spammer!")
print("")
print("[+] CHANGELOG")
print("UPDATE 0.2")
print("------------")
print("NEW UI!")
print("")
print("")
awnser = input("[!] (y): ")

if awnser == print("y"): print("[!] Connected!")
message = input("Message: ")   
duration = input("duration: ")
repeats = input("repeats: ")
print("[!] Spamming.....")
    
print("")
print("")
print("If you want to spam again open the console again.")
print("")
print("after spamming is done it will close.")

for i in range(int(repeats)):
    pyautogui.write(message)
    pyautogui.press('enter')
