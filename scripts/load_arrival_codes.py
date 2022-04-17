import pandas as pd
s = '''
    'AL'='ALABAMA'
	'AK'='ALASKA'
	'AZ'='ARIZONA'
	'AR'='ARKANSAS'
	'CA'='CALIFORNIA'
	'CO'='COLORADO'
	'CT'='CONNECTICUT'
	'DE'='DELAWARE'
	'DC'='DIST. OF COLUMBIA'
	'FL'='FLORIDA'
	'GA'='GEORGIA'
	'GU'='GUAM'
	'HI'='HAWAII'
	'ID'='IDAHO'
	'IL'='ILLINOIS'
	'IN'='INDIANA'
	'IA'='IOWA'
	'KS'='KANSAS'
	'KY'='KENTUCKY'
	'LA'='LOUISIANA'
	'ME'='MAINE'
	'MD'='MARYLAND'
	'MA'='MASSACHUSETTS'
	'MI'='MICHIGAN'
	'MN'='MINNESOTA'
	'MS'='MISSISSIPPI'
	'MO'='MISSOURI'
	'MT'='MONTANA'
	'NC'='N. CAROLINA'
	'ND'='N. DAKOTA'
	'NE'='NEBRASKA'
	'NV'='NEVADA'
	'NH'='NEW HAMPSHIRE'
	'NJ'='NEW JERSEY'
	'NM'='NEW MEXICO'
	'NY'='NEW YORK'
	'OH'='OHIO'
	'OK'='OKLAHOMA'
	'OR'='OREGON'
	'PA'='PENNSYLVANIA'
	'PR'='PUERTO RICO'
	'RI'='RHODE ISLAND'
	'SC'='S. CAROLINA'
	'SD'='S. DAKOTA'
	'TN'='TENNESSEE'
	'TX'='TEXAS'
	'UT'='UTAH'
	'VT'='VERMONT'
	'VI'='VIRGIN ISLANDS'
	'VA'='VIRGINIA'
	'WV'='W. VIRGINIA'
	'WA'='WASHINGTON'
	'WI'='WISCONSON'
	'WY'='WYOMING' 
'''
d = {}

for token in s.split('\n'):
    if len(token) > 0:
        left, right = token.split('=')
        left = left.strip('\t\' ')
        rigjt = right.strip('\t\' ')
        d[left]=right

pd.Series(d).to_csv(r'/Users/ani/Desktop/learning/udacity/final_submission/data/valid_arrival_codes.csv')
print('ok')

