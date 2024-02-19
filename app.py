# Framework web.py
import web

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.login.Login',
    )

app = web.application(urls, globals())

# Punto de Entrada
if __name__ == "__main__":
    web.config.debug = False
    app.run()