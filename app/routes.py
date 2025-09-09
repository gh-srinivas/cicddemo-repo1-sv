"""
Routes Module for Flask Web Application

This module defines all the routes and endpoints for the Flask application,
including the homepage, business logic endpoints, and API routes.

Author: Auto-generated for CICD Demo
Version: 1.0.0
"""

import json
import random
import datetime
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, current_app
from app.models import UserManager, DataAnalytics
from app.utils import validate_email, sanitize_input, format_currency


# Create blueprint for main routes
main_routes = Blueprint('main', __name__)

# Initialize business logic components
user_manager = UserManager()
analytics = DataAnalytics()


@main_routes.route('/')
def home():
    """
    Homepage route that displays the main landing page.
    
    This route renders the homepage with dynamic content including
    user statistics and featured content.
    
    Returns:
        str: Rendered HTML template for the homepage
        
    Examples:
        GET / -> Returns homepage with current statistics
    """
    try:
        # Get some dynamic data for the homepage
        stats = {
            'total_users': user_manager.get_user_count(),
            'active_sessions': random.randint(10, 50),
            'data_processed': analytics.get_total_processed(),
            'uptime_days': (datetime.datetime.now() - datetime.datetime(2024, 1, 1)).days
        }
        
        # Featured content
        features = [
            {
                'title': 'User Management',
                'description': 'Comprehensive user registration and management system',
                'icon': 'fas fa-users'
            },
            {
                'title': 'Data Analytics',
                'description': 'Real-time data processing and analytics dashboard',
                'icon': 'fas fa-chart-line'
            },
            {
                'title': 'API Integration',
                'description': 'RESTful API endpoints for seamless integration',
                'icon': 'fas fa-code'
            },
            {
                'title': 'Secure & Scalable',
                'description': 'Built with security best practices and scalability in mind',
                'icon': 'fas fa-shield-alt'
            }
        ]
        
        return render_template('index.html', stats=stats, features=features)
        
    except Exception as e:
        # Log error and show user-friendly message
        current_app.logger.error(f"Error in home route: {str(e)}")
        flash('An error occurred while loading the homepage. Please try again.', 'error')
        return render_template('error.html', error_message="Homepage temporarily unavailable")


@main_routes.route('/users')
def users():
    """
    Users page route that displays user management interface.
    
    This route renders the user management page with current user data
    and registration forms.
    
    Returns:
        str: Rendered HTML template for user management
        
    Examples:
        GET /users -> Returns user management interface
    """
    try:
        users_data = user_manager.get_all_users()
        return render_template('users.html', users=users_data)
        
    except Exception as e:
        current_app.logger.error(f"Error in users route: {str(e)}")
        flash('Unable to load user data. Please try again.', 'error')
        return redirect(url_for('main.home'))


@main_routes.route('/analytics')
def analytics_dashboard():
    """
    Analytics dashboard route that displays data analytics and insights.
    
    This route renders the analytics dashboard with charts, metrics,
    and data visualization components.
    
    Returns:
        str: Rendered HTML template for analytics dashboard
        
    Examples:
        GET /analytics -> Returns analytics dashboard with current metrics
    """
    try:
        # Generate sample analytics data
        analytics_data = analytics.get_dashboard_data()
        
        # Chart data for JavaScript consumption
        chart_data = {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'datasets': [{
                'label': 'User Growth',
                'data': [65, 59, 80, 81, 56, 55],
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }]
        }
        
        return render_template('analytics.html', 
                             analytics=analytics_data, 
                             chart_data=json.dumps(chart_data))
        
    except Exception as e:
        current_app.logger.error(f"Error in analytics route: {str(e)}")
        flash('Unable to load analytics data. Please try again.', 'error')
        return redirect(url_for('main.home'))


# API Endpoints

@main_routes.route('/api/users', methods=['GET', 'POST'])
def api_users():
    """
    REST API endpoint for user management operations.
    
    GET: Retrieves list of all users
    POST: Creates a new user account
    
    Returns:
        json: JSON response with user data or operation status
        
    Examples:
        GET /api/users -> Returns list of users
        POST /api/users -> Creates new user from JSON payload
    """
    try:
        if request.method == 'GET':
            # Return all users as JSON
            users = user_manager.get_all_users()
            return jsonify({
                'success': True,
                'data': users,
                'count': len(users)
            })
            
        elif request.method == 'POST':
            # Create new user from JSON payload
            try:
                data = request.get_json()
            except Exception:
                return jsonify({
                    'success': False,
                    'error': 'Invalid JSON data'
                }), 400
            
            if not data:
                return jsonify({
                    'success': False,
                    'error': 'No data provided'
                }), 400
            
            # Validate required fields
            required_fields = ['name', 'email']
            missing_fields = [field for field in required_fields if field not in data]
            
            if missing_fields:
                return jsonify({
                    'success': False,
                    'error': f'Missing required fields: {", ".join(missing_fields)}'
                }), 400
            
            # Validate email format
            if not validate_email(data['email']):
                return jsonify({
                    'success': False,
                    'error': 'Invalid email format'
                }), 400
            
            # Sanitize input data
            sanitized_data = {
                'name': sanitize_input(data['name']),
                'email': sanitize_input(data['email']),
                'company': sanitize_input(data.get('company', '')),
                'role': sanitize_input(data.get('role', 'user'))
            }
            
            # Create user
            user_id = user_manager.create_user(sanitized_data)
            
            return jsonify({
                'success': True,
                'message': 'User created successfully',
                'user_id': user_id
            }), 201
            
    except Exception as e:
        current_app.logger.error(f"Error in api_users route: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500


@main_routes.route('/api/analytics/summary')
def api_analytics_summary():
    """
    REST API endpoint for analytics summary data.
    
    Returns summary statistics and key metrics in JSON format
    for external consumption or AJAX requests.
    
    Returns:
        json: JSON response with analytics summary data
        
    Examples:
        GET /api/analytics/summary -> Returns current analytics metrics
    """
    try:
        summary = analytics.get_summary()
        return jsonify({
            'success': True,
            'data': summary,
            'timestamp': datetime.datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        current_app.logger.error(f"Error in api_analytics_summary route: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Unable to retrieve analytics data'
        }), 500


@main_routes.route('/api/health')
def api_health():
    """
    Health check API endpoint for monitoring and load balancers.
    
    This endpoint provides application health status and basic
    system information for monitoring tools.
    
    Returns:
        json: JSON response with health status and system info
        
    Examples:
        GET /api/health -> Returns application health status
    """
    try:
        health_data = {
            'status': 'healthy',
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'version': '1.0.0',
            'environment': 'production',
            'uptime': str(datetime.datetime.now() - datetime.datetime(2024, 1, 1)),
            'database_connected': user_manager.check_connection(),
            'analytics_service': analytics.check_health()
        }
        
        return jsonify(health_data)
        
    except Exception as e:
        current_app.logger.error(f"Error in health check: {str(e)}")
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.datetime.utcnow().isoformat()
        }), 500


# Error handlers

@main_routes.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 Not Found errors with custom error page.
    
    Args:
        error: The 404 error object
        
    Returns:
        tuple: Rendered error template and 404 status code
    """
    return render_template('errors/404.html'), 404


@main_routes.errorhandler(500)
def internal_error(error):
    """
    Handle 500 Internal Server errors with custom error page.
    
    Args:
        error: The 500 error object
        
    Returns:
        tuple: Rendered error template and 500 status code
    """
    current_app.logger.error(f"Internal server error: {str(error)}")
    return render_template('errors/500.html'), 500