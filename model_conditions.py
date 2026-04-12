model_name = 'DeepNet-1'
loss = 0.25
accuracy = 0.85
performance = accuracy - loss
print(f'model{model_name} has a loss of {loss} , an accuracy of {accuracy} and performance of {performance}')

if accuracy > 0.99 :
    print(f'\n great model with an accuracy of {accuracy} %' )
elif accuracy > 0.77 :
    print(f'\n good model with an accuracy of {accuracy} %')
else :
    print(f'\n model needs improvement with an accuracy of {accuracy} %')