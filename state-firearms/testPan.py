import pandas as pd
import numpy as np

# df = pd.read_csv('salaries.csv')

# # ser_of_bool = df['Age'] > 30
# print(df)
# print(df[df['Age'] > 30])

#all unique in a column
# print(df['Age'].unique())

#number of unique
# print(df['Age'].nunique())

# col names
# print(df.columns)

# print(df.info())
# print(df.describe())3
# print(df.index)

state_to_code = {
    # # Other
    # 'District of Columbia': 'DC',

    # States
    'Alabama': 'AL',
    'Montana': 'MT',
    'Alaska': 'AK',
    'Nebraska': 'NE',
    'Arizona': 'AZ',
    'Nevada': 'NV',
    'Arkansas': 'AR',
    'New Hampshire': 'NH',
    'California': 'CA',
    'New Jersey': 'NJ',
    'Colorado': 'CO',
    'New Mexico': 'NM',
    'Connecticut': 'CT',
    'New York': 'NY',
    'Delaware': 'DE',
    'North Carolina': 'NC',
    'Florida': 'FL',
    'North Dakota': 'ND',
    'Georgia': 'GA',
    'Ohio': 'OH',
    'Hawaii': 'HI',
    'Oklahoma': 'OK',
    'Idaho': 'ID',
    'Oregon': 'OR',
    'Illinois': 'IL',
    'Pennsylvania': 'PA',
    'Indiana': 'IN',
    'Rhode Island': 'RI',
    'Iowa': 'IA',
    'South Carolina': 'SC',
    'Kansas': 'KS',
    'South Dakota': 'SD',
    'Kentucky': 'KY',
    'Tennessee': 'TN',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Maine': 'ME',
    'Utah': 'UT',
    'Maryland': 'MD',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Virginia': 'VA',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Minnesota': 'MN',
    'West Virginia': 'WV',
    'Mississippi': 'MS',
    'Wisconsin': 'WI',
    'Missouri': 'MO',
    'Wyoming': 'WY',
}





df = pd.read_csv('laws.csv')
# print(df)
# # print(df.shape[0])
# # print(len(df.loc[0]))
# for i in range(0,df.shape[0]):

#     code =  state_to_code[df.loc[i, 'state']]
#     # print(code)
#     df.loc[i, 'code'] = code


df_2000 = (df[df['year'] == 2000])
print(df_2000['code'])
# print(df_new.shape[0])







# df.to_csv('laws.csv')

# for col in df.columns:
#     df[col] = df[col].astype(str)

# state = df['state'].unique()
# print([state_to_code[state]])





# df = pd.DataFrame.from_dict

# print(df[df['year'] == '2000'])
# print(df['lawtotal'])
# print(df_US[df_US['state'] == 'Florida'])
# print(df_US.columns) #column names
# print(df_US)
