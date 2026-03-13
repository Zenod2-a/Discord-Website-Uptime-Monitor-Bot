import pandas as pd

# load dataset
df = pd.read_csv("majestic_million.csv")

# take first 10000 domains
domains = df["Domain"].head(10000)

# convert to https URLs
urls = ["https://" + d for d in domains]

# create dataframe
out = pd.DataFrame({
    "URL": urls,
    "NAME": domains
})

# save file
out.to_csv("urls_10000.csv", index=False)

print("Dataset created: urls_10000.csv")