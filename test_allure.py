import allure
import pytest


@allure.title("This is a very important test")
@allure.description("There goes the description")
@allure.issue("http://support.lv.tieto.com/")
def test():
    # attach text
    allure.attach(
        "Some text data",
        "Contents of the text data",
        allure.attachment_type.TEXT,
    )

    # # attach image
    # allure.attach(
    #     ...
    # )
