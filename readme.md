# Memories

## Overview

This is a Python/Django based project. 

## Features:

### 1. User Registration:

![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/af382a25-2f43-4368-84f8-72776b4932e6)

Users register adding their username, first/last - name, email, phone number and password. Password needs to be typed in twice.

#### 1.1 Using a already registered email address:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/b20c0e60-6de9-4a75-8bc0-110e742d3b9e)

#### 1.2 Missmatch between passwords:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/f6acd8fb-ee14-41ff-8389-d798221294fb)

#### 1.3 Successful login:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/18f85c67-ed59-4cce-a3a0-cbd6dbe68c06)

When registering to the site a message will show:

##### 1.3.1 Activation email:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/35bc7c4c-4334-4951-8da8-3121e2070bd4)

The user needs to verify her account by pressing the verification link sent to her.

##### 1.3.2 Redirected to the login page:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/337e88e7-3540-4c11-b227-32ef02b1d9cb)

When she has logged in she gets redirected to her dashboard:

### 2. Dashboard:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/75a459f8-3ee9-4b73-8acc-54414735c246)

Here she will be greated with a welcome message in the navbar (username) as well as seeing that the login was a success. The dashboard contains of three tabs:

#### 2.1 Edit Profile:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/f2851fa6-1221-4ad4-ba2c-c2d7a8a4e99d)

Here she can change her details (except password) and add her profile picture. 

#### 2.2 Change Password:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/37d2bfe1-0c4c-41a5-978e-6f780f3a09cd)

Here she needs to add her current password and the new password twice. Just like the register process the passwords needs to match and if the current password is incorrect the following error will show:

<br>

![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/d28ddbff-9a61-4f19-8e45-a2334bb4dbea)

#### 2.3 Dashboard:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/a8788a39-550b-4f29-be90-63af1629462d)

When the profile picture has been added (in this case my picture) she will see her profile picture and beneath: her email address and phone number. 
  
### 3. Login/Logout:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/18808cd6-1bec-460d-88e2-a9e03d0d1255)

If she forgets her password there is a link provided "Forgot your Password?" where she will be able to create a new one.

#### 3.1 To logout the user has to press the profile picture button in the navbar where she will also have access to her dashboard. 
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/26bc3847-0dd6-4627-987d-7086f4736994)

### 4. Navbar:

The navbar contains of three buttons: 

#### 4.1 Brand button: 
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/f46b2772-2a41-4759-b3f9-c727f8a552e3)

This button will redirect the user to the homepage = Postwall

#### 4.2 Post Button:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/0fe64987-3424-4607-96cd-62752b77c167)

This button will redirect the user to the post template:
<br>
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/b373e0c1-9eed-4e94-9e82-0dd630c5e72b)

#### 4.3 Profile Picture Button:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/bb315b7f-dd81-44da-b094-0f3771a81f4c)

### 5. Postwall:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/72c2ee76-aef1-46c1-ab6f-9c6325dac477)

Here all users will see the following:

* All posts = Title, content, author and the date when the post was created. 
* Comments = Username followed by their comment. 
* Add a Comment button
  
### 6. Add a Comment:
![image](https://github.com/GlennJohansson85/p4-blog/assets/139962883/bfc4ff27-eed4-4285-aae4-47ca3d4fb458)

Here the user add/delete their comments or the post if they created it. Note that admin can delete all posts and comments. 

### Testing
* Env.py tests
* Button tests
* Email, passwords verifications
* Database tests to see if all is being stored correctly.
* Responsive tests (Desktop, smartphone, ipads resolution)
* Lighthouse
* Flake8
* I´ve used Visual Studios exetensions for most of the test so I hope these work correctly. 

### Agile
I´ve Used AGILE when estimating the work. I started rather late using this method due to I was sceptic about it. Spent so many hours and still the project is so small. 

#### Other
I wish I could have implemented the following: 

* Friendship between users
* PVP messaging
* Better styling to the forms - Note: I prefer the Postwall when everything is not centered on the page.
* Profile Button has another style than appear broken when not logged in.
* Profile picture with the username at comments.
* Another button for deleting post/comments instead of "Add a Comment!" button.
* Brand name change to home when hovering.
* Style outside the body instead of white.
* Footer at end of all templates.
* My two fontfamilies I spent hours on choosing actually worked

## Credits
- Code Institue lessons - and assessors for providing more timee
- Sean - Tutor at CI
- Facebook - as goal
- Pythontutor.com
- Django documentation
- Django Forum
- Upwork.com
- UDEMY - lessons
- FREE LOGO Maker
- FontSpace
- Temp Mail


### Developer
Glenn Johansson
