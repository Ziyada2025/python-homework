1class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"
    
    def mark_complete(self):
        self.status = "Complete"
    
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description, due_date):
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully!")
    
    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            print(f"Task '{self.tasks[task_index].title}' marked as complete!")
        else:
            print("Invalid task number!")
    
    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
            return
        
        print("\n=== ALL TASKS ===")
        for i, task in enumerate(self.tasks, 1):
            print(f"Task {i}:")
            print(task)
    
    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if task.status == "Incomplete"]
        
        if not incomplete_tasks:
            print("No incomplete tasks!")
            return
        
        print("\n=== INCOMPLETE TASKS ===")
        for i, task in enumerate(incomplete_tasks, 1):
            print(f"Task {i}:")
            print(task)

# Main Program
def main():
    todo_list = ToDoList()
    
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            todo_list.add_task(title, description, due_date)
        
        elif choice == '2':
            todo_list.list_all_tasks()
            if todo_list.tasks:
                try:
                    task_num = int(input("Enter task number to mark as complete: ")) - 1
                    todo_list.mark_task_complete(task_num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '3':
            todo_list.list_all_tasks()
        
        elif choice == '4':
            todo_list.list_incomplete_tasks()
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Test the application
if __name__ == "__main__":
    # Create some test tasks
    test_list = ToDoList()
    test_list.add_task("Buy groceries", "Milk, eggs, bread", "2024-01-15")
    test_list.add_task("Finish homework", "Math assignment", "2024-01-12")
    test_list.add_task("Call dentist", "Schedule appointment", "2024-01-20")
    
    # Mark one task as complete
    test_list.mark_task_complete(0)
    
    # Display all tasks
    test_list.list_all_tasks()
    
    # Display only incomplete tasks
    test_list.list_incomplete_tasks()
    
    # Run the main program
    main() 
2.class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []
    
    def add_post(self, title, content, author):
        new_post = Post(title, content, author)
        self.posts.append(new_post)
        print(f"Post '{title}' by {author} added successfully!")
    
    def list_all_posts(self):
        if not self.posts:
            print("No posts in the blog!")
            return
        
        print("\n=== ALL POSTS ===")
        for i, post in enumerate(self.posts, 1):
            print(f"Post {i}:")
            print(post)
    
    def list_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        
        if not author_posts:
            print(f"No posts found by author '{author}'!")
            return
        
        print(f"\n=== POSTS BY {author.upper()} ===")
        for i, post in enumerate(author_posts, 1):
            print(f"Post {i}:")
            print(post)
    
    def delete_post(self, post_index):
        if 0 <= post_index < len(self.posts):
            deleted_title = self.posts[post_index].title
            del self.posts[post_index]
            print(f"Post '{deleted_title}' deleted successfully!")
        else:
            print("Invalid post number!")
    
    def edit_post(self, post_index, new_title=None, new_content=None):
        if 0 <= post_index < len(self.posts):
            post = self.posts[post_index]
            if new_title:
                post.title = new_title
            if new_content:
                post.content = new_content
            print(f"Post updated successfully!")
        else:
            print("Invalid post number!")
    
    def display_latest_posts(self, count=5):
        latest_posts = self.posts[-count:] if len(self.posts) > count else self.posts
        
        if not latest_posts:
            print("No posts in the blog!")
            return
        
        print(f"\n=== LATEST {len(latest_posts)} POSTS ===")
        for i, post in enumerate(latest_posts, 1):
            print(f"Post {i}:")
            print(post)

# Main Program
def main():
    blog = Blog()
    
    while True:
        print("\n=== BLOG SYSTEM MENU ===")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(title, content, author)
        
        elif choice == '2':
            blog.list_all_posts()
        
        elif choice == '3':
            author = input("Enter author name to search: ")
            blog.list_posts_by_author(author)
        
        elif choice == '4':
            blog.list_all_posts()
            if blog.posts:
                try:
                    post_num = int(input("Enter post number to delete: ")) - 1
                    blog.delete_post(post_num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '5':
            blog.list_all_posts()
            if blog.posts:
                try:
                    post_num = int(input("Enter post number to edit: ")) - 1
                    new_title = input("Enter new title (press enter to keep current): ")
                    new_content = input("Enter new content (press enter to keep current): ")
                    blog.edit_post(post_num, new_title or None, new_content or None)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '6':
            try:
                count = int(input("How many latest posts to display? (default 5): ") or 5)
                blog.display_latest_posts(count)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Test the application
if __name__ == "__main__":
    # Create test blog with sample posts
    test_blog = Blog()
    
    # Add test posts
    test_blog.add_post("Python Basics", "Python is a great programming language...", "Alice")
    test_blog.add_post("Web Development", "Learn HTML, CSS and JavaScript...", "Bob")
    test_blog.add_post("Data Science", "Introduction to pandas and numpy...", "Alice")
    test_blog.add_post("Machine Learning", "Understanding neural networks...", "Charlie")
    test_blog.add_post("Python Advanced", "Decorators and generators...", "Alice")
    
    print("=== TESTING BLOG SYSTEM ===\n")
    
    # Test: List all posts
    print("1. All posts:")
    test_blog.list_all_posts()
    
    # Test: List posts by author
    print("\n2. Posts by Alice:")
    test_blog.list_posts_by_author("Alice")
    
    # Test: Display latest posts
    print("\n3. Latest 3 posts:")
    test_blog.display_latest_posts(3)
    
    # Test: Delete a post
    print("\n4. Deleting post 2:")
    test_blog.delete_post(1)  # Delete second post
    
    # Test: Edit a post
    print("\n5. Editing first post:")
    test_blog.edit_post(0, "Python Fundamentals", "Updated content about Python basics...")
    
    print("\n6. Final list of posts:")
    test_blog.list_all_posts()
    
    # Run the main program
    print("\n" + "="*50)
    print("STARTING INTERACTIVE BLOG SYSTEM")
    print("="*50)
    main() 
3.class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account: {self.account_number}\nHolder: {self.account_holder}\nBalance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account_number, account_holder, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, account_holder, initial_balance)
            print(f"Account {account_number} created for {account_holder} with ${initial_balance:.2f}")
        else:
            print("Account number already exists!")
    
    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        return None
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].deposit(amount):
                print(f"Deposited ${amount:.2f} to account {account_number}")
                return True
            else:
                print("Invalid deposit amount!")
        else:
            print("Account not found!")
        return False
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].withdraw(amount):
                print(f"Withdrew ${amount:.2f} from account {account_number}")
                return True
            else:
                print("Insufficient funds or invalid amount!")
        else:
            print("Account not found!")
        return False
    
    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account].withdraw(amount):
                self.accounts[to_account].deposit(amount)
                print(f"Transferred ${amount:.2f} from {from_account} to {to_account}")
                return True
            else:
                print("Transfer failed: Insufficient funds!")
        else:
            print("One or both accounts not found!")
        return False
    
    def display_account(self, account_number):
        if account_number in self.accounts:
            print("\n=== ACCOUNT DETAILS ===")
            print(self.accounts[account_number])
        else:
            print("Account not found!")
    
    def list_all_accounts(self):
        if not self.accounts:
            print("No accounts in the bank!")
            return
        
        print("\n=== ALL ACCOUNTS ===")
        for account in self.accounts.values():
            print(account)
            print("-" * 30)

# Main Program
def main():
    bank = Bank()
    
    while True:
        print("\n=== BANKING SYSTEM MENU ===")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. View Account Details")
        print("7. List All Accounts")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            acc_number = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            try:
                initial_balance = float(input("Enter initial balance: $") or 0)
                bank.add_account(acc_number, acc_holder, initial_balance)
            except ValueError:
                print("Please enter a valid amount!")
        
        elif choice == '2':
            acc_number = input("Enter account number: ")
            balance = bank.check_balance(acc_number)
            if balance is not None:
                print(f"Balance: ${balance:.2f}")
        
        elif choice == '3':
            acc_number = input("Enter account number: ")
            try:
                amount = float(input("Enter deposit amount: $"))
                bank.deposit(acc_number, amount)
            except ValueError:
                print("Please enter a valid amount!")
        
        elif choice == '4':
            acc_number = input("Enter account number: ")
            try:
                amount = float(input("Enter withdrawal amount: $"))
                bank.withdraw(acc_number, amount)
            except ValueError:
                print("Please enter a valid amount!")
        
        elif choice == '5':
            from_acc = input("Enter your account number: ")
            to_acc = input("Enter recipient account number: ")
            try:
                amount = float(input("Enter transfer amount: $"))
                bank.transfer(from_acc, to_acc, amount)
            except ValueError:
                print("Please enter a valid amount!")
        
        elif choice == '6':
            acc_number = input("Enter account number: ")
            bank.display_account(acc_number)
        
        elif choice == '7':
            bank.list_all_accounts()
        
        elif choice == '8':
            print("Thank you for using our banking system!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Test the application
if __name__ == "__main__":
    # Create test bank with sample accounts
    test_bank = Bank()
    
    print("=== TESTING BANKING SYSTEM ===\n")
    
    # Test: Create accounts
    test_bank.add_account("1001", "Alice Johnson", 1000.00)
    test_bank.add_account("1002", "Bob Smith", 500.00)
    test_bank.add_account("1003", "Charlie Brown", 2500.00)
    
    # Test: Check balance
    print(f"\nAlice's balance: ${test_bank.check_balance('1001'):.2f}")
    
    # Test: Deposit money
    test_bank.deposit("1001", 200.00)
    print(f"Alice's new balance: ${test_bank.check_balance('1001'):.2f}")
    
    # Test: Withdraw money
    test_bank.withdraw("1002", 100.00)
    print(f"Bob's new balance: ${test_bank.check_balance('1002'):.2f}")
    
    # Test: Transfer money
    test_bank.transfer("1003", "1001", 300.00)
    print(f"After transfer - Alice: ${test_bank.check_balance('1001'):.2f}")
    print(f"After transfer - Charlie: ${test_bank.check_balance('1003'):.2f}")
    
    # Test: Display account details
    print("\nAccount details:")
    test_bank.display_account("1001")
    
    # Test: List all accounts
    print("\nAll accounts:")
    test_bank.list_all_accounts()
    
    # Run the main program
    print("\n" + "="*50)
    print("STARTING INTERACTIVE BANKING SYSTEM")
    print("="*50)
    main()
