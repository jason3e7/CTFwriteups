import sys, socket, hashlib, re, gmpy2

def findStr (input1, input2):
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

def count (input1, input2):
	print("Range size = " + str(input1 - input2))
	count = 0
	for i in range(input2, input1 + 1):
		if gmpy2.is_prime(i):
			count += 1
		elif gmpy2.is_power(i):
			count += 1
	print("Count = " + str(count))
	return count	

def getSocketData(s, tails):
	data = ""
	while True:
		for tail in tails:
			if tail in data:
				return data
		data += s.recv(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('secuprim.asis-ctf.ir', 42738))
#print s.recv(1024)
inputString = getSocketData(s, ["Enter X:"])
#inputString = s.recv(1024)
print inputString
#pattern = "SHA256\(X + \"(*)\"\).hexdigest\(\) = \"(*)...\","
pattern = r'SHA256\(X \+ \"(.+)\"\)\.hexdigest\(\) = \"(.+)\.\.\.\",'
reSet = re.search(pattern ,inputString)
#print reSet.group(1)
#print reSet.group(2)
hashResult = findStr(reSet.group(1), reSet.group(2))
print hashResult
s.send(hashResult + '\n')
data = getSocketData(s, "---\n")
print data

while True :
	data = getSocketData(s, ["like n such", "corret!", "}"])
	print data

	if "ASIS" in data:
		print data
	
	if "corret" in data:
		print "failed"
		break
	else:
		sentence = getSocketData(s, ["that: "])
		sentence += getSocketData(s, ["\n"])
		print sentence
		b, e = re.findall("that: (\d+) <= n <= (\d+)", sentence)[0]
		numberB = int(b)
		numberE = int(e)
		#print numberB
		#print numberE
		sum = count(numberE, numberB)
		s.send(str(sum) + '\n')

