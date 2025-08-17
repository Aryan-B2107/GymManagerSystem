Example Test Flow
The tests/ directory is used to create 
and run automated tests all the functionalities

It will have various flows for different services:

let's say to check membership service:

we write a test:
It creates a new membership_service.

It creates a mock inventory_service. This is a
fake version of the real service that you can control.

It calls the membership_service.createNewMember()
function.
The test then checks that the membership_service
correctly called the mock 
inventory_service.reserveTshirt() function.


test is passed if memberhsip_service correctly called 
the inventory service