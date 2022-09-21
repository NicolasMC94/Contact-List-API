from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Contact, Group
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200


""" RUTAS """

@api.route('/contact/all', methods=['GET'])
def get_contacts_all():
    contacts = Contact.query.all()
    serializer = list(map(lambda contact: contact.serialize(), contacts))
    
    return jsonify({
        "data": serializer
    }), 200

@api.route('/contact/<int:id>', methods=['GET']) 
def get_contact(id):
    # coger el que coincide exactamente (query.get)
    contact = Contact.query.get(id)
    if contact is not None:
        return jsonify({
            "data": contact.serialize()
            }), 200
    
    return jsonify({"message": "El contacto no existe"}), 404

@api.route('/contact/create', methods=['POST'])
def create_contact():
    data = request.get_json()
    phone = data.get("phone", None)
    name = data.get("name", None)

    if phone is None:
        return jsonify({"message": "El teléfono no puede estar vacío"}), 400
    if name is None:
        return jsonify({"message": "El nombre no puede estar vacío"}), 400

    already_exist = Contac.query.filter_by(name=name).first()

    if already_exist is None:
        return jsonify({"message": "El nombre ya se ha utilizado"}), 400


    contact = Contact(
        full_name = name,
        phone = phone,
        address = data.get('address'),
        email = data.get('email'),
        groups = data.get('groups',[])
    )

    db.session.add(contact)
    db.session.commit()

    return jsonify({"data": contact.serialize()}), 201

@api.route('/group/<int:group_id/<int:contact_id>', methods=['PUT'])
def get_groups_all(group_id, contac_id):
    group = Group.query.get(group_id)
    contact = Contact.query.get(contac_id)
    group.contacts.append(contact)
    db.session.commit()
    return jsonify({'group': group.serialize(), 'contact': contact.serialize()}), 200
