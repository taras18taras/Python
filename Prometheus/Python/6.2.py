def encode_morze(x):
    morse_code = {"A": "^_^^^", "B": "^^^_^_^_^", "C": "^^^_^_^^^_^", "D": "^^^_^_^",
                  "E": "^", "F": "^_^_^^^_^", "G": "^^^_^^^_^", "H": "^_^_^_^",
                  "I": "^_^", "J": "^_^^^_^^^_^^^", "K": "^^^_^_^^^", "L": "^_^^^_^_^",
                  "M": "^^^_^^^", "N": "^^^_^", "O": "^^^_^^^_^^^", "P": "^_^^^_^^^_^",
                  "Q": "^^^_^^^_^_^^^", "R": "^_^^^_^", "S": "^_^_^", "T": "^^^",
                  "U": "^_^_^^^", "V": "^_^_^_^^^", "W": "^_^^^_^^^", "X": "^^^_^_^_^^^",
                  "Y": "^^^_^_^^^_^^^", "Z": "^^^_^^^_^_^"
                  }
    x = x.upper();
    x = x.strip();
    l = [];
    s = '';
    for i in x:
        if i in morse_code:
            l.append(morse_code.get(i))
        elif i == " ":
            l.append("_")
    s = "___".join(l)
    return (s)


print(encode_morze('Prometheus'))
print(encode_morze('Morze code'))
print(encode_morze('SOS'))
print(encode_morze('1'))
