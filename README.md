Module 14 Mini-Project: GraphQL API for a Movie Database
Our objective is to create a versatile GraphQL API for a Movie Database, enabling users to efficiently manage, explore, and enjoy their movie collections. The system should facilitate a seamless user experience by supporting a wide array of operations, including adding movies, filtering by genre, searching for specific titles, and retrieving movie details. To achieve this goal, we must implement a diverse set of functionalities using a combination of data structures, algorithms, and web development techniques.

Project requirements
💡 Note: We've already developed key functionalities for our GraphQL API for a Movie Database in the previous lessons of this Module. To save time and maintain consistency, consider reusing the Python code as a foundation. This approach ensures a unified and efficient codebase, making it easier to integrate the GraphQL API's new features into the existing solution.

Data Schema Creation with SQLAlchemy:
Create a relational database schema using SQLAlchemy to represent movie and genre entities:
Define a table for movies with columns for movie ID, title, description, release year, etc.
Define a table for genres with columns for genre ID and name.
Define appropriate table structures, schemas, constraints, and foreign key relationships in the database schema
Implementation of Mutations for Genres:
Develop GraphQL mutations to enable the creation, updating, and deletion of genres:
createGenre: Mutation to create a new genre. Accepts input parameters for the genre name.
updateGenre: Mutation to update an existing genre. Accepts input parameters for the genre ID and new name.
deleteGenre: Mutation to delete an existing genre. Accepts input parameter for the genre ID.
Ensure proper validation of input data for genre mutations:
Validate that the genre name is not empty and does not exceed a certain length.
Validate that the genre ID provided for update and delete mutations exists in the database.
Relationships Between Movies and Genres:
Implement GraphQL queries to retrieve movies based on genres and vice versa:
getMoviesByGenre: Query to retrieve a list of movies belonging to a specific genre. Accepts input parameter for the genre ID.
getGenreByMovie: Query to retrieve the genre(s) associated with a specific movie. Accepts input parameter for the movie ID.
Ensure that relationships between movies and genres are handled correctly. For example, ensure there aren't any issues if a movie has multiple genres or if a genre can be found on multiple movies.
GitHub Repository:
Create a GitHub repository for the project and commit code regularly.
Maintain a clean and interactive README.md file in the GitHub repository, providing clear instructions on how to run the application and explanations of its features.
Include a link to the GitHub repository in the project documentation.
Submission
Upon completing the project, submit your code, including all source code files, and the README.md file in your GitHub repository to your instructor or designated platform.
Project Tips
Mutations for Creation:
Ensure that mutations for creating new entities, such as movies and genres, include all required fields to avoid incomplete data entries.
Implement input validation within mutation resolvers to validate incoming data against predefined schema requirements, ensuring data integrity.
Utilize error handling mechanisms to provide informative feedback to users in case of validation failures or database errors during entity creation.
Queries for Retrieval:
Optimize queries for retrieving movie and genre information to minimize response times and improve overall system performance.
Consider implementing pagination for queries returning large datasets to enhance user experience and prevent overwhelming client applications.
Data Relationships Handling:
Ensure that mutations and queries handle data relationships correctly, especially in scenarios involving genres and movies.
Implement resolver functions to retrieve related data efficiently, such as fetching all movies belonging to a particular genre or vice versa.
Use GraphQL directives or custom resolver logic to handle complex data relationships effectively and optimize query execution.
Code Modularization:
Organize your code into modular components for better maintainability and scalability.
Separate concerns by dividing functionality into smaller modules such as schema definitions, resolvers, database models, and utility functions.ss
Project Rubric: Module 14 Mini-Project Rubric


