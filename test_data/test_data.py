class TestData:
    class Cookies:
        consent_cookie = {"domain": ".wearenotch.com", "expiry": 1801993993, "httpOnly": False,
                          "name": "cookieyes-consent", "path": "/", "sameSite": "Strict", "secure": True,
                          "value": "consentid:T0s5cjVJUW5rQ2VIeVVTVVNPa1V0bm9zQ0h5VlRwMUc,consent:yes,action:yes,"
                                   "necessary:yes,analytics:yes,advertisement:yes"}

    class UserData:
        mandatory_user_data = {
            "firstName": "Ivan",
            "lastName": "Horvat",
            "email": "ivan.horvat@gmail.com",
            "neededServices": ["Custom Software Development", "Scrum Coaching"]
        }

        user_data_invalid_email = {
            "firstName": "Ivan",
            "lastName": "Horvat",
            "email": "ivan.horvat",
        }

        complete_user_data = {
            "firstName": "Ivan",
            "lastName": "Horvat",
            "email": "ivan.horvat@gmail.com",
            "phoneNumber": "0911234567",
            "hearAboutUs": "Google",
            "companyName": "WeAreNotCh",
            "budget": "Up to €50.000",
            "neededServices": ["Custom Software Development", "Scrum Coaching"],
            "projectDetails": "We need a custom software development for our new startup."
        }

    confirmation_msg = "Thanks for contacting us! We will get in touch with you shortly."
    invalid_email_msg = "The email address entered is invalid, please check the formatting (e.g. email@domain.com)."
    missing_mandatory_fields_msg = "This field is required."
