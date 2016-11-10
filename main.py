# coding: utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

#Index
@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('Index.html')
  
#Index
@app.route('/success', methods=['GET', 'POST'])
def success():
  return render_template('Success.html')

@app.route('/bootstrap', methods=['GET', 'POST'])
def bootstrap():
  return render_template('Bootstrap.html')

@app.route('/carousel', methods=['GET', 'POST'])
def carousel():
  return render_template('carousel.html')

# Launch server
if __name__ == "__main__":
  app.run()


