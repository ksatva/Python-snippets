#MYDEVICES.py (phone/vbox/tab/..)

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