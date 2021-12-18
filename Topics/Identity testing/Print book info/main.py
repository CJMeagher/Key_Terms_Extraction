def print_book_info(title, author=None, year=None):
    was_text = 'was written ' if author or year else ''
    author_text = f'by {author} ' if author else ''
    year_text = f'in {year}' if year else ''
    print(f'"{title}" {was_text}{author_text}{year_text}')


# print_book_info('War and Peace', 'Leo Tolstoy', '1869')
# print_book_info('Crime and Punishment', year='1866')
# print_book_info('The Chronicles of Narnia', 'C.S. Lewis')
# print_book_info('Harry Potter')
