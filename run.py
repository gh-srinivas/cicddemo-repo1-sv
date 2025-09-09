#!/usr/bin/env python3
"""
Main Entry Point for Creative Flask Web Application

This script serves as the main entry point for running the Flask application.
It handles environment setup, configuration loading, and application startup.

Usage:
    python run.py                   # Run in development mode
    python run.py --production      # Run in production mode
    python run.py --testing         # Run in testing mode

Environment Variables:
    FLASK_ENV: Environment mode (development, production, testing)
    FLASK_HOST: Host to bind to (default: 0.0.0.0)
    FLASK_PORT: Port to bind to (default: 5000)
    FLASK_DEBUG: Enable debug mode (default: False)

Author: Auto-generated for CICD Demo
Version: 1.0.0
"""

import os
import sys
import argparse
import logging
from app import create_app
from app.config import get_config


def setup_logging(level='INFO'):
    """
    Configure logging for the application.
    
    Args:
        level (str): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def parse_arguments():
    """
    Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description='Run the Creative Flask Web Application',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py                     # Development mode
  python run.py --production        # Production mode
  python run.py --host 127.0.0.1    # Bind to specific host
  python run.py --port 8080         # Use different port
  python run.py --debug             # Enable debug mode
        """
    )
    
    parser.add_argument(
        '--environment', '-e',
        choices=['development', 'production', 'testing'],
        default=os.environ.get('FLASK_ENV', 'development'),
        help='Environment mode (default: %(default)s)'
    )
    
    parser.add_argument(
        '--production', '-p',
        action='store_const',
        const='production',
        dest='environment',
        help='Run in production mode'
    )
    
    parser.add_argument(
        '--testing', '-t',
        action='store_const',
        const='testing',
        dest='environment',
        help='Run in testing mode'
    )
    
    parser.add_argument(
        '--host',
        default=os.environ.get('FLASK_HOST', '0.0.0.0'),
        help='Host to bind to (default: %(default)s)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=int(os.environ.get('FLASK_PORT', 5000)),
        help='Port to bind to (default: %(default)s)'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        default=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true',
        help='Enable debug mode'
    )
    
    parser.add_argument(
        '--log-level', '-l',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO',
        help='Logging level (default: %(default)s)'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='Creative Flask Web App 1.0.0'
    )
    
    return parser.parse_args()


def validate_environment():
    """
    Validate the runtime environment and dependencies.
    
    Raises:
        SystemExit: If critical dependencies or configurations are missing
    """
    # Check Python version
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required", file=sys.stderr)
        sys.exit(1)
    
    # Check if required directories exist
    required_dirs = ['app', 'app/templates', 'app/static']
    for directory in required_dirs:
        if not os.path.exists(directory):
            print(f"Error: Required directory '{directory}' not found", file=sys.stderr)
            sys.exit(1)
    
    # Check if critical files exist
    critical_files = ['app/__init__.py', 'app/routes.py', 'app/models.py']
    for file_path in critical_files:
        if not os.path.exists(file_path):
            print(f"Error: Critical file '{file_path}' not found", file=sys.stderr)
            sys.exit(1)


def main():
    """
    Main function that sets up and runs the Flask application.
    
    This function handles command line arguments, environment validation,
    application configuration, and startup.
    """
    try:
        # Parse command line arguments
        args = parse_arguments()
        
        # Setup logging
        setup_logging(args.log_level)
        logger = logging.getLogger(__name__)
        
        logger.info(f"Starting Creative Flask Web App in {args.environment} mode")
        
        # Validate environment
        validate_environment()
        
        # Get configuration for the specified environment
        config_class = get_config(args.environment)
        
        # Create Flask application
        app = create_app(config_class)
        
        # Override debug setting if specified
        if args.debug:
            app.config['DEBUG'] = True
        
        # Log application configuration
        logger.info(f"Host: {args.host}")
        logger.info(f"Port: {args.port}")
        logger.info(f"Debug: {app.config['DEBUG']}")
        logger.info(f"Environment: {args.environment}")
        
        # Production deployment note
        if args.environment == 'production' and args.debug:
            logger.warning("Debug mode is enabled in production environment!")
        
        # Start the application
        if args.environment == 'production':
            logger.info("Production mode: Consider using a WSGI server like Gunicorn")
            logger.info("Example: gunicorn --bind 0.0.0.0:5000 --workers 4 app:app")
        
        # Run the Flask development server
        app.run(
            host=args.host,
            port=args.port,
            debug=app.config['DEBUG'],
            threaded=True,
            use_reloader=app.config['DEBUG']
        )
        
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Application failed to start: {str(e)}")
        if args.log_level == 'DEBUG':
            logger.exception("Full traceback:")
        sys.exit(1)


if __name__ == '__main__':
    main()