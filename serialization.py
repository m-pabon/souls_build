import os
import django
import json
import requests

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'souls_build.settings')

# Initialize Django
django.setup()

from weapons.models import Weapon, AttackAttribute, DefenseAttribute, Scaling, RequiredAttribute

# JSON payload json_payload = ''' { "id": "17f696356b4l0i1pljd3dmbyei0rzd", "name": "Broadsword",
# "image": "https://eldenring.fanapis.com/images/weapons/17f696356b4l0i1pljd3dmbyei0rzd.png", "description": "A
# straight sword with a wide blade, suited to slashing attacks. Horizontal swings boast wide attack range,
# making it easier to connect with foes. ", "attack": [ { "name": "Phy", "amount": 117 }, { "name": "Mag",
# "amount": 0 }, { "name": "Fire", "amount": 0 }, { "name": "Ligt", "amount": 0 }, { "name": "Holy", "amount": 0 },
# { "name": "Crit", "amount": 100 } ], "defence": [ { "name": "Phy", "amount": 47 }, { "name": "Mag", "amount": 31 },
# { "name": "Fire", "amount": 31 }, { "name": "Ligt", "amount": 31 }, { "name": "Holy", "amount": 31 },
# { "name": "Boost", "amount": 31 } ], "scalesWith": [ { "name": "Str", "scaling": "D" }, { "name": "Dex",
# "scaling": "E" } ], "requiredAttributes": [ { "name": "Str", "amount": 10 }, { "name": "Dex", "amount": 10 } ],
# "category": "Straight Sword", "weight": 4 } '''

# Deserialize JSON
# data = json.loads(json_payload)

# Make the GET request
response = requests.get('https://eldenring.fanapis.com/api/weapons?limit=100&page=3')

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()

    # Access the 'data' field in the response
    data = json_data['data']

    # Iterate over each item in the 'data' list
    for item in data:
        print("Processing: ")
        print(item)
        # Create Weapon object
        weapon, created = Weapon.objects.update_or_create(
            id=item['id'],
            defaults={
                'name': item['name'],
                'image': item['image'],
                'description': item['description'],
                'category': item['category'],
                'weight': item['weight']
            }
        )

        # The `created` variable will be True if a new record was created, False if an existing one was updated
        if created:
            print("New weapon created.")
        else:
            print("Weapon updated.")

        # Create attributes for attacks
        for attack_data in item['attack']:
            AttackAttribute.objects.update_or_create(weapon=weapon, name=attack_data['name'],
                                                     amount=attack_data['amount'])

        # Create attributes for defense
        for defense_data in item['defence']:
            DefenseAttribute.objects.update_or_create(weapon=weapon, name=defense_data['name'],
                                                      amount=defense_data['amount'])

        # Create scaling attributes
        for scaling_data in item['scalesWith']:
            name = scaling_data['name']
            scaling = scaling_data.get('scaling', '')  # Use get() to handle missing 'scaling' key
            # If 'scaling' is None or an empty string, set it to an empty string
            if not scaling:
                scaling = ''
            Scaling.objects.update_or_create(weapon=weapon, name=name, scaling=scaling)

        # Create required attributes
        for required_data in item['requiredAttributes']:
            RequiredAttribute.objects.update_or_create(weapon=weapon, name=required_data['name'],
                                                       amount=required_data['amount'])

        print("Data stored in the database.")

else:
    print("Failed to retrieve data:", response.status_code)
