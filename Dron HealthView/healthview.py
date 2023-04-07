import pandas as pd
import os

# create the data
data = {
    'name': ['CPR', 'Heimlich maneuver', 'Burns', 'Shock', 'Seizures', 'Heat exhaustion', 'Stroke', 'Bleeding', 'Fractures', 'Poisoning'],
    'description': ['Cardiopulmonary resuscitation (CPR) is an emergency procedure that combines chest compressions often with artificial ventilation in an effort to manually preserve intact brain function until further measures are taken to restore spontaneous blood circulation and breathing in a person who is in cardiac arrest.',
                    'The Heimlich maneuver is a first aid technique that is used to clear an obstructed airway. It involves applying pressure to the abdomen to force the object out of the airway.',
                    'Burns can be caused by heat, chemicals, electricity, or radiation. The severity of a burn is determined by the depth and size of the burn.',
                    'Shock is a life-threatening condition that occurs when the body is not getting enough blood flow. Symptoms include rapid heartbeat, shallow breathing, and low blood pressure.',
                    'Seizures are sudden, uncontrolled electrical disturbances in the brain. They can cause a wide range of symptoms, including convulsions, loss of consciousness, and confusion.',
                    'Heat exhaustion is a condition that occurs when the body overheats. Symptoms include weakness, headache, dizziness, nausea, and vomiting.',
                    'A stroke occurs when blood flow to the brain is blocked or reduced. Symptoms include weakness, numbness, and difficulty speaking and understanding.',
                    'Bleeding can be caused by an injury or a medical condition. It can range from mild to severe, and may require first aid or medical attention.',
                    'Fractures are breaks in the bone. They can be caused by a fall, a blow, or a sudden twisting motion.',
                    'Poisoning can be caused by ingesting, inhaling, or absorbing toxic substances. Symptoms can range from mild to severe, and may include nausea, vomiting, and seizures.'],
    'image': ['cpr.png', 'heimlich.jpg', 'burns.jpg', 'shock.jpg', 'seizures.jpg', 'heat_exhaustion.jpg', 'stroke.jpg', 'bleeding.jpg', 'fractures.jpg', 'poisoning.jpg']
}

file_csv = os.path.join(os.path.dirname(__file__), 'login.csv')
print(file_csv)

# create the DataFrame
data_df = pd.DataFrame(data)

def data(name):
    # get the row with the specified name
    row = data_df.loc[data_df['name'] == name]

    # convert the row to a list
    row_list = row.values.tolist()[0]

    return row_list

def add_to_login_database(data_list):
    # create a DataFrame from the data_list
    data_dict = {'name': [data_list[0]], 'password': [data_list[1]], 'email': [data_list[2]]}
    new_data = pd.DataFrame(data_dict)

    # read in the existing 'login' database as a DataFrame
    login_df = pd.read_csv(file_csv)

    # concatenate the existing DataFrame with the new data
    updated_df = pd.concat([login_df, new_data], ignore_index=True)

    # save the updated DataFrame back to the 'login' database
    updated_df.to_csv(file_csv, index=False)


def get_index_from_email(email):
    # read in the 'login' database as a DataFrame
    login_df = pd.read_csv(file_csv)

    # check if the email exists in the DataFrame
    if email in login_df['email'].values:
        # get the index of the row with the matching email
        index = login_df.index[login_df['email'] == email].tolist()[0]
        return index
    else:
        return None

def get_login_row(email):
    # read in the 'login' database as a DataFrame
    login_df = pd.read_csv(file_csv)

    # check if the email exists in the DataFrame
    if email in login_df['email'].values:
        # get the row with the matching email
        row = login_df.loc[login_df['email'] == email]

        # convert the row to a list
        row_list = row.values.tolist()[0]

        return row_list
    else:
        return None
    
add_to_login_database(['n','n','n'])