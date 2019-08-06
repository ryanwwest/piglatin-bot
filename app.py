import message_processor
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/groupme', methods=['POST'])
def webhook():
	print(request.get_json())
	message_processor.process(request.get_json())
	return "ok", 200

if __name__ == '__main__':
	app.run('0.0.0.0', port=80, debug=True)
