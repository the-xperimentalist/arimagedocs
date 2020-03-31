
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/temp_detect', methods=['POST'])
def temp_detect():
    pass

if __name__ == '__main__':
    app.run(debug=True)
