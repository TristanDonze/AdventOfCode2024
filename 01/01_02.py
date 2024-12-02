def read_column(file):
    column1 = []
    column2 = []
    
    with open(file, 'r') as f:
        for line in f:
            values = line.split()
            if len(values) == 2:
                column1.append(int(values[0]))
                column2.append(int(values[1]))
    
    return column1, column2

def resolve(column1, column2):
    result = sum([column1[i]*column2.count(column1[i]) for i in range(len(column1))])
    return result
column1, column2 = read_column('data.txt')
result = resolve(column1, column2)
print(result)