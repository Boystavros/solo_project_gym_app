from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, dob, title, pronouns, notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.dob, member.title, member.pronouns, member.notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member



