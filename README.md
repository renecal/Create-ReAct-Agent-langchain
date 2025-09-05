# ReAct Agents with Langchain

ReAct Agents combine reasoning and acting capabilities to solve complex tasks by interacting with external tools and environments. Using Langchain, you can easily build, customize, and deploy ReAct Agents for various applications in natural language processing and automation.

## Useful Links
- [Langchain ReAct Documentation](https://python.langchain.com/docs/how_to/migrate_agent/)
- [Langchain Agents Overview](https://python.langchain.com/docs/how_to/#agents)
- [Langchain API Reference render](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.render.render_text_description.html)
- [Tools](https://python.langchain.com/docs/concepts/tools/)
- [Tools Kits](https://python.langchain.com/docs/integrations/tools/)
- [Langchain hub hwchase17](https://smith.langchain.com/hub/hwchase17/react?organizationId=5c031c7d-225f-41cf-9def-21161772e1fa)
- [ReActSingleInputOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.output_parsers.react_single_input.ReActSingleInputOutputParser.html)
- [LCEL](https://python.langchain.com/docs/concepts/lcel/)

## arguments Models

```text
    // ChatGoogleGenerativeAI
    model_kwargs={"stop": ["\nObservation"]}  

    // ChatOpenAI
    stop= ["\nObservation"]
```
