#!/usr/bin/env python3
"""
MoneyPal Desktop - Native Windows Application
Embeds the Flask web app in a native Windows window
"""

import webview
import threading
import time
import sys
import os
from app import app

class MoneyPalDesktop:
    def __init__(self):
        self.flask_thread = None
        self.server_started = False
        
    def start_flask_server(self):
        """Start Flask server in background thread"""
        try:
            app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
        except Exception as e:
            print(f"Flask server error: {e}")
    
    def wait_for_server(self, timeout=10):
        """Wait for Flask server to start"""
        import requests
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                response = requests.get('http://127.0.0.1:5000', timeout=1)
                if response.status_code == 200:
                    self.server_started = True
                    return True
            except:
                time.sleep(0.1)
        return False
    
    def run(self):
        """Launch the desktop application"""
        print("Starting MoneyPal Desktop...")
        
        # Start Flask server in background
        self.flask_thread = threading.Thread(target=self.start_flask_server, daemon=True)
        self.flask_thread.start()
        
        # Wait for server to start
        if not self.wait_for_server():
            print("Failed to start Flask server")
            sys.exit(1)
        
        print("Server started successfully")
        
        # Create native window
        window = webview.create_window(
            title='MoneyPal - Personal Finance Tracker',
            url='http://127.0.0.1:5000',
            width=1200,
            height=800,
            min_size=(800, 600),
            resizable=True,
            shadow=True,
            on_top=False
        )
        
        # Start the native app with fallback backends
        try:
            webview.start(debug=False, gui='cef')
        except:
            try:
                webview.start(debug=False, gui='gtk')
            except:
                webview.start(debug=False)

if __name__ == '__main__':
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Launch desktop app
    desktop_app = MoneyPalDesktop()
    desktop_app.run()