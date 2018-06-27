import myfunclib

def main():
    str_file_name = ["newsafr.txt", "newscy.txt", "newsfr.txt", "newsit.txt"]
    for s_file in str_file_name:
        s = myfunclib.input_data(s_file)
        lw = myfunclib.text_to_words(6, s)
        low = myfunclib.list_to_dict(10,lw)
        print(low)


main()