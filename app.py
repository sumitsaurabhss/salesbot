from flask import Flask, request, render_template
from graph import build_graph
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
graph = build_graph()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def handle_query():
    question = request.form['question']
    thread = {"configurable": {"thread_id": "1"}}

    # Invoke the graph to get SQL query and visualization code
    result = graph.invoke({"question": question}, thread)
    sql_query = result['sql_query']
    visual_code = result['visual']

    # Execute the visual code (run the matplotlib code to generate image)
    exec(visual_code)
    #img = io.BytesIO()
    #plt.savefig(img, format='png')
    #img.seek(0)
    #plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('result.html', query=sql_query) #, plot_url=f"data:image/png;base64,{plot_url}")


if __name__ == '__main__':
    app.run(debug=True)
