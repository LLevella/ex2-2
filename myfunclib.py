import chardet

def input_data(str_file_name):

    with open('newsafr.txt', 'rb') as f:
        txt_afr = f.read()
        encod = chardet.detect(txt_afr)
        s = txt_afr.decode(encod['encoding'])
    return s

def text_to_words(n_letters, intext):
    symbols = ',.!?:;"\''
    words_list  = [ w.strip(symbols) for w in intext.split() if len(w.strip(symbols)) > n_letters]
    return words_list

def list_to_dict(n_words, words_list):
    words_dict = {w: words_list.count(w) for w in words_list}
    counted_words_list = sorted(words_dict.items(), key = lambda vx: vx[1], reverse=True)[:n_words]
    return counted_words_list