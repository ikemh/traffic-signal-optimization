import boto3
import time

# Inicializa o cliente DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TrafficAdjustmentsLog')

def log_adjustment(intersection_id, time_adjusted):
    table.put_item(
        Item={
            'IntersectionID': intersection_id,
            'TimeAdjusted': time_adjusted,
            'Timestamp': int(time.time())
        }
    )
    print(f"Log registrado: Interseção {intersection_id} ajustada para {time_adjusted} segundos.")
