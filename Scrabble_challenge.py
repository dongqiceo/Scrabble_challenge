from sys import argv

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}




def scrab():
    with open('sowpods.txt', 'r') as f:
        sowpods = f.read()
    word_list = []
    word_list = sowpods.lower().split()

    if len(argv) == 2 and not argv[1].isdigit():
        word1 = (argv[1]).lower()
        word1 = list(word1)

        target_list = []
        for line in word_list:
            tmp_list = []
            for word in line:
                if word not in tmp_list:
                    tmp_list.append(word)
            if set(tmp_list).issubset(set(word1)):
                target_list.append(line)
        return target_list

    else:
        exit('wrong')


def get_score(words):
    dict_score = {}
    for word in words:
        dict_score[word] = sum(scores[c] for c in word)
    return dict_score

def sort_dict(d):
    dict1 = sorted(zip(d.values(), d.keys()), reverse=True)
    for key, val in dict1:
        print(key, ',', val)

if __name__ == '__main__':
    d = get_score(scrab())
    print(sort_dict(d))