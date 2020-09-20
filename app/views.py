from flask import render_template, redirect, request, flash
import requests
from app import app
import json
import datetime

NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')


def fetch_posts():
    get_chain_address = f"{NODE_ADDRESS}/chain"
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["key"] = block["key"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route("/")
def index():
    fetch_posts()
    return render_template('index.html', node_address=NODE_ADDRESS, posts=posts, readable_time=timestamp_to_string)


@app.route("/submit", methods=['POST'])
def add_unconfirmed_transaction():
    message = request.form['tx-content']
    author = request.form['tx-author']
    obj = {
        'message': message,
        'author': author
    }
    url = f'{NODE_ADDRESS}/add_unconfirmed_transcations'
    requests.post(url, json=obj, headers={'Content-type': 'application/json'})
    return redirect('/')


@app.route("/mine", methods=['POST'])
def mine():
    url = f'{NODE_ADDRESS}/mine'
    requests.post(url)
    return redirect('/')
