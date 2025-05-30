"""
WSGI entry point for the application.
This file ensures eventlet monkey patching happens before any other imports.
"""

# Monkey patch before ANY other imports
import eventlet
eventlet.monkey_patch(
    os=True,
    socket=True,
    time=True,
    select=True,
    thread=True,
    all=False
)

# Configure eventlet
import eventlet.debug
eventlet.debug.hub_prevent_multiple_readers(False)
eventlet.debug.hub_exceptions(True)

# Import Flask app and create application instance
from app import create_app, socketio

# Create the application instance
app = create_app()

# The application is already wrapped by SocketIO in create_app()
application = app

if __name__ == '__main__':
    socketio.run(app) 