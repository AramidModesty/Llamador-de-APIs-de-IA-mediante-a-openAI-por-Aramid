#Archivo por Aramid Monsalve
#AFAn: AI functional assistant
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carga el archivo con tu clave api.
# El archivo con claves secretas siempre es llamado .env
# Crea un archivo con dicho nombre y ponle como contenido
# OPENAI_API_KEY={your_api_key}
# base_url={api_key_provider_url}
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")
if api_key == None:
    raise ValueError("OPENAI_API_KEY not found in .env file")
if base_url == None: #Si vienes directamente de openAI
    client = OpenAI(api_key=api_key)
    print("Si lees esto y no estas en openAI, hay un error en tu .env.",
          "En cuyo caso revisa que tu base_url si este en mayusculas",
          sep="\n")
else:#Si vienes con la api de otro sitio
    client = OpenAI(api_key=api_key,
    base_url=base_url)

def handleAiError(error):
    #Si tu clave api no reconocida.
    if(error.args[0].__contains__("401")):
        print("Error: Invalid API key. Please check your .env file.")
    #Si la id de tu modelo no existe.
    elif(error.args[0].__contains__("403")):
        print("Error: This one is only available on agentic harnesses."\
        "\nchoose another one")
    elif(error.args[0].__contains__("404")):
        print("Error: Model not found. Please check the model ID.")
    #Si tu clave api se quedo sin usos gratuitos.
    elif(error.args[0].__contains__("429")):
        print("Error: Rate limit exceeded. Please try again later.")
    else:
        print("Error:",error)

def askOnceToAI(idModel:str,messages
            ):
    if messages["role"] not in {"system", "user", "assistant"}:
        raise ValueError(f"Invalid role: {messages.role}")
    try:
        answer= client.chat.completions.create(
            model=idModel,
            messages=[messages]
        )
    except Exception as e:
        handleAiError(e)
        return None
    return answer
def conversation(idModel,messages):
    answer= client.chat.completions.create(
        model=idModel,
        messages=messages
    )
    return answer
def sample_message_summon():
    model=getFreeModels()[2]#codigo nombre del modelo
    role="user"
    tools=[ #Aqui es donde se pondrian las funciones de python.
        {"tool_name": "calculator", #El nombre de la funcion
         "tool_description": "A simple calculator for basic arithmetic operations." #El uso que la funcion tiene
         },
        {"tool_name": "weather",
         "tool_description": "Provides current weather information for a specified location."}
    ]
    context={
        "user_id": "user_123",
        "session_id": "session_456"
    }
    content="Who are you?"
    message={"role":role,"content":content,
             "tools":tools,"context":context}
    print("Llamando al modelo:\n", model)
    print("-"*50)
    answer=askOnceToAI(model,message)
    if answer:
        print(answer.choices[0].message.content)
    return answer
def genericMessage(role, content):
    return {
        "role":role,
        "content":content
    }
def getFreeModels():
    models = client.models.list()
    freemodels=[]
    for model in models.data:
        if(model.id.find('free')!=-1):
            freemodels.append(model.id)
    return freemodels
def sample_conversation():
    chat=[]
    message=genericMessage("user","say hello")
    chat.append(message)
    chat=conversation('gpt:free',chat)
    return chat
#Ejecutar desde terminal tambien activa a main.
if __name__=="__main__":
    print("Hola mundo")
    print(sample_message_summon())


#Conversation structure:
"""
messages=[
    {#Message 1
        "role":role,
        "content":text,
        "tools":tools,
    },
    {#Message 2
        "role":role,
        "content":text,
        "tools":tools,
    }
]
"""

#First analisis results
answerCheck={
"System": { #Atributo propio de analisis
    "has_tools": True,
    "has_context": True,
    "api_has_money": False
},
"Prompt": { #Atributo propio de analisis
    "Role": "User",
    "Content": "¿Who are you?"
},
"Made_to": #chat.
    "nvidia/nemotron-3.5-super-vl:free",
"Errors":
    "Only when asked in hours of high traffic",
"Answer": #chat.choices[0].message.content
    """
    I am an AI language model trained by researchers from NVIDIA.
    I don\'t have a physical body, personalexperiences, or consciousness.
    I exist as software designed to process and generate text.

    I can help with things like answering questions, writing and editing,
    coding, brainstorming, summarizing information, and explaining concepts.
    How can I assist you today?
    """,
"Reasoning": #chat.choices[0].message.reasoning
    """
    The user is asking "Who are you?"
    This is a straightforward question about my identity as an AI assistant.
    I should provide a clear, concise, and honest answer about being an AI
    language model trained by researchers from NVIDIA.


    Key points to cover:
    - I am an AI assistant
    - Trained by researchers from NVIDIA
    - I don\'t have a physical form, personal experiences, or consciousness
    - I can help with various tasks (answering questions, writing, coding, analysis, etc.)
    - I should avoid claiming to be human or having feelings/identity in the human sense
    I should be helpful, humble, and accurate. No need to overcomplicate it.
"""
,
"Tokenization details": #chat.usage
    {
        "total_tokens": 254, #chat.usage.total_tokens
        "prompt_tokens":20, #chat.usage.prompt_tokens
        "completion_tokens":214 #chat.usage.completion_tokens
    }
}