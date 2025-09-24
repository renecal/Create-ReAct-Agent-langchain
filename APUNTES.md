# Iniciar proyecto

## Actualizar e instalar dependencias básicas

```bash
sudo apt update
sudo apt upgrade python3
python3 --version
sudo apt install python3-pip
sudo apt install python3-venv
pip3 freeze
```

## Instalar manejador de paquetes y entorno `uv`

```bash
pip3 install uv
uv pip install -r pyproject.toml   # Para instalar dependencias si se clona la rama en otro PC
uv --help
```

## Iniciar uv y agregar dependencias

```bash
uv init
uv add langchain
```

## Instalar langchain, openai y/o google gemini

```bash
uv add langchain-openai
uv add python-dotenv black isort
uv add -U langchain-google-genai
```

## Argumentos de modelos

```text
// ChatGoogleGenerativeAI
model_kwargs={"stop": ["\nObservation"]}  

// ChatOpenAI
stop= ["\nObservation"]
```

# Definiciones en español de clases y funciones usadas en LangChain

## ReActSingleInputOutputParser (AgentOutputParser)

Clase que define un analizador de salida para agentes que utilizan el enfoque ReAct (Reasoning and Acting) con una sola entrada y salida. Este analizador interpreta la salida del agente y la convierte en un formato estructurado.

### Ejemplo:

```python
from langchain.agents import ReActSingleInputOutputParser

parser = ReActSingleInputOutputParser()

output = "Thought: I need to find the capital of France.\nAction: Search\nAction Input: What is the capital of France?\nObservation: The capital of France is Paris.\nThought: I now know the final answer.\nFinal Answer: The capital of France is Paris."
parsed_output = parser.parse(output)

print(parsed_output)

# Salida: {'thoughts': ['I need to find the capital of France.', 'I now know la respuesta final.'], 'actions': [{'action': 'Search', 'action_input': 'What is the capital of France?'}], 'final_answer': 'The capital of France is Paris.'}
```

## Agent Scratchpad
Clase que representa un bloc de notas para agentes, utilizado para registrar pensamientos, acciones y observaciones durante la ejecución del agente. Este bloc de notas ayuda a mantener un seguimiento del proceso de razonamiento del agente.

### Ejemplo:

```python
from langchain.agents import AgentScratchpad

scratchpad = AgentScratchpad()

scratchpad.add_thought("I need to find the capital of France.")
scratchpad.add_action("Search", "What is the capital of France?")
scratchpad.add_observation("The capital of France is Paris.")
scratchpad.add_thought("I now know the final answer.")

print(scratchpad)

# Salida: Thought: I need to find the capital of France.
# Action: Search
# Action Input: What is the capital of France?
# Observation: The capital of France is Paris.
# Thought: I now know the final answer.
``` 

## format_log_to_str
Función que formatea un registro de agente en una cadena de texto legible. Esta función toma un registro estructurado del agente y lo convierte en una representación de cadena que puede ser fácilmente entendida.

### Ejemplo:

```python
from langchain.agents import format_log_to_str 
log = {
    "thoughts": ["I need to find the capital of France.", "I now know the final answer."],
    "actions": [{"action": "Search", "action_input": "What is the capital of France?"}],
    "final_answer": "The capital of France is Paris."
}
formatted_log = format_log_to_str(log)
print(formatted_log)
# Salida: Thought: I need to find the capital of France.
# Action: Search
# Action Input: What is the capital of France?
# Thought: I now know the final answer.
# Final Answer: The capital of France is Paris.
```
## Callbacks (BaseCallbackHandler)
Clase base para manejar callbacks en LangChain. Permite definir métodos que se ejecutan en respuesta a ciertos eventos durante la ejecución de modelos, agentes o cadenas. Los callbacks son útiles para monitorear, registrar o modificar el comportamiento de los componentes de LangChain.

### Ejemplo:

```python
from langchain.callbacks.base import BaseCallbackHandler
class CustomCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print("LLM started with prompts:", prompts)

    def on_llm_end(self, response, **kwargs):
        print("LLM ended with response:", response)

    def on_tool_start(self, tool_name, input_text, **kwargs):
        print(f"Tool {tool_name} started with input:", input_text)

    def on_tool_end(self, output, **kwargs):
        print("Tool ended with output:", output)
    def on_chain_start(self, serialized, inputs, **kwargs):
        print("Chain started with inputs:", inputs) 
    def on_chain_end(self, outputs, **kwargs):
        print("Chain ended with outputs:", outputs)
    def on_text(self, text, **kwargs):
        print("Text output:", text)
    def on_agent_action(self, action, **kwargs):
        print("Agent action:", action)
    def on_agent_finish(self, finish, **kwargs):                
        print("Agent finished with:", finish)
```

## Entendiendo las iteraciones 
En LangChain, las iteraciones se utilizan para la ejecución de agentes que requieren múltiples pasos para llegar a una respuesta final. Esto se debe a que un agente es un modelo de lenguaje que razona sobre qué acciones tomar, y cada acción, como usar una herramienta o hacer una búsqueda, es un paso en un ciclo de "pensar, actuar, observar".

El resultado de la primera invocación (hasta antes de Observation) se obtiene porque representa el primer paso del agente: el pensamiento inicial y la acción que decide tomar. La estructura de un agente se puede ver como:

    Thought (Pensamiento): El agente analiza la entrada y determina el siguiente paso.

    Action (Acción): El agente selecciona una herramienta a usar (como una búsqueda en la web).

    Action Input (Entrada de la Acción): Proporciona la entrada para la herramienta seleccionada.

    Observation (Observación): Este es el resultado de la acción. Es lo que sucede después de que la herramienta se ha ejecutado.

Por lo tanto, en la primera invocación, obtienes el Thought, Action, y Action Input porque son la salida del modelo en un solo paso. La Observation es el resultado de la acción, que aún no ha ocurrido. El ciclo de iteración continúa, usando la Observation como entrada para el siguiente paso del agente hasta que se alcanza la respuesta final.

Proceso iterativo del agente:

    Paso 1:

        Entrada: ¿Cuál es el clima en París?

        Modelo de lenguaje: Thought: Necesito saber el clima, usaré la herramienta de búsqueda. Action: 'search', Action Input: 'clima en París'.

        Salida de la primera invocación: Thought, Action, Action Input.

    Paso 2:

        Se ejecuta la herramienta search con la entrada 'clima en París'.

        Se obtiene la Observation: 'El clima en París es 15°C y soleado'.

        El agente usa esta Observation como entrada para el siguiente paso.

    Paso 3 (iteración 2):

        Entrada: El clima en París es 15°C y soleado.

        Modelo de lenguaje: Thought: Ya tengo la información, puedo dar la respuesta. Final Answer: El clima en París es 15°C y soleado.

        Salida final: La respuesta completa.

Este ciclo Thought/Action -> Observation se repite hasta que el agente considera que tiene la información suficiente para generar la respuesta final. Es la base de los agentes de cadena de pensamiento (ReAct) en LangChain.

## Function Calling vs ReAct
Function Calling y ReAct son dos enfoques diferentes para interactuar con modelos de lenguaje en LangChain, cada uno con sus propias características y casos de uso.

### Function Calling
Function Calling se basa en la idea de que el modelo de lenguaje puede "llamar" a funciones específicas con entradas definidas. Este enfoque es útil cuando se necesita realizar tareas concretas y bien definidas, como buscar información en una base de datos o realizar cálculos. En este caso, el modelo actúa más como un orquestador que dirige el flujo de trabajo hacia funciones específicas.

### ReAct
Por otro lado, ReAct (Reasoning and Acting) se centra en el razonamiento del modelo sobre qué acciones tomar en función de la entrada del usuario y el contexto. Este enfoque es más flexible y permite al modelo adaptarse a situaciones cambiantes, utilizando un ciclo de pensamiento que incluye la observación de resultados intermedios y la adaptación de acciones futuras en consecuencia. ReAct es especialmente útil en escenarios donde se requiere un alto grado de interacción y adaptación, como en diálogos complejos o tareas de múltiples pasos.

En resumen, mientras que Function Calling es más adecuado para tareas específicas y bien definidas, ReAct ofrece una mayor flexibilidad y capacidad de adaptación en situaciones más complejas.

