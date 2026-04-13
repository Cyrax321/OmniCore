model_name = 'DeepNet-1'
loss = 0.25
accuracy = 0.85
epoch = 4 
performance = accuracy - loss
print(f'model{model_name} has a loss of {loss} , an accuracy of {accuracy} and performance of {performance}')

if accuracy > 0.99 :
    print(f'\n great model with an accuracy of {accuracy} %' )
elif accuracy > 0.77 :
    print(f'\n good model with an accuracy of {accuracy} %')
else :
    print(f'\n model needs improvement with an accuracy of {accuracy} %')


for epoch in range(3):
    print(f'Epoch {epoch}')

while loss > 0.1:
    print(f'loss is {loss} , too high!')
    loss = loss - 0.05 
print('model is training')