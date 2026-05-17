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
            self.visit()
        elif c in self.edges:
            self.edges[c].visit()
        else:
            self.visit()
 
    def __str__(self):
        edges = [ f"{key} - {self.edges[key].title}" for key in self.edges]
        return f"{self.title}\n{self.desc}\n\n{str(edges)}"

if __name__ == "__main__":

 # Create your house vertex/location
 casa = Vertex("Casa dos Moretti", "Você está dentro da casa dos Moretti.")
 # vertex do quarto
 quarto = Vertex("Quarto de Klein Moretti", "Você está dentro do quarto de Klein.")
 
 # Create the Edge that connects your house to your yard.
 casa.addEdge("sair do apartamento", tingen)
 casa.addEdge("entrar no seu quarto", quarto)
 # Create the Edge that connects your yard to your house.
 quarto.addEdge("sair", casa)
 
 # Start the game, by visiting your house.
 quarto.visit()