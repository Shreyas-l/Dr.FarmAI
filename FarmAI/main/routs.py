
from flask import render_template, url_for, flash, redirect,abort,request,Response
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm, LoginForm,PostForm
from flaskblog import app,db
from flask_login import login_user,current_user,logout_user,login_required


import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as k
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from flask import request
from flask import jsonify,make_response
from flask import Flask
import tensorflow as tf
import pandas as pd
import json
from tensorflow.python.keras.backend import set_session
#from flask_ngrok import run_with_ngrok

#run_with_ngrok(app)

db.create_all()


keras.backend.clear_session()

def get_model(name):
    global modelnearby
    #modelnearby=load_model(name)
    print("MODEL LOADED!")
    return load_model(name)

def preprocess_image(image,target_size):
    if image.mode!="RGB":
        image=image.convert("RGB")
    image=image.resize(target_size)
    image=img_to_array(image)
    image=np.expand_dims(image,axis=0)
    return image


print("LOADING KERAS NEARBY TOM MODEL!")
modelnearbytom=get_model("flaskblog/static/models/tomato.h5")
global graphnearbytom
graphnearbytom = tf.get_default_graph()

@app.route('/predicttom')
#@app.route('/predicttom<pred>')
def predicttom():
    return render_template('predicttom.html')

@app.route('/predict_tom',methods=['GET','POST'])
def predict_tom():
    message=request.get_json(force=True)
    encoded=message['image']
    decoded=base64.b64decode(encoded)
    image=Image.open(io.BytesIO(decoded))
    processed_image=preprocess_image(image,target_size=(256,256))
    g_1 = tf.Graph()
    with graphnearbytom.as_default():
        # sesstom = tf.Session()
        # set_session(sesstom)
        prediction=modelnearbytom.predict(processed_image)
        response={
        
        'c0':prediction[0][0],
        'c1':prediction[0][1],
        }
        print(response)
        return Response(pd.Series(response).to_json(orient='values'))


print("LOADING KERAS NEARBY PEP MODEL!")
modelnearbypep=get_model("flaskblog/static/models/pepper.h5")
# global sesspep
global graphnearbypep
graphnearbypep  = tf.get_default_graph()

@app.route('/predictpep')
def predictpep():
    return render_template('predictpep.html')


@app.route('/predict_pep', methods=["GET","POST"])
def predict_pep():
    message=request.get_json(force=True)
    encoded=message['image']
    decoded=base64.b64decode(encoded)
    image=Image.open(io.BytesIO(decoded))
    processed_image=preprocess_image(image,target_size=(256,256))
    with graphnearbypep.as_default():
        # set_session(sesspep)
        prediction=modelnearbypep.predict(processed_image)
        response={
        
        'c0':prediction[0][0],
        'c1':prediction[0][1],
        }
    return Response(pd.Series(response).to_json(orient='values'))


print("LOADING KERAS NEARBY POT MODEL!")
modelnearbypot=get_model("flaskblog/static/models/potato.h5")
# global sesspot
global graphnearbypot
graphnearbypot  = tf.get_default_graph()

@app.route('/predictpot')
def predictpot():
    return render_template('predictpot.html')

@app.route('/predict_pot', methods=["GET","POST"])
def predict_pot():
    message=request.get_json(force=True)
    encoded=message['image']
    decoded=base64.b64decode(encoded)
    image=Image.open(io.BytesIO(decoded))
    processed_image=preprocess_image(image,target_size=(256,256))
    with graphnearbypot.as_default():
        # set_session(sesspot)
        prediction=modelnearbypot.predict(processed_image)
        response={
        
        'c0':prediction[0][0],
        'c1':prediction[0][1],
        }
    return Response(pd.Series(response).to_json(orient='values'))


print("LOADING KERAS NEARBY GRP MODEL!")
modelnearbygrp=get_model("flaskblog/static/models/grape.h5")
# global sessgrp
global graphnearbygrp
graphnearbygrp  = tf.get_default_graph()

@app.route('/predictgrp')
def predictgrp():
    return render_template('predictgrp.html')

@app.route('/predict_grp', methods=["GET","POST"])
def predict_grp():
    message=request.get_json(force=True)
    encoded=message['image']
    decoded=base64.b64decode(encoded)
    image=Image.open(io.BytesIO(decoded))
    processed_image=preprocess_image(image,target_size=(256,256))
    with graphnearbygrp.as_default():
        # set_session(sessgrp)
        prediction=modelnearbygrp.predict(processed_image)
        response={
        
        'c0':prediction[0][0],
        'c1':prediction[0][1],
        }
    return Response(pd.Series(response).to_json(orient='values'))


print("LOADING KERAS FARBY MODEL!")
modelfarby=get_model("flaskblog/static/models/farby.h5")
# global sessfarby
global graphfarby
graphfarby  = tf.get_default_graph()

    
@app.route('/predictfarby')
def predictfarby():
    return render_template('predictfarby.html')

@app.route('/predict_farby', methods=["GET","POST"])
def predict_farby():
    message=request.get_json(force=True)
    encoded=message['image']
    encoded=encoded+str("==")
    decoded=base64.b64decode(encoded)
    image=Image.open(io.BytesIO(decoded))
    processed_image=preprocess_image(image,target_size=(256,256))
    with graphfarby.as_default():
        # set_session(sessfarby)
        prediction=modelfarby.predict(processed_image)
    response={
        
        'd1':prediction[0][0],
        'd2':prediction[0][1],
        'd3':prediction[0][2],
        'd4':prediction[0][3],
        'd5':prediction[0][4],
                    }
    return Response(pd.Series(response).to_json(orient='values'))


@app.route("/")
@app.route("/home")
def home():
    posts=Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)   

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.password==form.password.data :
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account') 
@login_required
def account():
    image_file=url_for('static',filename='profile_pics/' + str(current_user.image_file))
    posts=user_posts(current_user.username)
    return render_template('account.html', title='Account',image_file=image_file,posts=posts,current_user=current_user)

def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())
    return posts

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


#CHANGES FROKM HERE

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/predict_nearby')
def predict_nearby():
    return render_template('predict_nearby.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

