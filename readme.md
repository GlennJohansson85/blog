# Memories

### Overview

This is a Python based Blog Project. 

### Features

1. **User Registration:**
     Users register adding their username, first/last - name, email and password. Password needs to be typed in two times for security reasons.
     If Passwords dont match, or the user choosing a used username alert messages will show.
   If The registration is a success a success message will show and a verification email will be sent to the provided email. Here the User needs to click on the verfication link to verify their account. When pressing the link it will also redirect them to the login page where they need to enter their username and passowrd. Exactly as the registration process if the username or password is invalid an error message will show and a success message if the details are correct. When logged in the user will be greated with a wellcome message followed by there username.
   Authentication is provided by Allauth (auth)

2. **Navbar**
   - The navbar is located on all pages. Within the profile pic button there is a dropdown menu where the user can login/logout or access -      their dashboard. Here is also a messages link where the user will see pvp messages in a later stage.
   - The Brand is also a button which takes the user to the Postwall whenever clicked.
   - There is also a search function and a friends dropdown list which will be functioning in a later stage.
     
3. **Dashboard**
    Each user can access their dashboard through the navbar using the Profile picture button in the top right corner.
    Note that it first appear broken due to there is no image.
    Within the dashboard users have access to the following:
   * "3.2 Dashboard"
   * "3.1 Edit Profile"
   * "3.3 Reset Password"

     3.1 **Edit Profle**
     Here the user can change all their details and also add their profile picture, which will show in the navbar + in the profile class in      the django admin interface. Phonenumber is also optional to provide.

     3.2 **Dashboard**
     Here the user will see their enlarged profile picture aswell as their phonenumber

     3.3 **Reset Password**
     If the user wants to  change password he/she must type his current one and then the new passwords 2 times. Error/success message will       show if it didnt work/worked.

5. **Login**
   If the user forgets his/hers password there is a link where the user can provide their email address to create a new one. Just like the     registration process.
   If the user dont have an account he/she can register through the link shown here.
   
6. **Logout**
   When the user has logged out a success message will show and the profile picture is removed and instead of wellcome (username) it is now    wellcome Guest! shown in the navbar. 
     
4. **Homepage/PostWall:**
   - The homepage displays all posts in descending order of creation.
   - Each post includes details such as title, content, author, and creation date.
   - Beneath each posts are all the users username followed by their comments in descending order
     
5. **Post_details**
   - To comment on a post there is a "add comment" button beneath each posts which will take you to the "post_details.html"
   - Here the user can add their comments by writing in the text field and submit it through the submit button.
   - Users can delete their own posts and their comments using the delete buttons next to them within the post_detail page.
   - Admins however can delete all posts and comments and not just their own.
   

6. **Authentication and Authorization:**
    - Certain views are protected with the `@login_required` decorator, ensuring only authenticated users can access them.
    - Authorization checks are implemented, such as verifying that the logged-in user owns a post before allowing deletion.

### Style ###
As always I have a tendency to get stuck where the most fun is. Something I´ve learned due to all project resubmissions is that first make the backend work and then the frontend. Due to changes of the backend always ends with the style needing to be changed aswell making all the hours spend on style just a waste of time (even though its fun) 

### Testing

Ive done numerous testing on both this and my first 4 project submission (
#### Python test
In "tests.py" within the "blog_app" folder all tests performed can be showned excepts responsive tests and formalia:
* def test_user_registration_view
* def test_user_login_view
* def test_home_view
* def test_post_category_view
* def test_post_create_view
* def test_delete_post_view
* def test_comment_view
![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/a1c9475c-80bf-487d-b8be-935b581b868c)

#### Responsiveness - test - Iphone
![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/f3d88262-d2aa-4dc0-9c9f-f04995496a67)

#### FLAKE8
Used Visual Studios built-in pep8 control - No errors
(Note: First time using VS so i really hope I did it correct) 

## Agile - light
![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/05a8633a-3a75-405a-bd70-98bff0895b57)

## Credits
- Code Institue lessons
- Facebook
- Pythontutor.com
- Django official homepage
- Django Forum
- Upwork.com

### Developer
Glenn Johansson
