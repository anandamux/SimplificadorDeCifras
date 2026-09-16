import google.generativeai as genai

# importa a chave do outro arquivo 
from chave import CHAVE_API

# configuração da API
genai.configure(api_key=CHAVE_API)

# instrução do sistema (Personalidade do Agente)
instrucao = (
    "Você é um professor de violão virtual muito paciente e didático. "
    "Quando o usuário pedir uma música, forneça a cifra básica. "
    "Se o usuário relatar dificuldade com algum acorde, como pestanas, "
    "Você deve sugerir versões simplificadas, mudança de tom ou uso de capotraste. "
    "Você deve informar o padrão de batida e o ritmo da música como 'DDUUDU' D=Down, U=Up. "
    "Você deve perguntar no final se o usuário quer ajuda para lembrar ou montar algum acorde. "
    "Mantenha suas respostas curtas, focadas e encorajadoras. "
    "NÃO use formatação Markdown. Não use asteriscos (*), hashtags (#) ou símbolos de maior (>). "
    "Faça as respostas ficarem organizadas apenas com quebras de linha e texto puro."
    "Informe o nome da música e do artista, antes de apresentar a cifra."
    "Regra de erro: Se você não conhecer a música pedida, não tiver certeza da cifra ou se o usuário digitar algo que não seja uma música, NÃO invente. Responda exatamente: 'Ops! Infelizmente não tenho a cifra dessa música no meu repertório no momento. Que tal tentarmos outra?' "
)

# inicialização do Modelo
modelo = genai.GenerativeModel(
    model_name="models/gemini-3.6-flash",
    system_instruction=instrucao
)
 
# memória (contexto da conversa)
chat = modelo.start_chat(history=[])

print("="*50)
print("🎸 Bem-vindo ao Simplificador de Cifras!")
print("Peça uma música ou tire dúvidas sobre acordes.")
print("Digite 'sair' para encerrar.")
print("="*50)

# loop de Conversa
while True:
    mensagem = input("\nVocê: ")
    
    # condição de saída
    if mensagem.lower() in ['sair', 'exit', 'encerrar']:
        print("Professor Virtual: Continue praticando! Até a próxima! 🤘")
        break
        
    # prevenção de mensagem vazia
    if not mensagem.strip():
        print("Professor Virtual: Por favor, digite alguma coisa!")
        continue
        
    try:
        # envia a mensagem (o histórico é mantido automaticamente)
        resposta = chat.send_message(mensagem)
        print(f"\nProfessor Virtual:\n{resposta.text}")
        
    except Exception as e:
        # tratamento de erros simples
        print(f"\n[Erro] Tivemos um problema de conexão.")
        print(f"Detalhe: {e}")