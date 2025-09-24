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


