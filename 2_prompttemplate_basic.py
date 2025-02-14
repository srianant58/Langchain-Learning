from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain.prompts import ChatPromptTemplate

load_dotenv()

model  = ChatGroq(temperature = 0,model="llama-3.3-70b-versatile")

# part 1
# template = "Tell me a joke about {topic}"
# prompt_template = ChatPromptTemplate.from_template(template)

# print("----Prompt from Template------")
# prompt =prompt_template.invoke({"topic":"cats"})
# print(prompt)

# part 3: Prompt with System and Human messages
messages = [
    ("system","You are a comedian who tells joke about {topic}"),
    ("human","Tell me {joke_count} jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"lawyer","joke_count":3})
print("\n----Prompt with System and Human Message-----")
# print(prompt)

result = model.invoke(prompt)
print(result.content)