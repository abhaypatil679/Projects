import os
os.system("netsh wlan show profiles >new.txt")

with open("./new.txt") as f:
    content = f.readlines()
try:
    profiles = [content[i][27:] for i in range(10, 50)]
finally:
    profiles =[name[:-1] for name in profiles]
    # print(profiles)
    pass
os.system("netsh wlan show profile {profiles[0]} key = clear >pass.txt")
for profile in profiles:
    #print(profile)
    os.system(f'netsh wlan show profile {profile} key = clear >>pass.txt')