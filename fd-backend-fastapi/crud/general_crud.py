from sqlalchemy.orm import Session
from db.db import get_db
from sqlalchemy.orm import Session

def add_item(item) -> bool:
    db = get_db()
    session: Session = next(db)
    try:
        
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    except Exception as e:
        print(e)
        session.rollback()
        return e
    

def get_item(model, where_args: list):
    db = get_db()
    session: Session = next(db)
    try:
        q = session.query(
            model
        ).where(
            where_args[0]
        )
        res = q.first()
        return res
    except Exception as e:
        print(e)
        return e