# coding: utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

#Index
@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('Index.html')

# Launch server
if __name__ == "__main__":
  app.run()


