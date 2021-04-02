"""Group module of the YooniK Face API.
"""
from typing import List
from yk_face_api_models import TemplateRequest
from yk_face import util


def create(group_id: str):
    """Create a new group with specified `group_id`.
    :param group_id:
         ID of the group to be created.
    :return:
    """
    if group_id is None:
        raise ValueError("Group ID must be specified.")

    url = f'gallery/{group_id}'
    util.request('POST', url)


def delete(group_id: str):
    """Delete an existing group with specified `group_id`.
    :param group_id:
         ID of the group to be deleted. `group_id` is created in `group.create`.
    :return:
    """
    if group_id is None:
        raise ValueError("Group ID must be specified.")

    url = f'gallery/{group_id}'
    util.request('DELETE', url)


def list_ids(group_id: str) -> List[str]:
    """List all person ids in a specified `group_id`.
    :param group_id:
         ID of the group to be listed. `group_id` is created in `group.create`.
    :return:
        An array of person ids.
    """
    if group_id is None:
        raise ValueError("Group ID must be specified.")

    url = f'gallery/{group_id}'
    return util.request('GET', url)


def add_person(group_id: str, person_id: str, face_template: str):
    """Add a person to a group.
    :param group_id:
         ID of the group. `group_id` is created in `group.create`.
    :param person_id:
        Person ID.
    :param face_template:
        Biometric template to be associated with the provided `person_id` (obtained from `face.process`).
    :return:
    """
    if group_id is None:
        raise ValueError("Group ID must be specified.")
    if person_id is None:
        raise ValueError("Person ID must be specified.")

    url = f'gallery/{group_id}/{person_id}'
    template_request = TemplateRequest(face_template).to_dict()
    util.request('POST', url, json=template_request)


def get_person_template(group_id: str, person_id: str) -> str:
    """Get the biometric template of a specified `person_id` in `group_id`.
    :param group_id:
          ID of the group where the person is (used in `group.add_person`).
    :param person_id:
        Person ID. `person_id` is created in `group.add_person`.
    :return:
        The biometric template of this person.
    """
    if group_id is None:
        raise ValueError("Group ID must be specified.")
    if person_id is None:
        raise ValueError("Person ID must be specified.")

    url = f'gallery/{group_id}/{person_id}'
    json_response = util.request('GET', url)
    return json_response['template']


def remove_person(group_id: str, person_id: str):
    """Remove a person from a group.
    :param group_id:
         ID of the group where the person is (used in `group.add_person`).
    :param person_id:
        Person ID. `person_id` is created in `group.add_person`.
    :return:
    """
    if group_id is None:
        raise ValueError("Group ID must be specified.")
    if person_id is None:
        raise ValueError("Person ID must be specified.")

    url = f'gallery/{group_id}/{person_id}'
    util.request('DELETE', url)
