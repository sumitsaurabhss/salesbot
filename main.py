from graph import build_graph
from rich import print
import matplotlib.pyplot as plt

if __name__ == '__main__':
    graph = build_graph()
    while True:
        question = input("Please enter your question: ")
        thread = {"configurable": {"thread_id": "1"}}

        # Invoke the graph to get SQL query and visualization code
        # results = []
        # for s in graph.stream({
        #     'question': question,
        # }, thread):
        #     print(s)
        #     results.append(s)
        result = graph.invoke({"question": question}, thread)
        print(result)
        print(result['sql_query'])
        print(result['visual'])
        exec(result['visual'])

        # Continue
        more = input("Do you want to continue(y/n)?")
        if(more.lower() == 'n'):
            break