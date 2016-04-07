import vincent
import random
import pandas as pd

# stacked = vincent.StackedArea(df_1)
# stacked.colors(brew='Spectral')

# day1 = {'UOCD':3, 'sleep':9, 'eating':2, 'work':8}
# day2 = {'UOCD':1.5, 'sleep':10, 'eating':2.25, 'work':6}
# day3 = {'UOCD':0, 'sleep':7, 'eating':1.6, 'work':12}
# days = [day1, day2, day3]


cats = ['UOCD', 'sleep', 'work', 'eating']
index = range(1, 21, 1)
data = {'index': index}
for cat in cats:
    data[cat] = [random.randint(1, 6) for day in index]

# index = ['day1', 'day2', 'day3']

# data = {'index': index}
# # for i in range(len(days)):
# #     data[i] = days[i]
# for i in range(len(day1)):
#     for key, value in day1.items():
#         data[i] = key

# data = pd.DataFrame(days, index=index)

stacked = vincent.StackedArea(data, iter_idx='index')
stacked.axis_titles(x='Index', y='Data Value')
stacked.legend(title='Categories')
stacked.colors(brew='Spectral')
# stacked.display() #creates iPython object
stacked.to_json('stacked.json', html_out=True, html_path='stacked_template.html')