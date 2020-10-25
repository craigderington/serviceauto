"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    Get("/index", "WelcomeController@index").name("index"),
    Get("/cars", "CarController@show").name("cars"),
    Get("/cars/@id:int", "CarController@single").name("car"),
    Get("/cars/@id:int/engine", "EngineController@show").name("engine"),
    Get("/cars/@id:int/history", "ServiceHistoryController@show").name("history")
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
