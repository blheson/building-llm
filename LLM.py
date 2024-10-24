from tokenizer import SimpleTokenizerV1
from split import split_text
import json
def open_text():
    encoding="uft-8"
    with open("the-verdict.txt","r") as f:
        raw_text=f.read()
        # print("Total number of char:", len(raw_text))
        return raw_text
def open_vocab():
    with open("vocab.json","r") as f:
        raw_text=f.read()
        return raw_text
def create_vocab():
   raw_text= open_text()
   processed = split_text(raw_text)
   return create_dictionary(processed)
def create_dictionary(tokenized_units):
    all_words = sorted(set(tokenized_units))
    vocab = {token:integer for integer,token in enumerate(all_words)}
    return vocab
    
def start():
    # get text
    sample_text = "it's the last he painted, you know."
    # vocab =  create_vocab()
    vocab = open_vocab()
    tokenizer = SimpleTokenizerV1(json.loads(vocab))
    ids = tokenizer.encode(sample_text)
    back_text = tokenizer.decode(ids)
    print(ids,back_text)
    
start()