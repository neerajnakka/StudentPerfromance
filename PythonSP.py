import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# Define the attributes of the dataset
s_no = np.arange(1, 101)
names = np.array(['Student' + str(i) for i in range(1, 101)])
subjects = np.array(['Maths', 'Physics', 'Chemistry'])
grades = np.array(['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F'])
status = np.array(['happy', 'sad', 'neutral'])
time_spent_on_games = np.array(['none', 'less_than_an_hour', 'more_than_an_hour'])

# Create a synthetic dataset with the defined attributes
data = pd.DataFrame({
    's_no': s_no,
    'name': names,
    'maths': np.random.choice(grades, size=100),
    'physics': np.random.choice(grades, size=100),
    'chemistry': np.random.choice(grades, size=100),
    'status': np.random.choice(status, size=100),
    'time_spent_on_games': np.random.choice(time_spent_on_games, size=100)
})

# Map the grades to numerical values
le = LabelEncoder()
data['maths'] = le.fit_transform(data['maths'])
data['physics'] = le.fit_transform(data['physics'])
data['chemistry'] = le.fit_transform(data['chemistry'])

# Map the status to numerical values
data['status'] = np.where(data['status'] == 'happy', 1, np.where(data['status'] == 'sad', -1, 0))

# Map the time spent on games to numerical values
data['time_spent_on_games'] = np.where(
    data['time_spent_on_games'] == 'none', 1,
    np.where(
        data['time_spent_on_games'] == 'less_than_an_hour',
        np.random.uniform(1.0, 1.2, size=100),
        np.random.uniform(0.5, 1.0, size=100)
    )
)

# Create a new column for performance based on the attributes
def performance(row):
    if row['status'] == 1:
        if row['time_spent_on_games'] == 'none':
            return 'good'
        else:
            return 'normal'
    elif row['status'] == -1:
        return 'bad'
    else:
        if row['time_spent_on_games'] == 'less_than_an_hour':
            return np.random.choice(['slightly_increase', 'unchanged'])
        else:
            return 'unchanged'

data['performance'] = data.apply(performance, axis=1)

# Split the dataset into training and testing sets
train_data = data.sample(frac=0.8, random_state=1)
test_data = data.drop(train_data.index)

# Define the features and the target variable
features = ['maths', 'physics', 'chemistry', 'status', 'time_spent_on_games']
target = 'performance'

# Train a Random Forest model on the processed data
rf_model = RandomForestClassifier(n_estimators=100, random_state=1)
rf_model.fit(train_data[features], train_data[target])

# Make predictions on the test data
test_predictions = rf_model.predict(test_data[features])

# Print the classification report and confusion matrix
print(classification_report(test_data[target], test_predictions))
print(confusion_matrix(test_data[target], test_predictions))
