import boto3
import logging
import sys

my_session = boto3.session.Session()
print('region: '+my_session.region_name)
ml_client = my_session.client('machinelearning')

Results = ml_client.describe_batch_predictions()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting batch_prediction {}'.format(Result['BatchPredictionId']))
        Response = ml_client.delete_batch_prediction(BatchPredictionId=Result['BatchPredictionId'])
        print(Response)
        
else:
    logging.warning('No batch predictions found')

Results = ml_client.describe_evaluations()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting Evaluation {}'.format(Result['EvaluationId']))
        Response = ml_client.delete_evaluation(EvaluationId=Result['EvaluationId'])
        print(Response)
else:
    logging.warning('No evaluation found')


Results = ml_client.describe_ml_models()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting model and endpoint for {}'.format(Result['MLModelId']))
        Response = ml_client.delete_realtime_endpoint(MLModelId=Result['MLModelId'])
        print(Response)
        Response = ml_client.delete_ml_model(MLModelId=Result['MLModelId'])
        print(Response)
else:
    logging.warning('No models found')

Results = ml_client.describe_data_sources()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting model and endpoint for {}'.format(Result['DataSourceId']))
        Response = ml_client.delete_data_source(DataSourceId=Result['DataSourceId'])
        print(Response)
else:
    logging.warning('No data source found')

