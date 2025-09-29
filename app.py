from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    """Basic hello world endpoint"""
    return jsonify({
        'message': 'Hello from Flask Sample App!',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'timestamp': datetime.utcnow().isoformat(),
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/info', methods=['GET'])
def get_info():
    """Get application information"""
    return jsonify({
        'app_name': 'Flask Sample Application',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'build_time': os.getenv('BUILD_TIME', 'unknown'),
        'git_sha': os.getenv('GIT_SHA', 'unknown')
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo endpoint for testing"""
    data = request.get_json() or {}
    return jsonify({
        'received': data,
        'timestamp': datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('DEBUG', 'False').lower() == 'true')
