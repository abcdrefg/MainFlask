import os
from flask import Flask, render_template, request, json, redirect, session, url_for, send_from_directory, \
    jsonify, send_file
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path
from PDFoperations import deletePages, rotatePages, checkNumOfPages
from pdf2docx import Converter

app = Flask(__name__)
mysql = MySQL()
rootDir = os.path.dirname(os.path.abspath(__file__))

uploadPath = rootDir + '\\uploadedfiles'

app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin1'
app.config['MYSQL_DATABASE_DB'] = 'edytorpdf'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = uploadPath
app.config['MAX_CONTENT'] = 1000000
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
app.secret_key = 'pdf editor flask gold key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signUp.html')


@app.route('/showLogin', methods=['POST', 'GET'])
def showLogin():
    return render_template('login.html')


@app.route('/showMainPage')
def showMainPage():
    print(session.get('user'))
    print(uploadPath)
    return render_template('index.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _mail = request.form['inputEmail']
    _password = request.form['inputPassword']
    cursor.callproc('sp_createUser', (_name, _mail, _password))
    data = cursor.fetchall()
    if len(data) == 0:
        conn.commit()
        return render_template('signUpSucces.html')
    else:
        return render_template('signUpError.html')


@app.route('/loginUp', methods=['POST', 'GET'])
def loginUp():
    try:
        global xdata
        _name = request.form['inputName']
        _password = request.form['inputPassword']
        cursor.execute("SELECT * FROM users WHERE (_Username=%s)", _name)
        xdata = cursor.fetchall()
        if (len(xdata) > 0):
            if (_password == xdata[0][3]):
                session['user'] = xdata[0][0]
                return redirect('/uIndex')
            else:
                return render_template('errorlogin.html')
        else:
            print("erro")
            return render_template('errorlogin.html')
    except Exception as e:
        return render_template('errorlogin.html')


@app.route('/uIndex')
def uIndex():
    if session.get('user'):
        return render_template("uindex.html")
    else:
        return render_template('brak.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    session['user'] = xdata[0][0]
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        cursor.execute('SELECT * FROM files WHERE id_user = %s', session.get('user'))
        tabLen = cursor.fetchall()
        if len(tabLen) <= 4:
            if f.filename[-4:] == '.pdf':
                cursor.execute('INSERT INTO files(id_user, filename) VALUES ( %s, %s)',
                               (int(session.get('user')), f.filename))
                cursor.fetchall()
                conn.commit()
                cursor.execute('SELECT LAST_INSERT_ID();')
                newName = cursor.fetchall()
                newName = str(newName[0][0]) + '.pdf'
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
                return render_template('success.html')
        else:
            return render_template('max.html')


@app.route('/myFiles', methods=['GET', 'POST'])
def myFiles():
    img_url = url_for('static', filename='pdf.jpg')
    if session.get('user'):
        return render_template('myFiles.html', image_url=img_url)
    else:
        return render_template('brak.html')


@app.route('/myFilesJS', methods=['POST', 'GET'])
def myFilesJS():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    jsondata = jsonify(tempdata)
    return jsondata


@app.route('/myProfileJS', methods=['POST', 'GET'])
def myProfileJS():
    cursor.execute('SELECT * FROM users WHERE id=%s', session.get('user'))
    tempdata = cursor.fetchall()
    jsondata = jsonify(tempdata)
    return jsondata


@app.route('/delfile1')
def delfile1():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[0][0]
    os.remove(uploadPath + '\\' + str(x) + '.pdf')
    cursor.execute('DELETE FROM files WHERE id_file=%s', x)
    cursor.fetchall()
    conn.commit()
    return render_template('myFiles.html')


@app.route('/delfile2')
def delfile2():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[1][0]
    os.remove(uploadPath + '\\' + str(x) + '.pdf')
    cursor.execute('DELETE FROM files WHERE id_file=%s', x)
    cursor.fetchall()
    conn.commit()
    return render_template('myFiles.html')


@app.route('/delfile3')
def delfile3():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[2][0]
    os.remove(uploadPath + '\\' + str(x) + '.pdf')
    cursor.execute('DELETE FROM files WHERE id_file=%s', x)
    cursor.fetchall()
    conn.commit()
    return render_template('myFiles.html')


@app.route('/delfile4')
def delfile4():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[3][0]
    os.remove(uploadPath + '\\' + str(x) + '.pdf')
    cursor.execute('DELETE FROM files WHERE id_file=%s', x)
    cursor.fetchall()
    conn.commit()
    return render_template('myFiles.html')


@app.route('/delfile5')
def delfile5():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[4][0]
    os.remove(uploadPath + '\\' + str(x) + '.pdf')
    cursor.execute('DELETE FROM files WHERE id_file=%s', x)
    cursor.fetchall()
    conn.commit()
    return render_template('myFiles.html')


@app.route('/download1')
def download1():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[0][0]
    path = uploadPath + '\\' + str(x) + '.pdf'
    return send_file(path, as_attachment=True, cache_timeout=0)


@app.route('/download2')
def download2():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[1][0]
    path = uploadPath + '\\' + str(x) + '.pdf'
    return send_file(path, as_attachment=True, cache_timeout=0)


@app.route('/download3')
def download3():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[2][0]
    path = uploadPath + '\\' + str(x) + '.pdf'
    return send_file(path, as_attachment=True, cache_timeout=0)


@app.route('/download4')
def download4():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[3][0]
    path = uploadPath + '\\' + str(x) + '.pdf'
    return send_file(path, as_attachment=True, cache_timeout=0)


@app.route('/download5')
def download5():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    x = tempdata[4][0]
    path = uploadPath + '\\' + str(x) + '.pdf'
    return send_file(path, as_attachment=True, cache_timeout=0)


@app.route('/edit')
def edit1():
    if session.get('user'):
        return render_template('editFile.html')
    else:
        return render_template('brak.html')


@app.route('/edit1File')
def edit1File():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    currentFile = tempdata[0][0]
    modifyThisFile(currentFile)
    jsondata = jsonify(tempdata[0][0])
    return jsondata


@app.route('/edit2File')
def edit2File():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    currentFile = tempdata[1][0]
    modifyThisFile(currentFile)
    jsondata = jsonify(tempdata[0][1])
    return jsondata


@app.route('/edit3File')
def edit3File():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    currentFile = tempdata[2][0]
    modifyThisFile(currentFile)
    jsondata = jsonify(tempdata[0][2])
    return jsondata


@app.route('/edit4File')
def edit4File():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    currentFile = tempdata[3][0]
    modifyThisFile(currentFile)
    jsondata = jsonify(tempdata[0][3])
    return jsondata


@app.route('/edit5File')
def edit5File():
    cursor.execute('SELECT * FROM files WHERE id_user=%s', session.get('user'))
    tempdata = cursor.fetchall()
    currentFile = tempdata[4][0]
    modifyThisFile(currentFile)
    jsondata = jsonify(tempdata[0][4])
    return jsondata


@app.route('/delPage', methods=['POST', 'GET'])
def delPage():
    _page = request.form['delPage']  # do zrobienia
    if (int(_page) <= checkNumOfPages(thisFile)):
        deletePages(thisFile, int(_page))
        return render_template("sucDel.html")
    else:
        return render_template("errorEdit.html")


@app.route('/rotPage', methods=['POST', 'GET'])
def rotPage():
    _page = request.form['rotPage']
    if (int(_page) <= checkNumOfPages(thisFile)):  # do zrobienia
        rotatePages(thisFile, int(_page))
        return render_template("sucRot.html")
    else:
        return render_template("errorEdit.html")


@app.route('/myProfile', methods=['POST', 'GET'])
def myProfile():
    if session.get('user'):
        return render_template('myProfile.html')
    else:
        return render_template('brak.html')


def accessThisFile():
    return thisFile


def modifyThisFile(x):
    global thisFile
    thisFile = x
    return thisFile


@app.route('/docx', methods=['POST', 'GET'])
def downloadDOCX():
    pdf_file = uploadPath + "\\" + str(thisFile) + '.pdf'
    docx_file = uploadPath + "\\" + "JPWPpdfEditor_" + str(thisFile) + ".docx"
    f = Converter(pdf_file)
    f.convert(docx_file, start=0, end=None)
    f.close()
    return send_file(docx_file, as_attachment=True, cache_timeout=0)


if __name__ == '__main__':
    app.run(debug=True)
