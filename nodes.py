from langgraph.prebuilt import create_react_agent
from typing import TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from tools import clean_query, clean_code, get_context, tools
from prompts import process_query_prompt, sql_prompt, visualization_prompt
from model import model

class MultiAgentState(TypedDict):
    question: str
    context: str
    sql_query: str
    visual: str

def process_query_node(state: MultiAgentState) -> MultiAgentState:
    """contains an NLP agent to process user queries"""
    nlp_agent = create_react_agent(model, [get_context], state_modifier=process_query_prompt)
    message = [HumanMessage(content=state['question'])]
    result = nlp_agent.invoke({"messages": message})
    return {"context": result['messages'][-1].content}

def sql_node(state: MultiAgentState) -> MultiAgentState:
    """contains an SQL agent to process user queries"""
    sql_agent = create_react_agent(model, tools, state_modifier=sql_prompt)
    messages = [HumanMessage(content=state['context'])] + [AIMessage(content=state['context'])]
    result = sql_agent.invoke({"messages": messages})
    return {"sql_query": clean_query(result['messages'][-1].content)}

def visualization_node(state: MultiAgentState) -> MultiAgentState:
    """contains an Visualization agent to process user queries"""
    visualization_agent = create_react_agent(model, tools, state_modifier=visualization_prompt)
    messages = [HumanMessage(content=state['context'])]
    result = visualization_agent.invoke({"messages": messages})
    return {"visual": clean_code(result['messages'][-1].content)}
