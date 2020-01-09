from run import api, fields

get_direcotry_response = api.model('get_direcotry_response', {
    'href': fields.String(description='The directory href', required=True)
})

get_direcotries_response = api.model('get_direcotries_response', {
    'directories': fields.List(fields.Nested(get_direcotry_response))
})