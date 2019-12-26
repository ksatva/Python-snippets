import os
from MYDEVICESsignature import DEVICEid, COMMANDSn

"""FOR TROUBLESHOOT
DEVICEid = {
	1 : 'L3460-Gentoo', ## testing from this base --> other devices
	2 : 'ubuntu_dev',
	3 : 'ASUS_phone',
	4 : 'kali_dojo'
}

#ssh from one device to another
COMMANDS = {
	'ssh_1t2' : 'konsole --noclose -e ssh -p 3022 k@127.0.0.1',
	'ssh_1t3' : 'konsole --noclose -e ssh -p 2222 ASUS-X01AD-k@192.168.43.95',
	'ssh_1t4' : 'konsole --noclose -e ssh -p 3022 k@127.0.0.1', #xxxxx
	
	'ssh_2t1' : "gnome-terminal -x bash -c 'ssh -p 22 root@192.168.43.133'; exec bash'",
	'ssh_2t3' : "gnome-terminal -x bash -c 'ssh -p 2222 ASUS-X01AD-k@192.168.43.95; exec bash'",
	'ssh_2t4' : '', #xxxx
	
	'ssh_3t1' : '', #xxxx
	'ssh_3t2' : '', #xxxx
	'ssh_3t4' : '', #xxxx
	
	'ssh_4t1' : 'ssh -p 22 root@192.168.43.133', #xxxx
	'ssh_4t2' : 'ssh -p 3022 k@127.0.0.1', #xxxx
	'ssh_4t3' : 'ssh -p 2222 ASUS-X01AD-k@192.168.43.95' #xxxx
	#'ssh_'
}
"""


class _ssh():
    def __init__(self,devicex):
        self.device = devicex
		
		#initial test checks if device is listed in database
        if self.device in DEVICEid.values():
            print("PASS: Device identified.")
        else:
            return None#"Unidentified Device"
		
        ##write code to to know the host (self system)
        #.
        #.
        #OR
        ##***WRITE LOGIC FOR CHOOSING FROM 'COMMANDS'
        self.command = 'ssh_1t3' 

        ##COMMAND FROM L3460-Gentoo
        if self.command in COMMANDS:
	  	#pass
          # open a terminal and execute the command
          commandexec = COMMANDS[self.command]
            
          print(commandexec)
          #execute
          #try:
          os.system(commandexec)
          #print("ssh success")
          #except:
          #print("!!! UNSUCCESSFUL")
            
 






        
### main()
#obj = _ssh('ubuntu_dev')


"""TODO
1. Obtain unique signature of the host system (setecting ssh source)
2. (Advanced) find install terminal (konlose/xterm/gnome-terminal???)
           dynamically assign header to 'ssh command'
3. Then select 'ssh destination'
4. ssh connection success <--target>
"""



