/**
 * Main JavaScript file for Creative Flask Web App
 * 
 * This file contains common functionality used across all pages,
 * including navigation effects, API utilities, and UI enhancements.
 * 
 * @version 1.0.0
 * @author Auto-generated for CICD Demo
 */

(function() {
    'use strict';
    
    /**
     * Main application object containing all functionality
     */
    const App = {
        
        /**
         * Initialize the application
         */
        init() {
            this.setupNavigation();
            this.setupScrollEffects();
            this.setupTooltips();
            this.setupAPIHelpers();
            this.setupFormValidation();
            this.setupAccessibility();
            
            // Log initialization
            console.log('Creative Flask App initialized successfully');
        },
        
        /**
         * Setup navigation-related functionality
         */
        setupNavigation() {
            // Active navigation highlighting
            const currentPath = window.location.pathname;
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            
            navLinks.forEach(link => {
                if (link.getAttribute('href') === currentPath) {
                    link.classList.add('active');
                }
            });
            
            // Smooth scrolling for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        },
        
        /**
         * Setup scroll-based effects and animations
         */
        setupScrollEffects() {
            // Navbar transparency effect
            const navbar = document.querySelector('.navbar');
            if (navbar) {
                window.addEventListener('scroll', () => {
                    if (window.scrollY > 50) {
                        navbar.style.backgroundColor = 'rgba(13, 110, 253, 0.95)';
                        navbar.style.backdropFilter = 'blur(10px)';
                    } else {
                        navbar.style.backgroundColor = '';
                        navbar.style.backdropFilter = '';
                    }
                });
            }
            
            // Intersection Observer for animations
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate-slide-up');
                    }
                });
            }, observerOptions);
            
            // Observe cards and sections
            document.querySelectorAll('.card, .feature-card, .stat-card').forEach(el => {
                observer.observe(el);
            });
        },
        
        /**
         * Initialize Bootstrap tooltips and popovers
         */
        setupTooltips() {
            // Initialize tooltips
            const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
            tooltipTriggerList.map(function (tooltipTriggerEl) {
                return new bootstrap.Tooltip(tooltipTriggerEl);
            });
            
            // Initialize popovers
            const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
            popoverTriggerList.map(function (popoverTriggerEl) {
                return new bootstrap.Popover(popoverTriggerEl);
            });
        },
        
        /**
         * Setup API helper functions
         */
        setupAPIHelpers() {
            // Global API request function
            window.apiRequest = async function(url, options = {}) {
                const defaultOptions = {
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    }
                };
                
                const config = { ...defaultOptions, ...options };
                
                try {
                    const response = await fetch(url, config);
                    const data = await response.json();
                    
                    if (!response.ok) {
                        throw new Error(data.error || `HTTP error! status: ${response.status}`);
                    }
                    
                    return data;
                } catch (error) {
                    console.error('API Request Error:', error);
                    App.showNotification('error', `API Error: ${error.message}`);
                    throw error;
                }
            };
        },
        
        /**
         * Setup form validation enhancements
         */
        setupFormValidation() {
            // Custom validation for all forms
            const forms = document.querySelectorAll('form');
            
            forms.forEach(form => {
                form.addEventListener('submit', function(e) {
                    if (!form.checkValidity()) {
                        e.preventDefault();
                        e.stopPropagation();
                        
                        // Focus on first invalid field
                        const firstInvalid = form.querySelector(':invalid');
                        if (firstInvalid) {
                            firstInvalid.focus();
                        }
                    }
                    
                    form.classList.add('was-validated');
                });
                
                // Real-time validation feedback
                const inputs = form.querySelectorAll('input, textarea, select');
                inputs.forEach(input => {
                    input.addEventListener('blur', function() {
                        if (this.checkValidity()) {
                            this.classList.remove('is-invalid');
                            this.classList.add('is-valid');
                        } else {
                            this.classList.remove('is-valid');
                            this.classList.add('is-invalid');
                        }
                    });
                });
            });
        },
        
        /**
         * Setup accessibility enhancements
         */
        setupAccessibility() {
            // Keyboard navigation for dropdowns
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    // Close all open dropdowns
                    const openDropdowns = document.querySelectorAll('.dropdown-menu.show');
                    openDropdowns.forEach(dropdown => {
                        const toggle = dropdown.previousElementSibling;
                        if (toggle) {
                            bootstrap.Dropdown.getInstance(toggle).hide();
                        }
                    });
                    
                    // Close modals
                    const openModals = document.querySelectorAll('.modal.show');
                    openModals.forEach(modal => {
                        bootstrap.Modal.getInstance(modal).hide();
                    });
                }
            });
            
            // Skip to main content link
            const skipLink = document.createElement('a');
            skipLink.href = '#main-content';
            skipLink.textContent = 'Skip to main content';
            skipLink.className = 'skip-link sr-only sr-only-focusable';
            skipLink.style.cssText = `
                position: absolute;
                top: -40px;
                left: 6px;
                z-index: 1100;
                color: white;
                background: #007bff;
                padding: 8px;
                text-decoration: none;
                border-radius: 4px;
            `;
            
            skipLink.addEventListener('focus', function() {
                this.style.top = '6px';
            });
            
            skipLink.addEventListener('blur', function() {
                this.style.top = '-40px';
            });
            
            document.body.insertBefore(skipLink, document.body.firstChild);
            
            // Add main content ID if not present
            const mainContent = document.querySelector('main');
            if (mainContent && !mainContent.id) {
                mainContent.id = 'main-content';
            }
        },
        
        /**
         * Show notification/toast message
         * @param {string} type - 'success', 'error', 'warning', 'info'
         * @param {string} message - Message to display
         * @param {number} duration - Duration in ms (default: 5000)
         */
        showNotification(type, message, duration = 5000) {
            // Create toast container if it doesn't exist
            let toastContainer = document.getElementById('toast-container');
            if (!toastContainer) {
                toastContainer = document.createElement('div');
                toastContainer.id = 'toast-container';
                toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
                toastContainer.style.zIndex = '1080';
                document.body.appendChild(toastContainer);
            }
            
            // Create toast element
            const toast = document.createElement('div');
            toast.className = `toast align-items-center text-white bg-${type === 'error' ? 'danger' : type} border-0`;
            toast.setAttribute('role', 'alert');
            toast.setAttribute('aria-live', 'assertive');
            toast.setAttribute('aria-atomic', 'true');
            
            toast.innerHTML = `
                <div class="d-flex">
                    <div class="toast-body">
                        <i class="fas fa-${this.getIconForType(type)} me-2"></i>
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            `;
            
            toastContainer.appendChild(toast);
            
            // Initialize and show toast
            const bsToast = new bootstrap.Toast(toast, {
                autohide: true,
                delay: duration
            });
            
            bsToast.show();
            
            // Remove toast element after it's hidden
            toast.addEventListener('hidden.bs.toast', () => {
                toast.remove();
            });
        },
        
        /**
         * Get appropriate icon for notification type
         * @param {string} type - Notification type
         * @returns {string} Font Awesome icon class
         */
        getIconForType(type) {
            const icons = {
                'success': 'check-circle',
                'error': 'exclamation-triangle',
                'warning': 'exclamation-triangle',
                'info': 'info-circle'
            };
            return icons[type] || 'info-circle';
        },
        
        /**
         * Loading state management
         */
        loading: {
            show(element, text = 'Loading...') {
                if (typeof element === 'string') {
                    element = document.querySelector(element);
                }
                
                if (element) {
                    element.classList.add('loading');
                    const originalContent = element.innerHTML;
                    element.setAttribute('data-original-content', originalContent);
                    element.innerHTML = `
                        <div class="d-flex align-items-center justify-content-center">
                            <div class="spinner-border spinner-border-sm me-2" role="status">
                                <span class="visually-hidden">Loading...</span>
                            </div>
                            ${text}
                        </div>
                    `;
                }
            },
            
            hide(element) {
                if (typeof element === 'string') {
                    element = document.querySelector(element);
                }
                
                if (element) {
                    element.classList.remove('loading');
                    const originalContent = element.getAttribute('data-original-content');
                    if (originalContent) {
                        element.innerHTML = originalContent;
                        element.removeAttribute('data-original-content');
                    }
                }
            }
        },
        
        /**
         * Utility functions
         */
        utils: {
            /**
             * Debounce function calls
             * @param {Function} func - Function to debounce
             * @param {number} wait - Wait time in ms
             * @param {boolean} immediate - Execute immediately
             * @returns {Function} Debounced function
             */
            debounce(func, wait, immediate) {
                let timeout;
                return function executedFunction(...args) {
                    const later = () => {
                        timeout = null;
                        if (!immediate) func(...args);
                    };
                    const callNow = immediate && !timeout;
                    clearTimeout(timeout);
                    timeout = setTimeout(later, wait);
                    if (callNow) func(...args);
                };
            },
            
            /**
             * Format numbers with thousand separators
             * @param {number} num - Number to format
             * @returns {string} Formatted number
             */
            formatNumber(num) {
                return new Intl.NumberFormat().format(num);
            },
            
            /**
             * Validate email address
             * @param {string} email - Email to validate
             * @returns {boolean} Is valid email
             */
            validateEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            },
            
            /**
             * Copy text to clipboard
             * @param {string} text - Text to copy
             * @returns {Promise} Copy operation promise
             */
            async copyToClipboard(text) {
                try {
                    await navigator.clipboard.writeText(text);
                    App.showNotification('success', 'Copied to clipboard!');
                    return true;
                } catch (error) {
                    console.error('Copy failed:', error);
                    App.showNotification('error', 'Failed to copy to clipboard');
                    return false;
                }
            }
        }
    };
    
    // Initialize app when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => App.init());
    } else {
        App.init();
    }
    
    // Make App available globally for debugging
    window.App = App;
    
})();