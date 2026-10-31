from api_caller import client, handleAiError as hae
#Importamos al cliente ya con la API lista.

#El rol de un prompt especifica quien realiza el prompt.
#Un prompt puede tener 3 tipos de roles.
# system(sistema que le dice como se debe comportar a la IA)
# user(usuario que habla con el agente de IA)
# assistant(la memoria del agente de IA de la conversacion)

#Ejemplo de rol:
role="system" #Mensaje tipo sistema para decirle como comportarse a la maquina 

#Solo el rol de system puede definir la materia en que se especializa el sistema
matter="Software development" #Donde el modelo debe especializarse para su respuesta.
#En Prompt Enginering, una materia o area en la que se especializa la IA
# tambien puede ser llamada rol, por lo cual solo en este contexto el rol no es matter.

content=f"""You are an expert in {matter}, who was asked to answer questions of that matter.
You must answer shortly using less than a hundred words.
Use only spanish language to give your answers"""
#El contenido del mensaje es la pregunta, orden, o respuesta dirigida a la inteligencia artificial.


message={"role":role,"content":content}
#Un mensaje es un diccionario con los valores role y content

messages=[message]
#Una conversacion es una lista de mensajes

model="thinkingmachines/inkling:free"
#El modelo es el servicio al que se le pide que responda.
# todos los que tengan ":free" se pueden usar de forma gratuita.
#Tenga en cuenta sin embargo que cada modelo puede tener un limite de mensajes gratuitos.


#chat es donde se reciben las respuestas de un modelo.
try:
    chat= client.chat.completions.create(
        model=model,
        messages=[{
            "role":"system",
            "content":"hello"
        }]
    )
    print(chat)
    #El contexto de la IA
    #Esto es todo lo que la IA penso, asi como las regulaciones que tuvo.

    print(chat.choices)
    #chat choices son las opciones que la IA considero como respuestas

    print(chat.choices[0].message)
    #message es un mensaje prompt devuelta como si fueramos una IA,
    # con su role, content, y todo eso que le pones encima para codificacion.

    print(chat.choices[0].message.content)
    #Mensaje sencillo tal y como se les conoce
except Exception as e:
    hae(e)