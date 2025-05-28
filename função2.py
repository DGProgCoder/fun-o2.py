def login(): 
   nome = input("Crie um nome de usuário:")
   senha = input("Crie uma senha:")
   cadastro = input("digite novamente o usuário:")
   senha1 = input("digite novamente a senha:")
 
   while cadastro != nome or senha1 != senha:
         print("Tente Novamente")

   cadastro = input("digite novamente o nome de usúario:")

   senha1 = input("digite novamente a senha:")
   print ("Login bem-Sucedido!")

login()