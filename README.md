# Creative Flask Web Application

[![CI/CD Pipeline](https://github.com/gh-srinivas/cicddemo-repo1-sv/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/gh-srinivas/cicddemo-repo1-sv/actions/workflows/ci-cd-pipeline.yml)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen)](https://github.com/gh-srinivas/cicddemo-repo1-sv/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/dkrsrinivas/creative-flask-app)](https://hub.docker.com/r/dkrsrinivas/creative-flask-app)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![Flask Version](https://img.shields.io/badge/flask-3.0.0-blue)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE.txt)

A modern, creative, and eye-catching web application built with Flask and Bootstrap. This application demonstrates best practices in web development, including responsive design, RESTful APIs, comprehensive testing, and CI/CD automation.

## ✨ Features

### 🎨 Modern UI/UX
- **Responsive Design**: Mobile-first responsive layout using Bootstrap 5
- **Interactive Elements**: Dynamic charts, animations, and smooth transitions
- **Accessibility**: WCAG 2.1 compliant with keyboard navigation and screen reader support
- **Dark Mode Support**: Automatic dark mode detection and manual toggle

### 🚀 Core Functionality
- **User Management**: Complete CRUD operations for user accounts
- **Analytics Dashboard**: Real-time data visualization with Chart.js
- **RESTful API**: Well-documented JSON APIs for all major operations
- **Health Monitoring**: Built-in health checks and system status monitoring

### 🔒 Security & Performance
- **Input Validation**: Comprehensive server-side and client-side validation
- **XSS Protection**: HTML sanitization and Content Security Policy
- **Error Handling**: Graceful error handling with custom error pages
- **Caching**: Intelligent caching strategies for optimal performance

### 🛠️ Development Features
- **Comprehensive Testing**: 85%+ test coverage with unit and integration tests
- **Code Quality**: Automated linting, formatting, and security scanning
- **Documentation**: Detailed docstrings and API documentation
- **Docker Support**: Multi-stage Docker builds with security scanning

## 🚀 Quick Start

Get the application running in less than 5 minutes:

```bash
# Clone the repository
git clone https://github.com/gh-srinivas/cicddemo-repo1-sv.git
cd cicddemo-repo1-sv

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py

# Open your browser and navigate to
# http://localhost:5000
```

## 📦 Installation

### Prerequisites

- **Python 3.9+** (Python 3.11 recommended)
- **pip** (Python package manager)
- **Git** (for version control)
- **Docker** (optional, for containerized deployment)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/gh-srinivas/cicddemo-repo1-sv.git
   cd cicddemo-repo1-sv
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   # Using the run script (recommended)
   python run.py
   
   # Or using Flask directly
   python -m flask run
   
   # Or using Gunicorn (production)
   gunicorn --bind 0.0.0.0:5000 app:app
   ```

5. **Access the Application**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Enjoy exploring the features!

## ⚙️ Configuration

The application supports multiple configuration environments:

### Environment Modes

| Environment | Description | Use Case |
|-------------|-------------|----------|
| `development` | Debug enabled, detailed logging | Local development |
| `testing` | Test-specific settings | Automated testing |
| `production` | Optimized for production | Live deployment |

### Command Line Options

```bash
python run.py --help

Usage: run.py [-h] [--environment {development,production,testing}] 
              [--production] [--testing] [--host HOST] [--port PORT] 
              [--debug] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] 
              [--version]

Examples:
  python run.py                     # Development mode
  python run.py --production        # Production mode
  python run.py --host 127.0.0.1    # Bind to specific host
  python run.py --port 8080         # Use different port
  python run.py --debug             # Enable debug mode
```

## 📚 API Documentation

The application provides a comprehensive RESTful API:

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T14:30:00Z",
  "version": "1.0.0",
  "environment": "production",
  "uptime": "30 days, 0:00:00",
  "database_connected": true,
  "analytics_service": true
}
```

#### User Management

##### Get All Users
```http
GET /api/users
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid-string",
      "name": "John Doe",
      "email": "john.doe@example.com",
      "company": "TechCorp Inc.",
      "role": "admin",
      "status": "active",
      "created_at": "2024-01-15T14:30:00Z"
    }
  ],
  "count": 1
}
```

##### Create New User
```http
POST /api/users
Content-Type: application/json

{
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "company": "DataSoft LLC",
  "role": "analyst"
}
```

#### Analytics

##### Get Analytics Summary
```http
GET /api/analytics/summary
```

## 🧪 Testing

The application includes comprehensive testing with high code coverage.

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage report
python -m pytest --cov=app --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_routes.py

# Generate HTML coverage report
python -m pytest --cov=app --cov-report=html
```

### Coverage Requirements

- **Minimum Coverage**: 85%
- **Branch Coverage**: Enabled
- **Missing Lines**: Reported in detail
- **Coverage Enforcement**: Automated in CI/CD

## 🐳 Docker Deployment

The application supports Docker deployment with multi-stage builds and security scanning.

### Quick Docker Start

```bash
# Pull the latest image
docker pull dkrsrinivas/creative-flask-app:latest

# Run the container
docker run -d -p 5000:5000 --name flask-app dkrsrinivas/creative-flask-app:latest

# Access the application
open http://localhost:5000
```

### Building from Source

```bash
# Build the Docker image
docker build -t creative-flask-app .

# Run with custom configuration
docker run -d \
  -p 5000:5000 \
  -e FLASK_ENV=production \
  -e SECRET_KEY=your-production-secret \
  --name flask-app \
  creative-flask-app
```

## 🔄 CI/CD Pipeline

The application includes a comprehensive CI/CD pipeline with GitHub Actions.

### Pipeline Stages

1. **Code Quality Analysis**
   - Code formatting (Black)
   - Import sorting (isort)
   - Linting (flake8)
   - Security analysis (Bandit)
   - Dependency scanning (Safety)

2. **Comprehensive Testing**
   - Unit tests with pytest
   - Coverage analysis (85% minimum)
   - Multi-Python version testing (3.9, 3.10, 3.11)

3. **SonarCloud Integration**
   - Quality gate analysis
   - Code coverage tracking
   - Security vulnerability detection
   - Technical debt monitoring

4. **Docker Build & Push**
   - Multi-platform builds
   - Security scanning with Trivy
   - Automated tagging
   - Docker Hub publishing (dkrsrinivas/creative-flask-app)

5. **Email Notifications**
   - Automatic alerts to vvsrinivasbabu@yahoo.com if coverage < 85%
   - SMTP integration for pipeline notifications

### Environment Variables Required

Set these secrets in your GitHub repository:

```bash
SONAR_TOKEN                  # SonarCloud authentication
DOCKER_HUB_USERNAME         # Docker Hub username: dkrsrinivas
DOCKER_HUB_TOKEN           # Docker Hub access token: dckr_pat_oYM-x4-win43brA4iJBLAhj0jk4
SMTP_USERNAME              # SMTP username for notifications
SMTP_PASSWORD              # SMTP password for notifications
```

## 💻 Development Guide

### Development Setup

```bash
# Clone and setup
git clone https://github.com/gh-srinivas/cicddemo-repo1-sv.git
cd cicddemo-repo1-sv

# Setup development environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Install development tools
pip install black isort flake8 pytest-cov mypy pre-commit

# Setup pre-commit hooks
pre-commit install
```

### Project Structure

```
cicddemo-repo1-sv/
├── app/                     # Application source code
│   ├── __init__.py         # Application factory
│   ├── config.py           # Configuration classes
│   ├── routes.py           # Route definitions
│   ├── models.py           # Business logic models
│   ├── utils.py            # Utility functions
│   ├── static/             # Static files (CSS, JS, images)
│   │   ├── css/           # Custom stylesheets
│   │   ├── js/            # JavaScript files
│   │   └── images/        # Image assets
│   └── templates/          # Jinja2 templates
│       ├── base.html      # Base template
│       ├── index.html     # Homepage
│       ├── users.html     # User management
│       ├── analytics.html # Analytics dashboard
│       └── errors/        # Error pages
├── tests/                  # Test suite
│   ├── conftest.py         # Test configuration
│   ├── test_routes.py      # Route tests
│   └── test_models.py      # Model tests
├── .github/                # GitHub configuration
│   └── workflows/          # CI/CD workflows
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
└── README.md              # This file
```

## 🔧 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port 5000
   lsof -i :5000
   
   # Kill the process or use different port
   python run.py --port 8080
   ```

2. **Module Import Errors**
   ```bash
   # Ensure you're in the correct directory
   cd cicddemo-repo1-sv
   
   # Activate virtual environment
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

3. **Docker Build Issues**
   ```bash
   # Clear Docker cache
   docker builder prune
   
   # Rebuild without cache
   docker build --no-cache -t creative-flask-app .
   ```

### Debug Mode

Enable debug mode for detailed error information:

```bash
# Method 1: Command line
python run.py --debug

# Method 2: Environment variable
export FLASK_DEBUG=True
python run.py
```

## 🤝 Contributing

We welcome contributions from the community! Please follow these guidelines:

### Contribution Process

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Make Changes**: Follow code style and add tests
4. **Test Changes**: Ensure all tests pass with good coverage
5. **Commit Changes**: Use conventional commit messages
6. **Push to Branch**: `git push origin feature/amazing-feature`
7. **Create Pull Request**: Provide detailed description

### Commit Message Convention

```bash
feat: add new user registration feature
fix: resolve email validation bug
docs: update API documentation
test: add tests for user management
chore: update dependencies
```

## 📊 Application Architecture

### Technology Stack

- **Backend**: Python 3.11 + Flask 3.0.0
- **Frontend**: Bootstrap 5.3.2 + Chart.js + Font Awesome
- **Testing**: pytest + pytest-cov + pytest-flask
- **Containerization**: Docker multi-stage builds
- **CI/CD**: GitHub Actions + SonarCloud + Docker Hub
- **Code Quality**: Black, isort, flake8, Bandit, Safety

### Key Components

- **User Management System**: Complete CRUD operations with validation
- **Analytics Dashboard**: Real-time metrics and data visualization  
- **RESTful API**: JSON-based endpoints for all operations
- **Health Monitoring**: Application and system health checks
- **Security**: Input sanitization, XSS protection, CSRF protection

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/gh-srinivas/cicddemo-repo1-sv/issues)
- **Email**: vvsrinivasbabu@yahoo.com
- **Docker Hub**: [dkrsrinivas/creative-flask-app](https://hub.docker.com/r/dkrsrinivas/creative-flask-app)

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE.txt](LICENSE.txt) file for details.

---

<div align="center">
  <p>Made with ❤️ for the developer community</p>
  <p><strong>A comprehensive Flask web application with modern CI/CD pipeline</strong></p>
</div>