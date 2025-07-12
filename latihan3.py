import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
# Set visualization styles
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# For better visualization in the notebook
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Suppress warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

# 1. Load dataset
df = pd.read_csv('C:\latpython\StudentsSocialMediaAddiction.csv')

# 2. Preprocessing
# Buat label 'Addicted' berdasarkan Addicted_Score
df['Addicted'] = df['Addicted_Score'] > 7

# Pilih fitur yang relevan
features = [
    'Age', 'Academic_Level', 'Avg_Daily_Usage_Hours',
    'Most_Used_Platform', 'Affects_Academic_Performance',
    'Sleep_Hours_Per_Night', 'Mental_Health_Score',
    'Relationship_Status', 'Conflicts_Over_Social_Media'
]

X = df[features]
y = df['Addicted']

# Encode fitur kategorikal
X = pd.get_dummies(X)

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = RandomForestClassifier(random_state=78)
model.fit(X_train, y_train)

# 5. Evaluasi
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 6. Prediksi contoh baru
sample = X_test.iloc[0:1]
prediction = model.predict(sample)
print("Prediksi kecanduan:", "Ya" if prediction[0] else "Tidak")

# #### Most Used Platforms
plt.figure(figsize=(14, 7))
platform_counts = df['Most_Used_Platform'].value_counts()
sns.barplot(x=platform_counts.index, y=platform_counts.values, palette='viridis')
plt.title('Most Used Social Media Platforms', fontsize=14)
plt.xlabel('Platform', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.show()