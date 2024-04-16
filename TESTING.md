# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| index | index.html | ![screenshot](documentation/validation/index.png) | |
| reservation | cancel_reservation_confirm.html | ![screenshot](documentation/validation/cancel_reservation.png) | |
| reservation | delete_reservation_confirm.html | ![screenshot](documentation/validation/delete_reservation.png) | |
| reservation | edit_reservation.html | ![screenshot](documentation/validation/edit_reservation.png) | |
| reservation | mo_calendar.html | ![screenshot](documentation/validation/make_reservation.png) | |
| Reservation | profile.html | ![screenshot](documentation/validation/profile.png) | |
| accounts | login.html | ![screenshot](documentation/validation/logon.png) | |
| accounts | password_change.html | ![screenshot](documentation/validation/profile.png) | |
| accounts | password_reset_done.html | ![screenshot](documentation/validation/profile.png) | |
| accounts | password_reset_form_key_done.html | ![screenshot](documentation/validation/profile.png) | |
| accounts | password_reset_form_key.html | ![screenshot](documentation/validation/profile.png) | |
| accounts | logout.html | ![screenshot](documentation/validation/logout.png) | |
| accounts | signup.html | ![screenshot](documentation/validation/register.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | ice.css | ![screenshot](documentation/validation/css_valid.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter] (https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| ice_project | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/ice_project/settings.py) | ![screenshot](documentation/python/settings.png) | |
| ice_project | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/ice_project/urls.py) | ![screenshot](documentation/python/url.png) | |
| index | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/index/admin.py) | ![screenshot](documentation/python/index_admin.png) | |
| index | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/index/urls.py) | ![screenshot](documentation/python/index_url.png) | |
| index | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/index/views.py) | ![screenshot](documentation/python/index_view.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/manage.py) | ![screenshot](documentation/python/manage.png) | |
| reservation | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/reservation/admin.py) | ![screenshot](documentation/python/res_admin.png) | |
| reservation | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/reservation/forms.py) | ![screenshot](documentation/python/res_forms.png) | |
| reservation | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/reservation/models.py) | ![screenshot](documentation/python/res_models.png) | |
| reservation | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/reservation/urls.py) | ![screenshot](documentation/python/res_url.png) | |
| reservation | validators.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/reservation/validators.py) | ![screenshot](documentation/python/res_validators.png) | |
| reservation | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/mo_ice_cream/main/reservation/views.py) | ![screenshot](documentation/python/res_view.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Contact | Register | Sign In | Make Res | Profile | Edit Res | Cancel Res | Delete Res | Sign Out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opera | ![screenshot](documentation/browsers/opera_index.png) | ![screenshot](documentation/browsers/opera_contact.png) | ![screenshot](documentation/browsers/opera_register.png) | ![screenshot](documentation/browsers/opera_sign_in.png) | ![screenshot](documentation/browsers/opera_reservation.png) | ![screenshot](documentation/browsers/opera_profile.png) | ![screenshot](documentation/browsers/opera_edit.png) | ![screenshot](documentation/browsers/opera_cancel.png) | ![screenshot](documentation/browsers/opera_delete.png) | ![screenshot](documentation/browsers/opera_sign_out.png) | Works as expected |
| Chrome | ![screenshot](documentation/browsers/chrome_index.png) | ![screenshot](documentation/browsers/chrome_contact.png) | ![screenshot](documentation/browsers/chrome_register.png) | ![screenshot](documentation/browsers/chrome_sign_in.png) | ![screenshot](documentation/browsers/chrome_reservation.png) | ![screenshot](documentation/browsers/chrome_profile.png) | ![screenshot](documentation/browsers/chrome_edit.png) | ![screenshot](documentation/browsers/chrome_cancel.png) | ![screenshot](documentation/browsers/chrome_delete.png) | ![screenshot](documentation/browsers/chrome_sign_out.png) | Works as expected |
| Brave | ![screenshot](documentation/browsers/brave_index.png) | ![screenshot](documentation/browsers/brave_contact.png) | ![screenshot](documentation/browsers/brave_register.png) | ![screenshot](documentation/browsers/brave_sign_in.png) | ![screenshot](documentation/browsers/brave_reservation.png) | ![screenshot](documentation/browsers/brave_profile.png) | ![screenshot](documentation/browsers/brave_edit.png) |![screenshot](documentation/browsers/brave_cancel.png) |![screenshot](documentation/browsers/brave_delete.png) | ![screenshot](documentation/browsers/brave_sign_out.png) |Works as expected |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Contact | Register | Sign In | Make Res | Profile | Edit Res | Cancel Res | Delete Res | Log Out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile_index.png) | ![screenshot](documentation/responsiveness/mobile_contact.png) | ![screenshot](documentation/responsiveness/mobile_register.png) | ![screenshot](documentation/responsiveness/mobile_signin.png) | ![screenshot](documentation/responsiveness/mobile_reservation.png) | ![screenshot](documentation/responsiveness/mobile_profile.png) | ![screenshot](documentation/responsiveness/mobile_edit.png) | ![screenshot](documentation/responsiveness/mobile_cancel.png) | ![screenshot](documentation/responsiveness/mobile_delete.png)  | ![screenshot](documentation/responsiveness/mobile_signout.png)  
| Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet_index.png) | ![screenshot](documentation/responsiveness/tablet_contact.png) | ![screenshot](documentation/responsiveness/tablet_register.png) | ![screenshot](documentation/responsiveness/tablet_signin.png) | ![screenshot](documentation/responsiveness/tablet_reservation.png) | ![screenshot](documentation/responsiveness/tablet_profile.png) | ![screenshot](documentation/responsiveness/tablet_edit.png) | ![screenshot](documentation/responsiveness/tablet_cancel.png) | ![screenshot](documentation/responsiveness/tablet_delete.png)  | ![screenshot](documentation/responsiveness/tablet_signout.png)  | Works as expected |
| Desktop | ![screenshot](documentation/browsers/opera_index.png) | ![screenshot](documentation/browsers/opera_contact.png) | ![screenshot](documentation/browsers/opera_register.png) | ![screenshot](documentation/browsers/opera_sign_in.png) | ![screenshot](documentation/browsers/opera_reservation.png) | ![screenshot](documentation/browsers/opera_profile.png) | ![screenshot](documentation/browsers/opera_edit.png) | ![screenshot](documentation/browsers/opera_cancel.png) | ![screenshot](documentation/browsers/opera_delete.png)  | ![screenshot](documentation/browsers/opera_sign_out.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/validation/lighthouse_home_mobile.png) | ![screenshot](documentation/validation/lighthouse_index_desktop.png) | Some minor warnings |
| Contact | ![screenshot](documentation/validation/lighthouse_contact_mobile.png) | ![screenshot](documentation/validation/lighthouse_contact_desktop.png) | Some minor warnings |
| Register | ![screenshot](documentation/validation/lighthouse_register_mobile.png) | ![screenshot](documentation/validation/lighthouse_register_desktop.png) | Some minor warnings |
| Sign In | ![screenshot](documentation/validation/lighthouse_signin_mobile.png) | ![screenshot](documentation/validation/lighthouse_signin_desktop.png) | Some minor warnings |
| Make Reservation | ![screenshot](documentation/validation/lighthouse_reservation_mobile.png) | ![screenshot](documentation/validation/lighthouse_reservation_desktop.png) | Some minor warnings |
| Profile | ![screenshot](documentation/validation/lighthouse_profile_mobile.png) | ![screenshot](documentation/validation/lighthouse_profile_desktop.png) | Slow response time due to large images |
| Edit | ![screenshot](documentation/validation/lighthouse_edit_mobile.png) | ![screenshot](documentation/validation/lighthouse_edit_desktop.png) | Some minor warnings |
| Cancel | ![screenshot](documentation/validation/lighthouse_cancel_mobile.png) | ![screenshot](documentation/validation/lighthouse_cancel_desktop.png) | Some minor warnings |
| Delete | ![screenshot](documentation/validation/lighthouse_delete_mobile.png) | ![screenshot](documentation/validation/lighthouse_delete_desktop.png) | Some minor warnings |
| Forgot Password | ![screenshot](documentation/validation/lighthouse_pwreset_modile.png) | ![screenshot](documentation/validation/lighthouse_pwreset_desktop.png) | Some minor warnings |
| PW Reset Done | ![screenshot](documentation/validation/lighthouse_pwresetdone_modile.png) | ![screenshot](documentation/validation/lighthouse_pwresetdone_desktop.png) | Some minor warnings |
| Set PW | ![screenshot](documentation/validation/lighthouse_pwresetkey_modile.png) | ![screenshot](documentation/validation/lighthouse_pwresetkey_desktop.png) | Some minor warnings |
| PW Reset Key | ![screenshot](documentation/validation/lighthouse_pwresetkeydone_modile.png) | ![screenshot](documentation/validation/lighthouse_pwresetkeydone_desktop.png) | Some minor warnings |
| Sign Out | ![screenshot](documentation/validation/lighthouse_signout_mobile.png) | ![screenshot](documentation/validation/lighthouse_signout_desktop.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Contact is expected to do go to contact page when the user clicks on link | Tested the feature by doing clicking on link | The feature behaved as expected, and it did go to contact page | Test concluded and passed | ![screenshot](documentation/features/contact.png) |
| | Register is expected to do go to register page when the user clicks on link | Tested the feature by doing clicking on link | The feature behaved as expected, and it did go to register page | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | Sign In is expected to do go to Sign In page when the user clicks on link | Tested the feature by doing clicking on link | The feature behaved as expected, and it did go to Sign In page | Test concluded and passed | ![screenshot](documentation/features/signin.png) |
| | Profile is expected to do go to profile page when the user clicks on link | Tested the feature by doing clicking on link | The feature behaved as expected, and it did go to profile page | Test concluded and passed | ![screenshot](documentation/features/profile.png) |
| | Make Reservation is expected to do go to Make Reservation page when the user clicks on link | Tested the feature by doing clicking on link | The feature behaved as expected, and it did go to Make Reservation page | Test concluded          and passed | ![screenshot](documentation/features/make_reservation.png) |
| | Sign Out is expected to do go to Sign Out page when the user clicks on link | Tested the feature by doing clicking on link | The feature behaved as expected, and it did go to Log Out page | Test concluded and passed | ![screenshot](documentation/features/signout.png) |
| | About Us modal is expected to open 3 different modals when the user clicks on them | Tested the feature by doing clicking on the modal | The feature behaved as expected, and they did opened when clicked | Test concluded and passed | ![screenshot](documentation/features/modal.png) |
| | Flavors modal close Button is expected to to close tho modal when the user clicks on it | Tested the feature by doing clicking on the buttom | The feature behaved as expected, and closed when clicked | Test concluded and passed | ![screenshot](documentation/features/mod_fla.png) |
| | Village Pop Up modal Close Button is expected to to close tho modal when the user clicks on it | Tested the feature by doing clicking on the buttom | The feature behaved as expected, and closed when clicked | Test concluded and passed | ![screenshot](documentation/features/mod_cate.png) |
| | How to book Close Button modal is expected to to close tho modal when the user clicks on it | Tested the feature by doing clicking on the buttom | The feature behaved as expected, and closed when clicked | Test concluded and passed | ![screenshot](documentation/features/mod_book.png) |
| Contact | | | | | |
| | Name is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/name.png) |
| | Email is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/email.png) |
| |Message is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/message.png) |
| |Send Message Button is expected to send message to sever so that the admin can reply | Tested the feature by clicking the button | The feature behaved as expected, and it give the user a message that message was sent | Test concluded and passed | ![screenshot](documentation/features/send_message.png) |
| Register | | | | | |
| | Username is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/username.png) |
| | Email is expected to be required when the user does not not fill it out and will only accept email address format | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required or enter a valid email format message | Test concluded and passed | ![screenshot](documentation/features/email.png) |
| |Password is expected to be required when the user does not not fill it out and will only accept password format | Tested the feature by leaving it blank and inouting a invalid passowrd format | The feature behaved as expected, and it give the user a message a the input is required or in enter valid format | Test concluded and passed | ![screenshot](documentation/features/password.png) |
| | Register Button is expected to post registration of user when user clicks on the button | Tested the feature by doing clicking on button | The feature behaved as expected, and it gave success message | Test concluded and passed | ![screenshot](documentation/features/register_button.png) |
| Sign In | | | | | |
| | Username is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/username.png) |
| | Sign In Button is expected when successfull redirect to index page with a success message  | Tested the feature by filling out a valid username and password and clicking the sign in button | The feature behaved as expected, and it redirected to index page with success message. | Test concluded and passed | ![screenshot](documentation/features/signin_button.png) |
| | Forgot Passowrd Button expected to redirect to a forgot password page. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the forgot passowrd page. | Test concluded and passed | ![screenshot](documentation/features/forgot_pw.png) |
| MaKe Reservation | | | | | |
| | Phone Number is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/phone_number.png) |
| | Date Calendar is expected to display a calendar for the user to pick a date | Tested the feature by doing the calendar icon | The feature behaved as expected, and it displayed a calaendar | Test concluded and passed | ![screenshot](documentation/features/widget_calendar.png) |
| | Time Slot is expected to display a list when the user click on the input field | Tested the feature by doing clicking input field | The feature behaved as expected, and it displayed a list | Test concluded and passed | ![screenshot](documentation/features/time_slot.png) |
| | Location is expected to display a list when the user click on the input field | Tested the feature by doing clicking input field | The feature behaved as expected, and it displayed a list | Test concluded and passed | ![screenshot](documentation/features/location.png) |
| | Submit Reservation Button expected to redirect to a profile page with a success message. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the profile page with a success message. | Test concluded and passed | ![screenshot](documentation/features/reservation_submit.png) |
| Profile | | | | | |
| | Reservation list is expected to display users reservations when a user makes a reservation | Tested the feature by doing making a reservation | The feature behaved as expected, and it displays reservations | Test concluded and passed | ![screenshot](documentation/features/profile_l.png) |
| | Edit Reservation Button expected to redirect to a Edit Reservation page. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the Edit Reservation. | Test concluded and passed | ![screenshot](documentation/features/reservation_edit.png) |
| | Cancel Reservation Button expected to redirect to a Cancel Reservation with. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the Cancel Reservation Page. | Test concluded and passed | ![screenshot](documentation/features/reservation_cancel.png) |
| |Delete Reservation Button expected to redirect to a Cancel Reservation with. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the Delete Reservation Page. | Test concluded and passed | ![screenshot](documentation/features/reservation_delete.png) |
| Edit Reservtion | | | | | |
| | Phone Number is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/phone_number.png) |
| | Date Calendar is expected to display a calendar for the user to pick a date | Tested the feature by doing the calendar icon | The feature behaved as expected, and it displayed a calaendar | Test concluded and passed | ![screenshot](documentation/features/widget_calendar.png) |
| | Time Slot is expected to display a list when the user click on the input field | Tested the feature by doing clicking input field | The feature behaved as expected, and it displayed a list | Test concluded and passed | ![screenshot](documentation/features/time_slot.png) |
| | Location is expected to display a list when the user click on the input field | Tested the feature by doing clicking input field | The feature behaved as expected, and it displayed a list | Test concluded and passed | ![screenshot](documentation/features/location.png) |
| | Edit Reservation Button expected to redirect to a profile page with a success message. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the profile page with a success message. | Test concluded and passed | ![screenshot](documentation/features/reservation_edit.png) |
| Cancel Reservation | | | | | |
| | Cancel Reservation Button expected to redirect to a profile page with a success message. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the profile page with a success message. | Test concluded and passed | ![screenshot](documentation/features/cancel.png) |
| | Cancel Button expected to redirect to a profile page. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the profile page. | Test concluded and passed | ![screenshot](documentation/features/cancel.png) |
| Delete Reservation | | | | | |
| | Delete Reservation Button expected to redirect to a profile page with a success message. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the profile page with a success message. | Test concluded and passed | ![screenshot](documentation/features/delete.png) |
| | Cancel Button expected to redirect to a profile page. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the profile page. | Test concluded and passed | ![screenshot](documentation/features/delete.png) | |
| Sign out | | | | | |
| | Sign Out Button is expected sign out user and redirect to index page with a success message  | Tested the feature by clicking the sign out button | The feature behaved as expected, and it redirected to index page with success message. | Test concluded and passed | ![screenshot](documentation/features/signout_buttons.png) |
| Forgot Password | | |
| | Email is expected to be required when the user does not not fill it out and will only accept email address format | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required or enter a valid email format message | Test concluded and passed | ![screenshot](documentation/features/email.png) |
| | Reset My Password Button is expected to send a email to user with reset password link and then redirect user to reset info page. | Tested the feature by doing filling out email inout and clicking Reset Password Button. | The feature behaved as expected, and it send a email and redirected to info page. | Test concluded and passed | ![screenshot](documentation/features/password_reset.png) | |
| Change Password | | | | | |
| | Password is expected to be required when the user does not not fill it out and will only accept password format | Tested the feature by leaving it blank and inouting a invalid passowrd format | The feature behaved as expected, and it give the user a message a the input is required or in enter valid format | Test concluded and passed | ![screenshot](documentation/features/change_password_again.png) |
| | Reenter Password is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/change_password_again.png) |
| | Change Password Button is expected to redirect user to password change confirmation page. | Tested the feature by doing filling out email inout and clicking Change Password Button. | The feature behaved as expected, and it  redirected to password change confirmation page. | Test concluded and passed | ![screenshot](documentation/features/change_password.png) | |
| Messages | |
| | Success Messages is expected when user successfully sign in, sign out, register, reservation, edit reservation, cancel reservation, delete reservation  user is shown a green success message  | Tested the feature by successfully sign in, sign out, register, reservation, edit reservation, cancel reservation, delete reservation | The feature behaved as expected, and they show user a green success message. | Test concluded and passed | ![screenshot](documentation/features/success_messages.png) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to easily navigate the menu of ice cream flavors, so that I can quickly find that appeal to me and my family. | ![screenshot](documentation/features/icecream_menu.png) |
| As a new site user, I would like to view images and descriptions of the ice cream flavors, so that I can make an informed decision about what to order based on taste preferences. | ![screenshot](documentation/features/icecream_menu.png) |
| As a new site user, I would like to create an account to save my reservation, so that I can quickly keep track of my schedual. | ![screenshot](documentation/browsers/brave_register.png) |
| As a returning site user, I would like to cancel an existing reservation, so that I can adjust my plans based on unforeseen schedule changes. | ![screenshot](documentation/features/reservation_cancel.png) |
| As a returning site user, I would like to delete a past reservation from my history, so that I can keep my account organized and focused on upcoming plans. | ![screenshot](documentation/features/reservation_delete.png) |
| As a returning site user, I would like to edit the details of an existing reservation, so that I can adjust the time, date, or location according to my current needs. | ![screenshot](documentation/features/reservation_edit_page.png) |
| As a site administrator, I should be able to view, edit, and delete any reservations, so that I can assist users with their booking needs and resolve any conflicts. | ![screenshot](documentation/features/reservation_admin.png) |
| As a site administrator, I should be able to add, update, or remove ice cream flavors and descriptions, so that I can keep the menu current with available offerings. | ![screenshot](documentation/features/admin_menu.png) |
| As a site administrator, I should be able to manage the locations of the pop-up service, so that I can ensure accurate and up-to-date information is available for users. | ![screenshot](documentation/features/admin_locations.png) |

## Bugs

### GitHub **Issues**

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aprimarypigments%2Fmo_ice_cream%20label%3Abug&label=bugs)](https://github.com/primarypigments/mo_ice_cream/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/primarypigments/mo_ice_cream/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [Python `'E901 TokenError'`](https://github.com/primarypigments/mo_ice_cream/issues/13) | Closed |
| [Python `'E131 error urlpatterns'`](https://github.com/primarypigments/mo_ice_cream/issues/12) | Closed |
| [Python `'E128 continuation line under-indented for visual indent'`](https://github.com/primarypigments/mo_ice_cream/issues/11) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/primarypigments/mo_ice_cream/issues/2) | Closed |
| [Django `'TemplateDoesNotExist'` at /templates/account](https://github.com/primarypigments/mo_ice_cream/issues/18) | Closed |
| [Django `'Error NameError: name reverse' is not defined in base.py'`](https://github.com/primarypigments/mo_ice_cream/issues/17) | Closed |
| [Django `' Reset Password not working for specific email primarypigments@gmail.com'`](https://github.com/primarypigments/mo_ice_cream/issues/19) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/primarypigments/mo_ice_cream)](https://github.com/primarypigments/mo_ice_cream/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/primarypigments/mo_ice_cream)](https://github.com/primarypigments/mo_ice_cream/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/primarypigments/mo_ice_cream/issues).

## Unfixed Bugs

> There are no remaining bugs that I am aware of.
