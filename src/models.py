import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Profile(Base):
    __tablename__ = 'profile'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

class Friends(Base):
    __tablename__ = 'friends'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    friends_id = Column(Integer, ForeignKey('profile.id'))

class Direct_message(Base):
    __tablename__ = 'dm'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    message = Column(String(250))
    friends_id = Column(Integer, ForeignKey('friends.id'))

class Stories(Base):
    __tablename__ = 'stories'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    stories = Column(String(250))
    stories_id = Column(Integer, ForeignKey('profile.id'))

class Stories_dm(Base):
    __tablename__ = 'dmS'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    storiesdm = Column(String(250))
    storiesdm_id = Column(Integer, ForeignKey('stories.id'))

class Views(Base):
    __tablename__ = 'views'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    stories_views = Column(String(250))
    views_id = Column(Integer, ForeignKey('stories.id'))

class Summary(Base):
    __tablename__ = 'summary'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_summary = Column(String(250))
    summary_id = Column(Integer, ForeignKey('profile.id'))

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post = Column(String(250))
    post_id = Column(Integer, ForeignKey('profile.id'))

class Post_Description(Base):
    __tablename__ = 'post_description'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_description = Column(String(250))
    post_description_id = Column(Integer, ForeignKey('post.id'))

class Post_Likes(Base):
    __tablename__ = 'Post_Likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_likes = Column(String(250))
    post_likes_id = Column(Integer, ForeignKey('post.id'))

class Location(Base):
    __tablename__ = 'Post_Location'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_location = Column(String(250))
    post_location_id = Column(Integer, ForeignKey('post.id'))

class Comments(Base):
    __tablename__ = 'Post_Comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_comments = Column(String(250))
    post_comments_id = Column(Integer, ForeignKey('post.id'))

class Post_likes(Base):
    __tablename__ = 'Post_likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_likes = Column(String(250))
    post_likes_id = Column(Integer, ForeignKey('Post_Comments.id'))




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')