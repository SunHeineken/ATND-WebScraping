import requests
from bs4 import BeautifulSoup as bs
import MeCab

def collect_atnd_data(keyword):
    params = {
    'keyword':  keyword,
    'format':   'json',
    'count':    100
    }
    
    url = 'http://api.atnd.org/events/'
    res = requests.get(url, params=params)
    
    json = res.json()
    
    return json
    #return res, json

def _split_to_words(text, to_stem=False):
    """
    入力: 'すべて自分のほうへ'
    出力: tuple(['すべて', '自分', 'の', 'ほう', 'へ'])
    """
    tagger = MeCab.Tagger('mecabrc')  # 別のTaggerを使ってもいい
    mecab_result = tagger.parse(text)
    info_of_words = mecab_result.split('\n')
    words = []
    for info in info_of_words:
        # macabで分けると、文の最後に’’が、その手前に'EOS'が来る
        if info == 'EOS' or info == '':
            break
            # info => 'な\t助詞,終助詞,*,*,*,*,な,ナ,ナ'
        info_elems = info.split(',')
        # 6番目に、無活用系の単語が入る。もし6番目が'*'だったら0番目を入れる
        if info_elems[6] == '*':
            # info_elems[0] => 'ヴァンロッサム\t名詞'
            words.append(info_elems[0][:-3])
            continue
        if to_stem:
            # 語幹に変換
            words.append(info_elems[6])
            continue
        # 語をそのまま
        words.append(info_elems[0][:-3])
    return words    

def titles_desctiptions(keyword):
    json = collect_atnd_data(keyword)
    titles = [x['event']['title'] for x in json['events']]
    descriptions = [x['event']['description'] for x in json['events']]
    descriptions2 = []
    for desc in descriptions:
        soup = bs(desc, 'lxml')
        text = soup.get_text()
        text = text.replace('\n', ' ')
        descriptions2.append(text)
    # return    
    return titles, descriptions2




# print(json['events'][0]['event']['title'])


# ###################################
# res, json = collect_atnd_data('DeepLearning')

# titles = [x['event']['title'] for x in json['events']]
# descriptions = [x['event']['description'] for x in json['events']]

# descriptions2 = []
# for desc in descriptions:
#     soup = bs(desc)
#     text = soup.get_text()
#     text = text.replace('\n', ' ')
#     descriptions2.append(text)


# print(json['events'][0]['event']['title'])