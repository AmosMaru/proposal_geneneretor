from flask import Flask, request, jsonify
from openai import OpenAI
import os
import datetime
app = Flask(__name__)

# Set up OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
current_date = datetime.datetime.now().strftime("%Y-%m-%d") 
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    project_background = data.get('project_background')
    project_name = data.get('project_name')
    timeline = data.get('project_timeline')
    budget = data.get('project_budget')
    objectives = data.get('objectives')
    goals = data.get('goals')

    if not project_background or not project_name  or not timeline or not budget or not objectives or not goals:
        return jsonify({"error": "All fields are required"}), 400

    prompt = (
        f"Create a detailed project proposal based on the following details:\n\n"
        f"Project Background: {project_background}\n"
        f"Project Name: {project_name}\n"
        f"Timeline: {timeline} days\n"
        f"Budget: ${budget}\n\n"
        f"Objectives: {objectives}\n"
        f"Goals: {goals}\n\n"
        f"Please write a comprehensive project proposal."
        f"The proposal is prepared by PYRUSGROUP on date {current_date}.\n\n"
        f"Pyrus is the "
    )

    try:
        completion =  client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                  "content": "You are an advanced and professional proposal generator. Make sure you use few words and make it concise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            # max_tokens=1500,
            top_p=1,
        )
        assistant_response = completion.choices[0].message.content

        return jsonify({"response": assistant_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5553)
