import boto3
import json
import uuid
import logging

# S3 and Comprehend clients
s3_client = boto3.client('s3')
comprehend_client = boto3.client('comprehend')

def lambda_handler(event, context):
    try:
        # Extract bucket name and file key from the event
        review_bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']
        logging.info(f"Processing file: {file_name} from bucket: {review_bucket_name}")
        
        # Fetch the file content from S3
        file_content = s3_client.get_object(Bucket=review_bucket_name, Key=file_name)
        reviews = json.loads(file_content['Body'].read().decode('utf-8'))
        
        # Prepare a list to store sentiment analysis results
        sentiment_analysis_results = []
        
        # Perform sentiment analysis for each review
        for review in reviews:
            sentiment = comprehend_client.detect_sentiment(
                Text=review['product_review'],  
                LanguageCode='en'  
            )
             # Add the sentiment result to the review
            review['sentiment'] = sentiment['Sentiment'] 
            sentiment_analysis_results.append(review)
        
        # Upload the processed data to the output bucket in JSON Lines format
        output_bucket = 'sentiment-analysis-bucket-1234'  
        output_key = f"sentiment_analysis_results_{uuid.uuid4()}.json"
        
        # Writing the output as JSON Lines format in separate line
        lines = [json.dumps(result) for result in sentiment_analysis_results]  
        s3_client.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body='\n'.join(lines), 
            ContentType='application/json'  
        )
        
        logging.info(f"Sentiment results uploaded to {output_bucket}/{output_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Sentiment analysis completed')
        }
    
    except Exception as e:
        logging.error(f"Error processing the file: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")  
        }

