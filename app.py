from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "This is to verify that the CI/CD pipeline is established"


if __name__=="__main__":
    app.run(debug=True)



    