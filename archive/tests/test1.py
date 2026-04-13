data = [0.9,1.2,-5.0,0.8,99.0,0.7,0.5]
for results in data:
    if results < 0 or results > 10.0:
        print(f'skipping invalid values: {results}')
    else:
        print(f'processing valid data : {results}')