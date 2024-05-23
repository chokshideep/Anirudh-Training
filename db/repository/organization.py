from fastapi import HTTPException, status
from db.model.Organization import Organization
from db.repository.validation import password_validation, email_validation


def create_organization_logic(organization_data, db):
    if not email_validation(organization_data.mail_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Email ID/Invalid Password")
    if not password_validation(organization_data.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Email ID/Invalid Password")
    if db.query(Organization).filter(Organization.mail_id == organization_data.mail_id).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=" Organization with this mail Id already exists")
    try:
        new_organization = Organization(
            name=organization_data.name,
            mail_id=organization_data.mail_id
        )
        new_organization.set_password(organization_data.password)
        db.add(new_organization)
        db.flush()

    except Exception as e:
        db.rollback()
        print("Error", e)
    db.commit()
    response = {"uuid": new_organization.uuid,
                "detail": "Organization created successfully"}
    return response
