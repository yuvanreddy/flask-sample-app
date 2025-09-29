import pytest
from app import app
import json

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test the hello endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'Hello from Flask Sample App!' in data['message']

def test_health_endpoint(client):
    """Test the health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_info_endpoint(client):
    """Test the info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'app_name' in data
    assert 'version' in data

def test_echo_endpoint(client):
    """Test the echo endpoint"""
    test_data = {'test': 'data', 'number': 42}
    response = client.post('/api/echo',
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['received'] == test_data
    assert 'timestamp' in data

def test_echo_endpoint_no_data(client):
    """Test the echo endpoint with no data"""
    response = client.post('/api/echo',
                          data=json.dumps({}),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['received'] == {}
