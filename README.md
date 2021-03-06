**_Facebook Macbook Bot_**
==============

A Facebook bot used to scan the UT Buy/Sell/Trade page to find Macbook sales. Integrated with Twilio and Heroku to send a text every 24 hours notifying the user how many MacBook sales there are in the last 100 posts. Also developed using Python and the [Facebook for Python API](https://github.com/pythonforfacebook/facebook-sdk). It's probably not ideal to use that library now since it seems to be out of date, but it's the one with the most documentation and easiest to find information online, so I decided to stick with it. I also used [Facebook's FQL Reference](https://developers.facebook.com/docs/reference/fql/) to grab information I needed. To be frank, it was a pain in the ass and I couldn't have done it with looking around online. 

**_todo_**

- ~~Integrate with Twilio API~~ Done. 
- ~~Pull Facebook data from the UT Buy/Sell/Trade page~~ Done. 
- ~~Parse comments for MacBook sales~~ Done. 
- ~~Generate an extended access token every run.~~ Done.  
- ~~Set up Heroku variables~~ Done. 
- ~~Get the user name for the post and the price~~ Done with amazing regexes.
- Make the program notify me when the deadline is coming to extend the token (Lasts 60 days, hooray!)
- ~~Message Hoai Truong information through my account~~ Done. 




