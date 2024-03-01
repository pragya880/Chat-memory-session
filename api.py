from fastapi import FastAPI
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, MongoDBChatMessageHistory
from langchain.prompts.prompt import PromptTemplate

# Setup mongodb client
uri = "mongodb+srv://raipragya256:<password>@cluster0.fym3xyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0uri"

# Setup openai
llm = OpenAI(api_key="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", temperature=0.5, desc="Chatbot")

app = FastAPI(desc="Chatbot")

_DEFAULT_TEMPLATE = "You are a chatbot prepared by pragya"

@app.post("/chat")
def chatbot(input, session):
    message_history = MongoDBChatMessageHistory(
        connection_string=uri, session_id="abc"
    )
    PROMPT = PromptTemplate(
        input_variables=["history", "input"],
        template=_DEFAULT_TEMPLATE,
    )

    memory = ConversationBufferMemory(k=3)

    if len(message_history.messages):
        memory.save_context(
            {"input": message_history.messages[0].content},
            {"output": message_history.messages[1].content}
        )
    Conversation = ConversationChain(
        llm=llm,
        verbose=False,
        prompt=PROMPT,
        memory=memory
    )
    conv = Conversation.predict(input=input, session_id=session)
    message_history.add_user_message(input)
    message_history.add_ai_message(conv)
    return conv

   

