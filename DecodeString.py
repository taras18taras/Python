raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#first variant
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
f= raw.translate(table)
print("Vsriant 1 : ",f)

#second variant
def decode_char(char):
    if 'a' <= char <= 'z':
        t = ord(char) + 2
        t = (t - ord('a')) % 26
        c = chr(t + ord('a'))
        return c
    else:
        return char

result = ""
for c in raw:
    result += decode_char(c)
print("Vsriant 2 : ", result)

#third variant
a = "abcdefghijklmnopqrstuvwxyz,. '()"
b = "cdefghijklmnopqrstuvwxyzab,. '()"
list(zip(a, b))
d = dict(zip(a, b))
"".join(d[x] for x in raw)
print("Vsriant 3 : ", "".join(d[x] for x in raw))
