 flask_based_calculator_app 

 Project Documentation: Flask-based Web Application for Mathematical Operations
 1. Project Overview
 1.1 Project Title
Flask-based Mathematical Operations Web Application
 1.2 Project Description
The project consists of the development of a web-based calculator that performs basic mathematical operations, including addition, subtraction, multiplication, and division. The application accepts two numbers through URL endpoints and returns the result of the operation in JSON format.

The primary goal of this project is to meet the client’s demand for a publicly accessible URL that allows users to perform these calculations from their browsers.
 2. Software Process Model
 2.1 The Model used: Waterfall Model
We selected the Waterfall Model to develop this project because of its simplicity. The linear process flow fits well with the requirements of our mini-project, where each phase was completed before moving on to the next.
 2.2 Why did we pick the Waterfall Model:
- The model is suitable for projects with clear, non-changing requirements.
- It is simple and easy to manage for small teams.
- It ensures step-by-step progress, where phase 1 must be completed before phase 2.
 3. Functional Requirements
 3.1 Mathematical Operations
- The application should be able to perform addition, subtraction, multiplication, and division between two numbers.
- The result should be returned in a JSON format with a status code.
 3.2 Endpoints
- The user should be able to perform operations using the following URLs:
    - Addition: `/add/numberA/numberB`
    - Subtraction: `/minus/numberA/numberB`
    - Multiplication: `/multiply/numberA/numberB`
    - Division: `/divide/numberA/numberB`
 4. Non-Functional Requirements

1. Usability: The application should be simple to use via the browser.
2. Performance: The web app should handle small to medium-sized operations efficiently.
3. Reliability: The app should handle errors, such as division by zero, gracefully.

 6. Technologies Used

- Communication Tools: Slack and GitHub for collaboration and task management.
- Programming Language: Python
- Framework: Flask (for building the web app)
- Deployment: Vercel (for deploying the application)
- Version Control: Git and GitHub (each team member worked on separate branches and merged via pull requests)
 7. Potential Risks

- Division by Zero: If the division endpoint is called with `numberB` as 0, an error must be handled properly to avoid application crashes.
- Deployment Issues: Minor delays could occur while deploying on Vercel due to server or configuration issues.
 8. Testing

Testing was performed on all endpoints to verify the correct behavior of the following operations:
- Addition, subtraction, multiplication, and division of two numbers.
- Handling of edge cases, such as division by zero.
 9. What does the user need to access the application?

The user can access the application by entering the provided URL into a browser, and then calling the endpoints for the required operations.

- On Windows or Linux: No additional tools or commands are required, just a browser to access the web-based endpoints.
 10. Conclusion

This Flask-based web application successfully fulfills the client’s requirement of a publicly accessible calculator that performs basic mathematical operations. It was developed and deployed using Flask and Vercel, ensuring easy access through any modern browser. All team members collaborated via GitHub and contributed to different parts of the project.
