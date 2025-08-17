middleware is, in simple terms, is a function
that runs on every request before it gets to your
main business logic. It's like a security checkpoint

#Examples:
Authentication: (to check if user logged in)
Logging: (recording every request that comes into 
server which is helpful later on)
Error Handling

EXAMPLE FLOW:

1 Request comes: GET /api/memberships
2 Middle ware takes over before it reaches 
memberhsip_service. and checks user information
to see role ("admin", "Staff", "Member", "Manager")
3 Permission check-> example (if member trying to view
data of other member, well no, member can access 
only his own profile)

