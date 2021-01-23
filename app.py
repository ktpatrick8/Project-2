
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine


# importing pandas module 
import pandas as pd 

connection_string = f"postgres://zsjitnfqerggpe:27480e06806e4393e3e237d266c536ba9b0f7408ac6272551cfa665e694de859@ec2-52-204-113-104.compute-1.amazonaws.com:5432/d63qhs1d38oqh0"
engine = create_engine(f'postgres://zsjitnfqerggpe:27480e06806e4393e3e237d266c536ba9b0f7408ac6272551cfa665e694de859@ec2-52-204-113-104.compute-1.amazonaws.com:5432/d63qhs1d38oqh0')


# making data frame from csv file 
data_2015 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2015.csv") 
  
# changing index cols with rename() 
new_data_2015 = data_2015.rename(columns = {"Country": "country", "Happiness Rank": "happiness rank", "Happiness Score": "happiness score", "Economy (GDP per Capita)": "economy", "Health (Life Expectancy)": "health", "Family": "family", "Trust (Government Corruption)": "trust", "Freedom": "freedom", "Generosity": "generosity"},
                                 inplace = True) 
# dropping columns
data_2015.drop('Standard Error', axis=1, inplace=True)
data_2015.drop('Region', axis=1, inplace=True)
data_2015.drop('Dystopia Residual', axis=1, inplace=True)


# import df to sql
data_2015.to_sql(name='year2015', con=engine, if_exists='append', index=False)

# making data frame from csv file 
data_2016 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2016.csv") 
  
# changing index cols with rename() 
new_data_2016 = data_2016.rename(columns = {"Country": "country", "Happiness Rank": "happiness rank", "Happiness Score": "happiness score", "Economy (GDP per Capita)": "economy", "Health (Life Expectancy)": "health", "Family": "family", "Trust (Government Corruption)": "trust", "Freedom": "freedom", "Generosity": "generosity"},
                                 inplace = True) 
# dropping columns
data_2016.drop('Lower Confidence Interval', axis=1, inplace=True)
data_2016.drop('Upper Confidence Interval', axis=1, inplace=True)
data_2016.drop('Region', axis=1, inplace=True)
data_2016.drop('Dystopia Residual', axis=1, inplace=True)


# import df to sql
data_2016.to_sql(name='year2016', con=engine, if_exists='append', index=False)

# making data frame from csv file 
data_2017 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2017.csv") 
  
# changing index cols with rename() 
new_data_2017 = data_2017.rename(columns = {"Country": "country", "Happiness.Rank": "happiness rank", "Happiness.Score": "happiness score", "Economy..GDP.per.Capita.": "economy", "Health..Life.Expectancy.": "health",  "Family": "family", "Freedom": "freedom", "Generosity": "generosity", "Trust..Government.Corruption.": "trust", "Dystopia.Residual": "Dystopia Residual"}, 
                                 inplace = True) 
# dropping columns
data_2017.drop('Whisker.high', axis=1, inplace=True)
data_2017.drop('Whisker.low', axis=1, inplace=True)
data_2017.drop('Dystopia Residual', axis=1, inplace=True)

# import df to sql
data_2017.to_sql(name='year2017', con=engine, if_exists='append', index=False)

# making data frame from csv file 
data_2018 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2018.csv") 
  
# changing index cols with rename() 
new_data_2018 = data_2018.rename(columns = {"Overall rank": "happiness rank", "Score": "happiness score", "Country or region": "country", "Perceptions of corruption": "trust", "GDP per capita": "economy", "Healthy life expectancy": "health", "Social support": "family", "Freedom to make life choices": "freedom", "Generosity": "generosity"}, 
                                 inplace = True) 

# import df to sql
data_2018.to_sql(name='year2018', con=engine, if_exists='append', index=False)


# making data frame from csv file 
data_2019 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2019.csv") 
  
# changing index cols with rename() 
new_data_2019 = data_2019.rename(columns = {"Overall rank": "happiness rank", "Country or region": "country", "Perceptions of corruption": "trust",
                     "Score": "happiness score","GDP per capita": "economy", "Healthy life expectancy": "health", "Social support": "family", "Freedom to make life choices": "freedom", "Generosity": "generosity"}, 
                                 inplace = True) 
                
# import df to sql
data_2019.to_sql(name='year2019', con=engine, if_exists='append', index=False)


# making data frame from csv file 
country = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Country.csv") 
                  
# import df to sql
country.to_sql(name='country', con=engine, if_exists='append', index=False)

# making data frame from csv file 
years = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Years.csv") 
                  
# import df to sql
years.to_sql(name='years', con=engine, if_exists='append', index=False)