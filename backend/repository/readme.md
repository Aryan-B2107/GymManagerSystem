This folder has the logic which acts as the bridge
between the applications business logic and data 
storage.

It has the logic to retrieve, update, delete data
effectively hiding the details of the underlying 
data source. (DATABASE QUERIES)


Such that application logic will be a high level 
business rule: 
1)Validate the member's data (is the email format
correct?).
2)Check for existing users.
3)Call the repository to save the data.
4)Send a welcome email.
5)Handle any errors that occur.


While Database logic (in repository folder):

will be about direct database queries