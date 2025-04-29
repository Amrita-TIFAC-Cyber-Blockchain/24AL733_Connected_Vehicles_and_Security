import pandas as pd
import numpy as np
import tensorflow as tf
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout


df = pd.read_csv("/home/IDS_Alert/DoS_dataset.csv")


def safe_hex_to_int(value):
    try:
        return int(value, 16)
    except (ValueError, TypeError):
        return 0


def preprocess_data(df):
    df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors='coerce')
    df['CAN ID'] = df['CAN ID'].apply(lambda x: int(str(x), 16) if isinstance(x, str) and all(c in "0123456789abcdefABCDEF" for c in x) else x)
    df['Flag'] = df['Flag'].map({'T': 1, 'R': 0})


    for col in ['DATA[0]', 'DATA[1]', 'DATA[2]', 'DATA[3]', 'DATA[4]', 'DATA[5]', 'DATA[6]', 'DATA[7]']:
        df[col] = df[col].apply(lambda x: safe_hex_to_int(str(x)) if isinstance(x, str) else 0)


    features = ['Timestamp', 'CAN ID', 'DLC', 'DATA[0]', 'DATA[1]', 'DATA[2]', 'DATA[3]', 'DATA[4]', 'DATA[5]', 'DATA[6]', 'DATA[7]']
    target = 'Flag'

    X = df[features]
    y = df[target]

    df.dropna(inplace=True)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y


X, y = preprocess_data(df)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def build_ann():
    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

ann_model = build_ann()
ann_model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test), verbose=1)


X_train_lstm = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test_lstm = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))


def build_lstm():
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=(1, X_train.shape[1])),
        Dropout(0.3),
        LSTM(32, return_sequences=False),
        Dropout(0.2),
        Dense(16, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

lstm_model = build_lstm()
lstm_model.fit(X_train_lstm, y_train, epochs=20, batch_size=32, validation_data=(X_test_lstm, y_test), verbose=1)


ann_loss, ann_acc = ann_model.evaluate(X_test, y_test)
lstm_loss, lstm_acc = lstm_model.evaluate(X_test_lstm, y_test)


def generate_alert(predictions, model_name):
    alert_log = []
    for i, pred in enumerate(predictions):
        if pred > 0.5:
            alert_message = f"[{datetime.now()}] ALERT: Intrusion detected in {model_name} - Packet Index: {i}"
            print(alert_message)
            alert_log.append(alert_message)


    with open("intrusion_alerts.log", "a") as log_file:
        for entry in alert_log:
            log_file.write(entry + "\n")


ann_preds = ann_model.predict(X_test)
lstm_preds = lstm_model.predict(X_test_lstm)


generate_alert(ann_preds, "ANN")
generate_alert(lstm_preds, "LSTM")


print("\n===== IDS Detection Results =====")
print(f"ANN Accuracy: {ann_acc * 100:.2f}%")
print(f"LSTM Accuracy: {lstm_acc * 100:.2f}%")

if lstm_acc > ann_acc:
    print("LSTM performed better at detecting unknown attacks.")
else:
    print("ANN performed better at detecting known attacks.")
