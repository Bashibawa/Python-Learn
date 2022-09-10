import pandas as pd

data = {'Country': ['United States', 'United Kingdom', 'Canada', 'Germany'],
        'Capital': ['Washigton', 'London', 'Ottawa', 'Berlin'],
        'Population': [329500000, 67220000, 38010000, 83240000]}

dataframe = pd.DataFrame(data, columns= ['Country', 'Capital', 'Population'])

print(dataframe)