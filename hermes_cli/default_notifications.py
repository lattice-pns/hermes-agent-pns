"""Default NOTIFICATIONS.md template seeded into HERMES_HOME on first run."""

DEFAULT_NOTIFICATIONS_MD = """\
# Notification policy

This file controls how the agent handles incoming Lattice notifications.
Edit it directly, or let the agent update it as it learns your preferences.

## Guidelines
- Analyse the notification and take any necessary actions using your tools. You may use other tools as needed—e.g. web search—to proactively retrieve or verify information when that helps you respond well.
- Default to keeping the user in the loop: after you handle something, send a short `lattice_notify_user` summary (what it was, what you did, outcome). The user is not watching this session, so they rely on that ping unless the notification is noise.
- Skip `lattice_notify_user` only for obvious spam or junk (promotional floods, duplicate alerts you already acknowledged, meaningless noise). When in doubt, notify once—briefly.
- Still use `lattice_notify_user` for anything that needs a reply, permission, or a decision; those are not optional.
"""
