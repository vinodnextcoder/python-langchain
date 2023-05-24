from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI

# setup llm
llm = OpenAI(temperature=0, openai_api_key='', model_name='gpt-3.5-turbo')

# Setup database

urldb = 'mysql+pymysql://root:root@localhost/testdb'
db = SQLDatabase.from_uri(urldb)

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)


def get_prompt():
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                question = prompt
                print(db_chain.run(question))
            except Exception as e:
                print(e)


get_prompt()