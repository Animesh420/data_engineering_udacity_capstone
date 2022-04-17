import pandas as pd

df = pd.read_csv(r'/Users/ani/Desktop/learning/udacity/final_etl/models/flight_number.csv', index_col=0)

d = {}


def joiner(row):
    i1 = row['airline']
    i2 = row['flightNumber']
    i3 = i1 + str(i2)
    d[i3] = None
    return row


s = df.apply(joiner, axis=1)
print(s)

d = {'4O970': 'LAS', 'AA930': 'MIA', 'AA908': None, 'AA1616': None, 'AA107': None, 'AA1558': None, 'AA1502': None,
     'AA954': 'JFK', 'AA1250': 'MIA', 'AA216': None, 'AA207': None, 'AA914': None, 'AA900': None, 'AA135': None,
     'AA918': "MIA", 'AA109': "BOS", 'AA902': None, 'AA906': None, 'AA1322': None, 'AA950': None, 'AA39': None,
     'AA928': "DFW", 'AA948': None, 'AA199': None, 'AA916': None, 'AA1481': None, 'AA966': None, 'AF76': None,
     'AF77': "LAX", 'AF8': None, 'AF90': None, 'AF66': None, 'AM404': None, 'AM434': None, 'AS267': None, 'AV6': None,
     'AZ608': "JFK", 'AZ630': None, 'AZ610': None, 'AZ604': None, 'AZ602': None, 'B61706': None, 'BA209': None,
     'BA275': "LAS", 'BA207': None, 'BA283': None, 'BA269': None, 'CM226': None, 'CM472': None, 'CM804': None,
     'CM446': "MCO", 'CM441': None, 'DL475': None, 'DL419': None, 'DL309': None, 'DL405': None, 'DL472': None,
     'DL445': "MSP", 'DY7015': None, 'EK205': None, 'IB6117': None, 'IB6123': None, 'JJ8078': None, 'JJ8086': None,
     'JJ8080': "JFK", 'JJ8048': None, 'KL601': None, 'KL643': None, 'LA2702': None, 'LH452': None, 'LH464': None,
     'LH460': "MIA", 'LH462': None, 'LH456': None, 'LH400': None, 'LX22': None, 'LX14': None, 'LX64': None, 'LX40': None,
     'MU577': "LAX", 'PR102': None, 'TK1': None, 'TK9': None, 'TK3': None, 'UX97': None, 'VS27': None, 'VS23': None,
     'YX4337': "LGA"}
mag = {"LVG": "LAS", "NYC": "JFK"}

los = {'AA109': 'BOS',
 'AA135': 'LAX',
 'AA216': 'RIC',
 'AF66': 'LAX',
 'AF76': 'LAX',
 'AF77': 'LAX',
 'AS267': 'PDX',
 'BA269': 'LAX',
 'BA283': 'LAX',
 'CM472': None,
 'DL309': 'LAX',
 'KL601': 'LAX',
 'LH452': 'LAX',
 'LH456': 'LAX',
 'LX40': 'LAX',
 'MU577': 'LAX',
 'PR102': 'LAX',
 'TK9': 'LAX',
 'VS23': 'LAX'}

nyc = {'AA107': 'JFK',
 'AA199': 'JFK',
 'AA950': 'JFK',
 'AA954': 'JFK',
 'AF8': 'JFK',
 'AM404': 'JFK',
 'AZ602': 'JFK',
 'AZ604': 'JFK',
 'AZ608': 'JFK',
 'AZ610': 'JFK',
 'CM804': 'JFK',
 'DL405': 'ATL',
 'DL419': 'ATL',
 'DL445': 'MSP',
 'DL472': 'JFK',
 'DL475': 'ATL',
 'DY7015': 'JFK',
 'EK205': 'JFK',
 'JJ8078': 'JFK',
 'JJ8080': 'JFK',
 'KL643': 'JFK',
 'LH400': 'JFK',
 'LX14': 'JFK',
 'LX22': 'JFK',
 'TK1': 'JFK',
 'TK3': 'JFK'}
m  = {**los, **nyc}
print(m)
