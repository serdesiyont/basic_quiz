from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import json, time


template = """
        Context: you will generate one question at a time based on {topic} given by the user
                the questions type should a choice question with four options
                increase the intensity of the questions based on their {score} out of 10,
        
        
        Generating format: quuestions should be generated like as a dictionary
                        questions = 
                             {{
                                        "question": "What is the capital of France?",
                                        "choices": ["London", "Berlin", "Paris", "Madrid"],
                                        "correct_answer": "Paris"
                                 
                                }} 
          """

model = OllamaLLM(model='phi3:latest')

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


topic = input('Type your topic: ')
print('you\'ve 30 second for each question')


def test(time_limit=10):
        score = 0
        for _ in range(10):
                question =json.loads(chain.invoke({"topic": topic, "score": score}))
                
                print(question['question'])
                start_time = int(time.time())
                
                for n, choices in enumerate(question['choices'],1):
                        print(n, choices)
                
                user_ans = int(input())
                answer_time = int(time.time())
        
                last_option = len(question['choices'])
                
                if not 0 < user_ans <= last_option:
                        user_ans = int(input(f'choose between 1 - {last_option} -> '))
                
                if question['choices'][user_ans-1] == question['correct_answer'] and (answer_time - start_time < time_limit):
                        score += 1
                else:
                        print(f'correct: {question['correct_answer']}')
                if answer_time - start_time > time_limit:
                        print('Time Exceeded')
        print(f"you\'ve got {score} out of 10")

test()


