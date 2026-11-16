# CI/CD demo app (Flask)

Endpoints: `GET /`, `GET /health`, `GET /api/echo/<text>`

## Run tests locally
```
pip install -r requirements-dev.txt
pytest
```

## Build and run the container
```
docker build -t cicd-demo --build-arg APP_VERSION=local .
docker run --rm -p 5000:5000 cicd-demo
```
Then open http://localhost:5000/ and http://localhost:5000/health
