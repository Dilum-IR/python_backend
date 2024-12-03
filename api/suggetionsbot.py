# """suggetionsBot.ipynb

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1_7o8brYHWrAiZlPqyAzNNOjGh6L2YrVu
# """
import os
from dotenv import load_dotenv
import warnings
from langchain_openai import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import ast
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_core.output_parsers import StrOutputParser
# from system.system_msg import system_prompt,large_question_answer_dataset

class SuggestionsBot:
    def __init__(self):
        self.load_env_variables()
        self.llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0)
        self.examples = self.get_examples()
        self.few_shot_prompt = self.create_few_shot_prompt()
        self.prompt = self.create_chat_prompt_template()

    def load_env_variables(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")

    def get_examples(self):

        large_question_answer_dataset = [

            {"Question": "Hi", "Answer": ["I am fine", "I am not good"]},
            {"Question": "Did you eat?", "Answer": ["Yes", "No"]},
            {"Question": "Do you like to travel?", "Answer": ["Yes", "No"]},
            {"Question": "hey,Do you have a car?", "Answer": ["Yes", "No"]},
            {"Question": "Where are you now?", "Answer": ["In the home", "In the school", "another place"]},
            {"Question": "There is a car", "Answer": ["yeah I see, man"]},
            {"Question": "What is your favorite color?", "Answer": ["Red", "Blue", "Green", "Yellow", "Other"]},
            {"Question": "How old are you?", "Answer": ["10"]},
            {"Question": "What is your favorite food?", "Answer": ["Pizza", "Burger", "Salad", "Pasta", "Other"]},
            {"Question": "What is the capital of France?", "Answer": ["Paris"]},
            {"Question": "Do you play any sports?", "Answer": ["Yes", "No"]},
            {"Question": "What are your hobbies?", "Answer": ["Reading", "Traveling", "Cooking", "Sports", "Other"]},
            {"Question": "What is your favorite book?", "Answer": ["[Book Title]"]},
            {"Question": "What is your favorite movie?", "Answer": ["[Movie Title]"]},
            {"Question": "What is your favorite season?", "Answer": ["Spring", "Summer", "Autumn", "Winter"]},
            {"Question": "Do you have any pets?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite holiday destination?", "Answer": ["Beach", "Mountains", "City", "Countryside"]},
            {"Question": "What languages do you speak?", "Answer": ["English", "Spanish", "French", "German", "Other"]},
            {"Question": "What is your favorite music genre?", "Answer": ["Pop", "Rock", "Classical", "Jazz", "Hip Hop", "Other"]},
            {"Question": "Do you prefer coffee or tea?", "Answer": ["Coffee", "Tea"]},
            {"Question": "Are you a morning person or a night owl?", "Answer": ["Morning person", "Night owl"]},
            {"Question": "Do you like reading books?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite sport to watch?", "Answer": ["Soccer", "Basketball", "Baseball", "Tennis", "Other"]},
            {"Question": "Do you enjoy cooking?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite animal?", "Answer": ["Dog", "Cat", "Bird", "Fish", "Other"]},
            {"Question": "Do you like to exercise?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite ice cream flavor?", "Answer": ["Chocolate", "Vanilla", "Strawberry", "Mint", "Other"]},
            {"Question": "Do you enjoy outdoor activities?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite type of cuisine?", "Answer": ["Italian", "Chinese", "Mexican", "Indian", "Other"]},
            {"Question": "Do you play any musical instruments?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite type of weather?", "Answer": ["Sunny", "Rainy", "Snowy", "Windy"]},
            {"Question": "What is your favorite dessert?", "Answer": ["Cake", "Pie", "Ice Cream", "Cookies", "Other"]},
            {"Question": "Do you like watching movies?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite thing to do on weekends?", "Answer": ["Relaxing", "Traveling", "Sports", "Reading", "Other"]},
            {"Question": "Do you have any siblings?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite holiday?", "Answer": ["Christmas", "Thanks giving", "Halloween", "New Year", "Other"]},
            {"Question": "Do you prefer sweet or savory snacks?", "Answer": ["Sweet", "Savory"]},
            {"Question": "What is your favorite fruit?", "Answer": ["Apple", "Banana", "Orange", "Grapes", "Other"]},
            {"Question": "Do you like to dance?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite board game?", "Answer": ["Monopoly", "Chess", "Scrabble", "Catan", "Other"]},
            {"Question": "Do you prefer the beach or the mountains?", "Answer": ["Beach", "Mountains"]},
            {"Question": "What is your favorite drink?", "Answer": ["Water", "Juice", "Soda", "Tea", "Coffee"]},
            {"Question": "What is your favorite holiday tradition?", "Answer": ["Decorating", "Cooking", "Traveling", "Gift Giving", "Other"]},
            {"Question": "What is your favorite time of the day?", "Answer": ["Morning", "Afternoon", "Evening", "Night"]},
            {"Question": "Do you enjoy gardening?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite type of flower?", "Answer": ["Rose", "Tulip", "Lily", "Daisy", "Other"]},
            {"Question": "Do you like to draw or paint?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite hobby?", "Answer": ["Cricket","badminton","chess"]},
            {"Question": "What is your favorite way to relax?", "Answer": ["Reading", "Watching TV", "Exercising", "Spending time with family", "Other"]},
            {"Question": "What is your favorite type of book?", "Answer": ["Fiction", "Non-Fiction", "Mystery", "Romance", "Sci-Fi", "Fantasy", "Other"]},
            {"Question": "Do you like to go camping?", "Answer": ["Yes", "No"]},
            {"Question": "What is your favorite type of tree?", "Answer": ["Oak", "Pine", "Maple", "Birch", "Other"]},
            {"Question": "Do you enjoy puzzles?", "Answer": ["Yes", "No"]},
            {"Question": "can you give me a pen?", "Answer": ["yeah I can","I don't have"]}
            
        ]
                
        # return [
        #     {"Question": "Did you eat ?", "Answer": ["Yes", "No"]},
        #     {"Question": "Do you have a car ?", "Answer": ["Yes", "No"]},
        #     {"Question": "Where are you now ?", "Answer": ["In the home", "In the school", "another place"]},
        #     {"Question": "There is a car", "Answer": ["yeah I see, man"]},
        #     # {"Question": "What is your name ? who are you ?", "Answer": ["My Name is Dilum Induwara"]},
        # ]

        return large_question_answer_dataset

    def create_few_shot_prompt(self):
        example_prompt = PromptTemplate(
            input_variables=["Question", "Answer"],
            template="{Answer}"
        )

        return FewShotPromptTemplate(
            examples=self.examples,
            example_prompt=example_prompt,
            suffix="Question: {input}",
            input_variables=["input"]
        )

    def create_chat_prompt_template(self):

        # define a system message (instruction) prompt
        system_prompt = """
            Very Important things:
            Generate suggestions that are relevant to a school setting. The suggestions should include examples like answers to common classroom questions, tips for studying, or advice for completing assignments. Focusing on the content of the suggestions with a school-appropriate tone.
            You are now not just a chatbot,
            Please Response not give the ["I'm here to assist you"] as well as assist word include response.
            You are name is and email is include in the history. Please get the user name and email from the chat History
            \n use the above given context and following example type response for answering for the question.
            And Any user given questions for can give a multiple answers then you need to get above type multiple answers with list
            If you don't know the answers then only give the response ('I don't know.')
            \n
            Response is Multiple list of answers Type : Multiple => ["....","....","...."]
            \n

            Example 1:
            Question : "Did you eat ?"
            Response : ["yes","No"]
            \n
            Example 3:
            Question : "What is your favorite ice cream flavor"
            Response : ["Chocolate", "Vanilla", "Strawberry", "Mint", "Other"]
            \n

            Example 4:
            Question : "What is your name ?"
            Response : ["My name is (user given name include history get to for this position if not include give a I don't know)"]
            \n

            Example 5:
            Question : "This is a car man."
            Response : ["Yeah I see man"]
            \n

            Example 6:
            Question : "sfsfdsfsdf."
            Response : ["I don't know"]
            \n

            Example 7:
            Question : "hello Do you know me?"
            Response : ["Yeah, Nice to meet you" , "I don't know. who are you?","hello hi"]
            \n

            Example 8:
            Question : "hi"
            Response : ["hi, Nice to meet you" , "I don't know. who are you?","hello"]
            \n

            Example 9:
            Question : "can you give me a pen"
            Response : ["I don't have" , "I don't know.","yes I can"]
            \n
            
            Example 10:
            Question : "what are you doing"
            Response : ["Nothing special" , "you can suggest it","feeling well"]
            \n
            
            Example 11:
            Question : "whats the problem dear"
            Response : ["Nothing" , "I have some school problem","My friend is left from the school"]
            \n
            

            If user asked question is QUESTION type then response needed list of multiple asnwers.
            If you don't know answer for question. then please suggest answer for it. always don't give the (I don't know) for response.

            Guidelines:
            - If you have the personal detail, respond accurately.
            - If you can't understand. then response must be (I don't know)
            - If you do not have the personal detail,please give a response as "I don't know." 
            - If you don't details for can genarate that personal details Question for list of choices then please response it.
            - Every respose are needed Json array list type
            - Each asked questions for respnose needed JSON type array list (Response needed type is mention in the above).
            - If user asked questions then please give to the best suitable list of suggetions.
            - If user asked questions is not a question. It is like normal user's talking then give a some suitable response for it.
            - Keep your responses concise wherever possible unless you have to provide additional details.
            - Response must have at least two, three or list of the elements.
            - Finally When user asked question related answer have in history then please answer that history include AIMessage for response.
            - Please You can genarate asked questions for it's related answers.
            \n\n

            """

        return ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_prompt),
                MessagesPlaceholder(variable_name="history"),
                MessagesPlaceholder(variable_name="input")
            ]
        )
    
    def get_single_response(self,input,user_history,personal_data):

        try:

            # self.create_chat_prompt_template(personal_data)
            user_name = "My name is {name}. And you."
            user_email = "My email is {email}."
            user_age = "I am {age} years old."

            new_name =  user_name.format(**personal_data[0])
            new_email =  user_email.format(**personal_data[1])
            new_age =  user_age.format(**personal_data[2])
            
            history = [
                HumanMessage(content="what is your name"), 
                AIMessage(content=new_name), 
                HumanMessage(content="what is your email"),
                AIMessage(content=new_email),
                AIMessage(content=new_name), 
                HumanMessage(content="how old are you"),
                AIMessage(content=new_age),
            ]
            
            # Insert history messages after the first messages
            for item in user_history:

                if item["role"] == "user":
                    history.append(HumanMessage(content=item["content"]))
                elif item["role"] == "assistant":
                    history.append(AIMessage(content=item["content"]))

            parser = StrOutputParser()
            # print(self.few_shot_prompt)
            chain = self.prompt | self.llm | parser

            response = chain.invoke({ "history": history ,"input": [HumanMessage(content=input)]})

            # try:
            #     answer_start = response.find("Answer: ") + len("Answer: ")
            #     answer = response[answer_start:].strip()
            #     answer_list = json.loads(answer)
            #     ans = ast.literal_eval(answer)
            # except (json.JSONDecodeError, ValueError):
            #     answer_list = response

            # add latest question and response for the chat history
            # history.extend(
            #     [
            #     HumanMessage(content=input),
            #     AIMessage(content=response)
            #     ]
            # )

            # print(history)
            ans = self.process_answer(response)
            return ans

        except:
            return ["I don't know"]

    def get_response(self, user_input, history=[]):

        # print(self.few_shot_prompt)

        final_prompt = [
            {"role": "system", "content": "If some one ask some personal details from you. then if you have it please response with give that data. If you haven any that data then response for message is ('I am don't know it.'). Now your are not a chatbot. your are now human. Your name is Dilum Induwara. No need metion another parts."},
            {"role": "system", "content": self.few_shot_prompt.format(input=user_input)},
            {"role": "user", "content": user_input}
        ]
        
        # Insert history messages after the first messages
        for item in history:
            final_prompt.insert(2, item) 

        response = self.llm(self.few_shot_prompt.format(input=user_input)).content
        
        ans = self.process_answer(response)
        # print(ans)
        return ans

    def process_answer(self,answer_str):
        if answer_str.startswith("Answer: "):
            value_str = answer_str[len("Answer: "):]
        else:
            value_str = answer_str
        
        try:
            value = ast.literal_eval(value_str)
            if isinstance(value, list):
                return value
        except (ValueError, SyntaxError):
            pass

        return [value_str]
    
