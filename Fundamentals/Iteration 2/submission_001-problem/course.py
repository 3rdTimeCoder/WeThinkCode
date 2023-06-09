import random

def create_outline():
    """
    TODO: implement your code here
    """
    # #step 1
    topics = {'Introduction to Python', 'Tools of the Trade', 'How to make decisions', 'How to repeat code', 'How to structure data', 'Functions', 'Modules'}
    topics_list = sorted(list(topics)) #step 4
    print("Course Topics:")
    for topic in topics_list:
        print(f"* {topic}")
    print()
        
        
    # #step 2
    topics_and_problems = {topic : ['Problem 1', 'Problem 2', 'Problem 3'] for topic in topics}
    print("Problems:")
    for topic, problems in topics_and_problems.items():
        print(f"* {topic} : {', '.join(problems)}")
    print()
    
    
    # #step 3
    students = []
    names = ['Themba', 'Thuli', 'Thabo']
    status = ['GRADED', 'STARTED', 'COMPLETED']
    
    for i in range(len(status)):
        r_topic = random.choice(list(topics_and_problems.keys())) #random topic
        r_problem = random.choice(topics_and_problems['Modules']) #random problem
        students.append((names[i], r_topic, r_problem, status[i]))
        
    #step 4
    sorted_students = sorted(students, key=lambda x: x[3], reverse=True) # sort based on status
    
    #display student progress
    print("Student Progress:")
    for i in range(len(students)):
        print(f"{i+1}. {sorted_students[i][0]} - {sorted_students[i][1]} - {sorted_students[i][2]} [{sorted_students[i][3]}]")
    print() 
    
    
    
if __name__ == "__main__":
    create_outline()
