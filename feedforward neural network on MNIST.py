import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# 1. Load dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 2. Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# 3. Flatten
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# 4. Build model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# 5. Compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 6. Train
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)

# 7. Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)

print("\n📊 Final Results:")
print("Test Accuracy:", test_acc)
print("Test Loss:", test_loss)

# 8. Plot Accuracy Graph (WITH Test Accuracy)
plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title(f'Model Accuracy (Test Accuracy = {test_acc:.4f})')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['Training Accuracy', 'Validation Accuracy'])

# Add text inside graph
plt.text(2, 0.5, f'Test Acc: {test_acc:.4f}', fontsize=12)

plt.show()

# 9. Plot Loss Graph (WITH Test Loss)
plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title(f'Model Loss (Test Loss = {test_loss:.4f})')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['Training Loss', 'Validation Loss'])

# Add text inside graph
plt.text(2, max(history.history['loss']), f'Test Loss: {test_loss:.4f}', fontsize=12)

plt.show()