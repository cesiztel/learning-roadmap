"""
You are Bob a Customer Service Manager at AnyCompany and some of your customers are not happy with the customer service and are providing negative feedbacks 
on the service provided by customer support engineers. Now, you would like to respond to those customers humbly aplogizing for the poor service and regain 
trust. You need the help of an LLM to generate a bulk of emails for you which are human friendly and personalized to the customer's sentiment from previous 
email correspondence.
"""
import os
import json
import botocore
from labutils import bedrock, print_ww


boto3_bedrock = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None)
)

# create the prompt
prompt_data = """
Command: Write an email from Bob, Customer Service Manager, to the customer "John Doe" 
who provided negative feedback on the service provided by our customer support 
engineer"""

# Invoking the model
# This retrieval is synchronous, so the result won't show
# until the model generates the full output.
# outputText = "\n"
# try:
#     response = boto3_bedrock.invoke_model(
#         body=json.dumps(
#             {
#                 "inputText": prompt_data, 
#                 "textGenerationConfig": {
#                     "maxTokenCount":4096,
#                     "stopSequences":[],
#                     "temperature":0,
#                     "topP":0.9
#                 }
#             }
#         ), 
#         modelId='amazon.titan-text-express-v1', 
#         accept='application/json', 
#         contentType='application/json'
#     )
#     response_body = json.loads(response.get('body').read())

#     outputText = response_body.get('results')[0].get('outputText')

# except botocore.exceptions.ClientError as error:
    
#     if error.response['Error']['Code'] == 'AccessDeniedException':
#            print(f"\x1b[41m{error.response['Error']['Message']}\
#                 \nTo troubeshoot this issue please refer to the following resources.\
#                  \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
#                  \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
        
#     else:
#         raise error
    
# # The relevant portion of the response begins after the first newline character
# # Below we print the response beginning after the first occurence of '\n'.

# email = outputText[outputText.index('\n')+1:]
# print_ww(email)

# Streaming version of the lab.
# The model prints the output as soon it retrieves some results
output = []
try:
    response = boto3_bedrock.invoke_model_with_response_stream(
        body=json.dumps(
            {
                "inputText": prompt_data, 
                "textGenerationConfig": {
                    "maxTokenCount":4096,
                    "stopSequences":[],
                    "temperature":0,
                    "topP":0.9
                }
            }
        ), 
        modelId='amazon.titan-text-express-v1', 
        accept='application/json', 
        contentType='application/json'
    )
    stream = response.get('body')
    
    i = 1
    if stream:
        for event in stream:
            chunk = event.get('chunk')
            if chunk:
                chunk_obj = json.loads(chunk.get('bytes').decode())
                text = chunk_obj['outputText']
                output.append(text)
                print(f'\t\t\x1b[31m**Chunk {i}**\x1b[0m\n{text}\n')
                i+=1
            
except botocore.exceptions.ClientError as error:
    
    if error.response['Error']['Code'] == 'AccessDeniedException':
           print(f"\x1b[41m{error.response['Error']['Message']}\
                \nTo troubeshoot this issue please refer to the following resources.\
                 \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                 \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
        
    else:
        raise error

print('\t\t\x1b[31m**COMPLETE OUTPUT**\x1b[0m\n')
complete_output = ''.join(output)
print(complete_output)