from nltk import CFG

toy_grammar = CFG.fromstring("""
S -> NP VP
VP -> V NP
V -> "eats" | "drinks"
NP -> Det N
Det -> "a" | "an" | "the"
N -> "president" | "Obama" | "apple" | "coke"
""")

print toy_grammar.productions()
