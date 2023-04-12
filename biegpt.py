import nltk, datetime

from nltk.tokenize import word_tokenize

# Baixa os recursos necessários do NLTK
# nltk.download('punkt')

# Dicionário com as respostas para cada pergunta
respostas = {
    "oi": "Olá! Como posso te ajudar, nome?",
    "olá": "Olá! Como posso te ajudar, nome?",

    "colher": "Uma colher é um utensílio de cozinha usado para comer ou mexer alimentos.",
    "semana": "Uma semana é um período de sete dias consecutivos, geralmente começando no domingo e terminando no sábado.",
    "maçã": "Uma maçã é uma fruta comestível de casca fina e polpa suculenta, geralmente de cor vermelha ou verde.",
    "cachorro": "Um cachorro é um animal de estimação conhecido por sua lealdade e companheirismo, também chamado de cão.",
    "lápis": "Um lápis é uma ferramenta de escrita ou desenho feita de madeira, com uma mina de grafite no interior.",
    "chuva": "A chuva é a precipitação de gotas de água que caem da atmosfera em direção à superfície da Terra.",
    "internet": "A internet é uma rede global de computadores interconectados que permite a troca de informações e comunicação em todo o mundo.",
    "avião": "Um avião é uma aeronave motorizada que permite o transporte de pessoas ou cargas pelo ar.",
    "livro": "Um livro é uma obra escrita composta por páginas encadernadas, geralmente feitas de papel, com informações, histórias ou conhecimentos.",
    "bicicleta": "Uma bicicleta é um veículo de duas rodas impulsionado pelo movimento dos pedais, geralmente usado para transporte ou lazer.",
    "televisão": "Uma televisão é um aparelho eletrônico que recebe sinais de transmissão de televisão e exibe imagens e sons em uma tela.",
    "praia": "Uma praia é uma área de areia ou cascalho ao longo da costa de um oceano, mar, lago ou rio, geralmente usada para lazer ou recreação.",
    "computador": "Um computador é uma máquina eletrônica que processa informações de acordo com instruções programadas e é usada para realizar várias tarefas.",
    "guitarra": "Uma guitarra é um instrumento musical de cordas, geralmente com seis cordas, que é tocado usando os dedos ou uma palheta.",
    "montanha": "Uma montanha é uma elevação natural do terreno, geralmente com um pico pontiagudo e íngreme, que se projeta acima da paisagem circundante.",
    "oceano": "Um oceano é uma vasta massa de água salgada que cobre a maior parte da superfície da Terra, composta por diferentes corpos de água interconectados.",
    "carro": "Um carro é um veículo motorizado de quatro rodas, geralmente movido a combustível, que é usado para transporte de pessoas ou cargas.",
    "pizza": "Uma pizza é um prato de origem italiana, feito com uma base de massa coberta com molho de tomate, queijo e outros ingredientes variados.",
    "câmera": "Uma câmera é um dispositivo utilizado para capturar imagens ou vídeos, geralmente composto por uma lente, um sensor de imagem e um mecanismo de gravação.",
    "estrela": "Uma estrela é um objeto celeste que emite luz e calor próprio devido à reação nuclear que ocorre em seu núcleo, sendo um dos componentes básicos do universo.",
    "plantação": "Uma plantação é uma área onde culturas agrícolas são cultivadas em grande escala para produção de alimentos, fibras ou outros produtos.",
    "celular": "Um celular, também conhecido como smartphone, é um dispositivo eletrônico portátil que permite a comunicação sem fio e acesso à internet.",
    "rio": "Um rio é uma corrente de água que flui em uma direção específica, geralmente para o mar, e é uma importante fonte de água e habitat para a vida selvagem.",
    "nuvem": "Uma nuvem é uma massa visível de partículas de água ou gelo suspensas na atmosfera, que pode aparecer em várias formas e altitudes.",
    "arco-íris": "Um arco-íris é um fenômeno óptico que ocorre quando a luz do sol é refratada, refletida e dispersa pelas gotas de chuva na atmosfera, formando um arco multicolorido.",
    "moeda": "Uma moeda é uma peça de metal ou papel que é usada como meio de troca em transações comerciais, geralmente emitida por um governo.",

    "salve": "Olá! Como posso te ajudar, nome?",
    "hora atual": "O horário atual é ",
    "hoje é dia": "Hoje é dia ",
    "sair": "Até logo! Obrigado por usar o programa.",
    "nome": "Meu nome é BieGPT. Estou aqui para ter ajudar respondendo qualquer pergunta.",
    "melhor amigo": "Meu melhor amigo é Pedro.",
    "amigos bie": "Meus principais amigos são Pedro, Luca, Luisa, Gabi, Tiago, Lucas, Gabriel, Benjamim, dentre outros...",
    "idade": "Eu sou um programa de texto e não tenho idade.",
    "como vai você": "Como sou um programa de texto, não tenho emoções ou estados físicos, mas estou aqui para ajudar!",
    "propósito": "Meu propósito é fornecer respostas úteis às suas perguntas e ajudá-los da melhor forma possível.",
    "fazer": "Eu posso responder a perguntas sobre diversos assuntos, como ciência, história, tecnologia, entre outros.",
    "capital China": "A capital da China é Pequim.",
    "presidente China": "O atual presidente da China é Xi Jinping.",
    "moeda China": "A moeda da China é o Yuan Chinês (CNY).",
    "idioma China": "O idioma oficial da China é o Mandarim.",
    "maior cidade China": "A maior cidade da China é Xangai.",
    "população China": "A população da China é aproximadamente 1,4 bilhão de habitantes.",
    "clima China": "O clima da China varia de subtropical a subártico, dependendo da região.",
    "capital Brasil": "A capital do Brasil é Brasília.",
    "presidente Brasil": "O atual presidente do Brasil é Luiz Inácio Lula da Silva.",
    "moeda Brasil": "A moeda do Brasil é o Real (BRL).",
    "idioma Brasil": "O idioma oficial do Brasil é o Português.",
    "maior cidade Brasil": "A maior cidade do Brasil é São Paulo.",
    "população Brasil": "A população do Brasil é aproximadamente 213 milhões de habitantes.",
    "clima Brasil": "O clima do Brasil varia de tropical a equatorial, dependendo da região.",
    "capital Rússia": "A capital da Rússia é Moscou.",
    "presidente Rússia": "O atual presidente da Rússia é Vladimir Putin.",
    "moeda Rússia": "A moeda da Rússia é o Rublo Russo (RUB).",
    "idioma Rússia": "O idioma oficial da Rússia é o Russo.",
    "maior cidade Rússia": "A maior cidade da Rússia é Moscou.",
    "população Rússia": "A população da Rússia é aproximadamente 144 milhões de habitantes.",
    "clima Rússia": "O clima da Rússia varia de subártico a temperado continental, dependendo da região.",
    "capital Japão": "A capital do Japão é Tóquio.",
    "imperador Japão": "O atual imperador do Japão é Naruhito.",
    "moeda Japão": "A moeda do Japão é o Iene (JPY).",
    "idioma Japão": "O idioma oficial do Japão é o Japonês.",
    "maior cidade Japão": "A maior cidade do Japão é Tóquio.",
    "população Japão": "A população do Japão é aproximadamente 126 milhões de habitantes.",
    "clima Japão": "O clima do Japão varia de subtropical a subártico, dependendo da região.",
    "capital Austrália": "A capital da Austrália é Canberra.",
    "primeiro-ministro Austrália": "O atual primeiro-ministro da Austrália é Scott Morrison.",
    "moeda Austrália": "A moeda da Austrália é o Dólar Australiano (AUD).",
    "idioma Austrália": "O idioma oficial da Austrália é o Inglês.",
    "maior cidade Austrália": "A maior cidade da Austrália é Sydney.",
    "população Austrália": "A população da Austrália é aproximadamente 26 milhões de habitantes.",
    "clima Austrália": "O clima da Austrália varia de tropical a temperado, dependendo da região.",
    "capital Canadá": "A capital do Canadá é Ottawa.",
    "primeiro-ministro Canadá": "O atual primeiro-ministro do Canadá é Justin Trudeau.",
    "moeda Canadá": "A moeda do Canadá é o Dólar Canadense (CAD).",
    "idioma Canadá": "O idioma oficial do Canadá é o Inglês e o Francês.",
    "maior cidade Canadá": "A maior cidade do Canadá é Toronto.",
    "população Canadá": "A população do Canadá é aproximadamente 37 milhões de habitantes.",
    "clima Canadá": "O clima do Canadá varia de subártico a temperado, dependendo da região.",
    "capital Índia": "A capital da Índia é Nova Delhi.",
    "primeiro-ministro Índia": "O atual primeiro-ministro da Índia é Narendra Modi.",
    "moeda Índia": "A moeda da Índia é a Rúpia Indiana (INR).",
    "idioma Índia": "A Índia possui duas línguas oficiais, o Hindi e o Inglês, além de uma grande diversidade de outros idiomas regionais.",
    "maior cidade Índia": "A maior cidade da Índia é Mumbai.",
    "população Índia": "A população da Índia é aproximadamente 1,4 bilhão de habitantes.",
    "clima Índia": "O clima da Índia varia de tropical a subtropical, dependendo da região.",
    "capital África do Sul": "A capital da África do Sul é Pretória.",
    "presidente África do Sul": "O atual presidente da África do Sul é Cyril Ramaphosa.",
    "moeda África do Sul": "A moeda da África do Sul é o Rand (ZAR).",
    "idioma África do Sul": "A África do Sul possui 11 línguas oficiais, incluindo o Inglês, o Afrikaans e o Zulu.",
    "maior cidade África do Sul": "A maior cidade da África do Sul é Joanesburgo.",
    "população África do Sul": "A população da África do Sul é aproximadamente 59 milhões de habitantes.",
    "clima África do Sul": "O clima da África do Sul varia de subtropical a desértico, dependendo da região.",
    "capital México": "A capital do México é Cidade do México.",
    "presidente México": "O atual presidente do México é Andrés Manuel López Obrador.",
    "moeda México": "A moeda do México é o Peso Mexicano (MXN).",
    "idioma México": "O idioma oficial do México é o Espanhol.",
    "maior cidade México": "A maior cidade do México é Cidade do México.",
    "população México": "A população do México é aproximadamente 126 milhões de habitantes.",
    "clima México": "O clima do México varia de tropical a desértico, dependendo da região.",
    "capital Argentina": "A capital da Argentina é Buenos Aires.",
    "presidente Argentina": "O atual presidente da Argentina é Alberto Fernández.",
    "moeda Argentina": "A moeda da Argentina é o Peso Argentino (ARS).",
    "idioma Argentina": "O idioma oficial da Argentina é o Espanhol.",
    "maior cidade Argentina": "A maior cidade da Argentina é Buenos Aires.",
    "população Argentina": "A população da Argentina é aproximadamente 45 milhões de habitantes.",
    "clima Argentina": "O clima da Argentina varia de subtropical a subártico, dependendo da região.",
    "capital França": "A capital da França é Paris.",
    "presidente França": "O atual presidente da França é Emmanuel Macron.",
    "moeda França": "A moeda da França é o Euro (EUR).",
    "idioma França": "O idioma oficial da França é o Francês.",
    "maior cidade França": "A maior cidade da França é Paris.",
    "população França": "A população da França é aproximadamente 67 milhões de habitantes.",
    "clima França": "O clima da França varia de oceânico a mediterrâneo, dependendo da região.",
    "capital Alemanha": "A capital da Alemanha é Berlim.",
    "chanceler Alemanha": "A atual chanceler da Alemanha é Angela Merkel.",
    "moeda Alemanha": "A moeda da Alemanha é o Euro (EUR).",
    "idioma Alemanha": "O idioma oficial da Alemanha é o Alemão.",
    "maior cidade Alemanha": "A maior cidade da Alemanha é Berlim.",
    "população Alemanha": "A população da Alemanha é aproximadamente 83 milhões de habitantes.",
    "clima Alemanha": "O clima da Alemanha é diversificado, com variações regionais. Geralmente, o norte do país possui um clima mais fresco e úmido, enquanto o sul tem um clima mais continental, com invernos frios e verões quentes.",
    "geografia Alemanha": "A Alemanha está localizada na Europa Central, fazendo fronteira com a Dinamarca ao norte, Polônia e República Tcheca a leste, Áustria ao sudeste, Suíça ao sul, França, Luxemburgo e Bélgica a oeste, e Países Baixos ao noroeste.",
    "economia Alemanha": "A Alemanha é uma das maiores economias do mundo e é conhecida por sua indústria automobilística, maquinaria, engenharia, produtos químicos e tecnologia. É um importante centro financeiro e comercial na Europa.",
    "história Alemanha": "A Alemanha tem uma rica história que remonta a séculos, com eventos significativos como a Reforma Protestante, as duas guerras mundiais e a reunificação do país após a Guerra Fria.",
    "cultura Alemanha": "A cultura da Alemanha é conhecida por sua rica herança artística, literária, musical e filosófica. A Oktoberfest, a música clássica de compositores famosos como Beethoven e Bach, e a tradição da cerveja são alguns dos aspectos culturais mais conhecidos do país.",

    "álgebra": "Álgebra é um ramo da matemática que lida com símbolos e as regras para manipulá-los. Ela envolve o estudo de equações, polinômios, funções e suas propriedades.",
    "fórmula da área de um círculo?": "A fórmula da área de um círculo é A = π * r^2, onde 'A' representa a área e 'r' é o raio do círculo.",
    "teoria dos números": "A teoria dos números é um ramo da matemática que estuda as propriedades e relações dos números inteiros, incluindo tópicos como divisibilidade, congruências, números primos e teorema dos números primos.",

    "dna": "O DNA (ácido desoxirribonucleico) é uma molécula que contém as informações genéticas necessárias para a formação e funcionamento dos organismos. Sua função principal é armazenar e transmitir a informação genética de uma geração para outra, controlando a síntese de proteínas e determinando as características e traços hereditários de um organismo.",
    "fotosíntese": "A fotosíntese é o processo pelo qual as plantas, algas e algumas bactérias convertem a energia do sol em energia química, armazenada em moléculas de glicose e outros compostos orgânicos. É um processo essencial para a produção de oxigênio e para a manutenção do equilíbrio do ciclo do carbono na Terra.",
    "mitose": "A mitose é o processo de divisão celular que resulta em duas células filhas idênticas à célula mãe.",
    "meiose": "A meiose é o processo de divisão celular que resulta em células reprodutivas com metade do número de cromossomos das células somáticas.",
}


# Função para analisar a pergunta e retornar a resposta adequada
def analisar_pergunta(pergunta):
    tokens = word_tokenize(pergunta.lower())  # Transforma a pergunta em minúsculas e tokeniza
    resposta = "Desculpe, não entendi a pergunta."  # Resposta padrão caso não seja reconhecida

    # Verifica se a pergunta contém tanto "mitose" quanto "meiose"
    if "mitose" in tokens and "meiose" in tokens:
        resposta = respostas["mitose"] + "\n" + respostas["meiose"]

    if "hora" in tokens or "horas" in tokens or "horario" in tokens or "horário" in tokens :
        horario_atual = datetime.datetime.now().strftime("%H:%M:%S")
        resposta = respostas["hora atual"] + horario_atual + "."

    if "dia" in tokens or "dia da semana" in tokens or "dia hoje" in tokens :
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        resposta = respostas["hoje é dia"] + data_atual + "."

    # Verifica se a pergunta contém a sequência "melhor amigo"
    if "melhor" in tokens and "amigo" in tokens:
        resposta = respostas["melhor amigo"]
    else:
        for palavra in tokens:
            if palavra in respostas:
                resposta = respostas[palavra]
                break

    if "algebra" in tokens or "álgebra" in tokens or "algbera" in tokens:
        resposta = respostas["álgebra"]

    if "fotosíntese" in tokens or "fotosintese" in tokens or "fotossintese" in tokens or "fotossíntese" in tokens:
        resposta = respostas["fotosíntese"]

    # Verifica país e respectivos presidente e capitais
    if "brasil" in tokens or "brazil" in tokens:
        if "presidente" in tokens:
            resposta = respostas["presidente Brasil"]
        if "capital" in tokens:
            resposta = respostas["capital Brasil"]

    if "china" in tokens:
        if "presidente" in tokens:
            resposta = respostas["presidente China"]
        if "capital" in tokens:
            resposta = respostas["capital China"]

    if "alemanha" in tokens:
        if "presidente" in tokens or "chanceler" in tokens:
            resposta = respostas["chanceler Alemanha"]
        if "capital" in tokens:
            resposta = respostas["capital Alemanha"]

    if "india" in tokens or "índia" in tokens:
        if "presidente" in tokens or "primeiro-ministro" in tokens:
            resposta = respostas["primeiro-ministro Índia"]
        if "capital" in tokens:
            resposta = respostas["capital Índia"]

    if "africa" in tokens or "áfrica" in tokens and "sul" in tokens:
        if "presidente" in tokens:
            resposta = respostas["presidente África do Sul"]
        if "capital" in tokens:
            resposta = respostas["capital África do Sul"]

    if "canada" in tokens or "canadá" in tokens:
        if "presidente" in tokens or "primeiro-ministro" in tokens:
            resposta = respostas["primeiro-ministro Canadá"]
        if "capital" in tokens:
            resposta = respostas["capital Canadá"]

    if "japao" in tokens or "japão" in tokens:
        if "presidente" in tokens or "imperador" in tokens:
            resposta = respostas["imperador Japão"]
        if "capital" in tokens:
            resposta = respostas["capital Japão"]

    if "mexico" in tokens or "méxico" in tokens:
        if "presidente" in tokens:
            resposta = respostas["presidente México"]
        if "capital" in tokens:
            resposta = respostas["capital México"]

    if "franca" in tokens or "frança" in tokens:
        if "presidente" in tokens:
            resposta = respostas["presidente França"]
        if "capital" in tokens:
            resposta = respostas["capital França"]

    if "australia" in tokens or "austrália" in tokens:
        if "presidente" in tokens or "primeiro-ministro" in tokens:
            resposta = respostas["primeiro-ministro Austrália"]
        if "capital" in tokens:
            resposta = respostas["capital Austrália"]

    return resposta


# Loop infinito para receber perguntas e fornecer respostas
while True:
    pergunta = input("Digite sua pergunta (ou 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        print("Até logo! Obrigado por usar o programa.")
        break
    resposta = analisar_pergunta(pergunta)
    print(resposta)
