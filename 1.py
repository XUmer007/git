import datetime

# Global variables to store user count and user records
user_count = 0
user_records = []

# Function to record user activity
def record_user_activity(user_id, activity):
    timestamp = datetime.datetime.now()
    user_records.append((user_id, activity, timestamp))

# Function to upload user data and update user count
def upload_user_data(users):
    global user_count
    user_count = len(users)

# Example usage
if __name__ == "__main__":
    # Example user data
    users = ["user1", "user2", "user3"]

    # Upload user data
    upload_user_data(users)

    # Record user activities
    record_user_activity("user1", "login")
    record_user_activity("user2", "logout")
    record_user_activity("user3", "update_profile")

    # Display user count and records
    print("Number of users:", user_count)
    print("User Records:")
    for record in user_records:
        print(record)

