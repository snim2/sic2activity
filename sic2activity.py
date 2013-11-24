import os
from flask import Flask, abort, jsonify

# Import Office of National Statistics data
import data

app = Flask(__name__)

data_2003, data_2007 = data.load_data()

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=404, text=e), 404


@app.route('/api/sics2007/')
def sics2007():
    return jsonify(sic_2007=data_2007.keys())


@app.route('/api/sics2003/')
def sics2003():
    return jsonify(sic_2003=data_2003.keys())


@app.route('/api/sics/')
def sics():
    return jsonify(sic_2007=data_2007.keys())


@app.route('/api/activities/')
def activities():
    return jsonify(activities=data_2003.values())


@app.route('/api/sic/<code>')
def sic(code=''):
    try:
        act = data_2007[code]
        return jsonify(sic=code, activity=act)
    except KeyError:
        abort(404)


@app.route('/api/sic/2003/<code>')
def sic2003(code=''):
    try:
        act = data_2003[code]
        return jsonify(sic=code, activity=act)
    except KeyError:
        abort(404)


@app.route('/api/sic/2007/<code>')
def sic2007(code=''):
    try:
        act = data_2007[code]
        return jsonify(sic=code, activity=act)
    except KeyError:
        abort(404)


@app.route('/')
def index():
    """Simple page to direct people to the API.
    """
    html = """<!DOCTYPE html>
    <html>
    <head>
        <title>Convert UK Standard Industrial Classifiers to Textual Activity Descriptions</title>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
        <link href='http://fonts.googleapis.com/css?family=Quattrocento:700' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Philosopher:400italic' rel='stylesheet' type='text/css'>
        <style type="text/css">
            body {
                margin: 0 20px;
                color: #222;
                background: #fff;
                text-align: center;
                padding-top: 64px;
                font-family: Quattrocento, Helvetica, "Helvetica Neue", Arial, sans-serif;
            }
            h1 {
                font-weight: bold;
                font-size: 10em;
                margin: 0;
                padding: 0;
            }
            p, hr {
                width: 60%;
                margin-left: auto;
                margin-right: auto;
                text-align: left;
            }
            hr {
                color: #eee;
                border-bottom: 0;
            }
            a, a:visited {
				color:#00F;
                text-decoration: none;
            }
			a:hover {
                text-decoration: underline;
			}
			.source {
				font-family: 'Philosopher', sans-serif;
				font-weight: 400;
                font-style:italic;
				color:#403723;
				font-size:.8em;
			}
            .footer {
                text-align: center;
                font-size: 10px;
            }
            .info {
                text-align: center;
            }
            @media only screen and (max-width: 767px) {
                body {
                    padding-top: 20px;
                }

                p, hr {
                    width: 80%;
                }
            }

            @media only screen and (max-width: 480px) {
                h1 {
                    font-size: 8em;
                }

                body {
                    padding-top: 10px;
                }

                p, hr {
                    width: 90%;
                }
            }
        </style>
    </head>
    <body>
        <h1>sic2activity</h1>
        <p>
            This site is intended to help you convert 
            <a href="http://www.ons.gov.uk/ons/guide-method/classifications/current-standard-classifications/standard-industrial-classification/index.html">UK Standard Industrial Classifiers</a> (SICs) to textual 
            descriptions of the activities they represent. 
        </p>
        <p>
            This site is intended to be used programatically, via a REST API.
            Please see the 
            <a href="https://github.com/snim2/sic2activity">GitHub repo</a> for
            details.
       </p>
       <div class="info">
        <a href="https://twitter.com/share" class="twitter-share-button" data-text="Convert UK Standard Industrial Classifiers to Textual Activity Descriptions" data-via="snim2" data-hashtags="nhshd">Tweet</a>
        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
        </div>
        <hr/>
        <p class="footer">&copy; 2013 <a href="http://snim2.org/">Sarah Mount</a>
    </body>
</html>
"""
    return html

