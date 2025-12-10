♻️ Bot de Reciclagem e Sustentabilidade
Este projeto é um bot para Discord desenvolvido em Python com a biblioteca discord.py. O objetivo é promover educação ambiental de forma divertida e interativa, trazendo dicas de reciclagem, economia de água e quizzes sobre sustentabilidade.

🚀 Funcionalidades
O bot responde a diferentes comandos, cada um com uma função específica:

$tempo_decompor → Informa o tempo de decomposição de materiais comuns.

$dicas_agua → Envia dicas aleatórias para economizar água.

$cor das lixeiras → Explica a cor das lixeiras e o tipo de material correspondente.

$dicas_reciclagem → Sugere práticas criativas e úteis de reciclagem.

$funçoes → Lista todos os comandos disponíveis.

$jogo_recilagem → Inicia um quiz interativo sobre reciclagem e sustentabilidade.

🛠️ Tecnologias utilizadas
Python 3.10+

discord.py → Biblioteca para integração com o Discord.

asyncio → Para lidar com eventos assíncronos e controlar tempo limite nas respostas.

random → Para selecionar dicas e perguntas aleatórias.

📦 Instalação
Clone este repositório:

bash
git clone https://github.com/rafaelndegouveia17-png/Bot_ecologico/blob/main/Bot.py
cd bot-reciclagem
Instale as dependências:

bash
pip install discord.py
Configure o token do seu bot no arquivo principal:

python
client.run("SEU_TOKEN_AQUI")
🎮 Como usar
Inicie o bot com:

bash
python bot.py
No Discord, digite os comandos listados em Funcionalidades.

Exemplo:

Código
$tempo_decompor
$dicas_agua
$jogo_recilagem
🔧 Como modificar
Adicionar novos comandos: crie novos blocos if message.content.startswith('$comando').

Alterar dicas ou perguntas: edite as listas e dicionários (dicas, tempos, perguntas).

Mudar tempo limite do quiz: altere o valor de timeout=30.0 para o número de segundos desejado.

Personalizar mensagens: edite os textos enviados pelo bot para deixá-los mais criativos ou formais.

🌍 Objetivo
Este bot foi criado para incentivar práticas sustentáveis e tornar o aprendizado sobre reciclagem mais acessível e divertido. Ele pode ser usado em servidores escolares, comunidades ambientais ou grupos de amigos que queiram aprender e se engajar com o tema.
