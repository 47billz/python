
'''
describe_batch_predictions()
describe_data_sources()
describe_evaluations()
describe_ml_models()
describe_tags()
'''

'''
delete_batch_prediction()
delete_data_source()
delete_evaluation()
delete_ml_model()
delete_realtime_endpoint()
'''

import boto3
import logging

ml_client = boto3.client('machinelearning')

Results = ml_client.describe_batch_predictions()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting batch_prediction {}'.format(Result['BatchPredictionId']))
        ml_client.delete_batch_prediction(BatchPredictionId=Result['BatchPredictionId'])
else:
    logging.warning('No batch predictions found')

Results = ml_client.describe_evaluations()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting Evaluation {}'.format(Result['EvaluationId']))
        ml_client.delete_evaluation(EvaluationId=Result['EvaluationId'])
else:
    logging.warning('No evaluation found')


Results = ml_client.describe_ml_models()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting model and endpoint for {}'.format(Result['MLModelId']))
        ml_client.delete_realtime_endpoint(MLModelId=Result['MLModelId'])
        ml_client.delete_ml_model(MLModelId=Result['MLModelId'])
else:
    logging.warning('No models found')

Results = ml_client.describe_data_sources()['Results']
if len(Results)>0:
    for Result in Results:
        logging.warning('Deleting model and endpoint for {}'.format(Result['DataSourceId']))
        ml_client.delete_data_source(DataSourceId=Result['DataSourceId'])
else:
    logging.warning('No data source found')