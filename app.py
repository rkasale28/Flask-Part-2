from flask import Flask,request,redirect,render_template,send_from_directory
from models import db,Book,migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_uploads import configure_uploads, IMAGES, UploadSet

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/books'
    app.config['UPLOADED_IMAGES_DEST']='media/images'
    db.init_app(app)
    migrate.init_app(app, db)
    return app

app=create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

images=UploadSet('images',IMAGES)
configure_uploads(app,images)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        book_name=request.form['bookname']
        book_price=request.form['price']
        cover_page=request.files['cover_page']
        filename=images.save(cover_page)
        newbook=Book(name=book_name,price=book_price,filename=filename)

        try:
            db.session.add(newbook)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding book'
    else:
        books=Book.query.order_by('name').all()
        return render_template('index.html', books=books)
    
@app.route('/delete/<int:id>')
def delete(id):
    book_to_delete = Book.query.get_or_404(id)

    try:
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting this book'

@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    book=Book.query.get_or_404(id)
    if request.method=='POST':
        book.name=request.form['name']
        book.price=request.form['price']
        cover_page=request.files['cover_page']
        book.filename=images.save(cover_page)
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your book'
    else:
        return render_template('update.html',book=book)

@app.route('/media/images/<filename>')
def retrieve_image(filename):
    return send_from_directory(app.config['UPLOADED_IMAGES_DEST'],filename)

if __name__=="__main__":
    manager.run()
    app.run(debug=True)