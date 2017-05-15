#!/usr/bin/env python3

import re
import random
import argparse

from polyglot.text import Text
from polyglot.text import Word

from PIL import Image
import numpy as np

from wordcloud import WordCloud


def remove_stopwords(rawtext):
    stopwords = []
    
    with open('it_stopwords.txt') as f:
        # Generates the list
        for line in f:
            stopwords.append(line.strip())

    for sw in stopwords:
        # Substitute the stopword with a blank space
        rawtext = re.sub('\W{}\W'.format(sw), ' ', rawtext)

    return rawtext


def normalize(text):
    word2lemma = {}
    
    with open('it_lemmatization.txt') as f:
        # Generates the list
        for line in f:
            lemma, word = line.strip().split('\t')
            word2lemma.update({word: lemma})

    raw_text = text.raw

    for word in text.words:
        try:
            # If present, the word it brought back to its lemma
            replacement = ' {} '.format(word2lemma[word])
            raw_text = re.sub('\W{}\W'.format(word), replacement, raw_text)
        except:
            pass
    
    text = Text(raw_text)

    return text


def generate_dict(text):
    words = {}
    punctuation = ',.:!?-()""'
    for word in text.words:
        if word in punctuation: continue # skip punctuation
        
        if word not in words:
            # Add the new word
            words.update({word: 1}) 
        else:
            # Increment the counter for the given word
            words.update({word: words[word] + 1}) 

    return words


def color_by_sentiment(word='', **_):
    word = Word(word, 'it')
    
    if word.polarity > 0:
        hue = 75 # lime-like
    elif word.polarity < 0:
        hue = 300 # magenta-like
    else:
        hue = 250 # blue-like

    lightness = random.randint(40, 65) 
    color = "hsl({}, 90%, {}%)".format(hue, lightness)

    return color



# __MAIN__

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nwords', type=int, default=200, help="How many words will be extracted")
parser.add_argument('-b', '--background', default=None, help="Image filename that will be used as background")
parser.add_argument('-m', '--mask', default=None, help="Image filename that will be used as mask for placing images")
parser.add_argument('-o', '--output', default='output.png', help="Output image filename")
parser.add_argument('FILE', help="Filename of the .txt to analyse (it_IT only)")
args = parser.parse_args()


raw_text = open(args.FILE).read()

raw_text = raw_text.lower() # Force lowercase
raw_text = remove_stopwords(raw_text)

# Lemmatize and calculate frequencies of the words
text = normalize( Text(raw_text) )
word_dict = generate_dict(text)

if args.mask:
    maskpattern = np.array(Image.open(args.mask))
    wc = WordCloud(mode='RGBA', background_color=None, max_words=args.nwords, mask=maskpattern)
else:
    wc = WordCloud(mode='RGBA', background_color=None, max_words=args.nwords)

# Generates the image
wc.generate_from_frequencies(word_dict)

# Color the words
wc.recolor(color_func=color_by_sentiment)

wc_layer = wc.to_image()

if args.background:
    result_image = Image.open(args.background)
else:
    result_image = Image.new('RGBA', wc_layer.size)

result_image.paste(wc_layer, (0, 0), wc_layer)
result_image.save(args.output)

