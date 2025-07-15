import asyncio
from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, State
import gradio as gr

# 1️⃣ Set up your LLM
llm = OllamaLLM(model="mistral")

# 2️⃣ Define State
class AgentState(State):
    input: str
    output: str = ""

# 3️⃣ Define a simple node
async def agent_node(state: AgentState):
    prompt = f"Answer this: {state.input}"
    result = await llm.ainvoke(prompt)
    return AgentState(input=state.input, output=result)

# 4️⃣ Create the graph
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")

app = graph.compile()

# 5️⃣ Define a Gradio interface
def gradio_fn(user_input):
    result = asyncio.run(app.ainvoke({"input": user_input}))
    return result["output"]

demo = gr.Interface(
    fn=gradio_fn,
    inputs="text",
    outputs="text",
    title="LangGraph Ollama Gradio Agent",
    description="Ask me anything! Powered by LangGraph + Ollama + Gradio"
)

if __name__ == "__main__":
    demo.launch()
