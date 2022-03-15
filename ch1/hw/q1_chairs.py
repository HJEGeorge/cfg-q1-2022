chairs = '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))

# --- Solution ---

chairs = 15 # Notice no quotation marks, this means it's an integer, not a string
nails = 4
total_nails = chairs * nails
message = f'{total_nails} nails'
print(f'You need to buy {message}')
