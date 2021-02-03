def camel_case(sentence):
    title_case = sentence.title() #uppercase first letter of each word

    upper_camel_cased = title_case.replace(' ', '') #remove spaces

    #lowercase first letter, join rest of string
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def remove_special_characters(sentence):
    alphanumeric = ''

    for character in sentence:
        if character.isalnum():
            alphanumeric += character

    return alphanumeric
            
            




def main():
    sentence = input('Enter your sentence: ')
    output = camel_case(sentence)
    remove_special_characters(output)
    print(output)


if __name__ == '__main__':
    main()
