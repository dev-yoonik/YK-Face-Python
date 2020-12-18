"""Sample code for processing a face image
"""
import yk_face as YKF


KEY = 'subscription key'  # Replace with a valid Subscription Key here.
YKF.Key.set(KEY)

BASE_URL = 'https://127.0.0.1/v1.0/yoonik/'  # Replace with a valid API URL here.
YKF.BaseUrl.set(BASE_URL)

img_file_path = 'detection1.jpg'
detected_faces = YKF.face.process(img_file_path)
print(f'Detected faces: {detected_faces}')

matching_score = YKF.face.verify(detected_faces[0]['template'], detected_faces[0]['template'])
print(f'Verify - Matching score: {matching_score}')

group_id = 'demo_group'
YKF.group.create(group_id)

person_id = 'demo_person'
YKF.group.add_person(group_id=group_id, person_id=person_id, face_template=detected_faces[0]['template'])

template = YKF.group.get_person_template(group_id=group_id, person_id=person_id)
print(f'{person_id} biometric template: {template}')

ids_in_group = YKF.group.list_ids(group_id)
print(f'Person ids in {group_id}: {ids_in_group}')

verify_id_score = YKF.face.verify_id(
    face_template=detected_faces[0]['template'],
    person_id=person_id,
    group_id=group_id
)
print(f'Verify ID - Matching score: {verify_id_score}')

identification_candidates = YKF.face.identify(face_template=detected_faces[0]['template'], group_id=group_id)
print(f'Identification candidates: {identification_candidates}')

YKF.group.remove_person(group_id=group_id, person_id=person_id)
new_identification_candidates = YKF.face.identify(face_template=detected_faces[0]['template'], group_id=group_id)
print(f'Identification candidates (empty group): {new_identification_candidates}')

YKF.group.delete(group_id)
