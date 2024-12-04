import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique= True)
    userName = Column(String(250), nullable=False, unique= True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    likes = Column(Integer, nullable = True)
    image_id= Column(Integer, ForeignKey('image.id'))
    user_id= Column(Integer, ForeignKey('user.id'))
    
    user = relationship(User)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_content = Column(String(350))
    
    post = relationship(Post)


class Image(Base):
    __tablename__= 'image'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    
    post = relationship(Post)

class Curso(Base):
    __tablename__= 'curso'
    id = Column(Integer, primary_key=True)
    nameCurso = Column(String(250), nullable=False)
    priceCurso = Column(String(250), nullable=False)

class Pertenece(Base):
    __tablename__= 'pertenece'
    id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    user_id= Column(Integer, ForeignKey('user.id'))

    user = relationship(User)
    curso = relationship(Curso)

   
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
