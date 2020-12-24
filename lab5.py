def main():
    sentence = "enjoy the excellent band tonight"
    dictionary = create_dictionary("textese.txt")
    translation(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()

    #print(word', words)

translation = {}
[words.split(",") for word in words]