def solution(table_of_contents):
    def walk(table_of_contents, indent=''):
        chapters = []
        for chapter in table_of_contents:
            chapters.append(f"{indent}{chapter['title']}")
            if 'chapters' in chapter:
                chapters.extend(walk(chapter['chapters'], indent=indent + '* '))
        return chapters
    return '\n'.join(walk(table_of_contents))