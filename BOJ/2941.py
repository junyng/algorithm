cro_alphabets = {
    "c=" : "č",
    "c-" : "ć",
    "dz=" : "dž",
    "d-" : "đ",
    "lj" : "lj",
    "nj" : "nj",
    "s=" : "š",
    "z=" : "ž"
}

string = input()
start, end = 0, 0
count = 0

converted = ""

while start < len(string):
    word = string[start:end]
    
    if word in cro_alphabets:
        count += 1
        start += 1
        end = start
        continue
    
    end += 1
    
    if end > len(string):
        converted += string[start]
        start += 1
        end = start

print(len(converted))

