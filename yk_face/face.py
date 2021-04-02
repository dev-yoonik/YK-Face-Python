"""Face module of the YooniK Face API.
"""
from typing import List, Dict
from yk_face_api_models import ProcessRequest, VerifyRequest, VerifyIdRequest, IdentifyRequest
from yk_face import util


def process(image, processings: List[str] = None) -> List[Dict]:
    """Process human faces in an image.
    :param image:
        A base64 string or a file path or a file-like object representing an image.
    :param processings:
        List of desired processings (if None, it will perform all processings):
            'detect'   - Perform face and landmarks detection.
            'analyze'  - Perform quality analysis (brightness, contrast, sharpness, etc).
            'templify' - Perform template extraction.
    :return:
        List of face entries in json format.
    :raises:
        ValueError if image is not provided.
    """
    url = 'face/process'
    if image is None:
        raise ValueError("image must be provided")

    image_b64 = util.parse_image(image)
    if processings is None:
        processings = ['detect', 'analyze', 'templify']
    process_request = ProcessRequest(image_b64, processings).to_dict()
    return util.request('POST', url, json=process_request)


def verify(face_template: str, another_face_template: str) -> float:
    """Verify whether two faces belong to the same person.
    :param face_template:
        Biometric template of one face (obtained from `face.process`).
    :param another_face_template:
        Biometric template of another face (obtained from `face.process`).
    :return:
        The matching score.
    """
    url = 'face/verify'
    verify_request = VerifyRequest(face_template, another_face_template).to_dict()
    json_response = util.request('POST', url, json=verify_request)
    return float(json_response['score'])


def verify_id(face_template: str, person_id: str, group_id: str) -> float:
    """Verify whether one face belongs to a person.
    :param face_template:
        Biometric template of one face (obtained from `face.process`).
    :param person_id:
        Specify a certain person in a group. `person_id` is created in `group.add_person`.
    :param group_id:
        Specify a certain group where the person is. `group_id` is created in `group.create`.
    :return:
        The matching score.
    """
    url = 'face/verify_id'
    verify_id_request = VerifyIdRequest(template=face_template, template_id=person_id, gallery_id=group_id).to_dict()
    json_response = util.request('POST', url, json=verify_id_request)
    return float(json_response['score'])


def identify(face_template: str, group_id: str, minimum_score: float = -1.0,
             candidate_list_length: int = 1) -> List[Dict]:
    """Identify an unknown face in a group.
    :param face_template:
        Biometric template of the face to be identified (obtained from `face.process`).
    :param group_id:
        Specify a certain group to perform the identification. `group_id` is created in `group.create`.
    :param minimum_score:
        Minimum matching score for candidates.
    :param candidate_list_length:
        Maximum length of the list of resulting candidates.
    :return:
        The identified candidates for the provided face template.
    """
    url = 'face/identify'
    identify_request = IdentifyRequest(template=face_template,
                                       candidate_list_length=candidate_list_length,
                                       minimum_score=minimum_score,
                                       gallery_id=group_id).to_dict()
    return util.request('POST', url, json=identify_request)
