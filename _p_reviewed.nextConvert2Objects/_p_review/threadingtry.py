import threading, time
print('start of program')
def takanap():
    time.sleep(5)
    print('Wake up!')

threadobj = threading.Thread(target=takanap)
threadobj.start()

print('end of program')
