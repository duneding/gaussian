# Import the English language class
import os

import spacy

# Create the nlp object
# nlp = English()
nlp = spacy.load('en_core_web_sm')

# Created by processing a string of text with the nlp object
#doc = nlp("Hello world!")
data_home = os.environ['DATA_HOME']
doc = nlp(open(data_home + 'nlp/tlotr/lord_of_the_ring_v_short', 'r', encoding='utf-8').read())

# Iterate over tokens in a Doc
for token in doc:
    print(token.text)

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)

# A slice from the Doc is a Span object
span = doc[1:4]

# Get the span text via the .text attribute
print(span.text)

doc = nlp("It costs $5.")
print('Index:   ', [token.i for token in doc])
print('Text:    ', [token.text for token in doc])
print('is_alpha:', [token.is_alpha for token in doc])
print('is_punct:', [token.is_punct for token in doc])
print('like_num:', [token.like_num for token in doc])


# Load the small English model
nlp = spacy.load('en_core_web_sm')

# Process a text
doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)