class Vertex:
 
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.edges = {}
    
    def addEdge(self, desc, dest):
        self.edges[desc] = dest

    def visit(self):
        print(self)
        c = input(" > ")

        if c == 'inspect':
            print(f"{self.secret}\n")
            self.desc = f"{self.desc}\n{self.secret}"
            self.visit()
        elif c in self.edges:
            self.edges[c].visit()
        else:
            self.visit()
 
    def __str__(self):
        edges = [ f"{key} - {self.edges[key].title}" for key in self.edges]
        return f"{self.title}\n{self.desc}\n\n{str(edges)}"


if __name__ == "__main__":

    loop = 4
    # vertex dummy, para testes
    dummy = Vertex("Dummy", "Dummy")

    # Create your house vertex/location
    casa = Vertex("Casa dos Moretti", "Você está dentro da casa dos Moretti.")
    # vertex do quarto
    quarto = Vertex("Quarto de Klein Moretti", "Você está dentro do quarto de Klein.")
    # Create the Edge that connects your house to your yard.
    casa.addEdge("sair do apartamento", dummy)
    casa.addEdge("entrar no seu quarto", quarto)
    # Create the Edge that connects your yard to your house.
    quarto.addEdge("sair", casa)
    
    while True:
        # loop inicial, inicio de história
        while loop == 4:
            if loop == 4:
                print("---------------------------------------------------------")
                print("Escuridão.\nEntão, dor.\n\n")
                print("Uma dor violenta pulsa em suas têmporas, como se seu crânio estivesse sendo aberto de dentro.")
                second = input(" O que você faz (Examinar o revolver/Procurar por pistas no quarto/sair do quarto)? > ")

            if second.lower() == "examinar o revolver":
                print("---------------------------------------------------------")
                print("Você examina o revolver e percebe que ele está descarregado.")
                loop = 3
