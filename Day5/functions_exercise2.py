# 1. Funkcja sumująca
def list_sum(*args):
    lista_liczb = list(arg for arg in args)
    suma = sum(lista_liczb)
    return suma


print(list_sum(3, 5, 6, 12, 8))  # wywołanie funkcji


# 2. Funkcja sortująca - wyświetla najmniejszy i największy element listy
def sort_first_and_last(number_list):
    small_num = number_list[0]
    for number in number_list:
        if small_num > number:
            small_num = number
    large_num = number_list[0]
    for number in number_list:
        if large_num < number:
            large_num = number
    return small_num, large_num


num_list = (34, 5, 0, 1, 6, 72)
# print(num_list)
print(sort_first_and_last(num_list))  # wywołanie funkcji


# 3. Funkcja rozdzielająca zdanie na listę wyrazów
def split_sentence(sentence):
    wordlist = sentence.rsplit()
    return wordlist


print(split_sentence("Ala ma kota, kot ma Alę."))  # wywołanie funkcji


# 4. Funkcja przyjmująca listę stringów, zwracająca ilość stringów, które są palindromami
def palindrome_str_count(list_of_strings):
    palindrome_list = []
    for string in list_of_strings:
        if len(string)>=2 and string == string[::-1]:  # Notatka dla siebie: INDEKSY! PAMIĘTAJ O NICH!
            palindrome_list.append(string)
    palindrome_count = len(palindrome_list)  # Notatka dla siebie: len() zwraca ilość!
    return palindrome_count


str_list = ('abc', 'xyz', 'aba', '1221')
print(palindrome_str_count(str_list))

# 5. Funkcja wskazująca unikalne wartości w liście
lista_a = (10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40)
def get_unique_val(number_list):
    unique_values = []
    for value in number_list:
        if number_list.count(value) == 1:
            unique_values.append(value)
    return unique_values


print(get_unique_val(lista_a))

