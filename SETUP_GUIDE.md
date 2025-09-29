# Setup Guide & Credentials for Flask Sample Application

## **Required Credentials & Setup Steps**

### **1. GitHub Repository Setup**

**Required Credentials:**
- GitHub Personal Access Token (for repository operations)
- Repository URL

**Steps:**
1. Create a new GitHub repository
2. Generate a Personal Access Token:
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Select scopes: `repo`, `workflow`, `packages`
   - Copy the token (you won't see it again!)

### **2. Docker Registry Setup**

**Required Credentials:**
- Docker Hub username and password/access token
- Registry URL: `docker.io`

**Steps:**
1. Create Docker Hub account at https://hub.docker.com
2. Generate Access Token:
   - Account Settings → Security → New Access Token
   - Copy the token

3. Update workflow file (`.github/workflows/ci-cd.yml`):
   ```yaml
   env:
     REGISTRY: docker.io
     IMAGE_NAME: your-dockerhub-username/flask-sample-app  # Change this!
   ```

### **3. Kubernetes Cluster Setup (Optional)**

**Required Credentials:**
- Kubeconfig file or cluster access credentials
- kubectl installed and configured

**Steps:**
1. Set up Kubernetes cluster (local: minikube/kind, cloud: GKE/AKS/EKS)
2. Install kubectl: https://kubernetes.io/docs/tasks/tools/
3. Configure cluster access:
   ```bash
   kubectl config current-context
   kubectl get nodes
   ```

### **4. Environment Variables & Secrets**

**GitHub Secrets to Configure:**
1. Go to your repository → Settings → Secrets and variables → Actions
2. Add these secrets:

```bash
DOCKER_USERNAME = your-dockerhub-username
DOCKER_PASSWORD = your-dockerhub-access-token
```

**Optional Secrets (for production):**
```bash
DATABASE_URL = postgresql://user:password@host:port/dbname
API_KEYS = your-api-keys
SLACK_WEBHOOK = https://hooks.slack.com/services/...
```

### **5. Helm Package Registry (Optional)**

**Required Credentials:**
- CloudSmith, JFrog, or GitHub Packages credentials

**Steps:**
1. Set up Helm registry (e.g., CloudSmith)
2. Configure in workflow:
   ```yaml
   - name: Publish Helm chart
     uses: stefanprodan/helm-gh-pages@v1.7.0
     with:
       token: ${{ secrets.GITHUB_TOKEN }}
   ```

## **Deployment Steps**

### **Phase 1: Local Development**

```bash
# 1. Clone and setup
git clone <your-repo-url>
cd flask-sample-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run locally
python app.py
# Visit: http://localhost:5000

# 5. Run tests
pytest
```

### **Phase 2: Docker Setup**

```bash
# 1. Build image
docker build -t your-username/flask-sample-app:latest .

# 2. Test locally
docker run -p 5000:5000 your-username/flask-sample-app:latest

# 3. Test with docker-compose
docker-compose up --build
```

### **Phase 3: GitHub Actions Setup**

1. **Update workflow file:**
   ```yaml
   # In .github/workflows/ci-cd.yml
   env:
     IMAGE_NAME: your-actual-dockerhub-username/flask-sample-app
   ```

2. **Configure secrets:**
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_PASSWORD`: Your Docker Hub access token

3. **Push to repository:**
   ```bash
   git add .
   git commit -m "Initial Flask application setup"
   git push origin main
   ```

4. **Monitor workflow:**
   - Go to Actions tab in GitHub
   - Watch the CI/CD pipeline run

### **Phase 4: Kubernetes Deployment (Optional)**

```bash
# 1. Update Helm chart
# Edit helm-chart/flask-app/values.yaml
image:
  repository: your-username/flask-sample-app
  tag: "latest"

# 2. Package and deploy
helm package helm-chart/flask-app/
helm install flask-app ./flask-app-0.1.0.tgz

# 3. Verify deployment
kubectl get pods
kubectl get services
kubectl port-forward svc/flask-app 8080:80
# Visit: http://localhost:8080
```

## **Security Best Practices**

### **1. Secret Management**
- Never commit secrets to code
- Use GitHub Secrets for sensitive data
- Rotate secrets regularly
- Use different credentials for different environments

### **2. Security Scanning**
```yaml
# Add to workflow for security scanning
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    scan-type: 'fs'
    scan-ref: '.'
    format: 'sarif'
    output: 'trivy-results.sarif'
```

### **3. Environment-specific Configuration**
```yaml
# Use environment-specific values
env:
  STAGING:
    IMAGE_TAG: develop
    REPLICAS: 2
  PRODUCTION:
    IMAGE_TAG: main
    REPLICAS: 5
```

## **Monitoring & Observability**

### **1. Health Checks**
- Application has `/health` endpoint
- Kubernetes readiness/liveness probes configured
- Docker health checks included

### **2. Logging**
```yaml
# Add to deployment for better logging
env:
  - name: LOG_LEVEL
    value: "INFO"
```

### **3. Metrics (Optional)**
```python
# Add to app.py for Prometheus metrics
from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)
```

## **Troubleshooting**

### **Common Issues**

1. **Docker build fails:**
   ```bash
   # Check Docker BuildKit
   export DOCKER_BUILDKIT=1
   docker build --no-cache .
   ```

2. **Kubernetes deployment fails:**
   ```bash
   kubectl describe pod <pod-name>
   kubectl logs <pod-name>
   ```

3. **GitHub Actions fails:**
   - Check workflow logs in Actions tab
   - Verify secrets are configured correctly
   - Ensure Docker Hub credentials are valid

### **Debug Commands**
```bash
# Test Docker image locally
docker run --rm -it your-username/flask-sample-app:latest python -c "import app; print('App imported successfully')"

# Test Kubernetes deployment
kubectl exec -it deployment/flask-app -- /bin/bash
curl http://localhost:5000/health

# Check GitHub Actions logs
# Go to Actions → workflow run → specific job
```

## **Cost Optimization**

### **1. Development Environment**
- Use local Docker for development
- Consider using `kind` for local Kubernetes testing
- Use GitHub Actions free tier (2000 min/month)

### **2. Production Environment**
- Use cloud container registry
- Implement auto-scaling based on CPU/memory
- Use spot instances for non-critical workloads

## **Next Steps**

1. **Set up monitoring** (Prometheus, Grafana)
2. **Add API documentation** (Swagger/OpenAPI)
3. **Implement database integration** (PostgreSQL, MongoDB)
4. **Add authentication/authorization** (JWT, OAuth)
5. **Set up backup and disaster recovery**
6. **Implement blue-green or canary deployments**

## **Support**

For issues:
1. Check the troubleshooting section
2. Review GitHub Actions logs
3. Check application and container logs
4. Validate all credentials are correctly configured

---

**🚀 Your Flask application is now ready with enterprise-grade CI/CD pipeline!**

The setup includes automated testing, containerization, multi-environment deployment, and monitoring - following the same patterns as the original complex workflow but simplified for a single Flask application.
