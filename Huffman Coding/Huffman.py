
class Node:
    def __init__(self, alphabet, probability):
        self.alphabet = alphabet
        self.probability = probability
        self.code = ''
        self.father = None

def huffman_coding(alphabet, probability):
    items = list()
    for i in range(len(probability)):
        items.append(Node(alphabet[i], probability[i]))

    total = len(items)
    items.append(Node(None, (items[0].probability + items[1].probability)))
    items[0].code = '1'
    items[0].father = items[-1]
    items[1].code = '0'
    items[1].father = items[-1]
    
    for i in range(2, total):
        items.append(Node(None, items[-1].probability + items[i].probability))
        items[-2].father = items[-1]
        items[i].father = items[-1]
        if items[-2].probability > items[i].probability:
            items[i].code = '1'
            items[-2].code = '0'
        else:
            items[i].code = '0'
            items[-2].code = '1'
    return items

code_string = ""
def get_codes(node):
    global code_string
    if node.father == None:
        return
    else:
        code_string += node.code
        get_codes(node.father)
    

def sort_data(sour_alpha, pro_dis): 
    data_zipped = zip(source_alphabet, probability_distribution)
    sort_zipped = sorted(data_zipped, key = lambda x:(x[1],x[0]), reverse = 0)
    result = zip(*sort_zipped)
    x_axis, y_axis = [list(x) for x in result]
    return x_axis, y_axis

if __name__ == "__main__":
    source_alphabet = ["a", "b", "c", "d", "e"]
    probability_distribution = [0.2, 0.4, 0.2, 0.1, 0.1]
    
    total = len(source_alphabet)
    print("="*10 + "Data" + "="*10)
    for i in range(total):
        print("%s  %f" % (source_alphabet[i], probability_distribution[i]))
    print("="*24)

    sorted_alphabet, sorted_probability = sort_data(source_alphabet, probability_distribution)
    nodes = huffman_coding(sorted_alphabet, sorted_probability)
    
    for i in range(total - 1, -1, -1):
        code_string = ""
        get_codes(nodes[i])
        print(sorted_alphabet[i], ''.join(reversed(code_string)))
