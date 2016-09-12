import sys, socket, hashlib, re

def findStr (input1, input2) :
	strSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	for s1 in range(0, len(strSet)):
		for s2 in range(0, len(strSet)):
			for s3 in range(0, len(strSet)):
				for s4 in range(0, len(strSet)):
					temp = strSet[s1]+strSet[s2]+strSet[s3]+strSet[s4]
					#print temp
					hashString = hashlib.sha256(temp + input1).hexdigest() 
					#print hashString[:10]
					if (hashString[:32] == input2) :
						#print temp
						#print hashString
						return temp

#def findStr (input1, input2) :

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('secuprim.asis-ctf.ir', 42738))
print s.recv(1024)
inputString = s.recv(1024)
print inputString
#pattern = "SHA256\(X + \"(*)\"\).hexdigest\(\) = \"(*)...\","
pattern = r'SHA256\(X \+ \"(.+)\"\)\.hexdigest\(\) = \"(.+)\.\.\.\",'
reSet = re.search(pattern ,inputString)
#print reSet.group(1)
#print reSet.group(2)
hashResult = findStr(reSet.group(1), reSet.group(2))
print hashResult
s.send(hashResult + '\n')
print s.recv(1024)
#print s.recv(1024)
numberString = s.recv(5000)
#print s.recv(1024)
print numberString
#numberString = "What's the number of primes or perfect powers like n such that: 5243269291454887441469100664450379632166513715971446363090767797743156123546121519300580839849071258764736630767760378406484795094273101304997073596485627357105933492198431259237777507988709432110022263714645521682212217307411628628958076902922410631563384500367776412842903161451250989637903182181518743726002740517362559994092779140605243592815811881190178313218604189184143277334720117905878912731423503923298943557821465938558211625137607975639497374125064389388228823883380819977773588273288320212036835950957795597201626150674157512513153850062638919746194221256104320064512157545263476047025186270716225470598690735830207192770289501288 <= n <= 5243269291454887441469100664450379632166513715971446363090767797743156123546121519300580839849071258764736630767760378406484795094273101304997073596485627357105933492198431259237777507988709432110022263714645521682212217307411628628958076902922410631563384500367776412842903161451250989637903182181518743726002740517362559994092779140605243592815811881190178313218604189184143277334720117905878912731423503923298943557821465938558211625137607975639497374125064389388228823883380819977773588273288320212036835950957795597201626150674157512513153850062638919746194221256104320064512157545263476047025186270716225470598690735830207192770289502756"
pattern = r'What\'s the number of primes or perfect powers like n such that: (.+) <= n <= (.+)'
reSet = re.search(pattern ,numberString)
#print reSet.group(1)
#print reSet.group(2)
numberB = reSet.group(2)
numberS = reSet.group(1)
print int(numberB[-6:]) - int(numberS[-6:])

s.send('1111111' + '\n')
print s.recv(1024)
s.send('1111111' + '\n')
print s.recv(1024)

#https://www.wikiwand.com/en/Alphanumeric
#PPC (Professional Programming and Coding)
