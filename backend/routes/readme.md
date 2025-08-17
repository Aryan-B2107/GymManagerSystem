This folder has the routes or addresses for
API.

This maps HTTP methods like GET or POST to a 
relevant python function or service to process and
send back a response(mostly in context of frontend 
actions to backend connection)

(Also see later on how this folder applies to 
backend)

for example: 

GET /api/memberships->fetch list of all memberships
POST /api/memberships-> create new memberships
GET/api_memberships/{id}-> retrieve details for specific
memberhsip based on it's ID 