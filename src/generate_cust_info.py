import random
import uuid
from datetime import datetime, timezone

from faker import Faker
from faker.config import AVAILABLE_LOCALES
import pycountry

from src.constants import PLANS_DATA

fake = Faker()

def get_random_plan():
    """Randomly select a plan name from the PLANS_DATA dictionary.

    :return: plan_name
    :rtype: string
    """
    plan_key = random.choice(list(PLANS_DATA.keys()))
    return plan_key

def get_random_locale():
    """Randomly select a country and a corresponding city.

    :return: timezone, city, country
    :rtype: tuple (string, string)
    """
    locale = random.choice(AVAILABLE_LOCALES)
    country = locale.split('_')[1]
    fake = Faker(locale)

    return fake.city(), pycountry.countries.get(alpha_2=country).name

def generate_user_registered_event():
    """Generate a user registration with the service event
    Details are generated synthetically using Faker
    
    :return: user registration event details
    :rtype: event (dict)
    """
    user_id = str(uuid.uuid4())
    # For standard practice, use UTC
    event_ts = datetime.now(timezone.utc)
    
    city, country = get_random_locale()

    user_details = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "country": country,
        "city": city,
        "postal_code": fake.postcode(),
        "phone": fake.phone_number(),
        "timezone": fake.timezone(),
    }
    event = {
        "event_id": str(uuid.uuid4()),
        "user_id": user_id,
        "event_timestamp": event_ts.isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        "event_type": "user_registered",
        "user_details": user_details
    }
    return event

def generate_subscription_started_event(user_id, timestamp_str):
    """Generate a subscription start event for a given user.
    
    :param uuid4 user_id: The ID of the user
    :param str timestamp_str: The timestamp of user registration
    
    :return: subscription start event details
    :rtype: event (dict)
    """
    plan_id = get_random_plan()

    subscription_started_ts = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))

    event = {
        "event_id": str(uuid.uuid4()),
        "user_id": user_id,
        "event_timestamp": subscription_started_ts.isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        "event_type": "subscription_started",
        "plan_id": plan_id,
        "start_date": subscription_started_ts.strftime('%Y-%m-%d')
    }
    return event
