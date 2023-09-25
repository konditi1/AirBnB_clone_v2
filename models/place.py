#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship


place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", ForeignKey("places.id"), primary_key=True, nullable=False),
        Column("amenity_id", ForeignKey("amenities.id"), primary_key=True,nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0) 
    price_by_night = Column(Integer(), nullable=False, default=0) 
    latitude = Column(Float(), nullable=True) 
    longitude = Column(Float(), nullable=True)
    reviews = relationship("Review", backref="place")
    amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            backref="place_amenities"
    )

    @property
    def reviews(self):
        """
        Get the list of Review instances
        """
        from models import storage
        place_reviews = []
        reviews = storage.all(Review)
        
        for review in reviews:
            if review.place_id == self.id:
                place_reviews.append[city]

        return place_reviews
