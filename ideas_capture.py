# ideas_capture.py - Generic Quick Idea Capture System
from flask import render_template, request, jsonify, Response
import json
import csv
import os
from datetime import datetime
from io import StringIO


# File to store ideas (simple JSON storage)
IDEAS_FILE = 'ideas.json'


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


def add_idea_route(app):
    """Add idea capture routes to the Flask app"""
    
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
                'type': data.get('type', 'thought')  # thought, code, todo
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
        """Export all ideas in CSV format"""
        ideas = load_ideas()
        
        # Create CSV data
        csvfile = StringIO()
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow([
            'ID', 'Content', 'Category', 'Type', 'Tags',
            'Created At', 'Updated At'
        ])
        
        # Write data rows
        for idea in ideas:
            tags_str = (', '.join(idea.get('tags', []))
                        if idea.get('tags') else '')
            writer.writerow([
                idea['id'],
                idea['content'],
                idea['category'],
                idea['type'],
                tags_str,
                idea['created_at'],
                idea['updated_at']
            ])
        
        # Create response with CSV content
        output = csvfile.getvalue()
        csvfile.close()
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'ideas_export_{timestamp}.csv'
        
        return Response(
            output,
            mimetype='text/csv',
            headers={'Content-Disposition': f'attachment; filename={filename}'}
        )
    
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
