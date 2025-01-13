from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for health topics
health_advice = {
    "nutrition": "A balanced diet includes fruits, vegetables, whole grains, lean proteins, and healthy fats.",
    "fitness": "Regular physical activity helps maintain cardiovascular health and reduce stress.",
    "mental_health": "Practicing mindfulness and seeking social support can improve mental well-being."
}

# Welcome message
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Health Advice API. Use /advice?topic=<topic_name> to get health tips."})

# Fetch advice by topic
@app.route('/advice', methods=['GET'])
def get_advice():
    topic = request.args.get('topic')
    if topic in health_advice:
        return jsonify({"topic": topic, "advice": health_advice[topic]})
    else:
        return jsonify({"error": "Topic not found."}), 404

# Add new health advice
@app.route('/advice', methods=['POST'])
def add_advice():
    data = request.json
    topic = data.get('topic')
    advice = data.get('advice')
    if not topic or not advice:
        return jsonify({"error": "Topic and advice are required."}), 400
    health_advice[topic] = advice
    return jsonify({"message": f"Advice for '{topic}' added successfully."})

# Update existing advice
@app.route('/advice', methods=['PUT'])
def update_advice():
    data = request.json
    topic = data.get('topic')
    advice = data.get('advice')
    if topic in health_advice:
        health_advice[topic] = advice
        return jsonify({"message": f"Advice for '{topic}' updated successfully."})
    else:
        return jsonify({"error": "Topic not found."}), 404

# Delete health advice
@app.route('/advice', methods=['DELETE'])
def delete_advice():
    topic = request.args.get('topic')
    if topic in health_advice:
        del health_advice[topic]
        return jsonify({"message": f"Advice for '{topic}' deleted successfully."})
    else:
        return jsonify({"error": "Topic not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
