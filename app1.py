import flet as ft


class App:
    def main(self, x: ft.Page):
        self.page = x
        self.page.title = 'Login'
        self.page.window_height = 600
        self.page.window_width = 300
        self.page.bgcolor = '#070b11'
        self.colorBorders = '#121d25'
        self.colorButton = '#0c0f16'

        self.iLogo = ft.Image(src=f"/images/vascos.png", width=150,
                              height=150)

        self.eUser = ft.TextField(
            label='Nombre de Usuario', border_radius=10, border_color=self.colorBorders)
        self.ePassword = ft.TextField(
            label='Contraseña', password=True, can_reveal_password=True, border_radius=10, border_color=self.colorBorders)

        self.ebInicio = ft.ElevatedButton(
            "Inicio", on_click=self.fnInicio, bgcolor=self.colorButton)
        self.greetings = ft.Column()

        self.column1 = [
            self.iLogo,
            self.eUser,
            self.ePassword,
            self.ebInicio,
            self.greetings
        ]

        self.page.add(
            ft.Column(self.column1)
        )

        self.page.update()

    def fnInicio(self, e):
        str = f"""
        usuario: {self.eUser.value}
        contraseña: {self.ePassword.value}
        """
        print(self.iLogo.src)
        self.greetings.clean()
        self.greetings.controls.append(ft.Text(str))
        self.page.update()

    def play(self):
        ft.app(
            target=self.main,
            assets_dir="login"
        )


app1 = App()
app1.play()
