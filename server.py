from flask import Flask, render_template

app = Flask(__name__)


#always use the decoratore
#show a 8 * * cheakerboard
@app.route("/")
def displa_board():
    return  render_template("index.html",row_num= 4,col_num = 4)


# chose the amount of rows
@app.route("/<int:row_num>")
def chose_row_num(row_num):
    return render_template("index.html",row_num=row_num,col_num = 4)

# chose the amout of coloms
@app.route("/<int:row_num>/<int:col_num>")
def chose_coloms(row_num,col_num):
    return render_template("index.html",row_num=row_num,col_num = col_num)


# chose the color of the board
@app.route("/<int:row_num>/<int:col_num>/<string:color>/<string:color2>")
def chose_color(row_num,col_num,color,color2):
    return render_template("index.html",row_num=row_num,col_num = col_num,color = color,color2 = color2)












if __name__ == "__main__":
    app.run(debug = True)