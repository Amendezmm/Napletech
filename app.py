import os
from flask import Flask, render_template, request
from src.DataMoch import Products
from src.DataMoch import Advertising
 
ruta = os.path.join(os.path.dirname(__file__), '', 'src/templates')
app = Flask(__name__, template_folder=ruta)

@app.route('/', methods=["GET","POST"])
@app.route('/index', methods=["GET","POST"])
def home(): 
    products = Products.products  
    ads = Advertising.advertisesment
    if request.method == "POST":                
        filtro = request.form["txtsearch"]
        category = request.form["category"]
        if filtro and category =="True":            
            products = filter_productlist(products, "category" ,filtro)                     
            return render_template('index.html',ProductsList=products, ads=ads)
        
        if filtro:
            products = filter_productlist(products, "name" ,filtro)
            return render_template('index.html',ProductsList=products, ads=ads)
        
    return render_template('index.html',ProductsList=products, ads=ads)


def filter_productlist(productslist, clave ,finddata):   
    return [item for item in productslist if str(finddata).lower() in str(item.get(clave, "")).lower()]


if __name__ == '__main__':
    app.run(debug=True)