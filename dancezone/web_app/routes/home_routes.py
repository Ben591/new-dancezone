from flask import Blueprint, request, render_template, redirect, flash
from app.datafetch import fetch_search_data

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def form():
    print("Dance Zone...")
    return render_template("home.html")

@home_routes.route("/search/list", methods=["GET", "POST"])
def searchlist():

    if request.method == "POST":
        request_data = dict(request.form)
    else:
        request_data = dict(request.args)

    song = request_data.get("song")

    #try:
    #    items = fetch_search_data(search_song=song)

    return render_template("searchlist.html",song=song)