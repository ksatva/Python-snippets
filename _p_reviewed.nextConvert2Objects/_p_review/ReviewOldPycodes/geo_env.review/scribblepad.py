# get hostname by entering ip address.


import socket

def ip2host(ip):
	hostname = socket.gethostbyaddr(ip)
	return hostname

if __name__ =='__main__':
	
	for org1 in range(1,256):
		for org2 in range(1,256):
			for subnet in range(125,256):
				for machine in range(1,256):
					ip = str(org1)+'.'+str(org2)+'.'+str(subnet)+'.'+str(machine)
					try:
						hostname = ip2host(ip)				
					except:
						hostname = '-Exception-'						
					with open('ipandhost_NEW.txt','a') as f:			
						f.write(ip+'\t'+str(hostname)+'\n')
						#print('{} \t {}'.format(ip,hostname))

