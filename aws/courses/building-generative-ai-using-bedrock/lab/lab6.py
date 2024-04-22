"""
Model integration with Langchain Agents
"""
import json
import os
import sys
import boto3

from langchain.agents import load_tools
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms.bedrock import Bedrock
from langchain import LLMMathChain
# Community tools
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# ---- ⚠️ Un-comment and edit the below lines as needed for your AWS setup ⚠️ ----

# os.environ["AWS_DEFAULT_REGION"] = "<REGION_NAME>"  # E.g. "us-east-1"
# os.environ["AWS_PROFILE"] = "<YOUR_PROFILE>"
# os.environ["BEDROCK_ASSUME_ROLE"] = "<YOUR_ROLE_ARN>"  # E.g. "arn:aws:..."
# os.environ['SERPAPI_API_KEY'] = "<YOUR_SERP_API_KEY>" # Required for the search tool

react_agent_llm = Bedrock(
    model_id="anthropic.claude-instant-v1", 
    model_kwargs={
        "temperature": 0.0, 
        "top_p": .5, 
        "max_tokens_to_sample": 2000
    }
)

math_chain_llm = Bedrock(
    model_id="anthropic.claude-instant-v1",
    model_kwargs={
        "temperature": 0,
        "stop_sequences" : ["```output"]
    }
)

# Create the chain of tools
tools = load_tools(["wikipedia"], llm=react_agent_llm)
llm_math_chain =  LLMMathChain.from_llm(llm=math_chain_llm, verbose=True)

llm_math_chain.llm_chain.prompt.template = """Human: Given a question with a math problem, provide only a single line mathematical expression that solves the problem in the following format. Don't solve the expression only create a parsable expression.
```text
${{single line mathematical expression that solves the problem}}
```

Assistant:
 Here is an example response with a single line mathematical expression for solving a math problem:
```text
37593**(1/5)
```

Human: {question}

Assistant:"""

# prepare the plan
tools.append(
    Tool.from_function(
        func=llm_math_chain.run,
        name="Calculator",
        description="Useful for when you need to answer questions about math.",
    )
)

react_agent = initialize_agent(
    tools, 
    react_agent_llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True,
    #    max_iteration=2,
    #    return_intermediate_steps=True,
    #    handle_parsing_errors=True,
)

prompt_template = """Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do, Also try to follow steps mentioned above
Action: the action to take, should be one of ["Wikipedia", "Calculator"]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {input}

Assistant:
{agent_scratchpad}"""

react_agent.agent.llm_chain.prompt.template=prompt_template

question = "What is Amazon SageMaker? What is the launch year multiplied by 2"
react_agent(question)