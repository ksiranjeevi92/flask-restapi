from marshmallow import Schema,fields

class PlainItemSchema(Schema):
    id =  fields.Int(dump_only=True)
    name= fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Int(required=True)

class PlainItemUpdateSchema(Schema):
    name= fields.Str()
    price = fields.Float()

class PlainStoreSchema(Schema):
     id =  fields.Int(dump_only=True)
     name= fields.Str(required=True)

class ItemSchema(PlainItemSchema):
    store=fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema), dump_only=True)