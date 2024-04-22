"""
1. A large document (or a giant file appending small ones) is loaded
2. Langchain utility is used to split it into multiple smaller chunks (chunking)
3. First chunk is sent to the model; Model returns the corresponding summary
4. Langchain gets next chunk and appends it to the returned summary and sends the combined text as a new request to the model; the process repeats until all chunks are processed
5. In the end, you have final summary based on entire content
"""
import os
import json
from labutils import bedrock, print_ww
from langchain.llms.bedrock import Bedrock
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


boto3_bedrock = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None)
)

# Initialize langchain
llm = Bedrock(
    model_id='amazon.titan-text-express-v1',
    model_kwargs={
        "maxTokenCount": 4096,
        "stopSequences": [],
        "temperature": 0,
        "topP": 1,
    },
    client=boto3_bedrock,
)

# Load the text
with open("./letters/2022-letter.txt", "r") as file:
    letter = file.read()
    
llm.get_num_tokens(letter)

# split the text in chuncks
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n"], 
    chunk_size=4000, 
    chunk_overlap=100
)

# final list of chuncks
docs = text_splitter.create_documents([letter])
num_docs = len(docs)
num_tokens_first_doc = llm.get_num_tokens(docs[0].page_content)

print(
    f"Now we have {num_docs} documents and the first one has {num_tokens_first_doc} tokens"
)

# Loading the summary
summary_chain = load_summarize_chain(
    llm=llm, 
    chain_type="map_reduce", 
    verbose=False # Set as true for debugging
)

# Processing result
output = ""
try:
    output = summary_chain.run(docs)
except ValueError as error:
    if  "AccessDeniedException" in str(error):
        print(f"\x1b[41m{error}\
        \nTo troubeshoot this issue please refer to the following resources.\
         \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
         \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")      
        class StopExecution(ValueError):
            def _render_traceback_(self):
                pass
        raise StopExecution        
    else:
        raise error
    
print_ww(output.strip())