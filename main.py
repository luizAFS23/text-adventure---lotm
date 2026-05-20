import time


class Historia:

    def __init__(self):
        self.state = "start"
        self.cases_usados = set()
        self.opcoes_parte1 = ["examinar o revolver", 
        "examinar o livro empoeirado", 
        "procurar por pistas no quarto", 
        "sair do quarto"]

    def gerar_menu(self):
        return "/".join(self.opcoes_parte1)

    def remover_opcao_usada(self, case):
        if case in self.opcoes_parte1:
            self.opcoes_parte1.remove(case)

    def parte1(self):
        print("---------------------------------------------------------")
        print("Escuridão.\nEntão, dor.\n\n")
        time.sleep(1)
        print("Uma dor violenta pulsa em suas têmporas, como se seu crânio estivesse sendo aberto de dentro.\n")
        time.sleep(3)
        print("Você se força a abrir os olhos.\n")
        time.sleep(2)
        print("De repente, memórias fragmentadas gradualmente inudam sua mente. Klein Moretti... Cidadão da cidade de Tingen, condado de Awwa, Reino Loen.\nUm recém-graduando do Departamento de História da Universidade de Khoy...\n")
        time.sleep(10)
        print("O nome do corpo que você habita, o nome do homem que você é agora.\n")
        time.sleep(3)
        print("E outro nome: Zhou Mingrui, o nome do homem que você era antes. Um escravo corporativo da China moderna.\n")
        time.sleep(4)
        print("Um quarto mal-iluminado se revela para você. Em sua frente, uma mesa de estudos com um livro empoeirado, uma lâmpada de estilo ocidental clássico e o leve rastro de pólvora exala no ar.\n")
        time.sleep(9)
        print('Memórias de seus pais já falecidos, seu irmão e irmã que moram com você, a fé de sua família na Deusa de Toda Noite, e a difícil situação financeira dos Moretti completam as visões.\n')
        time.sleep(9)
        print("O seu corpo se sente pesado, e estranho. Como se não realmente pertencesse a você.\n")
        time.sleep(4)
        print('Na sua lateral, uma janela aberta que revela uma Lua vermelho-escarlate, grande e brilhante.')
        time.sleep(4)
        print('Aterrorizado, você ')
        time.sleep(1)
        print("Você institivamente leva a mão ainda tremendo à testa.\n")
        time.sleep(3)
        print("Uma sensação estranha permeia na sua mão. Pegajoso, úmido, e quente. Sangue.\n")
        time.sleep(4)
        print("Na mesa de estudos, você percebe outra coisa; Um revolver.\n")
        time.sleep(3)

if __name__ == "__main__":

    #estados responsaveis por trocar as ações para cada parte da historia
    state_parte1 = "start"
    state_parte2 = "start"
    #loop da história, para controle de fluxo. De 1 a 10, ato inicial. 11 a 20, segundo ato.
    loop = 1
    
    historia = Historia()
    historia.parte1()
    state_parte1 = input(f"O que você faz ({historia.gerar_menu()})? > ")
    
    while True:

        match state_parte1.lower():
            case "examinar o revolver":
                if "examinar o revolver" not in historia.cases_usados:
                    historia.cases_usados.add("examinar o revolver")
                    historia.remover_opcao_usada("examinar o revolver")

                print("---------------------------------------------------------")
                print("Você examina o revolver e percebe que ele está com uma bala a menos no tambor. O cano da arma ainda fervente, o que indica que o suicído deste corpo foi recente.\n")
                state_option1 = input(f'que você faz ({historia.gerar_menu()})? > ')
                if state_option1.lower() == "procurar por pistas no quarto":
                    state_parte1 = "procurar por pistas no quarto"
                    continue
                elif state_option1.lower() == "sair do quarto":
                    state_parte1 = "sair do quarto"
                    continue
                else:
                    print("Opção inválida, tente novamente.")
                    continue

            case "examinar o livro empoeirado":
                if "examinar o livro empoeirado" not in historia.cases_usados:
                    historia.cases_usados.add("examinar o livro empoeirado")
                    historia.remover_opcao_usada("examinar o livro empoeirado")

                print("---------------------------------------------------------")
                print("Como graduando do Departamento de História, Klein estudou línguas antigas, com foco especial em Feysac antigo, a língua que originou todas as línguas no Continente do Norte, e a língua Hermes, muito vista em mausoléus relacionados a rituais e rezas...\n")
                time.sleep(12)
                print("Ao abrir o livro, você imediatamente percebe que o mesmo está escrito na língua Hermes!\n")
                time.sleep(5)
                print('O texto em tinta preta diz: "Todos irão morrer, incluindo eu."\n')
                time.sleep(5)
                print('\x1B[3mHiss!\x1B[0m Você imediatamente fecha o livro, com o coração acelerado.\n')
                time.sleep(5)
                print("Depois de respirar fundo, você tenta investigar outros lugares.\n")
                state_option1 = input("O que você faz (Procurar por pistas no quarto/sair do quarto)? > ")
                


            case "procurar por pistas no quarto":
                if "procurar por pistas no quarto" not in historia.cases_usados:
                    historia.cases_usados.add("procurar por pistas no quarto")
                    historia.remover_opcao_usada("procurar por pistas no quarto")

                print("---------------------------------------------------------")
                print("Você institivamente lança o olhar ao espelho do quarto, e a figura que aparece refletida quase lhe faz gritar. É o rosto de seu corpo, com uma ferida horrenda na região das têmporas. Qualquer pessoa com uma ferida dessas certamente não seria capaz de continuar vivo.\n")
                print("Contudo, você percebe que a ferida está se regenerando. Se regenrando rápido. Aos poucos, ")
                state_option2 = input("sair do quarto)? > ")
                if state_option2.lower() == "sair do quarto":
                    state_parte1 = "sair do quarto"
                    continue
                else:
                    print("Opção inválida, tente novamente.")
                    continue
            
            case "sair do quarto":
                if "sair do quarto" not in historia.cases_usados:
                    historia.cases_usados.add("sair do quarto")
                    historia.remover_opcao_usada("sair do quarto")

                print("---------------------------------------------------------")
                print("Ao ir em direção à porta, outra rodada de memórias fragmentadas inundam sua mente.\n")
                print("O antigo dono deste corpo mora em um apartamento humilde, alugado em uma das partes mais pobres da cidade de Tingen.\n")
                print("Junto com Klein Moretti, moram juntos sua irmã mais nova e seu irmão mais velho Melissa e Benson Moretti.\n")
                print("Em meio aos fragmentos de memórias, você apenas percebe agora que a porta de seu quarto esteve batendo por um tempo.\n")
                print("Knock. Knock. Knock.\n")
                print('"Klein? Está tudo bem aí dentro?"\n\n')
                print("A voz de sua irmã Melissa soa do outro lado da porta, e você percebe que ela está preocupada. O cheiro de pólvora ainda exala no ar. E você percebe que a ferida em sua testa ainda não se recuperou totalmente.\n")
        
            