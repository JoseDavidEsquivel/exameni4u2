import web

from mvc.models.model_login import ModeloLogin

m_login = ModeloLogin()

render = web.template.render('mvc/views')

class Login:
    def GET(cls, mensaje = ""):
        return render.login(mensaje)

    def POST(self):
        form = web.input()
        user = form.num1
        password = form.num2
        if (user == m_login.nombre) and (password == m_login.contrasena):
            web.setcookie('user', user)
            web.setcookie('password', password)
            return render.inicio(user)
        else:
            mensaje = "Este usuario no existe en la base de datos, intente de nuevo"
            return render.login(mensaje)
