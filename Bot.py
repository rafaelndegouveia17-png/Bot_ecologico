import discord
import random
import asyncio
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$tempo_decompor'):
        tempos = {
            "Papel": "1 a 4 meses (média ~3 meses)",
            "Jornal": "2 a 6 semanas",
            "Cascas de banana": "2 a 12 meses",
            "Chiclete": "~5 anos",
            "Lata de alumínio": "100 a 500 anos",
            "Garrafas plásticas": "200 a 450 anos",
            "Pilhas": "100 a 500 anos",
            "Vidro": "Tempo indeterminado (pode ultrapassar milhares de anos, não se decompõe naturalmente)"
        }
        random_tempo = random.choice(list(tempos.keys()))
        await message.channel.send(f"O tempo de decomposição de {random_tempo} é: {tempos[random_tempo]}")

    if message.content.startswith('$dicas_agua'):
        dicas = [
            "Feche a torneira enquanto escova os dentes.",
            "Tome banhos mais curtos.",
            "Conserte vazamentos em torneiras e canos.",
            "Use baldes para lavar o carro em vez de mangueiras.",
            "Regue as plantas durante as horas mais frescas do dia."
        ]
        dica_aleatoria = random.choice(dicas)
        await message.channel.send(f"Dica para economizar água: {dica_aleatoria}")
    if message.content.startswith("$cor das lixeiras"):
        cores = {
            "azul":"papel",
            "verde":"vidro",
            "amarelo": "metal", 
            "vermelho":"plástico",
            "cinza": "Não reciclável",
            "marrom":"orgânico"
        }
        random_cor = random.choice(list(cores.keys()))
        await message.channel.send(f"A cor da lixeira é {random_cor} e serve para {cores[random_cor]}.")
        if message.content.startswith('$dicas_reciclagem'):
           dicas = [
                "Lave os recipientes antes de reciclá-los.",
                "Separe os materiais corretamente.",
                "Evite misturar lixo orgânico com reciclável.",
                "Reduza o uso de plástico descartável.",
                "Use jornais velhos para embalar objetos frágeis",
                "Transforme latas em porta-lápis ou luminárias criativas",
                "Reaproveite rolhas de vinho para fazer chaveiros ou murais",
                "Crie brinquedos com caixas de papelão para crianças",
                "Utilize restos de madeira para artesanato ou pequenas prateleiras",
                "Converta pneus usados em bancos ou vasos de jardim",
                "Reaproveite CDs antigos como espelhos decorativos",
                "Use retalhos de tecido para criar sacolas reutilizáveis",
                "Transforme garrafas de vidro em luminárias ou abajures",
                "Reutilize escovas de dentes velhas para limpeza de cantos difíceis",
                "Compre produtos feitos com material reciclado."
            ]
        dica_aleatoria = random.choice(dicas)
        await message.channel.send(f"Dica de reciclagem: {dica_aleatoria}")
    elif message.content.startswith('$funçoes'):
        funcoes = """Comandos disponíveis:  
        $dicas_agua - Receba dicas para economizar água.  
        $cor das lixeiras - Saiba a cor das lixeiras de reciclagem.
        $dicas_reciclagem - Receba dicas para reciclar melhor.
        $tempo_decompor - Descubra o tempo de decomposição de diferentes materiais.
        $jogo_recilagem - Jogue um quiz sobre reciclagem.
        """
        
        await message.channel.send(funcoes)
    elif message.content.startswith('$jogo_recilagem'):
        perguntas = {
            "Qual material deve ser colocado na lixeira azul?": "papel",
            "Qual material deve ser colocado na lixeira verde?": "vidro",
            "Qual material deve ser colocado na lixeira amarela?": "metal",
            "Qual material deve ser colocado na lixeira vermelha?": "plástico",
            "Qual material deve ser colocado na lixeira cinza?": "não reciclável",
            "Quanto tempo leva para o papel se decompor?": "1 a 4 meses",
            "Quanto tempo leva para uma lata de alumínio se decompor?": "100 a 500 anos",
            "Quanto tempo leva para uma garrafa plástica se decompor?": "200 a 450 anos",
            "Quanto tempo leva para o vidro se decompor?": "tempo indeterminado",
            "Qual é o destino correto das pilhas usadas?": "pontos de coleta específicos",
            "Qual é o destino correto dos eletrônicos antigos?": "centros de reciclagem especializados",
            "Qual é o destino correto do óleo de cozinha usado?": "pontos de coleta para reaproveitamento",
            "Qual é o destino correto das roupas em bom estado?": "doação",
            "Qual é o destino correto dos restos de comida?": "compostagem",
            "Qual é o destino correto dos medicamentos vencidos?": "farmácias e postos de coleta autorizados",
            "Qual material deve ser colocado na lixeira marrom?": "orgânico"
            }
        pergunta, resposta_correta = random.choice(list(perguntas.items()))
        await message.channel.send(pergunta)

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            resposta = await client.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            await message.channel.send(f"Tempo esgotado! A resposta correta era: {resposta_correta}.")
            return

        if resposta.content.lower() == resposta_correta:
            await message.channel.send("Resposta correta! Parabéns!")
        else:
            await message.channel.send(f"Resposta incorreta. A resposta correta era: {resposta_correta}.")
    else:
        await message.channel.send("Comando não reconhecido. Use $funçoes para ver a lista de comandos disponíveis.")

client.run("")
        
