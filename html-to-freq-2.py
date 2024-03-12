import urllib.request
import obo
import concurrent.futures

def process_url(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')
    text = obo.stripTags(html).lower()
    fullwordlist = obo.stripNonAlphaNum(text)
    wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
    dictionary = obo.wordListToFreqDict(wordlist)
    sorteddict = obo.sortFreqDict(dictionary)
    
    return sorteddict

def main():
    urls = [
        'https://programminghistorian.org/pt/licoes/contar-frequencias-palavras-python',
        'https://pt.wikipedia.org/wiki/.br',
        'https://www.normaculta.com.br/artigos/'
        # Adicione mais URLs conforme necessário
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Processa as URLs concorrentemente
        results = list(executor.map(process_url, urls))

    # Combina os resultados (se necessário)
    combined_result = []
    for result in results:
        combined_result.extend(result)

    # Imprime os resultados combinados
    for s in combined_result:
        print(str(s))

if __name__ == "__main__":
    main()
