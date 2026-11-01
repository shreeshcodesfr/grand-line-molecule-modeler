from flask import Flask, render_template, jsonify
import os
app = Flask(__name__)
@app.get("/")
def home():
    return render_template("index.html")
@app.get("/health")
def health():
    return jsonify(status="ok", app="Grand Line Molecular Modeler")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
