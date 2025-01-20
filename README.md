# AI-Powered-Sentiment-Analysis-of-Product-Review

In this project, we will create an automated pipeline for analyzing the sentiment of product reviews. Instead of building a full application, we will upload product reviews in JSON format to an Amazon S3 bucket. As soon as a new file is uploaded to S3, an S3 event notification will trigger an AWS Lambda function. This Lambda function will use the Amazon Comprehend API to perform sentiment analysis on each review in the uploaded file. Once the sentiment data is processed, the Lambda function will upload the analyzed results to a new S3 bucket in JSON format. Amazon Athena will then be used to query the sentiment data stored in S3. Finally, the data will be seamlessly integrated with Amazon QuickSight for interactive visualization, providing insightful analysis of the sentiment trends.


![AI-Powered Sentiment Analysis for Product Reviews (2)](https://github.com/user-attachments/assets/8189fb99-6979-432d-8525-a2c62d49342a)
## Prerequisite:

- AWS Account
- QuickSight Account Setup
- Experience working with AWS Services
- Programming skills: Python, JSON

## Steps:

✅ Create S3 Buckets

✅ Create Lambda Function

✅ Write Python code

✅ Create S3 Event Notification to Trigger Lambda

✅ Set up Athena for Querying S3 Data

✅ Setup Amazon QuickSight for Visualization

