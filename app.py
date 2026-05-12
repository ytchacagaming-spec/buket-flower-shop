from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT")),
        cursorclass=pymysql.cursors.DictCursor
    )

# ================== HOME ==================
@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products ORDER BY RAND()")
    products = cursor.fetchall()
    db.close()
    return render_template("index.html", products=products)


# ================== KATALOG ==================
@app.route("/katalog")
def katalog():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products ORDER BY RAND()")
    products = cursor.fetchall()
    db.close()
    return render_template("katalog.html", products=products)


# ================== DETAIL ==================
@app.route("/product/<int:id>")
def detail(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()
    db.close()
    return render_template("detail.html", product=product)

@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

# ================== RUN ==================
if __name__ == "__main__":
    app.run(debug=True)