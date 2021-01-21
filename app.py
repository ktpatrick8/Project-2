
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
new_data_2015 = data_2015.rename(columns = {"Happiness Rank": "Happiness_Rank", 
                     "Happiness Score": "Happiness_Score","Economy (GDP per Capita)": "Economy", "Health (Life Expectancy)": "Health",  "Trust (Government Corruption)": "Trust", "Dystopia Residual": "Dystopia_Residual"}, 
                                 inplace = True) 
# dropping columns
data_2015.drop('Standard Error', axis=1, inplace=True)
data_2015.drop('Region', axis=1, inplace=True)
data_2015.drop('Dystopia_Residual', axis=1, inplace=True)


# import df to sql
data_2015.to_sql(name='Year_2015', con=engine, if_exists='append', index=False)

# making data frame from csv file 
data_2016 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2016.csv") 
  
# changing index cols with rename() 
new_data_2016 = data_2016.rename(columns = {"Happiness Rank": "Happiness_Rank", 
                     "Happiness Score": "Happiness_Score","Economy (GDP per Capita)": "Economy", "Health (Life Expectancy)": "Health",  "Trust (Government Corruption)": "Trust", "Dystopia Residual": "Dystopia_Residual"}, 
                                 inplace = True) 
# dropping columns
data_2016.drop('Lower Confidence Interval', axis=1, inplace=True)
data_2016.drop('Upper Confidence Interval', axis=1, inplace=True)
data_2016.drop('Region', axis=1, inplace=True)
data_2016.drop('Dystopia_Residual', axis=1, inplace=True)


# import df to sql
data_2016.to_sql(name='Year_2016', con=engine, if_exists='append', index=False)

# making data frame from csv file 
data_2017 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2017.csv") 
  
# changing index cols with rename() 
new_data_2017 = data_2017.rename(columns = {"Happiness.Rank": "Happiness_Rank", 
                     "Happiness.Score": "Happiness_Score","Economy..GDP.per.Capita.": "Economy", "Health..Life.Expectancy.": "Health",  "Trust..Government.Corruption.": "Trust", "Dystopia.Residual": "Dystopia_Residual"}, 
                                 inplace = True) 
# dropping columns
data_2017.drop('Whisker.high', axis=1, inplace=True)
data_2017.drop('Whisker.low', axis=1, inplace=True)
data_2017.drop('Dystopia_Residual', axis=1, inplace=True)

# import df to sql
data_2017.to_sql(name='Year_2017', con=engine, if_exists='append', index=False)

# making data frame from csv file 
data_2018 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2018.csv") 
  
# changing index cols with rename() 
new_data_2018 = data_2018.rename(columns = {"Overall rank": "Happiness_Rank", "Country or region": "Country", "Perceptions of corruption": "Trust",
                     "Score": "Happiness_Score","GDP per capita": "Economy", "Healthy life expectancy": "Health", "Social support": "Family", "Freedom to make life choices": "Freedom", "Perceptions of corruption": "Dystopia_Residual"}, 
                                 inplace = True) 
# dropping columns
data_2018.drop('Dystopia_Residual', axis=1, inplace=True)

# import df to sql
data_2018.to_sql(name='Year_2018', con=engine, if_exists='append', index=False)


# making data frame from csv file 
data_2019 = pd.read_csv("/Users/jeffhitt/Desktop/JeffProject2/Project2/Project2/Year_2019.csv") 
  
# changing index cols with rename() 
new_data_2019 = data_2019.rename(columns = {"Overall rank": "Happiness_Rank", "Country or region": "Country", "Perceptions of corruption": "Trust",
                     "Score": "Happiness_Score","GDP per capita": "Economy", "Healthy life expectancy": "Health", "Social support": "Family", "Freedom to make life choices": "Freedom", "Perceptions of corruption": "Dystopia_Residual"}, 
                                 inplace = True) 
# dropping columns
data_2019.drop('Dystopia_Residual', axis=1, inplace=True)
                  
# import df to sql
data_2019.to_sql(name='Year_2019', con=engine, if_exists='append', index=False)
                     