
## FOUNDATION EXAM 
## THEORY QUESTIONS

### Section 1: Theory Questions [31 marks]


#### 1.1    What does SDLC stand for?

SDLC stands for Software Development Life Cycle.

#### 1.2   What exception is thrown when you divide a number by 0?

In Python, when you divide a number by 0 the exception that is thrown is 'ZeroDivisionError'.

#### 1.3   What is the git command that moves code from the local repository to the remote repository? 

To move code from your local repository to a remote repository you can use the 'git push' command. 

#### 1.4   What does NULL represent in a database? 

In the context of a database NULL represents the absence of a value in a column. It is not the same as a zero or an empty string. NULL is used to indicate that the data in a particular column is missing or unknown.

#### 1.5   Name 2 responsibilities of the Scrum Master 

The Scrum Master facilitates and supports the scrum team in an agile development environment. Two of the responsibilities of a Scrum Master are:

1. Facilitating scrum events: the Scrum Master is responsible for facilitating various scrum events, including sprint planning, daily standup, sprint review, and sprint retrospective. They ensure that these events are effectively organized, run smoothly, and that the team follows the scrum framework during these meetings.

2. Removing impediments: with the team identifies the distractions and roadblocks that can impede progress, and works within the team and across the organization to ensure impediments are removed, therefore helping team members to stay focused on the tasks that need to be done during each sprint. For example, if team members are being asked to attend unrelated meetings, the Scrum Master can work with meeting organizers to determine who really needs to attend the each meeting.

#### 1.6   Name 2 debugging methods, and when you would use them.

Debugging is the process of identifying and fixing errors or code issues. Two debugging methods are:

1. Print Statements: involves adding log messages or output statements at various points in the code to track if the programme is executing as planned.
- When to use: This method is helpful when you want to understand the flow of your code, inspect variable values, and identify the specific location where a problem occurs. Print statements are often used during the initial stages of debugging to gain insights into the code's behavior.

3. Interactive Debugging: when using an IDE e.g. PyCharm, we can use in-built debugging functionality to run a program in debugging mode. which involves setting breakpoints, stepping through code and inspecting variables.
- When to use: This method is particularly effective for more complex bugs. You would use interactive debugging when you need to pinpoint the exact cause of an issue or trace the code execution.


#### 1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. 

``` def can_pay(price, cash_given):
    if cash_given >= price:
        return True
    else:
        return False
```

The can_pay function checks whether a customer can pay for an item with a given price using the cash they've given. It returns True if the cash provided is greater than or equal to the price, and False otherwise.
A potential scenario where it could throw an error, is for example:
	- If the price or cash_given arguments are not numeric values (integer or float) for example if the value given by the user is a string, list or dictionary. 
This  could lead to a TypeError or ValueError when comparing them with the >= operator. 
To handle this, we could include exception handling to check for valid input types. 
By using try and except, we can catch any exceptions related to invalid input types and provide a user-friendly error message instead of the code throwing an error message.

Here's an example of how we could modify the function to handle this:

```
def can_pay(price, cash_given):
     try:
        price = float(price)
        cash_given = float(cash_given)
        if cash_given >= price:
            return True
        else:
            return False
    except (TypeError, ValueError):
        return "Please provide a number for price and cash given.Thank you!"
```


####  1.8    What is git branching? Explain how it is used in Git. 

Git is a version control system and Git branching is a fundamental concept in Git. 
Git branching allows developers to work on multiple independent lines of development within a single repository. Each branch represents a distinct path of code changes and can be used to isolate and manage different features, bug fixes, or experiments. Git branching is a powerful mechanism for collaborative software development and code management.
How it is used in Git:

1. Creating a Branch: To create a new branch, we can use the git branch command followed by the branch name:
```
git branch new-branch-name
```
2. Switching Between Branches: we can switch to a different branch using the git checkout command:
```
git checkout new-branch-name
```

Once we're on a branch, we can make changes to our code and commit those changes using git commit. These commits will be specific to the branch we are on.

3. Merging Branches: When we're ready to integrate the changes from one branch into main:
```
git push new-branch-name
```

4. Deleting Branches: Once a branch's changes have been merged and are no longer needed, we can delete the branch:
```
git branch -d new-branch-name
```

####   1.9  Design a restaurant ordering system. You do not need to write code, but describe a high-level approach:
a. Draw a list of key requirements. 
b. What are your main considerations and problems? 
c. What components or tools would you potentially use?

System design and process flow are key components in software development and engineering. 
System design is the phase of software development where you plan and specify the architecture and structure of a software system or application. It involves making high-level decisions about the system's components, their interactions, and the overall design to meet the project's requirements. The primary goal of system design is to create a blueprint for the system's construction. There are tools that can be used to aid the system design process, for exapmple: Draw.io, Microsoft Visio or Lucidchart.

In this case I will give examples of how it would look like when designing a restaurant ordering system: 

**a.Key Requirements:**

- User Authentication: Allow customers and staff to log in with their respective accounts to place and manage orders.

- Menu: Enable the restaurant to add, edit, and remove items from the menu, including descriptions, prices, and availability.

- Orders: Allow customers to browse the menu, select items, customize their orders (e.g., specify preferences or dietary restrictions), and place orders.

- Order Tracking: Provide real-time order tracking for customers and staff, allowing them to monitor the status of orders (e.g., preparing, out for delivery).

- Payment Processing: Support various payment methods (credit card, cash, mobile wallets) and ensure secure and reliable payment processing.

- Table Reservations: If it's a dine-in restaurant, offer a reservation system for customers to book tables in advance.

- Feedback and Ratings: Collect customer feedback and ratings for orders and dishes to improve service quality.

**b.Main Considerations and Problems:**

- Scalability: Ensure the system can handle a high volume of orders during peak hours without slowing down or crashing.
  
- Security: Implement robust security measures to protect user data, payment information, and prevent unauthorized access to the system.

- User Experience: Design a user-friendly and intuitive interface for both customers and restaurant staff.

- Customization: Allow restaurants to customize their menu, pricing, and available services.

**c.Potential Components/Tools:**

- Web and Mobile Apps: Develop customer and staff applications for order placement and management.

- Backend Server: Implement a robust server to handle order processing, user authentication, and database management.

- Database: Use a database system (e.g. SQL ) to store user accounts, menus, orders, and feedback.

- Payment Gateway: Integrate with a secure payment gateway for processing payments.

- Cloud Services: Use cloud services for scalability.

- Security Measures: Employ encryption, authentication, and authorization mechanisms to ensure data security.

- Third-Party APIs: Utilize APIs from external services, such as food delivery aggregators (e.g. UberEats), for extended delivery options.

