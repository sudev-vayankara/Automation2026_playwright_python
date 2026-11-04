class LoginPage:
    def __init__(self,page):
        self.page = page
        self.user_name = page.locator("#Email")
        self.pwd = page.locator("#Password")
        self.remember_me = page.locator("#RememberMe")
        self.forgot_pwd = page.locator("//a[text()='Forgot password?']")
        self.login = page.locator("//input[@value='Log in']")
        self.logout = page.locator("//a[text()='Log out']")
        self.error_msg = page.locator("//div[@class='message-error']")

    async def navigate_to_login_page(self):
        await self.page.goto("https://demowebshop.tricentis.com/login")

    async def enter_username(self, username):
        await self.user_name.fill(username)

    async def enter_password(self, password):
        await self.pwd.fill(password)
    async def click_remember_me(self, remember_me):
        await self.remember_me.click()
    async def click_forgot_pwd(self):
        await self.forgot_pwd.click()
    async def click_login(self):
        await self.login.click()
    async def valid_login_page(self):
        return await self.logout.is_visible()
    async def get_error_msg(self):
        return await self.error_msg.inner_text()