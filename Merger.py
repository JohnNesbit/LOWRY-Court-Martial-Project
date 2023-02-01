import pandas as pd

# read files to be merged
df = pd.read_csv("LOWRY_kb.csv", low_memory=False, encoding= 'unicode_escape')
new_df = pd.read_csv("Lowry_predicted_Real.csv", low_memory=False)

# get rid of dumb column that the pandas writer makes to index, comment this out if new_df was written without an index col
del new_df["Unnamed: 0"]
unique = []
for _ in range(len(new_df.columns)):
	if new_df.columns[_] not in df.columns: # find column differences
		print(new_df.columns[_])
		df[new_df.columns[_]] = new_df[new_df.columns[_]] # set df's new columns to the new values in new_df

df.to_csv("Lowry_Dataset_Merged1") # write to new file
