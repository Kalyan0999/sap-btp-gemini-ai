from flask import Flask, jsonify, request, render_template # Added render_template
import os
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route('/')
def home():
    # This line tells the app to show your colorful index.html page
    return render_template('index.html') 

@app.route('/ask')
def ask():
    query = request.args.get('q', 'Tell me about Chicken Basket.')
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        # This makes the AI "act" as your business assistant
        prompt = f"You are the AI for Chicken Basket in Nandyal. Answer this: {query}"
        response = model.generate_content(prompt)
        return jsonify({'gemini_answer': response.text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
