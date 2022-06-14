scores = {'python' : 80, 'algorithm' : 90, 'django' : 89, 'web' : 83}

def get_dict_avg(scores):
    return sum(scores.values()) / len(scores.values())

print(get_dict_avg(scores))