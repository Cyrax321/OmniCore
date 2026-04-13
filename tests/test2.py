actual = ['dog', 'cat', 'dog', 'dog', 'cat']
predicted = ['dog', 'bird', 'dog', 'cat', 'cat']

correct_count = 0 

for i in range(len(actual)):
    if actual[i] == predicted[i] :
        correct_count = correct_count + 1 
accuracy = correct_count / len(actual)

print(f"accuracy is {accuracy}")