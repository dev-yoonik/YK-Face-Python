"""Face module of the YooniK Face API.
"""
from dataclasses import dataclass
from typing import List, Dict
from yk_utils.images import parse_image
from yk_utils.apis import request, request_async
from yk_face_api_models import ProcessRequest, VerifyRequest, VerifyIdRequest, IdentifyRequest


@dataclass
class FaceRouterEndpoints:
    process = "face/process"
    verify = "face/verify"
    verify_id = "face/verify_id"
    identify = "face/identify"


def __process_request_validation(image, processings: List[str] = None) -> dict:
    """ Validates the process endpoint request.
        :param image:
            A base64 string or a file path or a file-like object representing an image.
        :param processings:
            List of desired processings (if None, it will perform all processings):
                'detect'   - Perform face and landmarks detection.
                'analyze'  - Perform quality analysis (brightness, contrast, sharpness, etc).
                'templify' - Perform template extraction.
        :return:
            dictionary of the payload to be sent in HTTP Request
        :raises:
            ValueError if image is not provided.
    """
    if image is None:
        raise ValueError("image must be provided")

    image_b64 = parse_image(image)
    if processings is None:
        processings = ['detect', 'analyze', 'templify']
    process_request = ProcessRequest(image_b64, processings).to_dict()
    return process_request


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
    process_request = __process_request_validation(image, processings)
    return request('POST', FaceRouterEndpoints.process, json=process_request)


async def process_async(image, processings: List[str] = None) -> List[Dict]:
    """
    Process human faces in an image.
    Performs the request asynchronously.
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
    process_request = __process_request_validation(image, processings)
    return await request_async('POST', FaceRouterEndpoints.process, json=process_request)


def verify(face_template: str, another_face_template: str) -> float:
    """Verify whether two faces belong to the same person.
    :param face_template:
        Biometric template of one face (obtained from `face.process`).
    :param another_face_template:
        Biometric template of another face (obtained from `face.process`).
    :return:
        The matching score.
    """
    verify_request = VerifyRequest(face_template, another_face_template).to_dict()
    json_response = request('POST', FaceRouterEndpoints.verify, json=verify_request)
    return float(json_response['score'])


async def verify_async(face_template: str, another_face_template: str) -> float:
    """
    Verify whether two faces belong to the same person.
    Performs the request asynchronously.
    :param face_template:
        Biometric template of one face (obtained from `face.process`).
    :param another_face_template:
        Biometric template of another face (obtained from `face.process`).
    :return:
        The matching score.
    """
    verify_request = VerifyRequest(face_template, another_face_template).to_dict()
    json_response = await request_async('POST', FaceRouterEndpoints.verify, json=verify_request)
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
    verify_id_request = VerifyIdRequest(
        template=face_template,
        template_id=person_id,
        gallery_id=group_id
    ).to_dict()
    json_response = request('POST', FaceRouterEndpoints.verify_id, json=verify_id_request)
    return float(json_response['score'])


async def verify_id_async(face_template: str, person_id: str, group_id: str) -> float:
    """
    Verify whether one face belongs to a person.
    Performs the request asynchronously.
    :param face_template:
        Biometric template of one face (obtained from `face.process`).
    :param person_id:
        Specify a certain person in a group. `person_id` is created in `group.add_person`.
    :param group_id:
        Specify a certain group where the person is. `group_id` is created in `group.create`.
    :return:
        The matching score.
    """
    verify_id_request = VerifyIdRequest(
        template=face_template,
        template_id=person_id,
        gallery_id=group_id
    ).to_dict()

    json_response = await request_async(
        'POST',
        FaceRouterEndpoints.verify_id,
        json=verify_id_request
    )
    return float(json_response['score'])


def identify(
        face_template: str,
        group_id: str,
        minimum_score: float = -1.0,
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
    identify_request = IdentifyRequest(
        template=face_template,
        candidate_list_length=candidate_list_length,
        minimum_score=minimum_score,
        gallery_id=group_id
    ).to_dict()
    return request('POST', FaceRouterEndpoints.identify, json=identify_request)


async def identify_async(
        face_template: str,
        group_id: str,
        minimum_score: float = -1.0,
        candidate_list_length: int = 1) -> List[Dict]:
    """
    Identify an unknown face in a group.
    Performs the request asynchronously.
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
    identify_request = IdentifyRequest(
        template=face_template,
        candidate_list_length=candidate_list_length,
        minimum_score=minimum_score,
        gallery_id=group_id
    ).to_dict()
    return await request_async('POST', FaceRouterEndpoints.identify, json=identify_request)
