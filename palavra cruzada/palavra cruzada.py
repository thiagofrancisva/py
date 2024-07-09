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

def copiar(i,lista,ref,palavrare):
    for c in range(palavrare):
        #print(c)
        letra_quadro_analise.append(lista[ref[i]+c])
        #print(letra_quadro_analise)

for x in range(8):
    if len(palavra_copia) == len(palavra):

        indice = random.randrange(0,len(palavra_copia))
        palavra_escrita.append(palavra_copia[indice])
        
        for y in range(0,len(palavra_escrita[0])):
            
            letra_escrita.append(palavra_escrita[0][y])

        #print(letra_escrita)    
        palavra_copia.remove(palavra_copia[indice])
        palavra_leitura.append(leitura[random.randrange(0,len(leitura))])
        #print(palavra_leitura)
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

        #print(palavra_escrita)

        for s in range(len(palavra_escrita)):
            
            palavra_analise = palavra_escrita[s]
            w = 0
            letra_quadro_analise = []
            copiar(s,letra_quadro_copia,indice_ref,len(palavra_escrita[s]))
            
            while w < len(palavra_copia):

                v = 0
                palavra_copia_analise = palavra_copia[w]
                #print(palavra_copia_analise)

                for i in range(len(palavra_copia_analise)):
                    
                    if palavra_leitura[s] == "v":

                        #print("if v")

                        #print(palavra_copia_analise[i:i+1])

                        if palavra_analise.count(palavra_copia_analise[i:i+1]) > 0:
                            
                            for a in range(len(palavra_analise)):
                                
                                if palavra_copia_analise[i] == palavra_analise[a] \
                                   and letra_cruzada.count(letra_quadro_analise[a]) == 0 \
                                   and quadro_invalido_h.count(letra_quadro_analise[a]) == 0:
                                            
                                        m = 0
                                        invalido = []

                                        while m < (i + 1) and invalido.count(True) == 0:

                                            sub = letra_quadro_analise[a] - (i - m)

                                            #print(invalido)
                                            
                                            if letra_quadro.count(sub) > 0 \
                                               and letra_escrita[letra_quadro.index(sub)] == palavra_copia_analise[(i-m)]:

                                                pass
                                            
                                            elif quadro_invalido.count(sub) > 0 \
                                                 or quadro_invalido.count(sub - 1) > 0 \
                                                 or letra_quadro.count(sub - 1) > 0 \
                                                 or quadro_invalido.count(sub + 100) > 0 \
                                                 or quadro_invalido.count(sub - 100) > 0 \
                                                 or quadro_invalido_h.count(sub + 100) > 0 \
                                                 or quadro_invalido_h.count(sub - 100) > 0:

                                                invalido.append(True)

                                            m += 1
                                                     
                                        while m < len(palavra_copia_analise) and invalido.count(True) == 0:

                                            soma = letra_quadro_analise[a] + abs(i - m)

                                            if letra_quadro.count(soma) > 0 \
                                               and letra_escrita[letra_quadro.index(soma)] == palavra_copia_analise[m]:

                                                pass
                                            
                                            elif quadro_invalido.count(soma) > 0 \
                                                 or quadro_invalido.count(soma + 1) > 0 \
                                                 or letra_quadro.count(soma + 1) > 0 \
                                                 or quadro_invalido.count(soma + 100) > 0 \
                                                 or quadro_invalido.count(soma - 100) > 0 \
                                                 or quadro_invalido_h.count(soma + 100) > 0 \
                                                 or quadro_invalido_h.count(soma - 100) > 0:

                                                invalido.append(True)

                                            m += 1

                                        print ("chegou")

                                        if invalido.count(True) == 0:
                                            
                                            letra_indice.append(i)
                                            letra_cruzavel_quadro.append(letra_quadro_analise[a])
                                            
                                            v += 1

                    elif palavra_escrita[s] == "h":

                        #print("if h")

                        if palavra_analise.count(palavra_copia_analise[i:i+1]) > 0:
                            
                            for a in range(len(palavra_analise)):
                                
                                if palavra_copia_analise[i] == palavra_analise[a]:
                                    
                                    if letra_cruzada.count(letra_quadro_analise[a]) == 0:
                                        
                                        if quadro_invalido_v.count(letra_quadro_analise[a]) == 0:
                                            
                                            m = 0
                                            invalido = []

                                            while m < (i + 1) and invalido.count(True) == 0:

                                                sub = letra_quadro_analise[a] - (i - m) * 100

                                                #print(invalido)
                                                

                                                if letra_quadro.count(sub) > 0 \
                                                   and letra_escrita[letra_quadro.index(sub)] == palavra_copia_analise[(i-m)]:

                                                    pass
                                                
                                                elif quadro_invalido.count(sub) > 0 \
                                                     or quadro_invalido.count(sub - 100) > 0 \
                                                     or letra_quadro.count(sub - 100) > 0 \
                                                     or quadro_invalido.count(sub + 1) > 0 \
                                                     or quadro_invalido.count(sub - 1) > 0 \
                                                     or quadro_invalido_v.count(sub + 1) > 0 \
                                                     or quadro_invalido_v.count(sub - 1) > 0:

                                                    invalido.append(True)

                                                m += 1
                                                         
                                            while m < len(palavra_copia_analise) and invalido.count(True) == 0:

                                                soma = letra_quadro_analise[a] + abs(i - m) * 100

                                                if letra_quadro.count(soma) > 0 \
                                                   and letra_escrita[letra_quadro.index(soma)] == palavra_copia_analise[m]:

                                                    pass
                                                
                                                elif quadro_invalido.count(soma) > 0 \
                                                     or quadro_invalido.count(soma + 100) > 0 \
                                                     or letra_quadro.count(soma + 100) > 0 \
                                                     or quadro_invalido.count(soma + 1) > 0 \
                                                     or quadro_invalido.count(soma - 1) > 0 \
                                                     or quadro_invalido_v.count(soma + 1) > 0 \
                                                     or quadro_invalido_v.count(soma - 1) > 0:

                                                    invalido.append(True)

                                                m += 1

                                            print("chegou")

                                            if invalido.count(True) == 0:
                                                
                                                letra_indice.append(i)
                                                letra_cruzavel_quadro.append(letra_quadro_analise[a])
                                                
                                                v += 1

                if v != 0:

                    print("if")
                    indice_palavra_copia.append(w)
                    indice_palavra_escrita.append(s)
                    letra_cruzavel_qtd.append(v)
                    
                w += 1
        
        print(letra_cruzavel_qtd)
        
##        if not letra_cruzavel_qtd:
##            palavra_copia = palavra.copy()
##            palavra_leitura = []
##            palavra_escrita = []
##            letra_escrita= []
##            letra_quadro = []
##            letra_cruzada = []
##            quadro_invalido = []
##            quadro_invalido_v = []
##            quadro_invalido_h = []
##            indice_ref = []
##            f -= f + 1
            



#print(letra_quadro)
