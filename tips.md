* [ ] Git in Plain English: Cascade Glossary for Solo Developers that bypasses the staging area.

1. COMMITTING CHANGES (skip staging area)

- "Commit all my changed files with message 'Describe changes here'"
- "Save all edits with message 'Update XYZ'"
- "Commit all tracked files and add message 'Fixed bugs'"

2. ADDING NEW FILES

- "Add new file [filename] to Git"
- "Track this new file [filename]"

3. CHECKING FILE STATUS

- "Show me files I modified"
- "List changed files"
- "Show Git status"

4. DISCARDING CHANGES

- "Discard changes in [filename]"
- "Revert file [filename] to last committed state"

5. PUSHING CHANGES TO REMOTE (like GitHub)

- "Push my latest changes to GitHub"
- "Upload my commits to remote repository"

6. VIEWING HISTORY

- "Show recent commit history"
- "List my last few commits"
- These plain English commands assume Cascade interprets them as Git operations.
- You may need to confirm or review before action is taken.

---

Result of copy/paste from Windsurf to Coda

When you copy and paste Markdown (.md) files into Coda, several things happen depending on how you paste and what the content contains:

**What Gets Converted:**

- **Headers** (# ## ###) become Coda's native heading styles
- **Bold** (**text**) and *italic* (*text*) formatting is preserved
- **Links** [text](url) become clickable links
- **Lists** (bulleted and numbered) convert to Coda's list format
- **Basic tables** often convert to Coda's table blocks

**What Doesn't Convert Well:**

- **Code blocks** (```code```) typically paste as plain text and lose syntax highlighting
- **Inline code** (`code`) may lose its monospace formatting
- **Complex tables** with advanced markdown formatting may not render properly
- **Images** referenced by markdown links won't automatically import
- **Custom HTML** within the markdown gets stripped out
- **Mathematical expressions** or LaTeX won't render

**Best Practices:**

1. **Paste in smaller chunks** - Large files can have inconsistent conversion
2. **Use "Paste and Match Style"** (Cmd/Ctrl+Shift+V) for cleaner results
3. **Manual cleanup** - You'll likely need to reformat code blocks and fix any broken elements
4. **Consider Coda's native blocks** - Convert markdown tables to actual Coda tables, code blocks to Coda's code blocks, etc.

**Alternative Approach:**

Instead of direct copy-paste, you might want to use Coda's import feature or manually recreate structured content using Coda's native blocks for better formatting control and functionality.

The conversion works reasonably well for basic markdown, but expect to do some manual cleanup for more complex documents.

---

* [ ] Windsurf automatically saves changes to files.

## Useful Extensions

- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) - For testing API endpoints
- [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) - For running tests
- [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools) - For database management
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - For code formatting

## Deployment Tips

- Set `FLASK_ENV=production` in production
- Use a production WSGI server like Gunicorn or uWSGI
- Configure proper logging
- Set up monitoring and alerts
- Regular database backups

---

To see actual database use https://sqlitebrowser.org/dl/

Open the database file located at
c:\Users\samst\CascadeProjects\MoneyPal\instance\moneypal.db
*Last updated: 2025-07-08*
