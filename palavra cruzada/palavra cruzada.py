import random

palavra  = ["goblin","prietess","monk","nest","maiden","knight","elf","elder","bow","arrow","sword", "armor"]
palavra_copia = palavra.copy()

leitura = ["v","h","v","h","v"]
palavra_leitura = []
indice_ref = []

palavra_escrita = []
letra_escrita = []
letra_quadro = []
letra_cruzada = []
quadro_invalido = []
quadro_invalido_v = []
quadro_invalido_h = []

def copiar(i,lista,ref,palavra):
    for x in range(len(palavra)):
        letra_quadro_analise.append(lista[ref[i]+x])

for x in range(8):
    if len(palavra_copia) == len(palavra):

        indice = random.randrange(0,(len(palavra_copia)-1))
        palavra_escrita.append(palavra_copia[indice])
        
        for y in range(0,len(palavra_escrita[0])):
            
            letra_escrita.append(palavra_escrita[0][y])
            palavra_copia.remove(palavra_copia[indice])
            palavra_leitura.append(leitura[random.randrange(0,len(leitura)-1)])
            quadro_inicial = 1050

        if palavra_leitura[0] == "v":
            
            quadro_invalido.append(quadro_inicial - 100)
            quadro_invalido.append(quadro_inicial + (len(letra_escrita) - 1) * 100)
            
            w = 0

            while w < len(letra_escrita):
                
                letra_quadro.append(quadro_inicial)
                quadro_invalido_v.append(quadro_inicial - 1)
                quadro_invalido_v.append(quadro_inicial + 1)
                quadro_inicial += 100
                
                w += 1
 
        else:
            
            quadro_invalido.append(quadro_inicial - 1)
            quadro_invalido.append(quadro_inicial + (len(letra_escrita) - 1))
         
            w = 0

            while w < len(letra_escrita):
                
                letra_quadro.append(quadro_inicial)
                quadro_invalido_h.append(quadro_inicial - 100)
                quadro_invalido_h.append(quadro_inicial + 100)
                quadro_inicial += 1

                w += 1

        indice_ref.append(0)
    
    else:
        indice_palavra_copia = []
        indice_palavra_escrita = []
        letra_cruzavel_quadro = []
        letra_cruzavel_qtd = []
        letra_quadro_copia = letra_quadro.copy()
        letra_indice = []

        for s in range(len(palavra_escrita)):
            
            palavra_analise = palavra_escrita[s].split()
            w = 0
            letra_quadro_analise = []
            copiar(s,letra_quadro_copia,indice_ref,palavra_escrita)

            #while w < len(palavra_copia):

                #v = 0
                

                
                    
                    #if palavra_leitura[s] == "v":

                    #elif palavra_escrita[s] == "h":
                #w += 1
            
        
print(letra_quadro)
