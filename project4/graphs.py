import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('day4/train.csv')

print(df.head())

print(df.shape)

print(df.describe())

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))

#data visualization
axes[0,0].hist(df['Age'].dropna(), bins=20, color='orange')
axes[0,0].set_xlabel('Age')
axes[0,0].set_ylabel('Frequency')
axes[0,0].set_title('Distribution of passenger Ages')

#Survival rates for tianic passengers
axes[0,1].bar(df['Survived'].value_counts().index, df['Survived'].value_counts(), color=['red', 'green'])
axes[0,1].set_xlabel('Survived')
axes[0,1].set_ylabel('count')
axes[0,1].set_title('Survival rate of passengers')
axes[0,1].set_xticks([0,1], ['Died', 'Survived'])

#survival rate by gender
survivalByGender = df.groupby('Sex')['Survived'].mean()
survivalByGender.plot(kind='bar', color=['purple', 'skyblue'], ax=axes[1,0])
axes[1,0].set_xlabel('Gender')
axes[1,0].set_ylabel('Survival rate')
axes[1,0].set_title('Survival Rate by gender')
axes[0, 1].set_xticks([0, 1])
axes[0, 1].set_xticklabels(['No', 'Yes'])

#passenger class
axes[1,1].bar(df['Pclass'].value_counts().index, df['Pclass'].value_counts(), color=['orange', 'green', 'blue'])
axes[1,1].set_xlabel('passenger class')
axes[1,1].set_ylabel('count')
axes[1,1].set_title('Distribution of passenger classes')
axes[1,1].set_xticks([1,2,3])

#distribution of passengers embarked
axes[2,0].bar(df['Embarked'].value_counts().index, df['Embarked'].value_counts(), color=['yellow', 'cyan', 'purple'])
axes[2,0].set_xlabel('Embarked')
axes[2,0].set_ylabel('Count')
axes[2,0].set_title('Distribution of Embarked')
axes[2,0].set_xticklabels(df['Embarked'].value_counts().index, rotation=0)

fig.delaxes(axes[2,1])

plt.tight_layout()

plt.show()
