import urllib.request
import random

#nome = input("seu nome: ")

#req = urllib.request.Request(url='http://iglicky.pythonanywhere.com/name/' + nome)
#with urllib.request.urlopen(req) as f:
#    print(f.read().decode('utf-8'))

x=0
erro=0
cores=["vermelho","amarelo","verde","azul"]
diff=0
sequencia= []
sequenciac= []
while x<50:
	sequenciac.append(random.choice(cores))
	#sequencia.append(input())
	x+=1
print(sequenciac)
while erro==0:
	x=0
	sequencia=[]
	while x<diff:
		#sequencia.append(chr(random.randrange(65, 87)))
		sequencia.append(input())
		print(sequencia)
		if sequenciac[x]!=sequencia[x]:
			print("Errou a sequencia")
			exit()
		print(1)
		x+=1

	x=0
	while x<diff:
		if sequenciac[x]!=sequencia[x]:
			print("Errou a sequencia")
			erro+=1
		x+=1
	x=0

	print(diff)
	diff+=1

#req = urllib.request.Request(url='http://iglicky.pythonanywhere.com/name/' + "".join(sequencia))
#with urllib.request.urlopen(req) as f:
#	print(f.read().decode('utf-8'))
