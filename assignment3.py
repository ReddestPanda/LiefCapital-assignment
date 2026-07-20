import json  # For reading JSON data from file
import string  # Provides a list of punctuation characters
from sklearn.feature_extraction.text import CountVectorizer  # Converts text into numerical features
from sklearn.model_selection import train_test_split  # Splits data into training and testing sets
from sklearn.linear_model import LogisticRegression  # Machine learning model for classification
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay  # For evaluating model performance
import matplotlib.pyplot as plt  # For visualizing the confusion matrix

# Define a simple set of stop words (common words to ignore)
stop_words = {"is", "the", "and", "a", "an", "of"}

# Load dataset from a JSON file
with open("dataset.txt", "r") as f:
    data = json.load(f)  # Expecting a list of objects with "text" and "label"

# Prepare lists to store processed text and corresponding labels
texts = []
labels = []

# Loop through each data item
for item in data:
    # Convert text to lowercase for consistency
    text = item["text"].lower()

    # Remove punctuation (e.g., ".", ",", "!")
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split text into individual words (tokens)
    tokens = text.split()

    # Remove stop words (common words that don't add much meaning)
    tokens = [word for word in tokens if word not in stop_words]

    # Join tokens back into a cleaned string
    cleaned_text = " ".join(tokens)

    # Store processed text and its label
    texts.append(cleaned_text)
    labels.append(item["label"])

# Convert text data into a matrix of word counts
# Each row = a document, each column = a word, values = word frequency
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Labels (target values)
y = labels

# Split data into training and testing sets
# 80% for training, 20% for testing
# random_state ensures reproducibility
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize Logistic Regression model
# max_iter increased to ensure convergence for larger datasets
model = LogisticRegression(max_iter=1000)
# Train (fit) the model using training data
model.fit(X_train, y_train)

# Use the trained model to predict labels for test data
y_pred = model.predict(X_test)

# Generate confusion matrix to evaluate predictions
cm = confusion_matrix(y_test, y_pred)

# Print confusion matrix values
print("Confusion Matrix:")
print(cm)

# Explain what the labels mean
print("\nLabel meaning:")
print("0 = Negative")
print("1 = Positive")

# Create a visual display of the confusion matrix
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Negative (0)", "Positive (1)"]
)
# Plot the confusion matrix
disp.plot()
# Show the plot window
plt.show()