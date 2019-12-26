import os, shutil

for folder, sub, file in os.walk('/home/kishore/backup'):
    try:
        os.unlink('/home/kishore/backup/var/lib/dkms/btusb-dw1802/1.0/build/btusb.c')
    except:
        shutil.rmtree(folder)
