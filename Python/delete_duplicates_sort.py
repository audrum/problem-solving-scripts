# Take the text from a file 'file.txt'
# and delete duplicates and sort by number
# the content of the file is in format
# five=5
# one=1
# two=2
# four=4
# three=3
# three=3

dict_file = {}

with open("file.txt") as file:
    for line in file:
        (key, value) = line.split("=")
        dict_file[key] = int(value)

dict_file = sorted(dict_file.items(), key = lambda x: x[1])
result = dict(dict_file)


for item in result:
    print(f"{item}={result[item]}")
