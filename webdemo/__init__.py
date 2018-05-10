from bottle import Bottle, template, TEMPLATE_PATH, request, static_file

from randomsentence.sentence_maker import SentenceMaker
from randomsentence.sentence_tools import SentenceTools

from diceware_utils.wordlist import Wordlist
from diceware_utils.policy import Conformize

word_list = Wordlist()
conformize = Conformize()
sentence_maker = SentenceMaker()
sentence_tools = SentenceTools()


dicewareapp = Bottle()
TEMPLATE_PATH.append('./webdemo/templates')


@dicewareapp.route('/')
def index():
    return template('index.html')


@dicewareapp.post('/randomize_words')
def randomize_words():
    count = int(request.forms.get('count', 6))
    return ' '.join([word_list.get_random_word() for _ in range(count)])


@dicewareapp.post('/generate_password')
def generate_password():
    keywords = request.forms.get('keywords', '')
    if keywords == '':
        keyword_list = [word_list.get_random_word() for _ in range(6)]
    else:
        keyword_list = keywords.split(' ')

    return conformize.conformize(keyword_list)


@dicewareapp.post('/generate_sentence')
def generate_sentence():
    visible_keywords = request.forms.get('visible_keywords', '')
    if visible_keywords == '':
        keyword_list = [word_list.get_random_word() for _ in range(6)]
    else:
        keyword_list = visible_keywords.split(' ')

    return render_token(keyword_list)


@dicewareapp.get('/static/js/<filename>')
def js(filename):
    return static_file(filename, root='webdemo/static/js')


def render_token(keyword_list):
    tagged_sentence = sentence_maker.from_keyword_list(keyword_list)
    sentence_tokens = []
    for word, match in tagged_sentence:
        if match:
            sentence_tokens.append('<b>{}</b>'.format(word))
        else:
            sentence_tokens.append(word)

    return sentence_tools.detokenize(sentence_tokens)
