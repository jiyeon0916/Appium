import allure

def attach_text(name, content):
    allure.attach(content, name=name, attachment_type=allure.attachment_type.TEXT)
