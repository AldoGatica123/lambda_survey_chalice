
TEST_MESSAGE = 'Test email. \nwoop woop!'

profile_map = {
    'man': 'Hombre',
    'woman': 'Mujer',
    'trans_man': 'Hombre Transgénero',
    'trans_woman': 'Mujer Transgénero',
    'male': 'Masculino',
    'female': 'Femenino',
    'intersexual': 'Intersexual',
    'gay': 'Gay',
    'lesbian': 'Lesbiana',
    'bisexual': 'Bisexual',
    'straight': 'Heterosexual',
}

slider_map = {
    'q_01': 'Estado de las instalaciones del espacio seguro',
    'q_02': 'Estado del alojamiento / dormitorio',
    'q_03': 'Calidad de actividades realizadas',
    'q_04': 'Profesionalismo del personal de atención',
    'q_05': 'Calidad de los alimentos recibidos',
    'q_06': 'Limpieza de las instalaciones',
    'q_07': 'Trato en general del personal hacia su persona',
    'q_08': 'Calidad de la información que se le brindó'
}

value_map = {
    5: 'Muy bueno',
    4: 'Bueno',
    3: 'Regular',
    2: 'Malo',
    1: 'Muy malo',
}

score_map = {
    'very_good': 'Muy bueno',
    'good': 'Bueno',
    'regular': 'Regular',
    'bad': 'Malo',
    'very_bad': 'Muy malo',
}


def get_multibutton_values(multibutton):
    values = ''
    for item in multibutton:
        if item['active']:
            values += item['label'].capitalize() + ' '
    if values == '':
        return 'Ninguno'
    return values


def get_biswitch_value(biswitch):
    return 'Sí' if biswitch['active'] else 'No'



# "needs_met":{
#          "on":"Si",
#          "off":"No",
#          "active":true
#       }
