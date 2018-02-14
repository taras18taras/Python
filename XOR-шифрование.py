#Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
# возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также
# функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
import itertools


def XOR_cipher(string, key):

    answer = []

    key = itertools.cycle(key)  # Повторяем ключ, чтобы зашифровать всю строку

    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))

    return ''.join(answer)

# Функция для расшифровки точно такая же
XOR_uncipher = XOR_cipher

print(XOR_cipher("Hello Vetal",",kjfhfyf"))
print(XOR_uncipher(XOR_cipher("Hello Vetal",",kjfhfyf"),",kjfhfyf"))
