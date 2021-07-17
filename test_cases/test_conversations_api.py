import pytest
from base.conversation_api import Conversation
from utilities.generic_method import GenericMethod


class TestConversation:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        # Object initialisation
        self.conversation = Conversation()
        self.generic_method = GenericMethod()

        random_name = self.generic_method.get_random_name("TEST")

        # Common input data
        self.creation_input = {"name": random_name,
                               "display_name": f'DP_{random_name}',
                               "image_url": "https://example.com/image.png",
                               "properties/ttl": 120}

    def test_create_conversation(self):
        response = self.conversation.create_conversation(input_data=self.creation_input)
        assert response, f"Expected a valid response but got -{response}"
        assert response.status_code == 200, f"Expected status is 200 but got -{response.status_code}"

    def test_retrieve_conversation(self):
        conversation_id = self.conversation.create_conversation(input_data=self.creation_input, parse=True)
        assert conversation_id, f"Conversation creation Failed"
        retrieved_id = self.conversation.retrieve_conversation(conversation_id=conversation_id, parse=True)
        assert retrieved_id, f"Conversation retrieval Failed"
        assert retrieved_id == conversation_id, "Failed due to Conversation ID mismatch"

    def test_list_conversation(self):
        conversation_id = self.conversation.create_conversation(input_data=self.creation_input, parse=True)
        assert conversation_id, f"Conversation creation Failed"
        list_of_conversation = self.conversation.list_conversation(parse=True)
        assert list_of_conversation, "Failed to get the list of conversation"
        assert len(
            list_of_conversation) != 0, f"List conversation api hit was successful but no data was returned -{list_of_conversation}"

    def test_update_conversation(self):
        conversation_id = self.conversation.create_conversation(input_data=self.creation_input, parse=True)
        assert conversation_id, f"Conversation creation Failed"

        update_input = {"name": self.generic_method.get_random_name("UPDATE")}

        response = self.conversation.update_conversation(input_data=update_input, conversation_id=conversation_id)
        assert response, f"Expected a valid response but got -{response}"
        assert response.status_code == 200, f"Expected status is 200 for update conversation but got -{response.status_code}"
        assert self.conversation.parse_response(response)[
                   'id'] == conversation_id, "Conversation ID changed after updating"

    def test_delete_conversation(self):
        conversation_id = self.conversation.create_conversation(input_data=self.creation_input, parse=True)
        assert conversation_id, f"Conversation creation Failed"

        delete_status = self.conversation.delete_conversation(conversation_id=conversation_id, parse=True)
        assert delete_status, "Deletion failed"

        retrieved_id = self.conversation.retrieve_conversation(conversation_id=conversation_id, parse=False)
        assert retrieved_id.status_code != 200 and retrieved_id.status_code == 404, f"Conversation was deleted before, but it is successfully fetched"

    def test_record_conversation(self):
        conversation_id = self.conversation.create_conversation(input_data=self.creation_input, parse=True)
        assert conversation_id, f"Conversation creation Failed"

        record_status = self.conversation.record_conversation(conversation_id=conversation_id, parse=True)
        assert record_status, f"Conversation record Failed"
