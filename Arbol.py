class Nodo():
    def __init__(self, valor, izq=None, der=None):
        self.valor=valor
        self.izq=izq
        self.der=der


def evaluar(arbol):     
    if arbol.valor == "+":
        return (arbol.izq) + (arbol.der)
    elif arbol.valor == "-":
        return (arbol.izq) - (arbol.der)
    elif arbol.valor == "*":
        return (arbol.izq) * (arbol.der)
    elif arbol.valor == "/":
        return (arbol.izq) / (arbol.der)
    
    return int(arbol.valor)


    
from Pila import *
def inicio():
    
    pila=Pila()

    m=input("ingreso en post-orden:").split(" ")
    k=len(m)
    
    for j in range(0, k):
        y=m[j]
                
        if y in ["+", "-", "*", "/"]:
            if(len(pila.items)>=2):
                der=pila.desapilar()
                izq=pila.desapilar()
                nodo=Nodo(y, izq, der)

                x=evaluar(nodo)
                pila.apilar(x)
            else:
                print("estructura incorrecta")
        else:
            y=int(y)
            pila.apilar(y)

    print(pila.desapilar())
            

                
                
                
            
