from rest_framework.renderers import JSONRenderer


class JsonRenderResponse(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # return error
        if data and 'error' in data and data['error']:
            data = {
                'status': data['status'],
                'body': data['body'],
                'error': data['error']
            }
            return super(JsonRenderResponse, self).render(data, accepted_media_type, renderer_context)

        # return data
        result = {
            'status': 'OK',
            'body': data,
            'error': None
        }
        # check is list and paging
        if data and 'links' in data and data['links']:
            result['body'] = {"data": data['data']}
            result['paging'] = data['links']
        return super(JsonRenderResponse, self).render(result, accepted_media_type, renderer_context)
