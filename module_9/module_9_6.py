
#Домашнее задание по теме "Генераторы"

def all_variants(text):
    for subseq_length in range(1, len(text) + 1):
        for start in range(len(text) - subseq_length + 1):
            yield text[start: start + subseq_length]

a = all_variants("abc")
for i in a:
    print(i)
