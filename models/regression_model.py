from sklearn.linear_model import LinearRegression
import numpy as np

# Função para treinar o modelo de regressão
def train_model(vehicle_counts, pedestrian_counts):
    X = np.array(vehicle_counts).reshape(-1, 1)
    y = np.array(pedestrian_counts)

    model = LinearRegression()
    model.fit(X, y)
    return model

# Função para prever o tempo de semáforo com base no fluxo de veículos
def predict_traffic_light_time(model, vehicle_count):
    return model.predict([[vehicle_count]])[0]
