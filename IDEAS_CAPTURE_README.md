# Ideas Capture System

A lightweight, sticky-note style idea capture system for Flask applications. Perfect for quickly capturing thoughts, code snippets, todos, and other ideas while programming.

## Features

- **Quick Capture**: Add ideas with type, category, and tags
- **Automatic Timestamps**: Creation and update times are automatically tracked
- **Rich Categorization**: Organize ideas by type (thought, code, todo, bug, feature)
- **Tagging System**: Add multiple tags for easy organization
- **Modern UI**: Clean, responsive design that works on all devices
- **CSV Export**: Export ideas as CSV for use in spreadsheet applications
- **Persistent Storage**: Ideas are saved locally and persist between sessions

## Quick Start

### 1. Copy Files

Copy these files to your Flask project:
- `ideas_capture.py` → Your project root
- `templates/ideas.html` → Your `templates/` folder

### 2. Import and Use

```python
from flask import Flask
from ideas_capture import add_idea_route

app = Flask(__name__)

# Add the ideas capture routes
add_idea_route(app)

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

- Click "Export All Ideas" to download a CSV file
- Perfect for importing into Excel, Google Sheets, or other spreadsheet tools
- Includes all metadata (timestamps, tags, categories)
- Filename format: `ideas_export_YYYYMMDD_HHMMSS.csv`

## Configuration

You can customize the system by modifying these variables in `ideas_capture.py`:

```python
# Change where ideas are stored
IDEAS_FILE = 'ideas.json'

# Change template folder location (in your Flask app)
app.template_folder = 'templates'
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

## CSV Export Format

The CSV export includes these columns:
- **ID**: Unique identifier
- **Content**: The idea text
- **Category**: Idea category
- **Type**: Idea type (thought, code, todo, etc.)
- **Tags**: Comma-separated tags
- **Created At**: ISO timestamp of creation
- **Updated At**: ISO timestamp of last update

## Requirements

- **Python**: 3.6 or higher
- **Flask**: Any recent version
- **Dependencies**: Only standard library modules (json, csv, os, datetime, io)

## API Endpoints

- `GET /ideas` - Display ideas page
- `POST /ideas/add` - Add new idea
- `PUT /ideas/<id>` - Update existing idea
- `DELETE /ideas/<id>` - Delete idea
- `GET /ideas/export` - Export ideas as CSV
- `POST /ideas/clear` - Clear all ideas (use with caution)

## Integration Tips

- **Standalone Use**: Can be used independently in any Flask project
- **Template Customization**: Modify `ideas.html` to match your app's design
- **Data Migration**: Ideas are stored in JSON format, easy to migrate or backup
- **Multi-Project**: Use different category names to organize ideas by project

## Troubleshooting

- **Ideas not saving**: Check file permissions for `ideas.json`
- **Export not working**: Ensure CSV module is available (Python 3.6+)
- **Template errors**: Verify `ideas.html` is in your templates folder
- **Import errors**: Make sure `ideas_capture.py` is in your Python path
