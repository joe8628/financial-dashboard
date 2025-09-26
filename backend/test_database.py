from app.core.database import SessionLocal
from app.models import User, Category, BankAccount, Transaction, TransactionType
from datetime import date
from decimal import Decimal

def test_database():
    db = SessionLocal()
    try:
        # Create a test user
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashedpassword"
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        
        # Create default categories
        categories = [
            Category(name="Food & Dining", color="#FF6B6B"),
            Category(name="Transportation", color="#4ECDC4"),
            Category(name="Shopping", color="#45B7D1"),
            Category(name="Income", color="#96CEB4"),
        ]
        
        for category in categories:
            db.add(category)
        db.commit()
        
        print("✅ Database test successful!")
        print(f"Created user: {user.email}")
        print(f"Created {len(categories)} categories")
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    test_database()