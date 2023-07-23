import random
import pandas as pd

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

value_to_index = {value: index for index, value in enumerate(unique_values)}

one_hot_matrix = []
for value in data['whoAmI']:
    one_hot_row = [0] * len(unique_values)
    one_hot_row[value_to_index[value]] = 1
    one_hot_matrix.append(one_hot_row)

one_hot_df = pd.DataFrame(one_hot_matrix, columns=unique_values)

data = pd.concat([data, one_hot_df], axis=1)

print(data.head())
