# datascienceproject

## Project tracking for interview prep

This repository includes a lightweight tracking setup so every meaningful change can be logged and reviewed later.

### Manual change log
Run this from the project root whenever you make a notable update:

```bash
python track_changes.py "Describe the change here"
```

This records:
- timestamp
- short change note
- current branch
- git status
- recent commit history

The log and report are stored under the hidden local folder [.project_tracking](.project_tracking), so they do not get pushed to GitHub.

### Auto-tracking monitor
To keep watching the project for file creation, edits, or deletions automatically, run:

```bash
python auto_track_changes.py
```

This monitor polls the project folder and logs detected changes into [.project_tracking/CHANGELOG.md](.project_tracking/CHANGELOG.md) without requiring you to remember to run the manual command each time.

### Generate the final interview report
When the project is complete, run:

```bash
python generate_interview_report.py
```

This creates a summary in [.project_tracking/INTERVIEW_REPORT.md](.project_tracking/INTERVIEW_REPORT.md) based on the tracked change history and git log.

### Local-only tracking files
- [.project_tracking](.project_tracking)
- [track_changes.py](track_changes.py)
- [auto_track_changes.py](auto_track_changes.py)
- [generate_interview_report.py](generate_interview_report.py)

This gives you a clean story of the work you did, which is very useful for revision and interview discussions.
