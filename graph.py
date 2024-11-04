from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from nodes import process_query_node, sql_node, visualization_node, MultiAgentState

memory = MemorySaver()

def build_graph():
    builder = StateGraph(MultiAgentState)
    builder.add_node("process_query", process_query_node)
    builder.add_node("sql", sql_node)
    builder.add_node("visualization", visualization_node)

    builder.set_entry_point("process_query")
    builder.add_edge("process_query", "sql")
    builder.add_edge("sql", "visualization")
    builder.add_edge("visualization", END)

    return builder.compile(checkpointer=memory)
