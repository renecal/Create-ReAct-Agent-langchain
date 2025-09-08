# ReAct Agents with Langchain

ReAct Agents combine reasoning and acting capabilities to solve complex tasks by interacting with external tools and environments. Using Langchain, you can easily build, customize, and deploy ReAct Agents for various applications in natural language processing and automation.

## Steps

QUERY -> AGENT -> LLM CALL -> THROUGH STEPS ->  PARSE -> TOOL -> TOOL EXECUTION -> OUTPUT -> OK -> ANSWER 

### 1. LLM Call
In this step, the agent makes a call to a Large Language Model (LLM) to generate a response based on the input query. The LLM processes the input and produces an output that may include reasoning, suggestions for actions, or requests for additional information.

### 2. Parsing
After receiving the response from the LLM, this step involves parsing the output to identify any tools that need to be used. The parser extracts relevant information, such as tool names and parameters, which will guide the subsequent tool execution phase.

### 3. Tool Execution
In this step, the agent executes the identified tools based on the parsed information. This may involve calling APIs, querying databases, or performing other actions as specified by the LLM's output. The results from these tool executions are then collected for further processing.

### 4. Okey
Once the tools have been executed and their results obtained, this step involves evaluating the outputs to determine if they are satisfactory or if further actions are needed. The agent may decide to make additional LLM calls or proceed to formulate a final answer based on the gathered information.

## Useful Links
- [Langchain ReAct Documentation](https://python.langchain.com/docs/how_to/migrate_agent/)
- [Langchain Agents Overview](https://python.langchain.com/docs/how_to/#agents)
- [Langchain API Reference render](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.render.render_text_description.html)
- [Tools](https://python.langchain.com/docs/concepts/tools/)
- [Tools Kits](https://python.langchain.com/docs/integrations/tools/)
- [Langchain hub hwchase17](https://smith.langchain.com/hub/hwchase17/react?organizationId=5c031c7d-225f-41cf-9def-21161772e1fa)
- [ReActSingleInputOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.output_parsers.react_single_input.ReActSingleInputOutputParser.html)
- [LCEL](https://python.langchain.com/docs/concepts/lcel/)
