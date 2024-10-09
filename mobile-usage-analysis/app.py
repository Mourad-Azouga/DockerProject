import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
# Use raw string to avoid escape sequences
df = pd.read_csv(r'/app/data/dataset.csv')

# # Print some basic information about the dataset
# print(df.info())
# print(df.describe())

# # Show the first few rows
# print(df.head())

# Visualize distribution of numerical features
numerical_features = ['App Usage Time (min/day)', 'Device Model', 'Data Usage (MB/day)', 'Age']
df[numerical_features].hist(bins=15, figsize=(15, 10))
plt.suptitle("Distribution of Numerical Features")
plt.savefig('/app/report/distribution_numerical_features.png')  # Save the histogram
plt.close()  # Close the figure to avoid displaying it in terminal

# Visualize the distribution of user behavior classes
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
sns.countplot(x='User Behavior Class', data=df)
plt.title('Distribution of User Behavior Classes')
plt.savefig('/app/report/distribution_user_behavior_classes.png')  # Save the countplot
plt.close()  # Close the figure to avoid displaying it in terminal
while True:
    time.sleep(1)