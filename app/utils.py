"""
Utility Functions Module for Flask Web Application

This module contains utility functions for input validation, data sanitization,
formatting, and other common operations used throughout the application.

Author: Auto-generated for CICD Demo
Version: 1.0.0
"""

import re
import html
import datetime
from typing import Any, Optional, Union, List
from decimal import Decimal, InvalidOperation


def validate_email(email: str) -> bool:
    """
    Validate email address format using regular expressions.
    
    This function checks if the provided email address follows the standard
    email format pattern and contains valid characters.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
        
    Examples:
        >>> validate_email('user@example.com')
        True
        >>> validate_email('invalid-email')
        False
        >>> validate_email('')
        False
    """
    if not isinstance(email, str) or not email:
        return False
    
    # More comprehensive email validation pattern
    email_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9._+-])*[a-zA-Z0-9]@[a-zA-Z0-9]([a-zA-Z0-9.-])*[a-zA-Z0-9]\.[a-zA-Z]{2,}$'
    
    try:
        # Check pattern match and length constraints
        if len(email) > 254:  # RFC 5321 limit
            return False
        
        # Check for consecutive dots in domain part
        if '@' in email:
            local, domain = email.rsplit('@', 1)
            if '..' in domain:
                return False
        
        # Check for consecutive dots in local part
        if '@' in email:
            local = email.split('@')[0]
            if '..' in local:
                return False
            
        return re.match(email_pattern, email.strip()) is not None
        
    except Exception:
        return False


def sanitize_input(input_data: Any) -> str:
    """
    Sanitize user input to prevent XSS and injection attacks.
    
    This function cleans user input by escaping HTML characters,
    removing potentially dangerous content, and normalizing the data.
    
    Args:
        input_data (Any): Input data to sanitize (will be converted to string)
        
    Returns:
        str: Sanitized and safe string
        
    Examples:
        >>> sanitize_input('<script>alert("xss")</script>')
        '&lt;script&gt;alert("xss")&lt;/script&gt;'
        >>> sanitize_input('Normal text')
        'Normal text'
        >>> sanitize_input(123)
        '123'
    """
    if input_data is None:
        return ''
    
    try:
        # Convert to string and strip whitespace
        text = str(input_data).strip()
        
        # HTML escape to prevent XSS
        sanitized = html.escape(text, quote=True)
        
        # Remove dangerous javascript and event handlers
        dangerous_patterns = [
            r'on\w+\s*=',  # event handlers like onclick, onerror
            r'javascript:',  # javascript protocol
            r'vbscript:',    # vbscript protocol
            r'data:text/html',  # data URLs with HTML
        ]
        
        for pattern in dangerous_patterns:
            sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE)
        
        # Remove null bytes
        sanitized = sanitized.replace('\x00', '')
        
        # Limit length to prevent DoS attacks
        max_length = 1000
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length] + '...'
        
        return sanitized
        
    except Exception:
        return ''


def format_currency(amount: Union[int, float, Decimal, str], currency: str = 'USD') -> str:
    """
    Format numeric amounts as currency strings.
    
    This function converts numeric values to properly formatted currency
    strings with appropriate symbols and decimal places.
    
    Args:
        amount (Union[int, float, Decimal, str]): Amount to format
        currency (str, optional): Currency code. Defaults to 'USD'.
        
    Returns:
        str: Formatted currency string
        
    Examples:
        >>> format_currency(1234.56)
        '$1,234.56'
        >>> format_currency(1000, 'EUR')
        '€1,000.00'
        >>> format_currency('invalid')
        '$0.00'
    """
    # Currency symbols mapping
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥',
        'CAD': 'C$',
        'AUD': 'A$'
    }
    
    try:
        # Convert to Decimal for precise calculations
        if isinstance(amount, str):
            decimal_amount = Decimal(amount)
        else:
            decimal_amount = Decimal(str(amount))
        
        # Format with thousands separators
        formatted_amount = f"{decimal_amount:,.2f}"
        
        # Add currency symbol
        symbol = currency_symbols.get(currency.upper(), '$')
        return f"{symbol}{formatted_amount}"
        
    except (InvalidOperation, ValueError, TypeError):
        # Return default format for invalid input
        symbol = currency_symbols.get(currency.upper(), '$')
        return f"{symbol}0.00"


def format_datetime(dt: datetime.datetime, format_type: str = 'default') -> str:
    """
    Format datetime objects into human-readable strings.
    
    This function provides multiple formatting options for datetime objects,
    making them suitable for different display contexts.
    
    Args:
        dt (datetime.datetime): Datetime object to format
        format_type (str, optional): Type of formatting to apply. 
                                   Options: 'default', 'short', 'long', 'iso'.
                                   Defaults to 'default'.
                                   
    Returns:
        str: Formatted datetime string
        
    Examples:
        >>> dt = datetime.datetime(2024, 1, 15, 14, 30, 0)
        >>> format_datetime(dt)
        'Jan 15, 2024 2:30 PM'
        >>> format_datetime(dt, 'short')
        '01/15/24'
        >>> format_datetime(dt, 'iso')
        '2024-01-15T14:30:00'
    """
    if not isinstance(dt, datetime.datetime):
        return 'Invalid date'
    
    try:
        format_patterns = {
            'default': '%b %d, %Y %I:%M %p',
            'short': '%m/%d/%y',
            'long': '%A, %B %d, %Y at %I:%M %p',
            'iso': '%Y-%m-%dT%H:%M:%S',
            'date_only': '%B %d, %Y',
            'time_only': '%I:%M %p'
        }
        
        pattern = format_patterns.get(format_type, format_patterns['default'])
        return dt.strftime(pattern)
        
    except Exception:
        return str(dt)


def calculate_percentage(value: Union[int, float], total: Union[int, float], decimal_places: int = 2) -> float:
    """
    Calculate percentage with proper handling of edge cases.
    
    This function safely calculates percentages while handling division by zero
    and other edge cases that might occur in percentage calculations.
    
    Args:
        value (Union[int, float]): The value to calculate percentage for
        total (Union[int, float]): The total value to calculate percentage against
        decimal_places (int, optional): Number of decimal places to round to. Defaults to 2.
        
    Returns:
        float: Calculated percentage, rounded to specified decimal places
        
    Examples:
        >>> calculate_percentage(25, 100)
        25.0
        >>> calculate_percentage(1, 3)
        33.33
        >>> calculate_percentage(10, 0)
        0.0
    """
    try:
        if total == 0:
            return 0.0
        
        percentage = (float(value) / float(total)) * 100
        return round(percentage, decimal_places)
        
    except (ValueError, TypeError, ZeroDivisionError):
        return 0.0


def truncate_text(text: str, max_length: int = 100, suffix: str = '...') -> str:
    """
    Truncate text to specified length with optional suffix.
    
    This function safely truncates text while preserving word boundaries
    when possible, and adds a suffix to indicate truncation.
    
    Args:
        text (str): Text to truncate
        max_length (int, optional): Maximum length of resulting text. Defaults to 100.
        suffix (str, optional): Suffix to add when truncating. Defaults to '...'.
        
    Returns:
        str: Truncated text with suffix if applicable
        
    Examples:
        >>> truncate_text('This is a very long sentence that needs truncating', 20)
        'This is a very long...'
        >>> truncate_text('Short text', 50)
        'Short text'
    """
    if not isinstance(text, str):
        text = str(text)
    
    if len(text) <= max_length:
        return text
    
    # Try to truncate at word boundary
    truncate_length = max_length - len(suffix)
    
    if truncate_length <= 0:
        return suffix[:max_length]
    
    # Find last space before truncate point
    last_space = text.rfind(' ', 0, truncate_length)
    
    if last_space > truncate_length // 2:  # Only use word boundary if it's not too early
        return text[:last_space] + suffix
    else:
        return text[:truncate_length] + suffix


def generate_slug(text: str, max_length: int = 50) -> str:
    """
    Generate URL-friendly slug from text.
    
    This function converts text into a URL-safe slug by removing special
    characters, converting to lowercase, and replacing spaces with hyphens.
    
    Args:
        text (str): Text to convert to slug
        max_length (int, optional): Maximum length of slug. Defaults to 50.
        
    Returns:
        str: URL-friendly slug
        
    Examples:
        >>> generate_slug('Hello World!')
        'hello-world'
        >>> generate_slug('Special Characters & Symbols!')
        'special-characters-symbols'
        >>> generate_slug('Multiple   Spaces')
        'multiple-spaces'
    """
    if not isinstance(text, str):
        text = str(text)
    
    # Convert to lowercase
    slug = text.lower()
    
    # Remove HTML tags
    slug = re.sub(r'<[^>]+>', '', slug)
    
    # Replace non-alphanumeric characters with spaces
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    
    # Replace multiple spaces/hyphens with single hyphen
    slug = re.sub(r'[\s-]+', '-', slug)
    
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    
    # Truncate to max length
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip('-')
    
    return slug or 'untitled'


def is_valid_url(url: str) -> bool:
    """
    Validate URL format and structure.
    
    This function checks if a given string is a valid URL format
    with proper protocol and domain structure.
    
    Args:
        url (str): URL string to validate
        
    Returns:
        bool: True if URL is valid, False otherwise
        
    Examples:
        >>> is_valid_url('https://example.com')
        True
        >>> is_valid_url('http://localhost:8080/path')
        True
        >>> is_valid_url('not-a-url')
        False
    """
    if not isinstance(url, str) or not url:
        return False
    
    # URL validation pattern
    url_pattern = r'^https?:\/\/(?:[-\w.])+(?:\:[0-9]+)?(?:\/(?:[\w\._~!$&\'()*+,;=:@]|%[0-9a-fA-F]{2})*)*(?:\?(?:[\w\._~!$&\'()*+,;=:@/?]|%[0-9a-fA-F]{2})*)?(?:\#(?:[\w\._~!$&\'()*+,;=:@/?]|%[0-9a-fA-F]{2})*)?$'
    
    try:
        return re.match(url_pattern, url.strip()) is not None
    except Exception:
        return False


def safe_int(value: Any, default: int = 0) -> int:
    """
    Safely convert value to integer with fallback default.
    
    This function attempts to convert any value to an integer,
    returning a default value if conversion fails.
    
    Args:
        value (Any): Value to convert to integer
        default (int, optional): Default value if conversion fails. Defaults to 0.
        
    Returns:
        int: Converted integer value or default
        
    Examples:
        >>> safe_int('123')
        123
        >>> safe_int('invalid')
        0
        >>> safe_int('invalid', -1)
        -1
        >>> safe_int(12.7)
        12
    """
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return default