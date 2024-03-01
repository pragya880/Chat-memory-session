# setup mongodb cloud
uri = "mongodb+srv://raipragya256:<password>@cluster0.fym3xyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0uri"
# connect mongodb client to langchain
message_history = MongoDBChatMessageHistory(
        connection_string=uri, session_id="abc"
)

# setup buffermemory

memory = ConversationBufferMemory()
 
 #3 add message hisory from mondgodb to bufferrmemory

memories.save_context(
    {"input": message_history.messages[0].conent},
    {"output": message_history.messages[1].content}

    # connect llm, buffermemory to langchain

    os.environ("OPENAI_API_KEY") = ""
    llm = OpenAI(temperature=0.5)
    Conversation = ConversationChain(
                                     llm=llm,
                                     Verbose=false,  
                                     prompt=PROMPT
                                     memory=memories
    )                               

    )
)