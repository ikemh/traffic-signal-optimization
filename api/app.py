from flask import Flask, request, jsonify
import boto3
import time

app = Flask(__name__)

# Inicializa o cliente DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TrafficData')

# Rota para coletar dados de tráfego
@app.route('/collect_traffic_data', methods=['POST'])
def collect_traffic_data():
    try:
        data = request.json
        timestamp = int(time.time())

        # Armazena os dados no DynamoDB
        table.put_item(
            Item={
                'IntersectionID': data['intersection_id'],
                'VehicleCount': data['vehicle_count'],
                'PedestrianCount': data['pedestrian_count'],
                'Timestamp': timestamp
            }
        )

        return jsonify({'message': 'Dados coletados com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
