

from flask import Flask , jsonify
 
app = Flask(__name__)
 
 
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Api is running fine '

@app.route('/op/<string:n>')
# ‘/’ URL is bound with hello_world() function.
def hello_world2(n):
    result =  {
        "number":int(n),
        "Name":"Om Prakash",
        "Date":"12/09/2024"
    }
    return jsonify(result)
 
# main driver function
if __name__ == '__main__':
    app.run(debug=True)