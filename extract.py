from konlpy.tag import Okt
import pandas as pd

def extract_data(contents):
    okt = Okt()
    df = pd.read_csv('C:/Users/user/ipynb/data/company_name.csv', index_col=0)

    li =  okt.phrases(contents)
    company = list(set(li)&set(df['한글 종목약명']))

    return df[df['한글 종목약명'].isin(company)][['한글 종목약명', '업종', '단축코드']].reset_index()