# Without DRY
class UserService:
    def register_user(self, email, password):
        # Email validation
        if not email or '@' not in email:
            raise ValueError("Invalid email")
        
        # Password validation
        if len(password) < 8 or not any(c.isupper() for c in password):
            raise ValueError("Invalid password")
        
        return {"email": email.lower()}
    
    def update_email(self, user_id, new_email):
        # Duplicated validation
        if not new_email or '@' not in new_email:
            raise ValueError("Invalid email")
        
        return {"user_id": user_id, "email": new_email.lower()}
    
    def reset_password(self, user_id, new_password):
        # Duplicated validation
        if len(new_password) < 8 or not any(c.isupper() for c in new_password):
            raise ValueError("Invalid password")
        
        return {"user_id": user_id, "updated": True}
    
# With DRY applied
class UserService:
    def validate_email(self, email):
        if not email or '@' not in email:
            raise ValueError("Invalid email")
        return email.lower()
    
    def validate_password(self, password):
        if len(password) < 8 or not any(c.isupper() for c in password):
            raise ValueError("Invalid password")
        return password
    
    def register_user(self, email, password):
        validated_email = self.validate_email(email)
        validated_password = self.validate_password(password)
        return {"email": validated_email}
    
    def update_email(self, user_id, new_email):
        return {"user_id": user_id, "email": self.validate_email(new_email)}
    
    def reset_password(self, user_id, new_password):
        self.validate_password(new_password)
        return {"user_id": user_id, "updated": True}