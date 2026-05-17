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

def historia_parte1():
    print("---------------------------------------------------------")
    print("Escuridão.\nEntão, dor.\n\n")
    print("Uma dor violenta pulsa em suas têmporas, como se seu crânio estivesse sendo aberto de dentro.\n")
    print("Você se força a abrir os olhos.\n")
    print("Um quarto mal-iluminado se revela para você. Uma mesa de estudos com um livro empoeirado, papéis espalhados e o leve rastro de pólvora exala no ar.\n")
    print("O seu corpo se sente pesado, e estranho. Como se não realmente pertencesse a você.\n")
    print("De repente, memórias fragmentadas gradualmente inudam sua mente. Você se lembra de um nome: Klein Moretti.\n")
    print("O nome do corpo que você habita, o nome do homem que você é agora.\n")
    print("E outro nome: Zhou Mingrui, o nome do homem que você era antes. Um escravo corporativo da China moderna.\n")
    print("Você institivamente leva a mão ainda tremendo à testa.\n")
    print("Uma sensação estranha permeia na sua mão. Pegajoso, úmido, e quente. Sangue.\n")
    print("Na mesa de estudos, você percebe outra coisa; Um revolver.\n")

if __name__ == "__main__":

    #estado responsavel por trocar as ações
    state = "start"
    #loop da história, para controle de fluxo. De 1 a 10, ato inicial. 11 a 20, segundo ato.
    loop = 1
    # vertex dummy, para testes
    dummy = Vertex("Dummy", "Dummy")

    # vertex da casa dos Moretti, onde o protagonista acorda
    casa = Vertex("Casa dos Moretti", "Você está dentro da casa dos Moretti.")
    # vertex do quarto
    quarto = Vertex("Quarto de Klein Moretti", "Você está dentro do quarto de Klein.")
    # conectar a casa ao quarto, e o quarto à casa
    casa.addEdge("sair do apartamento", dummy)
    casa.addEdge("entrar no seu quarto", quarto)
    quarto.addEdge("sair", casa)
    

    historia_parte1()
    state = input("O que você faz (Examinar o revolver/Procurar por pistas no quarto/sair do quarto)? > ")
    while True:

        match state.lower():
            case "examinar o revolver":
                print("---------------------------------------------------------")
                print("Você examina o revolver e percebe que ele está com uma bala a menos no tambor. O cano da arma ainda fervente, o que indica que o suicído deste corpo foi recente.\n")
                state_option1 = input("O que você faz (Procurar por pistas no quarto/sair do quarto)? > ")
                if state_option1.lower() == "procurar por pistas no quarto":
                    state = "procurar por pistas no quarto"
                    continue
                elif state_option1.lower() == "sair do quarto":
                    state = "sair do quarto"
                    continue
                else:
                    print("Opção inválida, tente novamente.")
                    continue

            case "procurar por pistas no quarto":
                print("---------------------------------------------------------")
                print("Você institivamente lança o olhar ao espelho do quarto, e a figura que aparece refletida quase lhe faz gritar. É o rosto de seu corpo, com uma ferida horrenda na região das têmporas. Qualquer pessoa com uma ferida dessas certamente não seria capaz de continuar vivo.\n")
                state_option2 = input("sair do quarto)? > ")
                if state_option2.lower() == "sair do quarto":
                    state = "sair do quarto"
                    continue
                else:
                    print("Opção inválida, tente novamente.")
                    continue
            
            case "sair do quarto":
                print("---------------------------------------------------------")
                print("exemplo")
                break
        
            
            
            # if first.lower() == "examinar o revolver":
            #     print("---------------------------------------------------------")
            #     print("Você examina o revolver e percebe que ele está com uma bala a menos no tambor. O cano da arma ainda fervente, o que indica que o suicído deste corpo foi recente.\n")
            #     second = input("O que você faz (Procurar por pistas no quarto/sair do quarto)? > ")
            #     if second.lower() == "procurar por pistas no quarto":
            #         print("---------------------------------------------------------")
            #         print("Você examina o revolver e percebe que ele está com uma bala a menos no tambor. O cano da arma ainda fervente, o que indica que o suicído deste corpo foi recente.\n")
            #     loop = 2
            # elif first.lower() == "procurar por pistas no quarto":
            #     loop = 3
            #     print("---------------------------------------------------------")
            #     print("Você institivamente lança o olhar ao espelho do quarto, e a figura que aparece refletida quase lhe faz gritar. É o rosto de seu corpo, com uma ferida horrenda na região das têmporas. Qualquer pessoa com uma ferida dessas certamente não seria capaz de continuar vivo.\n")
