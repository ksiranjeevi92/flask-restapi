
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import ItemSchema,PlainItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel

blp = Blueprint("Items", __name__, description="Operations on items"
)

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema(many=False))
    def get(self, item_id):
        return ItemModel.query.get_or_404(item_id)

    @blp.arguments(PlainItemUpdateSchema)
    @blp.response(200, PlainItemUpdateSchema)
    def put(self,item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.name = item_data["name"]
            item.price = item_data["price"]
        else:
            item = ItemModel(id=item_id, **item_data)
        
        db.session.add(item)
        db.session.commit()
        return item


    def delete(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted!"}


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema(many=False))
    def post(self,item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Internal server error")
        return item,201
