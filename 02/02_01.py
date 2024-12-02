def read_column(file):
    data = []
    
    with open(file, 'r') as f:
        for line in f:
            values = line.split()
            data.append(list(map(int, values)))
    
    return data

def resolve(data):
    result = 0
    for level in data:
        if level[0] < level[-1]:
            sorted_level = sorted(level)
        else:
            sorted_level = sorted(level, reverse=True)
        if level == sorted_level and len(level) == len(set(level)):
            check = all(abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))
            if check:
                result += 1
    return result

data = read_column('./data.txt')
result = resolve(data)
print(result)
