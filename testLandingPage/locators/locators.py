class SearchPageLocators:
    loginInput = "input[id='form2Example17']"
    passwordInput = "input[id='form2Example27']"
    confirmLoginButton = "button[class='btn btn-dark btn-lg btn-block']"
    welcomeMessage = "//div[@class='div-center']/h1"
    logout = "//a[text()='Wyloguj']"

class SearchNavBarItemsServiceTechnician:
    home = "//ul[@class='navigation']/li[1]/a"
    vessel = "//ul[@class='navigation']/li[2]/a"
    warehouse = "//ul[@class='navigation']/li[3]/div/a"
    nickname = "//ul[@class='navigation']/li[4]/div/a"

    textField = "//div[@id='drugi_div']/input"
    frame2 = "iframe[id='vesselfinder']"
    vesselImo = "//div[@id='ship-info-popup']//td[@id='vessel_imo']"
    imoMmsi = "/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[2]/table/tbody/tr[7]/td[2]"
    flag = "/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[2]/table/tbody/tr[9]/td[2]"
    destinationPort = "/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[1]"
    arrivalTime = "/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div/span[1]"
    moreInfoButton = "a[id='details-btn']"

class SearchNavBarItemsCoordinator:
    home = "//ul[@class='navigation']/li[1]/a"
    vessel = "//ul[@class='navigation']/li[2]/a"
    warehouse = "//ul[@class='navigation']/li[3]/div/a"
    order = "//ul[@class='navigation']/li[4]/a"
    nickname = "//ul[@class='navigation']/li[5]/div/a"

class SearchNavBarItemsWarehouseman:
    home = "//ul[@class='navigation']/li[1]/a"
    warehouse = "//ul[@class='navigation']/li[2]/div/a"
    nickname = "//ul[@class='navigation']/li[3]/div/a"


# class SearchNewOrderItems:

class SearchAdminDashboard:
    # Login Form
    username = "//input[@name='username']"
    password = "//input[@name='password']"
    loginButton = "input[type='submit']"

    # Site Administration
    accountsNameModule = "a[title='Models in the Accounts application']"
    authenticationAndAuthorizationModule = "a[title='Models in the Authentication and Authorization application']"
    ordersModule = "a[title='Models in the Orders application']"
    shipsModule = "a[title='Models in the Ships application']"
    tokenBlacklistModule = "a[title='Models in the Token Blacklist application']"
    warehouseModule = "a[title='Models in the Warehouse application']"
    addButtonAccounts = "//div[@class='app-accounts module']//a[text()='Add']"
    changeButtonAccounts = "//div[@class='app-accounts module']//a[text()='Change']"

    # Site user add
    usernameTextField = "input[name='username']"
    passwordTextField = "input[name='password1']"
    confirmationPasswordTextField = "input[name='password2']"

    # Personal info
    firstNameTextField = "input[name='first_name']"
    lastNameTextField = "input[name='last_name']"
    mailTextField = "input[name='mail']"
    roleOptions = "select[id='id_role']"
    saveButton = "//div[@class='submit-row']/input[@name='_save']"
    serwisantRole = "//div[@class='form-row field-role']//select[@id='id_role']/option[text()='Serwisant']"
    addUserSuccessMessage = "//li[@class='success']"

