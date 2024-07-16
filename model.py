import numpy as np
from numpy.random import multinomial
from tqdm import tqdm
from collections import defaultdict
import os

def prepare_data(dataset: np.ndarray, n: int):
    startchar = ("< " * (n-1))
    endchar = " " + ("> " * (n-1))[:-1]  
    out = []   
    for sample in dataset:
        out.append(startchar + sample + endchar)
    return out

class NGram_Words:
    def __init__(self, name: str, prepped_data: np.array, n: int):   
        if os.path.exists("npy/" + name + ".npy"):
            self.ngrams = np.load("npy/" + name + ".npy", allow_pickle=True).item()
        else:
            self.ngrams = self.calculate_probabilities(self.count_ngrams(prepped_data, n))
            np.save("npy/" + name + ".npy", self.ngrams, allow_pickle=True)
        self.n = n
    
    def count_ngrams(self, prepped_data: np.array, n: int) -> defaultdict(dict):
        ngram_probabilities = defaultdict(dict)
        for sample in tqdm(prepped_data):
            tokens = sample.split(' ')
            for i in range(len(tokens)-(n-1)):
                cur_gram = tokens[i:i+(n-1)]
                cur_gram = ' '.join(cur_gram)
                next_word = tokens[i + (n-1)]
                #print(cur_gram, "---->", next_word)
                if next_word in ngram_probabilities[cur_gram]:
                    ngram_probabilities[cur_gram][next_word] += 1
                else:
                    ngram_probabilities[cur_gram][next_word] = 1           
        return ngram_probabilities
        
    def calculate_probabilities(self, ngrams: defaultdict(dict)) -> defaultdict(dict):
        for ngram, next_words in tqdm(ngrams.items()):
            s = sum(next_words.values())
            for w in next_words:
                ngrams[ngram][w] /= s
        return ngrams
    
    def forward(self):
        out = []
        for i in range(self.n-1): out.append("<")
        #print(out, "--->", last)
        while True:
            last = ' '.join(out[-(self.n-1):])

            probs = self.ngrams[last]
            idx = multinomial(1, [*probs.values()]).argmax()

            word = [*probs.keys()][idx]
            if word == '>': break

            out.append(word)

        return ' '.join(out).replace('<','').replace('>','').strip()