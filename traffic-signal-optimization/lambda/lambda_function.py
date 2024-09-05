import boto3
from sklearn.linear_model import LinearRegression
import numpy as np

# Inicializa o cliente DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TrafficData')

# Função Lambda para ajustar os semáforos com base no modelo preditivo
def lambda_handler(event, context):
    intersection_id = event['intersection_id']
    
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('IntersectionID').eq(intersection_id)
    )

    vehicle_counts = [item['VehicleCount'] for item in response['Items']]
    pedestrian_counts = [item['PedestrianCount'] for item in response['Items']]

    X = np.array(vehicle_counts).reshape(-1, 1)
    y = np.array(pedestrian_counts)

    model = LinearRegression()
    model.fit(X, y)

    predicted_time = model.predict([[vehicle_counts[-1]]])[0]

    adjust_traffic_light(intersection_id, predicted_time)

    return {'message': 'Semáforo ajustado com sucesso'}

def adjust_traffic_light(intersection_id, time):
    print(f"Semáforo da interseção {intersection_id} ajustado para {time} segundos.")
