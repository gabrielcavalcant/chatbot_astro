import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet as wn
from difflib import get_close_matches

# Baixar os recursos necessários
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Texto sobre Astro, o super-herói fictício
text = """
Astro é um super-herói que protege a cidade de Nova Metropolis. Ele possui a habilidade de voar e superforça. Sua identidade secreta é Alex Silva, um repórter investigativo que usa sua profissão para descobrir informações sobre criminosos. Astro tem um grande senso de justiça e sempre age para proteger os inocentes. Ele enfrenta vilões poderosos, como o Doutor Caos, um gênio do mal que tenta controlar a cidade. Nas horas vagas, Alex gosta de ler livros sobre ciência e explorar o espaço com seus poderes. Seu grande objetivo é manter a paz em Nova Metropolis e inspirar as pessoas a fazer o bem.
"""

# Função para encontrar sinônimos em português
def get_synonyms(word):
    synonyms = set(lemma.name() for syn in wn.synsets(word, lang='por') for lemma in syn.lemmas('por'))
    return synonyms

# Função de similaridade semântica e correspondência de palavras próximas
def semantic_similarity(user_input, keywords):
    user_words = word_tokenize(user_input)
    for word in user_words:
        # Verificar correspondências aproximadas e sinônimos
        close_matches = get_close_matches(word, keywords, n=1, cutoff=0.8)
        if close_matches:
            return True
        synonyms = get_synonyms(word)
        if any(get_close_matches(syn, keywords, n=1, cutoff=0.8) for syn in synonyms):
            return True
    return False

# Função do chatbot com tema de super-herói
def chatbot():
    print("Olá! Eu sou o chatbot sobre Astro. Pergunte-me sobre o super-herói e sua história.")
    
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input in ['sair', 'exit', 'quit']:
            print("Chatbot: Até mais!")
            break

        if 'habilidade' in user_input or semantic_similarity(user_input, ['habilidade', 'poderes', 'superforça', 'voar']):
            response = "Astro possui a habilidade de voar e tem superforça, o que o ajuda a combater o crime em Nova Metropolis."
        elif 'identidade secreta' in user_input or semantic_similarity(user_input, ['identidade', 'secreta', 'alex silva']):
            response = "Astro mantém sua identidade secreta como Alex Silva, um repórter investigativo."
        elif 'vilão' in user_input or semantic_similarity(user_input, ['vilão', 'doutor caos', 'inimigo']):
            response = "O principal vilão de Astro é o Doutor Caos, um gênio do mal que tenta controlar Nova Metropolis."
        elif 'cidade' in user_input or semantic_similarity(user_input, ['cidade', 'nova metropolis']):
            response = "Astro protege a cidade de Nova Metropolis, garantindo a segurança de seus cidadãos."
        elif 'objetivo' in user_input or semantic_similarity(user_input, ['objetivo', 'missão']):
            response = "O grande objetivo de Astro é manter a paz em Nova Metropolis e inspirar as pessoas a fazer o bem."
        elif 'tempo livre' in user_input or semantic_similarity(user_input, ['tempo livre', 'hobbies']):
            response = "Nas horas vagas, Astro, como Alex Silva, gosta de ler livros sobre ciência e explorar o espaço."
        else:
            response = "Desculpe, não entendi sua pergunta. Pergunte sobre Astro, seus poderes ou sua história!"
            
        print(f"Chatbot: {response}")

# Iniciar o chatbot
chatbot()
