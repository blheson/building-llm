
import re
from split import split_text
class SimpleTokenizerV1: 
    def __init__(self,vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    def encode(self, text):
        preprocessed = split_text(text)
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text =re.sub(r'\s+([,.()?:;_!"\'])',r'\1', text)
        return text
