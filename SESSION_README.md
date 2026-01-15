# Session Restore Instructions

This workspace snapshot was saved so you can pause work and return later.

- Snapshot file: `.moneypal_session.json`
- Saved at: `2026-01-10T00:00:00Z`

Quick restore steps
- Open the workspace in VS Code (if not already open).
- Open the file `app.py` (Explorer → click `app.py`).
- Jump to the saved line: use `Ctrl+G` and enter `3` to go to line 3.

To open the file in two editor panes (if you want the same file in two tabs):
- Right-click the `app.py` tab and choose `Split Right` (or `Split Down`), then re-open the file in one of the panes if it closed.
- Or from the Explorer: right-click `app.py` → `Open to the Side`, then click `app.py` again to open it in the other pane.

Command-line helpers (PowerShell)
- Open file at line 3 in the current window: `code -g "app.py:3"`
- Open a new window focused on that file: `code -n -g "app.py:3"`

Notes
- The snapshot is lightweight: it records which file and the selected line range only.
- If you want a fuller session snapshot (open tabs, unsaved changes, breakpoints), say so and I can create a `vscode` workspace file or recommend an extension.

If you'd like, I can also commit these two files to a branch or create a timestamped backup of `app.py` contents — tell me which you prefer.

## Charts UI Note (2026-01-15)

- The Charts page now includes a custom horizontal double-thumb slider with mini-controls and a lock feature for controlling the visible date range. Thumbs support keyboard navigation and show live `mm/dd/yyyy` tooltips while dragging.
