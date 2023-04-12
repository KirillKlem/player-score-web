from sqlalchemy.orm import ColumnProperty, class_mapper

def attribute_names(cls):
    properties = class_mapper(cls)._polymorphic_properties
    return [prop.key for prop in properties] 