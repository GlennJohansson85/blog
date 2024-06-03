# Memories

### Overview

This is a Python/Django based project. 

### Features:

#### 1. User Registration:

![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/af382a25-2f43-4368-84f8-72776b4932e6)

Users register adding their username, first/last - name, email, phone number and password. Password needs to be typed in twice.

##### 1.1 Using a already registered email address:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/b20c0e60-6de9-4a75-8bc0-110e742d3b9e)

##### 1.2 Missmatch between passwords:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/f6acd8fb-ee14-41ff-8389-d798221294fb)

##### 1.3 Successful login:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/18f85c67-ed59-4cce-a3a0-cbd6dbe68c06)

When registering to the site a message will show:

##### 1.3.1 Activation email:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/35bc7c4c-4334-4951-8da8-3121e2070bd4)

The user needs to verify her account by pressing the verification link sent to her.

##### 1.3.2 Redirected to the login page:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/337e88e7-3540-4c11-b227-32ef02b1d9cb)

When she has logged in she gets redirected to her dashboard:

#### 2. Dashboard:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/75a459f8-3ee9-4b73-8acc-54414735c246)

Here she will be greated with a welcome message in the navbar (username) as well as seeing that the login was a success. The dashboard contains of three tabs:

##### 2.1 Edit Profile:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/f2851fa6-1221-4ad4-ba2c-c2d7a8a4e99d)

Here she can change her details (except password) and add her profile picture. 

##### 2.2 Change Password:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/37d2bfe1-0c4c-41a5-978e-6f780f3a09cd)

Here she needs to add her current password and the new password twice. Just like the register process the passwords needs to match and if the current password is incorrect the following error will show:

<br>

![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/d28ddbff-9a61-4f19-8e45-a2334bb4dbea)

#### 2.3 Dashboard:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/a8788a39-550b-4f29-be90-63af1629462d)

When the profile picture has been added (in this case my picture) she will see her profile picture and beneath: her email address and phone number. 
  
#### 3. Login/Logout:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/18808cd6-1bec-460d-88e2-a9e03d0d1255)

If she forgets her password there is a link provided "Forgot your Password?" where she will be able to create a new one.

#### 3.1 To logout the user has to press the profile picture button in the navbar where she will also have access to her dashboard. 
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/26bc3847-0dd6-4627-987d-7086f4736994)


     
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

Ive done numerous testing on both this and my first 4 project submission "Memories" and "Memories1" which also are puplic here on github. 
Ive also taken alot of the work from P5 and implemented here in p4. In otherwords please check those repos aswell to see the tests ive done. 

I´ve used Visual Studios extensions for Flake8/pep8 tests and no errors. 
I´ve check all pages in various views (smartphone/Ipad/4k/1080p/1440p)



### Agile
I´ve Used AGILE when estimating what work must/should/could be done. 

## Credits
- Code Institue lessons
- Facebook
- Pythontutor.com
- Django official homepage
- Django Forum
- Upwork.com
- UDEMY
- FREE LOGO Maker
- FontSpace
- Temp Mail

### Deployment

God, I hope I really can make it work this time. 

### Notes:

* Wish I could have fixed the search function, the pvp messaging, the friends dropdown button and the profile picture button nicer looking when in guest mode.
* Overall I´m happy with my work even though with out mentor support. 
  

### Developer
Glenn Johansson
