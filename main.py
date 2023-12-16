import pandas

nato_alpa_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {name.letter: name.code for (index, name) in nato_alpa_data.iterrows()}

# print(nato_dict)

word = input().upper()

word_list = [nato_dict[user] for user in word]
print(word_list)

