# 03 - Database Design 

## Models

### User 
    Purpose:
        - store user account information 
        - Authentication is handles y Django's build-in User Model 
    
    Relationships:
        - Can own multiple Projects.
        - Can be assigned multiple Tasks.
        - Can write multiple Coments

### Projects 
    Purpose:
        - Represents a projet that contains multiple tasks.
    Files:
        - id 
        - name
        - description 
        - create_at
        - update_at 
    
    Relationships:
        - Own Project has many Tasks
        - One Projects has many Members
    
### Task 
    Purpose:
        - Represents a task within a projects.
    
    Fields:
        -id 
        - title 
        - description
        - status 
        - priority 
        - due_date
        - created_at
        - update_at 
    
    Relationship:   
        - Belongs to one Project.
        - Assignment to one User
    
### Comment
    Purpose:
        - User can comment on tasks.
    
    Fields:
        - id
        - message
        - created_at 
    
    Relationships:
        - Belongs to one Task 
        - Written by one User
    