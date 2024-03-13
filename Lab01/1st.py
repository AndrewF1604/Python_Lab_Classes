import os
import re
print("Zad1:")
def count_files(path):
    list_of_files=os.listdir(path)
    count = len(list_of_files)
    return count

test = 'D:\PyCharm Community Edition 2023.2.3'

print(f"Files in '{test}': {count_files(test)}")
print()
print("Zad2:")
def display_files(path):
    list_of_files = os.listdir(path)
    for element in list_of_files:

        if(os.path.isdir(path+'/'+element)):
            display_files(path+'/'+element)
            print(f" +{element}")
        else:
            print(f"\t+{element}")


test2=r'C:\Users\Andrzej\My project\UserSettings'      #r od uniknac bledow, z interpretacji znakow
display_files(test2)
print()
print("Zad3:")
def delete_string(sentence, phrase):
    sentence_splited=sentence.split(" ")
    result=[]
    for element in sentence_splited:
        if element != phrase:
            result.append(element)

    return " ".join(result)
def delete_string2(sentence, phrase):
    modified_sentence = sentence

    pattern = re.escape(phrase)
    modified_sentence = re.sub(pattern, '', modified_sentence)

    return modified_sentence.strip()

lista=["ala","ma"]
print(delete_string("ala ala ma kota","ala"))
print(delete_string2("ala ala ma kota",lista))
print("Zad4:")
def swap_string(sentence, phrase,word ):
    sentence_splited=sentence.split(" ")
    result=[]
    for element in sentence_splited:
        if element == phrase:
            result.append(word)
        else:
            result.append(element)
    return " ".join(result)
print(swap_string("ala ala ma kota","ala","baran"))

print()
print("Zad5:")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
test5=[1,3,7,2,4,1,9]

bubble_sorted_list = test5.copy()
insertion_sorted_list = test5.copy()

bubble_sort(bubble_sorted_list)
insertion_sort(insertion_sorted_list)

print("Lista przed sortowaniem:")
print(test5)

print("Lista po sortowaniu przez bubble sort:")
print(bubble_sorted_list)

print("Lista po sortowaniu przez insertion sort:")
print(insertion_sorted_list)

