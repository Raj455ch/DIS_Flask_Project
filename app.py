from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/category")
def category():
    return render_template("category.html")


@app.route("/booksCategory/<bookCategory>",  methods=['GET'])
def booksCategory(bookCategory):
    if request.method == "GET":
        try:
            with sqlite3.connect('database.db')as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM BOOKS WHERE CATEGORY = '" +
                            bookCategory + "'")
                rows = cur.fetchall()
                return render_template("bookCategory.html", bookData=rows, title=bookCategory)
        except Exception as e:
            con.rollback()
            print(e)
            return " <script>alert('Error in loading Categories');location.replace('/')</script>"
        finally:
            con.close()


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        return render_template("contactus.html")
    elif request.method == "POST":
        username = request.form['textfield1']
        email = request.form['textfield3']
        query = request.form['query']

        try:
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO CONTACTQUERIES (NAME, EMAIL, QUERY) VALUES ('" +
                            username + "','" + email + "','"+query + "')")
                con.commit()
                return "<script> alert('Thank you for reaching out to us. Your query id is '+ Math.floor(Math.random() * 100000)+' and our team will resolve your issue sometime soon.');location.replace('/contact') </script>"
        except Exception as e:
            con.rollback()
            print(e)
            return "<script>alert('Error in storing details');location.replace('/')</>"
        finally:
            con.close()
        return request.form


@app.route("/cart", methods=['POST'])
def cart():
    bookIDs = request.form['booksIDs']
    print(bookIDs)
    try:
        with sqlite3.connect('database.db')as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM BOOKS WHERE BOOKID IN " +
                        bookIDs)
            rows = cur.fetchall()
            totalPrice = 0
            if (len(rows) == 0):
                return render_template("cart.html", bookData=rows, totalPrice=totalPrice, title="Cart")

            personalGrowth = 0
            healthWellness = 0
            history = 0
            sports = 0
            travel = 0
            sciFi = 0

            for item in rows:
                totalPrice = totalPrice + int(item[7])
                if item[4] == "Health Wellness":
                    healthWellness += 1
                elif item[4] == "History":
                    history += 1
                elif item[4] == "Personal Growth":
                    personalGrowth += 1
                elif item[4] == "Science Fiction":
                    sciFi += 1
                elif item[4] == "Sports":
                    sports += 1
                elif item[4] == "Travel":
                    travel += 1

            chart = str(personalGrowth)+","+str(healthWellness)+"," + \
                str(history)+","+str(sports)+","+str(travel) + ","+str(sciFi)

            return render_template("cart.html", bookData=rows, totalPrice=totalPrice, title="Cart", chart=chart)

    except Exception as e:
        con.rollback()
        print(e)
        return " <script>alert('Empty cart! Please add some books');location.replace('/')</script>"
    finally:
        con.close()


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['userpassword']

            with sqlite3.connect('database.db')as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM REGISTRATION WHERE FULLNAME = '" +
                            username + "' AND PASSWORD = '"+password+"'")
                rows = cur.fetchall()
                if len(rows) == 0:
                    return render_template("ErrorModal.html")
                elif len(rows) > 0:
                    return "<script>localStorage.setItem('isLoggedIn', true);localStorage.setItem('username', '" + rows[0][1] + "');localStorage.setItem('email', '"+rows[0][2]+"');location.replace('/')</script>"

        except Exception as e:
            con.rollback()
            print(e)
            return "<script>alert('unable to login');location.replace('/')</script>"
        finally:
            cur.close()


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        try:
            with sqlite3.connect('database.db')as con:
                cur = con.cursor()
                cur.execute("INSERT INTO REGISTRATION (FULLNAME,EMAIL,PASSWORD,ROLE) VALUES(?,?,?,?)",
                            (username, email, password, ''))
                con.commit()
                return render_template("RegSuccess.html")
        except Exception as e:
            con.rollback()
            print(e)
            return " <script>alert('Error in user registration');location.replace('/')</script>"
        finally:
            con.close()


@app.route("/Logout")
def logout():
    return '<script>localStorage.clear();location.replace("/")</script>'


@app.route("/ourservices")
def ourservices():
    return render_template("ourServices.html")


@app.route("/privacyPolicy")
def privacyPolicy():
    return render_template("privacyPolicy.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/contactus")
def contactus():
    return render_template("contactus.html")


@app.route("/ViewData", methods=['POST', 'GET'])
def ViewData():
    if request.method == 'GET':
        return render_template("ViewData.html", title="View Query")
    elif request.method == 'POST':
        try:
            tabName = request.form['tabName']
            query = ""
            title = ""
            headers = []
            if tabName == "registration":
                query = "SELECT USERID, FULLNAME, EMAIL, PASSWORD  FROM REGISTRATION"
                title = "Registration"
                headers = ["USERID", "FULLNAME", "EMAIL", "PASSWORD"]
            elif tabName == "contactquery":
                query = "SELECT QID, NAME, EMAIL, QUERY FROM CONTACTQUERIES"
                title = "Contact Queries"
                headers = ["QID", "NAME", "EMAIL", "QUERY"]

            with sqlite3.connect('database.db')as con:
                cur = con.cursor()
                cur.execute(query)
                rows = cur.fetchall()

            return render_template("ViewData.html", title=title, headers=headers, tableData=rows)
        except Exception as e:
            con.rollback()
            print(e)
            return " <script>alert('Error in user registration');location.replace('/')</script>"
        finally:
            con.close()

    print(request.form)


if __name__ == "__main__":
    app.run(debug=True)
