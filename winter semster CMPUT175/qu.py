queu = [""] * 20
queu[0] = 1
start = 0
end = 1

print(queu)
while True:
    i = input("Enter: ")
    queu[end] = i

    end+=1

    o = input("Out(y/n): ")
    if o.lower() == 'y':
        print(queu[start].pop())

    if (input("exit?: ")) == 'e':
        break