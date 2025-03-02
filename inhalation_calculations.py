import pandas as pd
import streamlit as st

def zip_code_valdation(zip):
    return True

def calculation_inhalation_data(zip, home_hrs, office_hrs, outdoor_hrs):
    df = pd.read_excel('Microplastics Data.xlsx', sheet_name='App Research - US County Info')
    for x,y in df.iterrows():
        zip_list = str(y['zips'])
        if str(zip) in zip_list:
            home_exposure =float(y['Estimated home air inhalation per hour'])*home_hrs
            office_exposure = float(y['Estimated office air inhalation per hour'])*office_hrs
            outdoor_exposure = float(y['Estimated outdoor air inhalation per hour'])*outdoor_hrs
            total_inhalation = round(home_exposure+office_exposure+outdoor_exposure,2)
            county = y['county_full']
            state = y['state_name']
    return (total_inhalation, home_exposure, office_exposure, outdoor_exposure, county, state)



