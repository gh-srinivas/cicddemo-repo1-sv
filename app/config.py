"""
Configuration Module for Flask Web Application

This module contains configuration classes for different environments
(development, testing, production) and application settings.

Author: Auto-generated for CICD Demo
Version: 1.0.0
"""

import os
from datetime import timedelta


class Config:
    """
    Base configuration class containing default settings for the Flask application.
    
    This class defines common configuration options that can be inherited
    by environment-specific configuration classes.
    """
    
    # Application settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    TESTING = False
    
    # Server settings
    HOST = os.environ.get('FLASK_HOST') or '0.0.0.0'
    PORT = int(os.environ.get('FLASK_PORT') or 5000)
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Application metadata
    APP_NAME = os.environ.get('APP_NAME') or 'Creative Flask Web App'
    APP_VERSION = '1.0.0'
    APP_DESCRIPTION = 'A creative and eye-catching Flask web application with Bootstrap styling'
    
    # Feature flags
    FEATURE_USER_REGISTRATION = True
    FEATURE_DATA_ANALYTICS = True
    FEATURE_API_ENDPOINTS = True


class DevelopmentConfig(Config):
    """
    Development environment configuration.
    
    This configuration is used during local development and includes
    debug settings and relaxed security constraints.
    """
    
    DEBUG = True
    SESSION_COOKIE_SECURE = False  # Allow HTTP in development
    
    # Development-specific settings
    LOG_LEVEL = 'DEBUG'
    DEVELOPMENT_MODE = True


class TestingConfig(Config):
    """
    Testing environment configuration.
    
    This configuration is used during automated testing and includes
    settings optimized for test execution.
    """
    
    TESTING = True
    DEBUG = True
    SESSION_COOKIE_SECURE = False  # Allow HTTP in testing
    WTF_CSRF_ENABLED = False  # Disable CSRF for easier testing
    
    # Testing-specific settings
    LOG_LEVEL = 'INFO'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    """
    Production environment configuration.
    
    This configuration is used in production environments and includes
    security-hardened settings and performance optimizations.
    """
    
    DEBUG = False
    TESTING = False
    
    # Production-specific settings
    LOG_LEVEL = 'WARNING'
    SESSION_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = 'https'


# Configuration mapping for easy access
config_map = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def get_config(config_name=None):
    """
    Get configuration class based on environment name.
    
    Args:
        config_name (str, optional): Name of the configuration environment.
                                   If None, uses FLASK_ENV environment variable.
                                   Defaults to 'development' if not found.
    
    Returns:
        class: Configuration class for the specified environment
        
    Examples:
        >>> config = get_config('production')
        >>> app.config.from_object(config)
    """
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    return config_map.get(config_name, DevelopmentConfig)