"""Admin command helpers (placeholders) for bot_masterslot333.

Commands to implement in a full bot:
- /setinterval <min>
- /mute on|off
- /postnow
- /status
"""
def is_admin(user_id, admin_list):
    return user_id in admin_list
