x=1
y=2

values = [x, y]
values.reverse()
x, y = values

print(x)
print(y)


def name_splitter(full_name):
    first_name, last_name = full_name.split(" ")
    return (first_name, last_name)

print(name_splitter("Mert Eren"))


def char_counts(s):
    vowels="aeiou"
    vowel_count=0
    consonant_count=0
    for char in s:
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1

    return vowel_count, consonant_count

print(char_counts("Mert Eren"))

def mean(*args):
    tot=0
    for i in arg:
        x=int(i)
        tot+=x

    return tot/len(args)


