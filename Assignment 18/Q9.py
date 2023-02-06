#  Write a python program to merge two python dictionaries into one dictionary

from heapq import merge


about_person={'name':'Wasiq', 'age':22, 'gender':'male'}
about_job={'company':'Google', 'status':'CEO', 'salary':'10000000000$'}

# def merge(dic1,dic2):
#     res={**dic1,**dic2}
#     return res

# dic=merge(about_person,about_job)

about_person.update(about_job)
print("After merging dictionary are :  ")
print(about_person)