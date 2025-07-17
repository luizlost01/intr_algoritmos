dividendo = int(input("Dividendo: ")) #Pede pro usuario digitar um dividendo
divisor = int(input("Divisor: ")) #Pede pro usuario digitar um divisor
quociente = 0 #Define que o quociente é 0 
x = dividendo #Define a variavel x como dividendo 
while x >= divisor: #Equanto x for maior que o divisor
	x = x - divisor #faz x - divisor
	quociente = quociente + 1 #Faz quociente mais 1 
resto = x #Define a variavel resto como x 
print(f"O resto de {dividendo} / {divisor} é {resto}") #Impreme na tela a mensagem


#pede pro usuario um dividendo e um divisor coloca isso num loop define o x como contador 
#e imprime no final a mensagem dizendo a divisão do dividendo pelo divisor e o resto da dessa divisão que ´