# Zusammenarbeit mit folgenden Teilnehmern:
def mean(data):
        sum = 0
        for i in data:
            sum += i
        mean = sum / len(data)
        return mean

def variance(data):
        sum = 0
        m = mean(data)
        for i in data:
            sum += (i - m) ** 2
        variance = sum / len(data)
        return variance

def median(data):
        size = len(data)
        if size % 2 == 0:
            median = (data[size // 2 - 1] + data[size // 2]) / 2
        else:
            median = data[size // 2]
        return median

def statistics(data):
    if len(data) == 0:
        raise ValueError("List must contain at least 1 element")

    sorted_data = sorted(data)
    max = sorted_data[len(sorted_data) - 1]
    min = sorted_data[0]

    dic = {
        "mean": mean(sorted_data),
        "variance": variance(sorted_data),
        "median": median(sorted_data),
        "minimum": min,
        "maximum": max
    }
    return dic
