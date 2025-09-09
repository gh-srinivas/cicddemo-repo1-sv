"""
Flask Web Application Entry Point

This module serves as the main entry point for the creative Flask web application.
It includes configuration, initialization, and the main application factory.

Author: Auto-generated for CICD Demo
Version: 1.0.0
"""

import os
import logging
from flask import Flask
from app.routes import main_routes
from app.config import Config


def create_app(config_class=Config):
    """
    Application factory function that creates and configures a Flask application instance.
    
    Args:
        config_class (class, optional): Configuration class to use for the application.
                                      Defaults to Config.
    
    Returns:
        Flask: Configured Flask application instance
        
    Raises:
        Exception: If application initialization fails
    """
    try:
        # Create Flask application instance
        app = Flask(__name__)
        
        # Load configuration
        app.config.from_object(config_class)
        
        # Configure logging
        if not app.debug and not app.testing:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = logging.FileHandler('logs/webapp.log')
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            )
            file_handler.setFormatter(formatter)
            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('Web application startup')
        
        # Register blueprints
        app.register_blueprint(main_routes)
        
        return app
        
    except Exception as e:
        logging.error(f"Failed to create Flask application: {str(e)}")
        raise


# Create application instance
app = create_app()


if __name__ == '__main__':
    """
    Main execution block for running the Flask application directly.
    This is primarily used for local development.
    """
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode
    )