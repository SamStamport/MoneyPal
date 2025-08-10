#!/usr/bin/env python3
"""
Generic Ideas Capture System for Flask Applications

This is a standalone module that can be copied into any Flask project to add
a quick idea capture system. It provides sticky-note style functionality for
capturing thoughts, code snippets, todos, and other ideas.

Features:
- Add, edit, delete ideas
- Automatic creation and update timestamps
- Categorization and tagging
- Export to JSON for external tools
- Clean, modern UI
- Responsive design

Usage:
1. Copy this file to your Flask project
2. Copy the templates/ideas.html file to your templates folder
3. Import and use: from ideas_capture_standalone import add_idea_routes
4. Call: add_idea_routes(app)

Requirements:
- Flask
- Python 3.6+
"""

from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime


# Configuration - customize these for your project
IDEAS_FILE = 'ideas.json'  # Change this to store ideas elsewhere
TEMPLATE_FOLDER = 'templates'  # Change if your templates are elsewhere


def load_ideas():
    """Load existing ideas from JSON file"""
    if os.path.exists(IDEAS_FILE):
        try:
            with open(IDEAS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_ideas(ideas):
    """Save ideas to JSON file"""
    with open(IDEAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(ideas, f, indent=2, ensure_ascii=False)


def add_idea_routes(app):
    """
    Add idea capture routes to the Flask app
    
    Args:
        app: Flask application instance
    """
    
    @app.route('/ideas', methods=['GET'])
    def ideas_page():
        """Main ideas capture page"""
        ideas = load_ideas()
        return render_template('ideas.html', ideas=ideas)
    
    @app.route('/ideas/add', methods=['POST'])
    def add_idea():
        """Add a new idea"""
        try:
            data = request.get_json()
            content = data.get('content', '').strip()
            category = data.get('category', 'general')
            
            if not content:
                return jsonify({'error': 'Content cannot be empty'}), 400
            
            ideas = load_ideas()
            current_time = datetime.now().isoformat()
            new_idea = {
                'id': len(ideas) + 1,
                'content': content,
                'category': category,
                'created_at': current_time,
                'updated_at': current_time,
                'tags': data.get('tags', []),
                'type': data.get('type', 'thought')
            }
            
            ideas.append(new_idea)
            save_ideas(ideas)
            
            return jsonify(new_idea), 201
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @app.route('/ideas/<int:idea_id>', methods=['PUT'])
    def update_idea(idea_id):
        """Update an existing idea"""
        try:
            data = request.get_json()
            ideas = load_ideas()
            
            for idea in ideas:
                if idea['id'] == idea_id:
                    if 'content' in data:
                        idea['content'] = data['content']
                    if 'category' in data:
                        idea['category'] = data['category']
                    if 'tags' in data:
                        idea['tags'] = data['tags']
                    if 'type' in data:
                        idea['type'] = data['type']
                    
                    # Always update the updated_at timestamp
                    idea['updated_at'] = datetime.now().isoformat()
                    
                    save_ideas(ideas)
                    return jsonify(idea), 200
            
            return jsonify({'error': 'Idea not found'}), 404
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @app.route('/ideas/<int:idea_id>', methods=['DELETE'])
    def delete_idea(idea_id):
        """Delete an idea"""
        try:
            ideas = load_ideas()
            ideas = [idea for idea in ideas if idea['id'] != idea_id]
            
            # Reassign IDs to maintain continuity
            for i, idea in enumerate(ideas, 1):
                idea['id'] = i
            
            save_ideas(ideas)
            return jsonify({'success': True}), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @app.route('/ideas/export', methods=['GET'])
    def export_ideas():
        """Export all ideas for external import"""
        ideas = load_ideas()
        return jsonify({
            'export_date': datetime.now().isoformat(),
            'total_ideas': len(ideas),
            'ideas': ideas
        })
    
    @app.route('/ideas/clear', methods=['POST'])
    def clear_ideas():
        """Clear all ideas (use with caution!)"""
        try:
            save_ideas([])
            return jsonify({
                'success': True, 
                'message': 'All ideas cleared'
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400


# Example usage for standalone testing
if __name__ == '__main__':
    app = Flask(__name__)
    add_idea_routes(app)
    
    @app.route('/')
    def home():
        return '''
        <h1>Ideas Capture System</h1>
        <p><a href="/ideas">Go to Ideas Capture</a></p>
        '''
    
    print("Starting Ideas Capture System...")
    print("Visit http://localhost:5000/ideas to use the system")
    app.run(debug=True, port=5000)
