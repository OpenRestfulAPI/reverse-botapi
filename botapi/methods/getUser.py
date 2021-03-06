from botapi import app, sessions

@app.get('/getUser')
@app.post('/getUser')
async def get_user(token: str, user_id: int):
    client = await sessions(token)
    u = await client.get_users(user_id)
    try:
        return {
            "id": u.id,
            "is_self": u.is_self,
            "is_contact": u.is_contact,
            "is_mutual_contact": u.is_mutual_contact,
            "is_deleted": u.is_deleted,
            "is_bot": u.is_bot,
            "is_verified": u.is_verified,
            "is_restricted": u.is_restricted,
            "is_scam": u.is_scam,
            "is_support": u.is_support,
            "first_name": u.first_name,
            "last_name": u.last_name or None,
            "status": u.status,
            "username": u.username or None,
            "language_code": u.language_code,
            "dc_id": u.dc_id or None,
            "photo": {"small_file_id": u.photo.small_file_id or None,
                        "big_file_id": u.photo.big_file_id or None,
            },
        }
    except AttributeError:
        return {
            "id": u.id,
            "is_self": u.is_self,
            "is_contact": u.is_contact,
            "is_mutual_contact": u.is_mutual_contact,
            "is_deleted": u.is_deleted,
            "is_bot": u.is_bot,
            "is_verified": u.is_verified,
            "is_restricted": u.is_restricted,
            "is_scam": u.is_scam,
            "is_support": u.is_support,
            "first_name": u.first_name,
            "last_name": u.last_name or None,
            "status": u.status,
            "username": u.username or None,
            "language_code": u.language_code,
            "dc_id": u.dc_id or None
        }