#  Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {'C': 92, 'Java': 66, 'Python': 85}

sample_dict = {
'C': 92,
'Java': 66,
'Python': 85,
}

m=min(sample_dict.values())
for key,value in sample_dict.items():
    if m==value:
        print("The key of lowest value from dictionary are : ",key)
        break