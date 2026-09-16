# Simplificador de Cifras 🎸

## Sobre o Projeto

O Simplificador de Cifras é um agente conversacional desenvolvido em Python para atuar como um professor de música virtual. Ele fornece cifras, ensina ritmos e o posicionamento dos dedos, além de adaptar dinamicamente a dificuldade dos acordes em tempo real. Este projeto foi desenvolvido como trabalho prático para a disciplina de Inteligência Artificial da UFSC Araranguá, demonstrando a aplicação prática de modelos de linguagem no ensino interativo.

## Funcionalidades Principais

* **Ensino Adaptativo:** Adaptação de cifras complexas (como remoção de pestanas ou sugestão de capotraste, além de mudança do tom da música) com base no nível de habilidade e feedback do usuário.
* **Manutenção de Contexto:** Interação contínua em linguagem natural, mantendo a memória da música escolhida durante toda a conversa.
* **Prevenção de Alucinações:** Tratamento de erros de conexão e de repertório, garantindo que o agente não invente cifras para músicas desconhecidas.

## Tecnologias Utilizadas

* **Python:** Linguagem base para a estruturação da lógica do agente e do loop de conversa no terminal.
* **Google Gemini API:** Modelo de Linguagem Grande (LLM) responsável pelo processamento de linguagem natural e conhecimento musical.

## Como Executar Localmente

1. Clone este repositório em sua máquina local:
   ```bash
   git clone [https://github.com/anandamux/SimplificadorDeCifras.git](https://github.com/anandamux/SimplificadorDeCifras)

2. Instale as bibliotecas necessárias executando o comando em seu terminal:
```bash
pip install google-generativeai python-dotenv
```
3. Crie um arquivo chamado .env na raiz do projeto e insira sua chave da API no formato:
```bash
GEMINI_API_KEY=sua_chave_aqui
````
4. Inicie o agente e comece a interagir:
```bash
python agente_violao.py
