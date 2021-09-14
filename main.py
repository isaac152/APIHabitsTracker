from app import create_app

app=create_app()

@app.route('/hello')
def helloworld():
    return 'hello'



if __name__=='__main__':
    app.run(debug=True)