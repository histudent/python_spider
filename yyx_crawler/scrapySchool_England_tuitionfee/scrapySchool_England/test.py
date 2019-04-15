from scrapySchool_England.clearSpace import clear_space, clear_space_str
list1 = ["a b fff", "hello", "", "", "\n", "\n", "", "lll", "", " ", " ", "", "hehehehe...", " "]

print(list1)
clear_space(list1)
print(list1)
list1Str = ' '.join(list1)
print(list1Str)
# print(list1Str.split())
# list1StrN = '\n'.join(list1Str.split()).strip()
# print("*"+list1StrN+"*")


# for s in list1:
#     if "" in list1:
#         list1.remove("")
# print(list1)
list1StrN = '\n'.join(list1).strip()
print("*"+list1StrN+"*")
while '' in list1:
    list1.remove('')
print(list1)
list1StrN = '\n'.join(list1).strip()
print("*"+list1StrN+"*")