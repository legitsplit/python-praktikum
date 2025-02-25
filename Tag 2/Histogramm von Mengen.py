# Zusammenarbeit mit folgenden Teilnehmern:
def histogram(list_of_lists):
    dic = {}
    for sublist in list_of_lists:
        key = frozenset(sublist)

        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1
    return dic