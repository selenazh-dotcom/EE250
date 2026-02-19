# Lab 3

## Team Members
- Selena Zhang (2575286626)

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

    They are efficient because of statelessness, which allows it so the server doesn't have to retain past information, and has well managed caching that minimizes server-client interactions. This allows for very efficient server-client communication. It always operates independent of the technology and can work on many different programming languages.
    

Question 2: According to the definition of “resources” provided in the AWS article above, what are the resources the mail server is providing to clients?

    The resources the mail server is providing include the dictionaries of mail, its identification, and information about the sender / recipient.


Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

    One method we did not use in the mail server was PUT. We can extend our mail server to use this method for all the same functions that use POST, as it works similarly. This would be especially useful in cases where we don't want duplicate emails.


Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve?

    API keys are used for many RESTful APIs because it's a very simple method of authentication, and doesn't require any encoding or decoding. They allow for unique users to access resources via a code.
