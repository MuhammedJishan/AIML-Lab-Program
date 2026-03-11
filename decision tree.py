# =====================================================
# Decision Tree Classifier on Iris Dataset
# =====================================================

# 1. Import Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 2. Load the Iris Dataset
iris = load_iris()

X = iris.data          # Features
y = iris.target        # Target labels

feature_names = iris.feature_names
class_names = iris.target_names


# 3. Split Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# 4. Create the Decision Tree Model
model = DecisionTreeClassifier(
    criterion='gini',     # Splitting criterion (gini or entropy)
    max_depth=3,          # Optional: control overfitting
    random_state=42
)


# 5. Train the Model
model.fit(X_train, y_train)


# 6. Make Predictions
y_pred = model.predict(X_test)


# 7. Model Evaluation

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Evaluation")
print("-----------------")
print("Accuracy:", round(accuracy, 4))
print("Overall Accuracy = {:.2f}%".format(accuracy * 100))


# Classification Report
print("\nClassification Report")
print("---------------------")
print(classification_report(y_test, y_pred, target_names=class_names))


# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix")
print("----------------")
print(cm)


# 8. Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=feature_names,
    class_names=class_names,
    filled=True
)
plt.title("Decision Tree - Iris Dataset")
plt.show()