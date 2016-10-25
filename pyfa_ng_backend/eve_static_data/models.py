

from ..extensions import db


class InvCategory(db.Model):
    __tablename__ = 'invCategories'
    __bind_key__ = 'sde'

    categoryID = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.Text)
    iconID = db.Column(db.Integer)
    published = db.Column(db.Integer)


class InvGroup(db.Model):
    __tablename__ = 'invGroups'
    __bind_key__ = 'sde'

    groupID = db.Column(db.Integer, primary_key=True)
    categoryID = db.Column(db.Integer, db.ForeignKey('invCategories.categoryID'))
    category = db.relationship('InvCategory', backref=db.backref('groups', lazy='dynamic'))
    groupName = db.Column(db.Text)
    iconID = db.Column(db.Integer)
    useBasePrice = db.Column(db.Integer)
    anchored = db.Column(db.Integer)
    anchorable = db.Column(db.Integer)
    fittableNonSingleton = db.Column(db.Integer)
    published = db.Column(db.Integer)


class InvType(db.Model):
    __tablename__ = 'invTypes'
    __bind_key__ = 'sde'

    typeID = db.Column(db.Integer, primary_key=True)
    groupID = db.Column(db.Integer, db.ForeignKey('invGroups.groupID'))
    group = db.relationship('InvGroup', backref=db.backref('types', lazy='dynamic'))
    typeName = db.Column(db.Text)
    description = db.Column(db.Text)
    mass = db.Column(db.Float)
    volume = db.Column(db.Float)
    capacity = db.Column(db.Float)
    portionSize = db.Column(db.Integer)
    raceID = db.column(db.Integer)
    basePrice = db.Column(db.Float)
    published = db.Column(db.Integer)
    marketGroupID = db.Column(db.Integer)
    iconID = db.Column(db.Integer)
    soundID = db.Column(db.Integer)
    graphicID = db.Column(db.Integer)


class InvMarketGroups(db.Model):
    __tablename__ = 'invMarketGroups'
    __bind_key__ = 'sde'

    marketGroupID = db.Column(db.Integer, primary_key=True)
    parentGroupID = db.Column(db.Integer)
    marketGroupName = db.Column(db.Text)
    description = db.Column(db.Text)
    iconID = db.Column(db.Integer)
    hasTypes = db.Column(db.Integer)
