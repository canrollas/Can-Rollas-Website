from flask import Flask,render_template,redirect,url_for,request

import sqlite3

from wtforms import Form,StringField,validators


app = Flask(__name__,static_url_path='/static',template_folder='template')



class register_form(Form):
    name = StringField("İsim Soyisim:",validators=[validators.length(min=4,max=25)])
    email=StringField("E-Mail:",validators=[validators.Email("Lütfen gecerli bir e-mail giriniz!")])
    

@app.route("/")
def index():
    number=10
    return render_template("index.html",number=number)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")
@app.route("/register" , methods = ["GET","POST"])
def register():
    con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

    cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

    form = register_form(request.form)

    if(request.method=="POST") and form.validate():
        
        name = form.name.data
        email = form.email.data
        cursor.execute("SELECT `email` from 'users' ")
        #first_query="SELECT `email` FROM `users`"

       # cursor.execute(first_query)
        users=cursor.fetchall()
        print("Kullanılmıs:",users)
        if((users==[])):
            sorgu="INSERT INTO `users` (`id`, `name`, `email`) VALUES ('', '{}', '{}')".format(name,email)
            cursor.execute(sorgu)
            con.commit()
            cursor.close()
            return redirect(url_for("index",data="succes"))
        else:
            return redirect(url_for("register",data="failed"))
    else:
        return render_template("register.html" ,form=form,stringer="unsucces1")


if __name__=="__main__":
    app.run(debug=True)