from telegraph import Telegraph

telegraph = Telegraph()

telegraph.create_account(short_name='1337')

response = telegraph.create_page(
    'Hey',
    html_content='<p>Hello, world!</p>'
)

print('https://telegra.ph/{}'.format(response['path']))