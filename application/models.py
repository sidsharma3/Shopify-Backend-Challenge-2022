from . import db
from sqlalchemy.sql import func
# These are the database models as we can see the relationship
# between Inventory and InventoryItems is One to Many
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    inventoryId = db.Column(db.Integer, db.ForeignKey('inventory.id'))

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    allInventoryItems = db.relationship('InventoryItem')