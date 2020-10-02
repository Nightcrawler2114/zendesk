from db import DatabaseHandler

import requests

# Zendesk Token ed0e7f7af2d1a04ebb53a774cde3959e15896139afcf793be22a7c92e6a7dca1


class ZendeskAPIHandler():

    def __init__(self, token='ed0e7f7af2d1a04ebb53a774cde3959e15896139afcf793be22a7c92e6a7dca1'):

        self.token = token

    # def authenticate(self):

    #     response = requests.get('https://api.getbase.com/v2/users/self', headers={'Authorization': f'Bearer {self.token}'})
    #     data = response.json()

    def get_contacts(self):

        response = requests.get('https://api.getbase.com/v2/contacts', headers={'Authorization': f'Bearer {self.token}'})
        data = response.json()

        if data.get('errors', None):

            print(data['errors'])

            return data['errors']

        items = data['items']
        
        return items

    def get_contacts(self):

        # response = requests.get('https://api.getbase.com/v2/opportunities', headers={'Authorization': f'Bearer {self.token}'})
        # data = response.json()

        # if data.get('errors', None):

        #     print(data['errors'])

        #     return data['errors']

        # items = data['items']
        
        # return items

        pass


class ContactsHandler():

    def save_contacts_to_db(self):

        contacts = ZendeskAPIHandler().get_contacts()

        db_client = DatabaseHandler()

        for contact in contacts:

            db_client.save_contact_to_db(contact['data'])


class OpportunitiesHandler():

    def save_opportunities_to_db(self):

        opportunities = ZendeskAPIHandler().get_contacts()

        db_client = DatabaseHandler()

        for opportunity in opportunities:

            db_client.save_opportunity_to_db(opportunity['data'])


if __name__ == '__main__':
    ContactsHandler().save_contacts_to_db()
    OpportunitiesHandler().save_opportunities_to_db()