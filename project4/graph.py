import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('day4/train.csv')

print(df.head())

print(df.shape)

print(df.describe())


#data visualization

plt.hist(df['Age'].dropna(), bins=20, color='orange')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of passenger Ages')
plt.show()

#Survival rates for tianic passengers
plt.bar(df['Survived'].value_counts().index, df['Survived'].value_counts(), color=['red', 'green'])
plt.xlabel('Survived')
plt.ylabel('count')
plt.title('Survival rate of passengers')
plt.xticks([0,1], ['Died', 'Survived'])
plt.show()

#survival rate by gender
survivalByGender = df.groupby('Sex')['Survived'].mean()
survivalByGender.plot(kind='bar', color=['purple', 'skyblue'])
plt.xlabel('Gender')
plt.ylabel('Survival rate')
plt.title('Survival Rate by gender')
plt.xticks(rotation=0)
plt.show()

#passenger class
plt.bar(df['Pclass'].value_counts().index, df['Pclass'].value_counts(), color=['orange', 'green', 'blue'])
plt.xlabel('passenger class')
plt.ylabel('count')
plt.title('Distribution of passenger classes')
plt.xticks([1,2,3])
plt.show()

#distribution of passengers embarked

plt.bar(df['Embarked'].value_counts().index, df['Embarked'].value_counts(), color=['yellow', 'cyan', 'purple'])
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.title('Distribution of Embarked')
plt.xticks(rotation=0)
plt.show()
