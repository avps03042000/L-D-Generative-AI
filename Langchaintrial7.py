from langchain.llms import FakeListLLM

# Create a fake language model
llm = FakeListLLM(responses=["Simulated response to the query."])
response = llm.predict("What is LangChain?")
print(response)
