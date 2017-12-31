def read_files(file):
    f = open(file)
    lines = []

    for eachLine in f.read("\n"):
        if len(eachLine) > 0:
            lines.append(eachLine)

    f.close()
    return lines

dolar = read_files("btc_to_dolar.txt")
for i in dolar:
    print(i)

