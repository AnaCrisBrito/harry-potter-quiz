# Hogwarts Quiz — Planejamento do Projeto

## 1. Sobre o projeto

O Hogwarts Quiz é um jogo interativo de perguntas e respostas sobre o universo Harry Potter, desenvolvido inicialmente em Python e executado diretamente no terminal.

O jogador deverá responder a perguntas de múltipla escolha, com quatro alternativas (A, B, C e D), acumulando pontos conforme seus acertos e o nível de dificuldade de cada pergunta.

O objetivo é desenvolver um quiz funcional, com diferentes níveis de dificuldade, sistema de pontuação e apresentação do desempenho final do jogador.

## 2. Funcionamento do jogo

O jogo seguirá o seguinte fluxo:

1. Apresentar uma mensagem de boas-vindas ao jogador.
2. Solicitar o nome do jogador.
3. Apresentar as instruções e regras do jogo.
4. Aguardar o jogador digitar "INICIAR" para começar.
5. Apresentar as perguntas individualmente, começando pelo nível fácil e avançando progressivamente.
6. Disponibilizar quatro alternativas para cada pergunta (A, B, C e D).
7. Receber e validar a resposta do jogador.
8. Informar imediatamente se a resposta está correta ou incorreta.
9. Quando a resposta estiver correta, adicionar os pontos correspondentes à dificuldade da pergunta.
10. Quando a resposta estiver incorreta, informar qual era a alternativa correta, sem adicionar pontos.
11. Ao terminar todas as perguntas, apresentar o mural com o resultado final.

As perguntas serão apresentadas em ordem fixa, seguindo a progressão dos níveis de dificuldade.

## 3. Organização das perguntas

O quiz terá 20 perguntas, divididas igualmente em quatro níveis de dificuldade.

| Nível | Quantidade de perguntas |
|-------|------------------------|
| Fácil | 5 |
| Médio | 5 |
| Intermediário | 5 |
| Difícil | 5 |
| **Total** | **20** |

Cada pergunta deverá conter as seguintes informações:

- Enunciado da pergunta;
- Quatro alternativas de resposta;
- Identificação da alternativa correta;
- Nível de dificuldade;
- Pontuação correspondente.

## 4. Sistema de pontuação

A pontuação será definida de acordo com o nível de dificuldade da pergunta.

| Nível | Pontuação por acerto |
|-------|---------------------|
| Fácil | 1 ponto |
| Médio | 2 pontos |
| Intermediário | 4 pontos |
| Difícil | 8 pontos |

Cada resposta correta adicionará os pontos correspondentes ao nível da pergunta.

Respostas incorretas não adicionarão pontos.

Com cinco perguntas em cada nível, a pontuação máxima possível será de 75 pontos.

## 5. Validação das respostas

O jogador deverá responder utilizando as alternativas A, B, C ou D.

O programa deverá diferenciar duas situações:

**Resposta correta ou incorreta:**
- Se a alternativa escolhida estiver correta, o programa informará o acerto e adicionará a pontuação correspondente.
- Se estiver incorreta, o programa informará o erro e apresentará a alternativa correta.

**Resposta inválida:**
- Caso o jogador digite uma opção diferente de A, B, C ou D, o programa solicitará uma nova resposta.
- Respostas inválidas não serão contabilizadas como erros nem como respostas concluídas.

## 6. Resultado final — Mural de Hogwarts

Ao finalizar as 20 perguntas, o programa apresentará um resumo do desempenho do jogador.

O mural deverá apresentar:

- Nome do jogador;
- Quantidade total de perguntas respondidas;
- Quantidade de acertos;
- Quantidade de erros;
- Pontuação total;
- Desempenho por nível de dificuldade.

O desempenho por dificuldade deverá mostrar:

- Quantidade de acertos em cada nível;
- Pontuação acumulada em cada nível.

As perguntas respondidas incorretamente não serão exibidas individualmente no mural.

### Classificação do jogador

A classificação será definida de acordo com a pontuação final:

| Pontuação | Classificação |
|-----------|---------------|
| 0 a 15 pontos | Trouxa em treinamento |
| 16 a 30 pontos | Aprendiz de Hogwarts |
| 31 a 55 pontos | Bruxo experiente |
| 56 a 75 pontos | Lenda de Hogwarts |

## 7. Funcionalidades da primeira versão (V1)

A primeira versão do Hogwarts Quiz deverá implementar:

1. Mensagem de boas-vindas.
2. Solicitação do nome do jogador.
3. Apresentação das regras do jogo.
4. Início do jogo mediante confirmação do jogador.
5. Exibição de 20 perguntas de múltipla escolha.
6. Organização das perguntas em quatro níveis de dificuldade.
7. Recebimento de respostas entre A e D.
8. Validação das alternativas digitadas.
9. Feedback imediato sobre as respostas.
10. Apresentação da alternativa correta quando houver erro.
11. Cálculo automático da pontuação.
12. Contabilização dos acertos por nível de dificuldade.
13. Apresentação do mural com o resultado final.

## 8. Tecnologias e ambiente de desenvolvimento

- Linguagem: Python.
- Ambiente de execução: Terminal.
- Editor de código: Visual Studio Code.
- Versionamento: Git e GitHub.

## 9. Possíveis evoluções futuras

Após a conclusão da primeira versão, o projeto poderá receber melhorias, como:

- Embaralhamento das perguntas.
- Opção para jogar novamente.
- Exibição das perguntas que o jogador errou.
- Armazenamento do histórico de pontuações em arquivo.
- Criação de um ranking de jogadores.
- Desenvolvimento de uma interface gráfica utilizando Python.

Essas melhorias não fazem parte do escopo inicial da V1.

---

**Status do projeto:** Planejamento concluído.

**Próxima etapa:** Desenvolvimento da primeira versão (V1).