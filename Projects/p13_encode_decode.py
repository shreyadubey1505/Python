# Caesar Cipher Encoder & Decoder

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encode(data, shift):
    result = ""
    for i in data:
        if i in alphabets:
            index = alphabets.index(i)
            new_index = (index + shift) % 26
            result = result + alphabets[new_index]
        else:
            result = result + i
    return result


def decode(data, shift):
    result = ""
    for i in data:
        if i in alphabets:
            index = alphabets.index(i)
            new_index = (index - shift) % 26
            result = result + alphabets[new_index]
        else:
            result = result + i
    return result


while True:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if choice == "exit":
        break
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    if choice == "encode":
        print("Encoded text is:", encode(message, shift))
    elif choice == "decode":
        print("Decoded text is:", decode(message, shift))
else:
    print("Invalid choice")
