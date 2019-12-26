import subprocess  
import PySimpleGUI as sg  

#CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  
xdm = 'java -jar /root/_ToolBox/xdman.jar'

layout = [  [sg.Text('Text area', key='_TEXT_')],  
            [sg.Input(do_not_clear=True, key='_URL_')],  
            [sg.Button('xdm'), sg.Button('Exit')]]  

window = sg.Window('Window Title', layout)  

while True:     # Event Loop
    event, values = window.Read()
    print(event, values)  
    if event is None or event == 'Exit':
    	break
    if event == 'xdm':  
        sp = subprocess.Popen([xdm, values['_URL_']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  

window.Close()