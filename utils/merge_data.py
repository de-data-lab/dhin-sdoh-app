import pandas as pd

dhin_2018 = pd.read_csv('cd2018.csv')
dhin_2018 = dhin_2018[dhin_2018['insurance'] == 'Any']
dhin_2018_wide = pd.pivot_table(dhin_2018, values = ['perc'], index = ['GEOID'], columns = ['disease'], aggfunc = 'sum')
dhin_2018_wide.columns =  dhin_2018_wide.columns.get_level_values(1)
dhin_2018_wide = dhin_2018_wide.reset_index()
dhin_2018_wide['year'] = 2018

dhin_2019 = pd.read_csv('cd2019.csv')
dhin_2019 = dhin_2019[dhin_2019['insurance'] == 'Any']
dhin_2019_wide = pd.pivot_table(dhin_2019, values = ['perc'], index = ['GEOID'], columns = ['disease'], aggfunc = 'sum')
dhin_2019_wide.columns =  dhin_2019_wide.columns.get_level_values(1)
dhin_2019_wide = dhin_2019_wide.reset_index()
dhin_2019_wide['year'] = 2019
dhin_2019_wide

dhin = pd.concat([dhin_2018_wide, dhin_2019_wide])
dhin['GEOID'] = dhin['GEOID'].astype('str')

cwi = pd.read_csv('cwi_2012_2019_tract_12_15_21.csv')
cwi = cwi[cwi['year'].isin([2018, 2019])]
cwi = cwi.rename(columns = {'fips':'GEOID'})
cwi['GEOID'] = cwi['GEOID'].astype('str')

dhin_cwi = dhin.merge(cwi, on = ['GEOID', 'year'])
dhin_cwi.to_csv('dhin-cwi.csv', index = False)
