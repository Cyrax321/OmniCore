# Corey Schafer Python Tutorial: Lists, Tuples, and Sets
# Fill in the blanks or write the code below each question to practice!

courses = ['History', 'Math', 'Physics', 'CompSci']

# 1. Print the first and last item of the 'courses' list using indexing.
# Your code here:

print(courses[0])
print(courses[-1])

# 2. Add 'Art' to the END of the 'courses' list.
# Your code here:

courses.append('Art')

print(courses)

# 3. Insert 'Geography' at the beginning (index 0) of the list.
# Your code here:
courses.insert(0,"Geography")
print(courses)
# 4. You have another list:
courses_2 = ['Education', 'Biology']
# Add all items from 'courses_2' into 'courses' so they are individual items, not a nested list.
# Your code here:
courses_2.extend(courses)
print(courses_2)
# 5. Remove 'Math' from the 'courses' list using the .remove() method.
# Your code here:
courses.remove("Math")
print(courses)
# 6. Remove the LAST item of the list using the .pop() method and print the removed item.
# Your code here:
courses.pop()
print(courses)

# 7. Reverse the 'courses' list in-place.
# Your code here:


# 8. Sort the 'courses' list in alphabetical order in-place.
# Your code here:

courses.sort()

# 9. Sort the 'courses' list in reverse alphabetical order.
# Your code here:


nums = [1, 5, 2, 4, 3]

# 10. Find and print the minimum, maximum, and sum of the 'nums' list.
# Your code here:


# 11. Find the index of 'Physics' in the 'courses' list.
# Your code here:


# 12. Turn the 'courses' list into a single comma-separated string using .join()
# Expected output: "History, Physics, ..." (depending on the current state of the list)
# Your code here:


# 13. Turn the string you just created back into a list using .split()
# Your code here:

