from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model  = ChatGroq(temperature = 0,model="llama-3.3-70b-versatile")

messages = [
    ("system","You are a comedian who tells joke about {topic}"),
    ("human","Tell me {joke_count} jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic":"lawyers","joke_count":3})

print(result)