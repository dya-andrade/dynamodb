import boto3

# URL do endpoint do LocalStack
endpoint_url = "http://localhost.localstack.cloud:4566"

def create_dynamodb_table():
    # Conectar ao serviço DynamoDB no LocalStack
    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url=endpoint_url,
        region_name='sa-east-1',
        aws_access_key_id='fake_access_key',
        aws_secret_access_key='fake_secret_key'
    )

    table_name = 'player_history_entity'

    # Criar a tabela
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'game_id',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'game_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Esperar até a tabela estar ativa
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    print(f'Tabela {table_name} criada com sucesso.')

def main():
    create_dynamodb_table()

if __name__ == "__main__":
    main()