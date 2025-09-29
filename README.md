# Flask Sample Application

A sample Flask web application demonstrating CI/CD best practices with Docker, Kubernetes, and GitHub Actions.

## Features

- RESTful API endpoints
- Health check endpoint
- Environment-based configuration
- Comprehensive testing with pytest
- Docker containerization
- Kubernetes deployment with Helm
- GitHub Actions CI/CD pipeline

## Quick Start

### Prerequisites

- Python 3.11+
- Docker
- Kubernetes cluster (for deployment)
- Helm 3.x
- GitHub repository

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd flask-sample-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run locally**
   ```bash
   python app.py
   ```

5. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

The application will be available at `http://localhost:5000`

### Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_app.py::test_hello_endpoint -v
```

## API Endpoints

- `GET /` - Hello world endpoint
- `GET /health` - Health check
- `GET /api/info` - Application information
- `POST /api/echo` - Echo endpoint for testing

## Deployment

### Docker

1. **Build image**
   ```bash
   docker build -t your-username/flask-sample-app:latest .
   ```

2. **Run container**
   ```bash
   docker run -p 5000:5000 your-username/flask-sample-app:latest
   ```

### Kubernetes

1. **Install dependencies**
   ```bash
   helm dependency update helm-chart/flask-app/
   ```

2. **Deploy to cluster**
   ```bash
   helm install flask-app helm-chart/flask-app/ \
     --set image.repository=your-username/flask-sample-app \
     --set image.tag=latest
   ```

3. **Check deployment**
   ```bash
   kubectl get pods
   kubectl get services
   ```

## CI/CD Pipeline

The GitHub Actions workflow includes:

1. **Testing**: Runs pytest with coverage
2. **Docker Build**: Multi-platform image build and push
3. **Deployment**: Automated deployment to staging/production
4. **Notifications**: Status updates on completion

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Application port | `5000` |
| `DEBUG` | Debug mode | `False` |
| `ENVIRONMENT` | Environment name | `development` |
| `APP_VERSION` | Application version | `1.0.0` |
| `BUILD_TIME` | Build timestamp | - |
| `GIT_SHA` | Git commit SHA | - |

## Project Structure

```
flask-sample-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Local development setup
├── pytest.ini           # Test configuration
├── tests/               # Test files
│   ├── __init__.py
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions workflow
├── helm-chart/
│   └── flask-app/       # Helm chart for Kubernetes
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           └── _helpers.tpl
└── README.md
```

## Development

### Adding New Endpoints

1. Add route to `app.py`
2. Write corresponding test in `tests/`
3. Update this README if needed

### Configuration

The application supports configuration through:
- Environment variables
- Helm values
- Docker build args

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the PORT environment variable
2. **Import errors**: Ensure virtual environment is activated
3. **Docker build fails**: Check Dockerfile syntax and dependencies
4. **Kubernetes deployment fails**: Verify cluster access and resource quotas

### Logs

- **Application logs**: Check container logs with `kubectl logs <pod-name>`
- **Build logs**: View in GitHub Actions workflow runs
- **Test logs**: Run `pytest -v` for detailed output

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

MIT License - see LICENSE file for details
