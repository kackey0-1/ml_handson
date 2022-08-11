https://py4macro.github.io/index.html

## Fetch data from World Bank

- Check for World Bank
    - https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#world-bank
- Country Codes
    - https://datahelpdesk.worldbank.org/knowledgebase/articles/898590-api-country-queries

```python
from pandas_datareader import wb

dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2005, end=2008)
dat 
```

## Fetch data from econdb

```python
import pandas_datareader.data as web

start_date = '1980'
# IMFの指定国CPIデータを取得
df_imf = web.DataReader('dataset=IMF_CPI&FREQ=[M]&INDICATOR=[PCPI_PC_CP_A_PT]&REF_AREA=[AF,AL,DZ,AO]', 'econdb')
# OECDの消費者信頼感データ
df_oecd = web.DataReader('dataset=OE_KEI&FREQUENCY=[M]&LOCATION=[AUS,AUT]&SUBJECT=[CSCICP02]', 'econdb')
# OECDから実質GDPの前年同期比のデータを取得
web.DataReader(
    'dataset=OE_KEI&FREQUENCY=Y&MEASURE=[GY]&LOCATION=[AUS,BRA,CAN,CHN,EU28,FRA,DEU,GRC,ESP,ITA,IND,IDN,ISR,JPN,MEX,NLD,NZL,NOR,OECD,RUS,SWE,TUR,GBR,USA]&SUBJECT=[NAEXKP01]',
    'econdb', start=start_date)
```

