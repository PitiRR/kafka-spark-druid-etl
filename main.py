import json
from src import generate_cust_info

def main():
    print("--- Generating 'user_registered' event (for 'account_events' topic) ---")
    user_reg_event = generate_cust_info.generate_user_registered_event()
    print(json.dumps(user_reg_event, indent=2))
    print("\n")

    user_id = user_reg_event["user_id"]
    registration_ts = user_reg_event["event_timestamp"]

    print("--- Generating 'subscription_started' event (for 'subscription_events' topic) ---")
    sub_started_event = generate_cust_info.generate_subscription_started_event(user_id, registration_ts)
    print(json.dumps(sub_started_event, indent=2))


if __name__ == "__main__":
    main()