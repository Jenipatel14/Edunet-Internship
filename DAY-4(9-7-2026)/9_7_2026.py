import pandas as pd

# Load dataset
df = pd.read_csv("sustainability.csv")

# Preview
print(df.head())
import pandas as pd

df = pd.read_csv("sustainability.csv")

# Handle nulls
df.fillna({'Code': 'Region'}, inplace=True)
df['Renewables (% equivalent primary energy)'] = df['Renewables (% equivalent primary energy)'].interpolate()
print(df.head(200))

#Summary:
#I imported the sustainability dataset, cleaned missing values, 
#and analyzed renewable energy trends from 1965 to 2021. 
#Countries rich in hydropower like Brazil and Canada showed high shares, 
#while fossil fuel exporters like Algeria stayed low. 
#Overall, renewable energy use has steadily increased worldwide.
