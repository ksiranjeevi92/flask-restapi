import uuid
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import StoreSchema
from sqlalchemy.exc import IntegrityError,SQLAlchemyError

from db import db
from models import StoreModel
blp = Blueprint("stores", __name__, description="Operations on stors"
)

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema(many=False))
    def get(self, store_id):
            store = StoreModel.query.get_or_404(store_id)
            return store

    def delete(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted!"}

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
       return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema(many=False))
    def post(self,store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Name already exist!")
        except SQLAlchemyError:
            abort(500, message="Internal server error!")
        return store,201
