# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:26:57 2023

@author: trevb
"""

import pandas as pd
import time

def get_prices():
    groups = pd.read_csv('./PokemonGroups.csv')
    
    prices = pd.DataFrame()
    
    exceptions = ['TradingCardGameClassic',
                  'MyFirstBattle',
                  'PrizePackSeriesThree',
                  'SVScarletVioletPromoCards', 
                  'PrizePackSeriesTwo',
                  'DPTrainingKit1Blue',
                  'DPTrainingKit1Gold']
    
    for row, whatever in groups.iterrows():
        ID = whatever['groupId']
        name = whatever['name'].replace(' ','')
        name = name.replace(':','')
        name = name.replace('&','And')
        if name in exceptions:
            pass
        else:
            temp =  pd.read_csv(f'https://tcgcsv.com/3/{ID}/{name}ProductsAndPrices.csv')
            sub = temp[['name','cleanName','groupId','extNumber',
                        'extRarity','lowPrice','midPrice', 'highPrice',
                        'marketPrice','subTypeName']]
            prices = pd.concat([prices,sub])
            time.sleep(2)
        print(f'{row} completed!')
    return prices


if __name__ == "__main__":
    prices = get_prices()