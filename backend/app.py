import openai
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

# Endpoint to handle code analysis
@app.route('/api/analyse-code', methods=['POST'])
def analyse_code():
    # Extract the code from the request
    code_snippet = request.json.get('code')

    # Define the prompt to be sent to the LLM
    prompt = f"""
    You are an expert Python developer. Please examine the following code for:
    1) Syntax correctness
    2) Performance or memory improvements
    3) Adherence to best practices like PEP 8
    4) Potential security concerns
    Code snippet:
    {code_snippet}
    """

    try:
        # Send the prompt to OpenAI's GPT model
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )

        # Parse the LLM response and send back the feedback
        feedback = response.choices[0].text.strip()
        return jsonify({"feedback": feedback})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
