from sqlalchemy import select, func, or_, extract
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Contact, User
from typing import List

from datetime import date, timedelta

#from sqlalchemy.orm import Session
from src.schemas.contacts import ContactModel



async def get_contacts(limit: int, offset: int, db: AsyncSession, user: User) -> List[Contact]:
    stmt = select(Contact).filter_by(user=user).offset(offset).limit(limit)
    contacts =  await db.execute(stmt)
    return contacts.scalars().all()
   


async def get_contact(contact_id: int, db: AsyncSession, user: User) -> Contact:
    stmt = select(Contact).filter_by(user_id=user.id).filter_by(id=contact_id)
    contact =  await db.execute(stmt)
    return contact.scalar_one_or_none()


async def get_contact_firstname(limit: int, offset: int, firstname: str ,lastname: str,email: str  ,  db: AsyncSession, user: User):
    stmt = select(Contact).filter_by(user=user).where(or_(Contact.firstname == firstname,Contact.lastname == lastname,Contact.email == email)).offset(offset).limit(limit)
    contacts =  await db.execute(stmt)
    return contacts.scalars().all()  

async def get_contact_birthday(skip: int, limit: int,  db: AsyncSession, user: User):
    date_now = date.today()
    year_now = date_now.year
    diff = date_now + timedelta(days = 7)
    date_to = date(year=year_now, month=diff.month, day=diff.day)
    stmt = select(Contact).filter_by(user=user).\
        filter((extract('month', Contact.databirthday) >= date_now.month)).\
        filter((extract('month', Contact.databirthday) <= date_to.month)).\
        filter(extract('day', Contact.databirthday) >= date_now.day).\
        filter(extract('day', Contact.databirthday) <= date_to.day).\
        offset(skip).limit(limit)
    result =  await db.execute(stmt)
    return result.scalars().all()  

async def create_contact(body: ContactModel, db: AsyncSession, user: User):
    contact = Contact(**body.model_dump(exclude_unset=True), user=user )
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: AsyncSession, user: User) -> Contact :
    stmt = select(Contact).filter_by(user_id=user.id).filter_by(id=contact_id)
    result = await db.execute(stmt)
    contact = result.scalar_one_or_none()
    if contact:
        contact.firstname = body.firstname
        contact.lastname = body.lastname
        contact.email = body.email
        contact.mobilenamber = body.mobilenamber
        contact.databirthday = body.databirthday
        contact.note = body.note
        await db.commit()
        await db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: AsyncSession, user: User)  -> Contact :
    stmt = select(Contact).filter_by(user=user).filter_by(id=contact_id)
    contact = await db.execute(stmt)
    contact = contact.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact

