# """
dict1 = {
    "ID": 1,
    "Salary": 2000,
    "Sales Percentage": 13
}
dict2 = {
    "ID": 2,
    "Salary": 3000,
    "Sales Percentage": 10
}
dict3 = {
    "ID": 3,
    "Salary": 4000,
    "Sales Percentage": 15
}
dict4 = {
    "ID": 4,
    "Salary": 2500,
    "Sales Percentage": 14
}
dict5 = {
    "ID": 5,
    "Salary": 2900,
    "Sales Percentage": 19
}
# """

# Question 1

"""
merged_dict = dict1, dict2, dict3, dict4, dict5
# print(merged_dict)


# d3 = dict(dict3, **dict4)
# print(d3)

# maximum = max(merged_dict.items(), key=lambda v: int(merged_dict[v[0]]['ID']))[1]['ID']
# print(maximum)

"""
"""
id_array = [dict1["ID"], dict2["ID"], dict3["ID"], dict4["ID"], dict5["ID"]]
# print("Highest ID: ")
# print(max(id_array))
print(f"Highest ID: {max(id_array)}")

salary_array = [dict1["Salary"], dict2["Salary"], dict3["Salary"], dict4["Salary"], dict5["Salary"]]
# print("Highest Salary: ")
# print(max(salary_array))
print(f"Highest Salary: {max(salary_array)}")

percent_array = [dict1["Sales Percentage"], dict2["Sales Percentage"],
                 dict3["Sales Percentage"], dict4["Sales Percentage"],
                 dict5["Sales Percentage"]]
# print("Highest Sales Percentage: ")
# print(max(percent_array))
print(f"Highest Sales Percentage: {max(percent_array)}")

"""

# Question 2

"""
def test_duplicate(array_numbers):
    numbers_set = set(array_numbers)
    return len(array_numbers) != len(numbers_set)


# two = input("Enter numbers: ")
print([3, 3, 1, 2, 6, 4, 1, 2, 4, 5])
print(test_duplicate([3, 3, 1, 2, 6, 4, 1, 2, 4, 5]))
print([1, 2, 3, 4])
print(test_duplicate([1, 2, 3, 4]))
"""

# Question 3

"""
def intersection_set(nums1, nums2):
    nums3 = nums1.intersection(nums2) 
    print(nums3)


set1 = {2, 3, 3, 2}
set2 = {3, 3}

intersection_set(set1, set2)

set1 = {5, 7, 4}
set2 = {5, 7, 5, 8, 5}

intersection_set(set1, set2)
"""
