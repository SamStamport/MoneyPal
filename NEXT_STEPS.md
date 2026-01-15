# Next Steps After Break

When you come back, here's a short checklist to pick up where you left off.

- Open the workspace and jump to `app.py` line 3:
  - GUI: Explorer → `app.py` → `Ctrl+G` → `3`
  - PowerShell: `code -g "c:\Users\samst\VSCodeprojects\MoneyPal\app.py:3"`

- If you want the same file in two panes:
  - Right-click the `app.py` tab → `Split Right` (or `Open to the Side` from Explorer).

- Quick housekeeping to resume work safely:
  1. Commit the snapshot files if you want them stored in Git:
     - `git add .moneypal_session.json .moneypal_snapshot_2026-01-10.json SESSION_README.md NEXT_STEPS.md`
     - `git commit -m "Session snapshot: 2026-01-10"`
  2. Activate virtualenv: `& .\.venv\Scripts\Activate.ps1`
  3. Run the app locally (dev mode): `python app.py`

- Useful checks before editing code:
  - Ensure `db_preference.txt` contains the mode you want (LIVE or SAMPLE).
  - If working on forecasting, consider installing `prophet` and `pandas` in the venv.

- Quick chart testing note: open `/charts` and verify the custom double-thumb slider, mini-controls, keyboard navigation, and the Lock button. Dates display as `mm/dd/yyyy` and selections persist across reloads.

If you want, I can:
- Create a `.code-workspace` that reopens `app.py` automatically in split view.
- Commit the snapshot files to a branch named `session-snapshot/2026-01-10`.

Tell me which of those you'd like and I'll do it now.
