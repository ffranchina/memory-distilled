# Memory Distilled - Trasformatorio 2017 Project
Memory Distilled is a Python script that extracts the most used words from a text and places them into a shaped wordcloud.

## The concept behind
This project starts in the bosom of the artistic residence of [Trasformatorio 2017](http://www.trasformatorio.net/?p=2424), to which I was honored to partecipate.

The main idea was to *transform* the energies and the resources that we found aboundant in [Scaletta Zanclea](https://en.wikipedia.org/wiki/Scaletta_Zanclea) into something to give back.

For days I observed the people, the feelings, the landscapes, the thoughts: an explosion of beauty that was awaking in me lots of forgotten stimuli. Only in the last days, I've suddenly realized that the biggest *transformation* had occurred inside me thanks to the new experiences I was put into: as a project I wanted to distillate my thoughts as the deepest expression of my inner processes.

I keep a diary in which I record my days and thoughts, that was my starting point.

## The process
The starting point was given by the things I wrote down in those days. I've applied to it algorithms of [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) to split the text, to bring back the words to their original *lemma* (basic form) and to compute the frequencies of usage of every single word.

At this stage, I can deduce which are the most dominant concepts reported in my diary. Through algorithms of [Sentiment Analisys](https://en.wikipedia.org/wiki/Sentiment_analysis), I can assign different color to the words that belongs to the neutral, positive or negative semantic field. When it's all set I print them onto the shape of the beautiful castle that has hosted us for 10 days.

## The result
![Output Trasformatorio 2017 - Francesco Franchina](https://github.com/ferdas/memory-distilled/raw/master/output_trasformatorio_2017.jpg)

## The technical stuffs
The script it's written for Python3. It requires a couple Python libraries to be installed:
- [Polyglot](https://pypi.python.org/pypi/polyglot) NLP library very easy and quite sufficient for trivial tasks
- [Wordcloud](https://pypi.python.org/pypi/wordcloud) cool library to generate wordclouds, highly customizable
- [Pillow](https://pypi.python.org/pypi/Pillow) image library to manipulate the result images

The libraries can be installed typing:
```
pip3 install polyglot wordcloud pillow
```
**NOTE**: Since the script is designed to work exclusively on **italian text**, polyglot must be instructed to get the proper libraries:
```
polyglot download sentiment2.it
```
To generate the image above I've used the following command:
```
./alembic.py -b castle_background.png -m castle_mask.png memories.txt 
```
For more usage options check:
```
./alembic.py --help
```

## Thanks to
- Trasformatorio
- Trasformatori
- Scaletta Zanclea, the place and the inhabitants

## Licence
Creative Commons [BY-NC](https://creativecommons.org/licenses/by-nc/4.0/).

