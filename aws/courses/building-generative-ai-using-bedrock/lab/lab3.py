"""
Question and answers.

Before being able to answer the questions, the documents must be processed and
a stored in a document store index.
"""
import os
import json
import botocore
from labutils import bedrock, print_ww


boto3_bedrock = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None)
)

# First prompt
prompt_data = """You are an helpful assistant. Answer questions in a concise way. If you are unsure about the
answer say 'I am unsure'

Question: How can I fix a flat tire on my Audi A8?
Answer:"""

# Parameters
parameters = {
    "maxTokenCount": 512,
    "stopSequences": [],
    "temperature": 0,
    "topP": 0.9
}

# The first answer won't give I am unsure. 
# try:
#     response = boto3_bedrock.invoke_model(
#         body=json.dumps(
#             {
#                 "inputText": prompt_data, 
#                 "textGenerationConfig": parameters
#             }
#         ), 
#         modelId='amazon.titan-text-express-v1', 
#         accept='application/json', 
#         contentType='application/json'
#     )
#     response_body = json.loads(response.get("body").read())
#     answer = response_body.get("results")[0].get("outputText")
#     print_ww(answer.strip())

# except botocore.exceptions.ClientError as error:
#     if  error.response['Error']['Code'] == 'AccessDeniedException':
#         print(f"\x1b[41m{error.response['Error']['Message']}\
#         \nTo troubeshoot this issue please refer to the following resources.\
#          \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
#          \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")      
#         class StopExecution(ValueError):
#             def _render_traceback_(self):
#                 pass
#         raise StopExecution        
#     else:
#         raise error

# Now we can train the model given more holistic answer, close
# to the real one. This model is hallucinating
# prompt_data = "How can I fix a flat tire on my Amazon Tirana?"
# response = boto3_bedrock.invoke_model(
#     body=json.dumps(
#         {
#             "inputText": prompt_data, 
#             "textGenerationConfig": parameters
#         }
#     ), 
#     modelId='amazon.titan-text-express-v1', 
#     accept='application/json', 
#     contentType='application/json'
# )
# response_body = json.loads(response.get("body").read())
# answer = response_body.get("results")[0].get("outputText")
# print_ww(answer.strip())

# To fix that we use the RAG approach. Retrieval Augmented Generation
# Giving information to inflate the context base, so the model can match
# the question with the required information.
context = """Tires and tire pressure:

Tires are made of black rubber and are mounted on the wheels of your vehicle. They provide the necessary grip for driving, cornering, and braking. Two important factors to consider are tire pressure and tire wear, as they can affect the performance and handling of your car.

Where to find recommended tire pressure:

You can find the recommended tire pressure specifications on the inflation label located on the driver's side B-pillar of your vehicle. Alternatively, you can refer to your vehicle's manual for this information. The recommended tire pressure may vary depending on the speed and the number of occupants or maximum load in the vehicle.

Reinflating the tires:

When checking tire pressure, it is important to do so when the tires are cold. This means allowing the vehicle to sit for at least three hours to ensure the tires are at the same temperature as the ambient temperature.

To reinflate the tires:

    Check the recommended tire pressure for your vehicle.
    Follow the instructions provided on the air pump and inflate the tire(s) to the correct pressure.
    In the center display of your vehicle, open the "Car status" app.
    Navigate to the "Tire pressure" tab.
    Press the "Calibrate pressure" option and confirm the action.
    Drive the car for a few minutes at a speed above 30 km/h to calibrate the tire pressure.

Note: In some cases, it may be necessary to drive for more than 15 minutes to clear any warning symbols or messages related to tire pressure. If the warnings persist, allow the tires to cool down and repeat the above steps.

Flat Tire:

If you encounter a flat tire while driving, you can temporarily seal the puncture and reinflate the tire using a tire mobility kit. This kit is typically stored under the lining of the luggage area in your vehicle.

Instructions for using the tire mobility kit:

    Open the tailgate or trunk of your vehicle.
    Lift up the lining of the luggage area to access the tire mobility kit.
    Follow the instructions provided with the tire mobility kit to seal the puncture in the tire.
    After using the kit, make sure to securely put it back in its original location.
    Contact Audi or an appropriate service for assistance with disposing of and replacing the used sealant bottle.

Please note that the tire mobility kit is a temporary solution and is designed to allow you to drive for a maximum of 10 minutes or 8 km (whichever comes first) at a maximum speed of 80 km/h. It is advisable to replace the punctured tire or have it repaired by a professional as soon as possible."""

# Now ask again but this time with context
question = "How can I fix a flat tire on my Audi A8?"
prompt_data = f"""Answer the question based only on the information provided between ## and give step by step guide.
#
{context}
#

Question: {question}
Answer:"""

response = boto3_bedrock.invoke_model(
    body=json.dumps(
        {
            "inputText": prompt_data, 
            "textGenerationConfig": parameters
        }
    ), 
    modelId='amazon.titan-text-express-v1', 
    accept='application/json', 
    contentType='application/json'
)
response_body = json.loads(response.get("body").read())
answer = response_body.get("results")[0].get("outputText")
print_ww(answer.strip())