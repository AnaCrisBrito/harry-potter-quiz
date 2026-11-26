import os
import time
import re

perguntas = [
    {
        "pergunta" : "1. Qual é o nome da coruja de estimação de Harry Potter?",
        "opcoes": [
            "A) Edwiges" ,
            "B) Pichitinho", 
            "C) Errol", 
            "D) Bichento"
        ],
        "resposta": "A",
        "pontuacao": 1,
        "nivel": "Fácil"
    },
    
    {
        "pergunta" : "2. Qual é o número da plataforma de embarque para o Expresso de Hogwarts?",
        "opcoes": [
            "A) Plataforma 8 ½" , 
            "B) Plataforma 9 ¾", 
            "C) Plataforma 10 ¼", 
            "D) Plataforma 7 ¾"],
        "resposta": "B",
        "pontuacao": 1,
        "nivel": "Fácil"
    },
    
     {
            "pergunta": "3. Quais são as quatro casas da Escola de Magia e Bruxaria de Hogwarts?",
            "opcoes": [
                "A) Grifinória, Sonserina, Corvinal e Lufa-Lufa",
                "B) Grifinória, Sonserina, Beauxbatons e Durmstrang",
                "C) Grifinória, Lufa-Lufa, Ilvermorny e Corvinal",
                "D) Sonserina, Corvinal, Azkaban e Lufa-Lufa"
            ],
            "resposta": "A",
            "pontuacao": 1,
            "nivel": "Fácil"
        },
        {
            "pergunta": "4. Qual é a posição de Harry Potter no time de Quadribol da Grifinória?",
            "opcoes": [
                "A) Artilheiro", 
                "B) Batedor", 
                "C) Goleiro", 
                "D) Apanhador"
            ],
            "resposta": "D",
            "pontuacao": 1,
            "nivel": "Fácil"
        },
        {
            "pergunta": "5. Qual feitiço é utilizado para desarmar o oponente, fazendo sua varinha voar longe?",
            "opcoes": [
                "A) Estupefaça", 
                "B) Expelliarmus", 
                "C) Accio", 
                "D) Petrificus Totalus"
            ],
            "resposta": "B",
            "pontuacao": 1,
            "nivel": "Fácil"
        },
        {
            "pergunta": "6. Qual poção garante sorte extraordinária a quem a bebe por um período limitado?",
            "opcoes": [
                "A) Poção Polissuco", 
                "B) Amortentia", 
                "C) Felix Felicis", 
                "D) Veritaserum"
            ],
            "resposta": "C",
            "pontuacao": 2,
            "nivel": "Médio"
        },
        {
            "pergunta": "7. Quem deu o Mapa do Maroto para Harry Potter?",
            "opcoes": [
                "A) Remo Lupin", 
                "B) Sirius Black", 
                "C) Fred e Jorge Weasley", 
                "D) Alvo Dumbledore"
            ],
            "resposta": "C",
            "pontuacao": 2,
            "nivel": "Médio"
        },
        {
            "pergunta": "8. Qual é o nome do pub localizado no vilarejo de Hogsmeade famoso por sua cerveja amanteigada?",
            "opcoes": [
                "A) Caldeirão Furado", 
                "B) Três Vassouras", 
                "C) Cabeça de Javali", 
                "D) Dedosdemel"
            ],
            "resposta": "B",
            "pontuacao": 2,
            "nivel": "Médio"
        },
        {
            "pergunta": "9. Qual criatura mágica só pode ser vista por pessoas que já testemunharam a morte de perto?",
            "opcoes": [
                "A) Hipogrifo", 
                "B) Testrálio", 
                "C) Tronquilho", 
                "D) Basilisco"
            ],
            "resposta": "B",
            "pontuacao": 2,
            "nivel": "Médio"
        },
        {
            "pergunta": "10. Quem foi o professor de Defesa Contra as Artes das Trevas no segundo ano de Harry em Hogwarts?",
            "opcoes": [
                "A) Quirino Quirrell", 
                "B) Remo Lupin", 
                "C) Gilderoy Lockhart", 
                "D) Olho-Tonto Moody"
            ],
            "resposta": "C",
            "pontuacao": 2,
            "nivel": "Médio"
        },
        {
            "pergunta": "11. Qual é a forma corpórea do Patrono de Severo Snape?",
            "opcoes": [
                "A) Uma corça", 
                "B) Um cervo", 
                "C) Um lobo", 
                "D) Uma raposa"
            ],
            "resposta": "A",
            "pontuacao": 4,
            "nivel": "Intermediário"
        },
        {
            "pergunta": "12. Qual objeto da casa Lufa-Lufa foi transformado em uma das Horcruxes de Voldemort?",
            "opcoes": [
                "A) Um medalhão", 
                "B) Uma taça", 
                "C) Um diadema", 
                "D) Um anel"
            ],
            "resposta": "B",
            "pontuacao": 4,
            "nivel": "Intermediário"
        },
        {
            "pergunta": "13. Qual é o verdadeiro nome do príncipe mestiço, antigo dono do livro de Poções usado por Harry?",
            "opcoes": ["A) Tom Riddle", 
                       "B) Régulo Black", 
                       "C) Severo Snape", 
                       "D) Bartô Crouch Jr."
            ],
            "resposta": "C",
            "pontuacao": 4,
            "nivel": "Intermediário"
        },
        {
            "pergunta": "14. Qual dragão Harry enfrentou na primeira tarefa do Torneio Tribruxo?",
            "opcoes": [
                "A) Meteoro-Chinês", 
                "B) Verde-Galês Comum", 
                "C) Focinho-Curto Sueco", 
                "D) Rabo-Córneo Húngaro"
                ],
            "resposta": "D",
            "pontuacao": 4,
            "nivel": "Intermediário"
        },
        {
            "pergunta": "15. Qual é a senha para entrar na sala do diretor Alvo Dumbledore no segundo livro?",
            "opcoes": [
                "A) Sorvete de Limão", 
                "B) Sapo de Chocolate", 
                "C) Feijõezinhos de Todos os Sabores", 
                "D) Delícias Gasosas"
            ],
            "resposta": "A",
            "pontuacao": 4,
            "nivel": "Intermediário"
        },
        {
            "pergunta": "16. Qual é o nome do meio completo de Alvo Dumbledore?",
            "opcoes": [
                "A) Percival Wulfrico Brian",
                "B) Aberforth Wulfrico Percival",
                "C) Percival Aberforth Brian",
                "D) Wulfrico Godric Percival"
            ],
            "resposta": "A",
            "pontuacao": 8,
            "nivel": "Difícil"
        },
        {
            "pergunta": "17. Qual era o nome da mãe de Lord Voldemort?",
            "opcoes": [
                "A) Mérope Gaunt", 
                "B) Hepzibah Smith", 
                "C) Andrômeda Tonks", 
                "D) Kendra Dumbledore"
            ],
            "resposta": "A",
            "pontuacao": 8,
            "nivel": "Difícil"
        },
        {
            "pergunta": "18. Em que data exata ocorreu a Batalha de Hogwarts?",
            "opcoes": [
                "A) 31 de outubro de 1997",
                "B) 2 de maio de 1998",
                "C) 31 de julho de 1998",
                "D) 1º de setembro de 1997"
            ],
            "resposta": "B",
            "pontuacao": 8,
            "nivel": "Difícil"
        },
        {
            "pergunta": "19. Qual é o núcleo da varinha de Belatriz Lestrange, segundo o Sr. Olivaras?",
            "opcoes": [
                "A) Pelo de unicórnio",
                "B) Pena de fênix",
                "C) Fibra de coração de dragão",
                "D) Cabelo de Veela"
            ],
            "resposta": "C",
            "pontuacao": 8,
            "nivel": "Difícil"
        },
        {
            "pergunta": "20. Qual foi o cargo ocupado por Kingsley Shacklebolt logo após o fim da Segunda Guerra Bruxa?",
            "opcoes": [
                "A) Diretor de Hogwarts",
                "B) Chefe do Departamento de Execução das Leis da Magia",
                "C) Ministro da Magia",
                "D) Chefe dos Aurores"
            ],
            "resposta": "C",
            "pontuacao": 8,
            "nivel": "Difícil"
        }
]


#"Tela" de inicio 
print("=" * 50)
print(" HARRY POTTER QUIZ".center(50))
print("=" * 50)

print("\nVocê conhece o mundo bruxo?")
print("\nPrepare-se para testar seus conhecimentos \nsobre Hogwarts!\n")

print("-" * 50)

while True:
  nome = input("Digite seu nome: ").strip()

  if not nome:
    print("O nome não pode ficar vazio.")
    continue

  if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*", nome):
    print("Digite um nome válido (apenas letras e espaços).")
    continue

  break

print("=" * 50)


time.sleep(.5)
os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 50)
print("INSTRUÇÕES".center(50))
print("=" * 50)

print("\n1. O quiz possui 20 perguntas. \n2. Cada pergunta possui quatro alternativas. \n3. Existem quatro níveis de dificuldade. \n4. Cada nível possui uma pontuação diferente. \n5. Você receberá o resultado após cada resposta.\n")

print("-" * 50)

print("\nPontuação por dificuldade:")
print("Fácil           : 1 ponto \nMédio           : 2 pontos \nIntermediário   : 4 pontos \nDifícil         : 8 pontos\n")

print("-" * 50)


while True:
    iniciar = input("Quando estiver preparado digite INICIAR\n: ").upper().strip()
    if iniciar in ["INICIAR"]:
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        input("Quando estiver preparado digite INICIAR\n: ").upper().strip()
    
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')

pontuacao = 0
respostasCertas = 0
respostasErradas = 0
facilCertas = 0
medioCertas = 0
intermediarioCertas = 0
dificilCertas = 0

for  index, pergunta, in enumerate(perguntas):
    print("=" * 50)
    print(f"Pergunta {index + 1} de {len(perguntas)}".center(50))
    print("=" * 50)
    
    print(f"\nNível: {pergunta['nivel']}")
    print(f"Vale: {pergunta["pontuacao"]} ponto.\n")
    
    print(f"{pergunta["pergunta"]}\n")
    
    
    for opcoes in pergunta["opcoes"]:
        print(opcoes)
      
    while True:
        resposta = input("\nDigite a letra de sua resposta: ").upper().strip()

        if resposta in ["A", "B", "C", "D"]:
            break  # Sai do loop apenas se a resposta for válida
        else:
            print("Resposta inválida! Digite A, B, C ou D.")
    
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear') 

    if resposta == pergunta["resposta"]:
        print("=" * 50)
        print(f"✅  RESPOSTA CORRETA!".center(50)) 
        print("=" * 50)
        
        print("\nParabéns! Você acertou!")
        
        print(f"\n+{pergunta["pontuacao"]} ponto")
        
        pontuacao += pergunta["pontuacao"]  
        respostasCertas += 1   
        
        print(f"\nPontuação atual: {pontuacao}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear') 
    else:
        print("-" * 50)
        print(f"❌ RESPOSTA INCORRETA!".center(50))  
        respostasErradas += 1
        print("=" * 50)
        
        print("\nQue pena! Essa não era a resposta correta.")
        print(f"\nResposta correta: {pergunta["resposta"]}")
        print(f"\nPontuação atual: {pontuacao}")
        
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    break
      
print("=" * 50)
print("MURAL DE HOGWARTS".center(50))
print("=" * 50)

print(f"JOGADOR: {nome}")
print("-" * 50)

print("Resultado Final".center(50))



   