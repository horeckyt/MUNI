from random import randint


def my_sum(ls):
    total = 0
    for i in ls:
        total += i
    return total

def my_max(ls):
    max = ls[0]
    for i in ls:
        if i > max:
            max = i

    return max


def my_min(ls):
    min = ls[0]
    for i in ls:
        if i < min:
            min =  i

    return min


def my_in(x, ls):
    for i in ls:
        if i == x:
            return True
    return False


def nonzero_product(ls):
    product = 1
    for i in ls:
        if i != 0:
            product *= i
    return product


def double_all(ls):
    for i in range(len(ls)):
        ls[i] *= 2


def create_double(ls):
    doubled = ls[:]
    for i in range(len(ls)):
        doubled[i] *= 2
    return doubled


def flatten(ls):
    flattened = []
    for i in ls:
        for j in i:
            if j not in flattened:
                flattened.append(j)
    return flattened


def dummy(text, garb):
    dummy_text = ""
    for i in text:
        dummy_text += i + garb
    return dummy_text


def duplication(text):
    duplicated = ""
    for i in text:
        duplicated += 2*i
    return duplicated


def reverse(text):
    return text[::-1]


def censorship(text):
    censored = ""
    for i in range(len(text)):
        if i % 2 == 1:
            censored += "x"
        else:
            censored += text[i]
    return censored


def count_a(text):
    count = 0
    for i in text.lower():
        if i == 'a':
            count += 1
    return count


def string_intersection(left, right):
    intersection = []
    for i in range(min(len(left),len(right))):
        if left[i] == right[i]:
            intersection.append(left[i])
    print(intersection)


def diff_a(left, right):
    left_a = count_a(left)
    right_a = count_a(right)

    if left_a == right_a:
        print("Strings contain the same number of a/A")
    elif left_a > right_a:
        print("First string contains more a/A: ", left_a - right_a)
    else:
        print("Second string contains more a/A: ", right_a - left_a)


def is_palindrome(text):
    length = len(text)
    text = text.lower()
    for i in range(len(text)):
        if text[i] != text[length-1-i]:
            return False
    return True


def letter_count(letter, text):
    count = 0
    for i in text.lower():
        if i == letter:
            count += 1
    return count


def letter_analysis(text):
    letters = []
    text = text.lower()
    for i in text:
        if i not in letters:
            letters.append(i)

    for j in letters:
        if j != " ":
            count = letter_count(j, text)
            print(j, count)


def word_value(text):
    val = 0
    text = text.upper()
    for i in text:
        val += ord(i)-64
    return val


def strange_filter(text):
    text = text.upper()
    final_text = text[:2]
    for i in range(2, len(text)):
        if word_value(text[i]) != word_value(text[i-1]) + word_value(text[i-2]):
            final_text += text[i]
    return final_text


def capitalize(text):
    words = text.split(" ")
    for i in range(len(words)):
        words[i] = list(words[i])
        words[i][0] = words[i][0].upper()
        words[i] = "".join(words[i])
    return " ".join(words)


def random_char(length, chars):
    text = ""
    for i in range(length):
        text += chars[randint(0, len(chars)-1)]
    return text


def vignere(text, key):
    encrypted = ""
    text = text.upper()
    for i in range(len(text)):
        j = i
        if j > (len(key)-1):
            j %= len(key)
        encrypted += chr(ord(text[i]) + ord(key[j])-64)

    return encrypted


def tuple_reverse(text, n):
    parts = []

    for i in range(len(text)//n + len(text) % n):
        parts.append(text[i*n : i*n+n])

    for i in range(len(parts)):
        parts[i] = parts[i][::-1]

    return "".join(parts)


def morse(text):
    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                  '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    translation = ""
    text = text.upper()
    for i in text:
        if i != " ":
            translation += morse_code[ord(i)-65] + " "
        else:
            translation += '| '
    return translation

print(tuple_reverse(tuple_reverse("HESLOJETAJEMNO", 3), 3))

