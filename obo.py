# obo.py

stopwords = [
    'a', 'à', 'adeus', 'agora', 'ainda', 'além', 'algo', 'algumas', 'alguns', 'ali', 'ampla',
    'amplas', 'amplo', 'amplos', 'ano', 'anos', 'antes', 'ao', 'aos', 'apenas', 'apoio', 'após',
    'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'área', 'as', 'às', 'assim', 'até', 'atrás',
    'através', 'baixo', 'bastante', 'bem', 'boa', 'boas', 'bom', 'bons', 'breve', 'cá', 'cada',
    'catorze', 'cedo', 'cento', 'certamente', 'certeza', 'cima', 'cinco', 'coisa', 'coisas',
    'com', 'como', 'comprido', 'conhecido', 'corrente', 'cuja', 'cujas', 'cujo', 'cujos', 'da',
    'dá', 'dão', 'daquela', 'daquelas', 'daquele', 'daqueles', 'daqui', 'daí', 'das', 'de',
    'debaixo', 'débil', 'depois', 'desde', 'dessa', 'dessas', 'desse', 'desses', 'desta',
    'destas', 'deste', 'destes', 'deve', 'devem', 'devendo', 'dever', 'deverá', 'deverão',
    'deveria', 'devia', 'deviam', 'dez', 'dezanove', 'dezasseis', 'dezassete', 'dezoito',
    'dia', 'diante', 'diz', 'dizem', 'dizer', 'do', 'dois', 'dos', 'doze', 'duas', 'dúvida',
    'e', 'é', 'ela', 'elas', 'ele', 'eles', 'em', 'embora', 'entre', 'era', 'eram', 'éramos',
    'és', 'essa', 'essas', 'esse', 'esses', 'esta', 'está', 'estamos', 'estão', 'estar', 'estará',
    'estas', 'estás', 'estava', 'estavam', 'estávamos', 'este', 'esteja', 'estejam', 'estejamos',
    'estes', 'esteve', 'estive', 'estivemos', 'estiver', 'estivera', 'estiveram', 'estivéramos',
    'estiverem', 'estivermos', 'estivesse', 'estivessem', 'estivéssemos', 'estiveste',
    'estivestes', 'estou', 'eu', 'exemplo', 'faço', 'falta', 'favor', 'faz', 'fazeis', 'fazem',
    'fazemos', 'fazer', 'fazes', 'fazia', 'faço', 'fez', 'fim', 'final', 'foi', 'fomos',
    'for', 'fora', 'foram', 'fôramos', 'forem', 'forma', 'formos', 'fosse', 'fossem',
    'fôssemos', 'foste', 'fostes', 'fui', 'geral', 'grande', 'grandes', 'grupo', 'há',
    'haja', 'hajam', 'hajamos', 'hão', 'havemos', 'haver', 'há-de', 'hão-de', 'havia',
    'hei', 'hoje', 'hora', 'horas', 'houve', 'houvemos', 'houver', 'houvera', 'houverá',
    'houveram', 'houverão', 'houverei', 'houverem', 'houveremos', 'houveria', 'houveriam',
    'houveríamos', 'houvermos', 'houvesse', 'houvessem', 'houvéssemos', 'isso', 'isto',
    'já', 'la', 'lá', 'lado', 'lhe', 'lhes', 'lo', 'local', 'logo', 'longe', 'lugar', 'maior',
    'maioria', 'mais', 'mal', 'mas', 'máximo', 'me', 'meio', 'menor', 'menos', 'mês', 'meses',
    'mesma', 'mesmas', 'mesmo', 'mesmos', 'meu', 'meus', 'mil', 'minha', 'minhas', 'momento',
    'muita', 'muitas', 'muito', 'muitos', 'nada', 'não', 'naquela', 'naquelas', 'naquele',
    'naqueles', 'nas', 'nem', 'nenhuma', 'nessa', 'nessas', 'nesse', 'nesses', 'neste',
    'nestes', 'ninguém', 'nível', 'no', 'noite', 'nome', 'nós', 'nossa', 'nossas', 'nosso',
    'nossos', 'nova', 'novas', 'nove', 'novo', 'novos', 'num', 'numa', 'número', 'nunca',
    'o', 'obra', 'obrigada', 'obrigado', 'oitava', 'oitavo', 'oito', 'onde', 'ontem',
    'onze', 'os', 'ou', 'outra', 'outras', 'outro', 'outros', 'para', 'parece', 'parte',
    'partir', 'pela', 'pelas', 'pelo', 'pelos', 'perto', 'pode', 'podem', 'poder',
    'poderá', 'poderão', 'poderia', 'podia', 'por', 'porquanto', 'porque', 'posição',
    'possível', 'possivelmente', 'posso', 'pouca', 'poucas', 'pouco', 'poucos',
    'primeira', 'primeiras', 'primeiro', 'primeiros', 'própria', 'próprias', 'próprio',
    'próprios', 'próxima', 'próximas', 'próximo', 'próximos', 'pude', 'pôde', 'p'
]
def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# Dada uma lista de palavras, retorna um dicionário de pares palavra-frequência.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

# Ordena um dicionário de pares palavra-frequência em ordem decrescente de frequência.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]