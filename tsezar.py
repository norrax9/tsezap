alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("Введите ваше сообщение: ")

secured = []

for letter in message:
    if letter == " ":
        secured.append(" ")
        continue
    
    for i in range(26):
        if alphabet[i] == letter:
            if i == 25:
                secured.append(alphabet[0])
            else:
                secured.append(alphabet[i + 1])

print("Результат:", "".join(secured))
