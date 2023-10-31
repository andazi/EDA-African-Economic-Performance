import os

trends = [
    'Real GDP growth (annual %)',
    'Inflation, consumer prices (annual %)',
    'Exports of goods and services (% of GDP)',
    'Imports of goods and services (% of GDP)',
    'Gross capital formation (% of GDP)',
    'Current account balance (Net, BoP, cur. US$)',
    'General government final consumption expenditure (% of GDP)',
    'Household final consumption expenditure  (% of GDP)'	
]

analysis = [
'Trend Analysis',
'Inflation-Economic Growth analysis',
'Trade Analysis',
'Balance of Payments',
'Governament and Household Spending Analysis'
]

country = ['Malawi', 'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso',
       'Burundi', 'Cameroon', 'Cabo Verde', 'Central African Republic',
       'Chad', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.',
       "Cote d'Ivoire", 'Djibouti', 'Egypt', 'Equatorial Guinea',
       'Eritrea', 'eSwatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana',
       'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
       'Madagascar', 'Mali', 'Mauritania', 'Mauritius', 'Morocco',
       'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda',
       'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone',
       'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania',
       'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']


folder_name = 'trial'


for i in  analysis:
	if i == 'Trend Analysis':
		for j in country:
			for k in trends:
				os.makedirs(f'{folder_name}/{i}/{j}/{k}')
	else:
		for j in country:
                        os.makedirs(f'{folder_name}/{i}/{j}')

