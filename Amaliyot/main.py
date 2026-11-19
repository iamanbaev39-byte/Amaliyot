class User:
    def __init__(self, username, ism, email):
        self.username = username
        self.ism = ism
        self.email = email
        self.obunachilar = 0

    def get_info(self):
        print("Foydalanuvchi: " + self.username + ", ismi: " + self.ism + ", email: " + self.email)

    def obuna_qosh(self):
        self.obunachilar += 1

    def email_ozgartir(self, yangi_email):
        self.email = yangi_email



u1 = User("jonyvxck", "Eshpolatov Jonibek", "jonibeeshpolatov@gmail.com")
u2 = User("jony_002", "Eshpolatov jonibek", "iamanbaev39@gmail.com")

print(u1.username)
print(u2.ism)


u1.get_info()
u2.get_info()

u1.obuna_qosh()
u1.obuna_qosh()
print(u1.obunachilar)

u2.email_ozgartir("iamanbaev39@gmail.com")
u2.get_info()