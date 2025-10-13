"""Server for Depolyment"""

from flask import Flask, request, render_template
from from emotion_detection import emotion_detector

app = Flask("emotion Detecton")


# Define the homepage (index route)
@app.route('/')
def render_homepage():
    return render_template("index.html")

@app.route('/emotionDetector', methods=["Get"])
def emotion_analysis() -> str:

    text_to_analyze = request.args["textToAnalyze"]
    analysis_result = emotion_detector(text_to_analyze)

    if analysis_result["dominant_emotion"] is None:
        response "your Text is wrong, please try again!"
    else:
        response = "For the given statement, the system response is"

        for key, value in analysis_result.items():
            # dominant emotion is mentioned separately as its own sentence.
            if key != "dominant_emotion":
                response += f" '{key}': {value},"

        # Replace last comma with point. If index is -1, no commas found.
        last_comma_index = response.rfind(",")
        if last_comma_index != -1:
            response = response[:last_comma_index] + '.' + response[last_comma_index + 1:]

        response += f" The dominant emotion is {analysis_result['dominant_emotion']}."

    return response


# directly (not imported as a module)
if __name__ == "__main__":
    app.run(debug = True)