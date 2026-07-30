# Problem191
a = input('Enter the alphabet = ')
match a:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('Vowel')
    case _:
        print('Consonant')
