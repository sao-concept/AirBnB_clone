class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

if __name__ == "__main__":
    from datetime import datetime

    # Example usage
    base_model = BaseModel(id="1", created_at=datetime.now(), updated_at=datetime.now())
    base_model.save()
    print(base_model.to_dict())
