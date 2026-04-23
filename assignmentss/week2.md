# Week 2 Functional Application Task
**Project Title:** The Simple Grade Tracker
**Estimated Time:** 45 - 60 Minutes

### **The Scenario**
You are a teacher who needs a quick Python script to store your students' test scores. You will use a **Dictionary** to store the names and grades, write two small **Functions** to handle the data, and use a simple **While Loop** to let the user type in the information.

---

### **Part 1: The Data Structure**
You will use a basic dictionary to store your data. 
* The **Key** will be the student's name (a string).
* The **Value** will be their test score (a number).

*Example of how your dictionary will look when it has data:*
```python
grades_db = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
```
*(Note: Your script should start with an empty dictionary: `grades_db = {}`)*

---

### **Part 2: The Functions**
Write two simple functions to interact with your dictionary.

**1. `add_grade(db, student_name, score)`**
* **What it does:** Adds a new student and their score to the dictionary.
* **Logic:** Simply assign the `score` to the `student_name` key in the `db` dictionary. Then, print a message saying the grade was saved.

**2. `show_all_grades(db)`**
* **What it does:** Prints out every student and their score.
* **Logic:** Use a `for` loop to iterate through the dictionary (hint: use the `.items()` method). Print each name and score in a nice sentence, like: *"Alice scored 85 on the test."*

---

### **Part 3: The User Input Loop**
Instead of a complex menu, you will write a simple `while` loop that keeps asking the teacher for names and grades until they are finished.

1. Create a `while True:` loop.
2. Inside the loop, `input()` the student's name.
3. **The Exit Condition:** If the user types `"done"` for the name, use the `break` keyword to stop the loop.
4. If they don't type "done", ask for the student's score using another `input()` (remember to convert it to an integer!).
5. Call your `add_grade()` function to save the data.
6. Once the loop ends (after the user types "done"), call your `show_all_grades()` function to display the final class roster!

---

### **Example of Expected Terminal Output:**

```text
Enter student name (or type 'done' to finish): Alice
Enter Alice's score: 85
✅ Alice's grade has been saved.

Enter student name (or type 'done' to finish): Bob
Enter Bob's score: 92
✅ Bob's grade has been saved.

Enter student name (or type 'done' to finish): done

--- Final Class Grades ---
Alice scored 85 on the test.
Bob scored 92 on the test.
```

---

### **Submission Instructions**
* Write all your code in a single Python file named `week2_grades_yourname.py`.
* Make sure your code runs without errors before submitting.
* Submit the link to your code in the assignment portal!