def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print(f"Contagem de {i} até {f} de {p} em {p} ")
    
    if i < f:
        c = i
        while c <= f:
            print(f"{c}", end=" ",flush=True)
            c += p
        print("FIM")
    else:
        c = i
        while c >= f:
            print(f"{c} ", end=" ", flush=True)
            c -= p
        

contador(1,10,1)
contador(10,0,2)
print("Agora e sua vez de adicionar")
ini = int(input("Adicione o inicio: "))
fi = int(input("Adicione o fim: "))
pa = int(input("Adicione o passo: "))
contador(ini,fi,pa)