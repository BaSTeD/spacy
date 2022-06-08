import spacy

nlp = spacy.load("de_core_news_sm")

doc = nlp("Hallo, ich heiße Sebastian und schreibe die nächsten 6 Monate an meiner Masterarbeit in Deutschland bei Twitter.")

#Print grammatical structure
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

    ###abcdefg

print("\n##############################")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

print("\n##############################")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


