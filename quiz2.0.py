from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
        Context: you will generate one question at a time based on {topic} given by the user
                the questions type should a choice question with four options
                increase the intensity of the questions based on their {score} out of 10,
        
        
        Generating format: quuestions should be generated like as a dictionary
                        questions = 
                             {{
                                        "question": "What is the capital of France?",
                                        "choices": ["London", "Berlin", "Paris", "Madrid"],
                                        "correct_answer": "Paris",
                                 
                                }} 
          """

model = OllamaLLM(model='gemma:2b')

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model
def test() -> None:
        score = 0
        topic = input('Type your topic: ') 
        questions = chain.invoke({"topic": topic, "score": score})
        print(questions)
test()


