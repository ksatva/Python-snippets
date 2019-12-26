
# --UNDER CONSTRUCTION 
##TO ROTATE 'USER-AGENT' and 'IP' THROUGH 'URLS'

# IP: strategy: Proxy
##for latest available proxies
# https://free-proxy-list.net/
# find more (TODO)   



#url = 'https://httpbin.org/user-agent'	

#class _search():


#input urlx, agentx
class _www():
	import requests
	from bs4 import BeautifulSoup as bs
	def __init__(self,agentx,urlx,proxies):
		self.agent = agentx    # DI: name of agent
		self.url = urlx        # DI: name of url
		self.proxies = proxies # DI: proxies

		self.headers = {'User-Agent': agentx}
		self.rdata = requests.get(urlx,headers=self.headers,proxies=self.proxies)
		
		self._data = self.rdata.content
		self.soup = bs(self._data)







"""OBSOLETE --one line code already available: 'agentx = random.choice(someList)'
class randomizer():
	import random
	def __init__(self,someList):
		self.agentx = random.choice(someList)
"""


if __name__ == "__main__":
	import random
	import inputData_userAgentLatest as di_ual
	import inputData_proxiesLatest as di_prx

	#get somelist --useragentnames
	agentList = di_ual.user_agent_list
    
    urlx = 
	agentx = random.choice(someList)
	proxies = di_prx.proxies
    
    _wwwx = _www(agentx,urlx,proxies) ##A _www object "with soup :p bs4"
    ### work more on this "content" of '_www'










