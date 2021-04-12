from flask import Flask
from flask import request, jsonify
from flask_cors import cross_origin
from flask_cors import CORS
from googlesearch import search


app = Flask(__name__)
CORS(app)


@app.route('/link', methods=['GET'])
def single_link():
    query = request.args.get('query')
    link = ""
    for j in search(query, num_results=1):
        link = j

    return jsonify({"link": link})


@app.route('/links', methods=['POST'])
@cross_origin()
def get_link():
    content = request.get_json(silent=True)

    links = get_links(content)

    my_dict = {"links": links}

    response = jsonify(my_dict)

    return response


def get_links(content):
    links = []

    for query in content:
        link = google_link(query)
        links.append(link)

    return links


def google_link(query):
    link = ""

    for j in search("топ 10" + query, num_results=0):
        link = j
        print(j)

    return link


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


