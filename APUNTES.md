```bash
 sudo apt update
 sudo apt upgrade python3
 python3 --version
 sudo apt install python3-pip
 sudo apt install python3-venv
 pip3 freeze
```

# Iniciar proyecto

## Instalar manejador de paquetes y entorno `uv`

```bash

pip3 install uv
uv pip install -r pyproject.toml   para instalar dependecias si se clona la rama en otro pc
uv --help
```

## Iniciar uv

```bash
uv init
uv add langchain
```

## Instalar langchain openai y/o google gemini

```bash
uv add langchain-openai
uv add python-dotenv black isort

uv add -U langchain-google-genai
```

# Definiciones en español de clases y funciones usadas en LangChain

## ReActSingleInputOutputParser(AgentOutputParser)
Clase que define un analizador de salida para agentes que utilizan el enfoque ReAct (Reasoning and Acting) con una sola entrada y salida. Este analizador interpreta la salida del agente y la convierte en un formato estructurado.

### Ejemplo:
```python
from langchain.agents import ReActSingleInputOutputParser

parser = ReActSingleInputOutputParser()

output = "Thought: I need to find the capital of France.\nAction: Search\nAction Input: What is the capital of France?\nObservation: The capital of France is Paris.\nThought: I now know the final answer.\nFinal Answer: The capital of France is Paris."
parsed_output = parser.parse(output)

print(parsed_output)

# Salida: {'thoughts': ['I need to find the capital of France.', 'I now know the final answer.'], 'actions': [{'action': 'Search', 'action_input': 'What is the capital of France?'}], 'final_answer': 'The capital of France is Paris.'}
```

