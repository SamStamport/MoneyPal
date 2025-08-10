# Ideas Capture System

A lightweight, sticky-note style idea capture system for Flask applications. Perfect for quickly capturing thoughts, code snippets, todos, and other ideas while programming.

## Features

- **Quick Capture**: Add ideas with type, category, and tags
- **Automatic Timestamps**: Creation and update times are automatically tracked
- **Rich Categorization**: Organize ideas by type (thought, code, todo, bug, feature)
- **Tagging System**: Add multiple tags for easy organization
- **Modern UI**: Clean, responsive design that works on all devices
- **Export Functionality**: Export ideas as JSON for use in other tools (like Coda)
- **Persistent Storage**: Ideas are saved locally and persist between sessions

## Quick Start

### 1. Copy Files

Copy these files to your Flask project:
- `ideas_capture_standalone.py` → Your project root
- `templates/ideas.html` → Your `templates/` folder

### 2. Import and Use

```python
from flask import Flask
from ideas_capture_standalone import add_idea_routes

app = Flask(__name__)

# Add the ideas capture routes
add_idea_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Access the System

Visit `/ideas` in your browser to start capturing ideas!

## Usage

### Adding Ideas

1. Fill out the form with:
   - **Type**: Choose from thought, code, todo, bug, or feature
   - **Category**: Your project name or general category
   - **Tags**: Comma-separated tags for organization
   - **Content**: Your actual idea or thought

2. Click "Add Idea" to save

### Managing Ideas

- **Edit**: Click the pencil icon on any idea card
- **Delete**: Click the trash icon to remove ideas
- **View Timestamps**: See when ideas were created and last updated

### Exporting

- Click "Export All Ideas" to download a JSON file
- Perfect for importing into Coda, Notion, or other tools
- Includes all metadata (timestamps, tags, categories)

## Configuration

You can customize the system by modifying these variables in `ideas_capture_standalone.py`:

```python
# Change where ideas are stored
IDEAS_FILE = 'ideas.json'

# Change template folder location
TEMPLATE_FOLDER = 'templates'
```

## Data Structure

Each idea is stored with this structure:

```json
{
  "id": 1,
  "content": "Remember to implement user authentication",
  "category": "MoneyPal",
  "type": "todo",
  "tags": ["auth", "security", "frontend"],
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00"
}
```

## Requirements

- **Python**: 3.6 or higher
- **Flask**: Any recent version
- **Dependencies**: Only standard library modules (json, os, datetime)

## Standalone Testing

You can test the system independently:

```bash
python ideas_capture_standalone.py
```

This will start a minimal Flask server at `http://localhost:5000` with just the ideas capture functionality.

## Integration Examples

### With Existing Flask Apps

```python
# app.py
from flask import Flask
from ideas_capture_standalone import add_idea_routes

app = Flask(__name__)

# Your existing routes
@app.route('/')
def home():
    return "My App"

# Add ideas capture
add_idea_routes(app)
```

### With Blueprints

```python
# ideas_blueprint.py
from flask import Blueprint
from ideas_capture_standalone import add_idea_routes

ideas_bp = Blueprint('ideas', __name__)
add_idea_routes(ideas_bp)

# In your main app
app.register_blueprint(ideas_bp, url_prefix='/ideas')
```

## Customization

### Adding New Idea Types

Edit the HTML template to add new types:

```html
<option value="research">🔬 Research</option>
<option value="meeting">📅 Meeting</option>
```

### Styling

The system uses CSS Grid and modern CSS features. Modify the styles in `templates/ideas.html` to match your app's theme.

### Database Integration

To use a database instead of JSON files, modify the `load_ideas()` and `save_ideas()` functions in `ideas_capture_standalone.py`.

## Troubleshooting

### Ideas Not Saving
- Check file permissions for `ideas.json`
- Ensure the `templates/` folder is in the right location

### Template Errors
- Verify `ideas.html` is in your `templates/` folder
- Check Flask template configuration

### Import Errors
- Ensure `ideas_capture_standalone.py` is in your Python path
- Check that all required Flask imports are available

## License

This system is provided as-is for educational and development purposes. Feel free to modify and use in your projects.

## Contributing

Improvements and bug fixes are welcome! The system is designed to be simple and extensible.
