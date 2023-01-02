import spacy

en_core_web_md = "C:/Users/User/AppData/Local/Programs/Python/Python311/Lib/" \
                 "site-packages/en_core_web_md/en_core_web_md-3.4.1"

nlp = spacy.load(en_core_web_md)


# Run all the code of sample below
# Similary of cat, monkey, and banana
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

''' Simiarity result
0.5929930274321619
0.40415016164997786
0.22358825939615987
'''

# Similary of cat, apple monkey, and banana
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

''' Simiarity result
cat cat 1.0
cat apple 0.2036806046962738
cat monkey 0.5929930210113525
cat banana 0.2235882580280304
apple cat 0.2036806046962738
apple apple 1.0
apple monkey 0.2342509925365448
apple banana 0.6646699905395508
monkey cat 0.5929930210113525
monkey apple 0.2342509925365448
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882580280304
banana apple 0.6646699905395508
banana monkey 0.4041501581668854
banana banana 1.0
'''

# Similary of number of sentences below
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


''' Simiarity result
where did my dog go -  0.630065230699739
Hello, there is my car -  0.8033180111627156
I've lost my car in my car -  0.6787541571030323
I'd like my boat back -  0.5624940517078084
I will name my dog Diana -  0.6491444739190607
'''



# From the similarities between cat, monkey and banana, cat and monkey has the highest simiarity.
# It is because cat and moneky both are animals, monkey and banana has higher siminarity than cat and banana because
# we know monkey eat banana, but cat don't


word1 = nlp("tiger")
word2 = nlp("cat")
word3 = nlp("dog")
print(f"{word1} and {word2} simiarity: {word1.similarity(word2)}")
print(f"{word3} and {word2} simiarity: {word3.similarity(word2)}")
print(f"{word3} and {word1} simiarity: {word3.similarity(word1)}")

''' Simiarity result
tiger and cat simiarity: 0.5670855075810189
dog and cat simiarity: 0.8220816752553904
dog and tiger simiarity: 0.42287226182503856
'''
# I can think of other example of looking at the similarities of tiger, cat, and dog above
# Although they all are animals, but their similarities are not the same. Firstly dog and cat has the highest similarity
# because we all love cat and dog to be our lovely pet. Secondly, tiger and cat has higher similarity than tiger and dog
# It is because we already known tiger and cat belong to the same family with more than 95% of DNA in common



