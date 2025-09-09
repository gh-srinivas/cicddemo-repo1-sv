"""
Test Configuration for Flask Web Application

This module contains test configuration and fixtures for pytest testing.
It provides setup and teardown functionality for the test suite.

Author: Auto-generated for CICD Demo
Version: 1.0.0
"""

import pytest
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.config import TestingConfig


@pytest.fixture
def app():
    """
    Create and configure a test application instance.
    
    This fixture creates a Flask application configured for testing,
    with all necessary settings and test data initialized.
    
    Yields:
        Flask: Configured Flask application for testing
    """
    test_app = create_app(TestingConfig)
    
    with test_app.app_context():
        yield test_app


@pytest.fixture
def client(app):
    """
    Create a test client for the Flask application.
    
    This fixture provides a test client that can be used to make
    HTTP requests to the application during testing.
    
    Args:
        app: Flask application fixture
        
    Yields:
        FlaskClient: Test client for making HTTP requests
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """
    Create a test CLI runner for the Flask application.
    
    This fixture provides a CLI runner that can be used to test
    command-line interface functionality.
    
    Args:
        app: Flask application fixture
        
    Yields:
        FlaskCliRunner: Test CLI runner
    """
    return app.test_cli_runner()


@pytest.fixture
def auth_headers():
    """
    Create authentication headers for API testing.
    
    This fixture provides common headers used for API authentication
    and content type specification.
    
    Returns:
        dict: Dictionary of HTTP headers for API requests
    """
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


@pytest.fixture
def sample_user_data():
    """
    Provide sample user data for testing.
    
    This fixture returns a dictionary containing valid user data
    that can be used in tests for user creation and validation.
    
    Returns:
        dict: Sample user data for testing
    """
    return {
        'name': 'Test User',
        'email': 'test@example.com',
        'company': 'Test Company',
        'role': 'user'
    }


@pytest.fixture
def invalid_user_data():
    """
    Provide invalid user data for testing validation.
    
    This fixture returns a dictionary containing invalid user data
    that can be used to test validation logic and error handling.
    
    Returns:
        dict: Invalid user data for testing
    """
    return {
        'name': '',
        'email': 'invalid-email',
        'company': 'Test Company',
        'role': 'invalid_role'
    }